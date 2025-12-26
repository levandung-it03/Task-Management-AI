import os
import pandas as pd
import evaluate
import numpy as np
from groq import Groq
import json
import time

# --- CẤU HÌNH ---
os.environ["GROQ_API_KEY"] = "" 
client = Groq()

# Chọn Model Giám khảo: Llama 3 70B là lựa chọn tốt nhất trên Groq hiện tại cho việc suy luận
JUDGE_MODEL = "llama3-70b-8192" 

# --- DỮ LIỆU MẪU ---
# Cấu trúc: Mỗi input có 1 Golden và list 10 Generated
data_samples = {
    "completed_report": {
        "input_json": "{json data}", # Dữ liệu đầu vào gốc
        "golden": "Dear Boss,\nTask A is done.\nSincerely, Me",
        "generated_list": [
            "Dear Boss,\nI finished Task A.\nSincerely, Me",
            "Dear Manager,\nTask A is complete.\nSincerely, Me",
            # ... thêm 8 mẫu nữa
        ]
    },
    "processing_report": {
        "input_json": "{json data}",
        "golden": "Dear Boss,\nTask A is done.\nSincerely, Me",
        "generated_list": [
            "Dear Boss,\nI finished Task A.\nSincerely, Me",
            "Dear Manager,\nTask A is complete.\nSincerely, Me",
            # ... thêm 8 mẫu nữa
        ]
    },
    "daily_report": {
        "input_json": "{json data}",
        "golden": "Dear Boss,\nTask A is done.\nSincerely, Me",
        "generated_list": [
            "Dear Boss,\nI finished Task A.\nSincerely, Me",
            "Dear Manager,\nTask A is complete.\nSincerely, Me",
            # ... thêm 8 mẫu nữa
        ]
    }
}

# --- PHẦN 1: TÍNH TOÁN ROUGE & BERTSCORE ---
def calculate_standard_metrics(references, predictions):
    print(">>> Đang tính toán ROUGE và BERTScore...")
    
    # Load metrics
    rouge = evaluate.load('rouge')
    bertscore = evaluate.load('bertscore')
    
    # Tính ROUGE
    rouge_res = rouge.compute(predictions=predictions, references=references)
    
    # Tính BERTScore
    bert_res = bertscore.compute(predictions=predictions, references=references, lang='en')
    
    return {
        "rouge1": rouge_res['rouge1'],
        "rougeL": rouge_res['rougeL'],
        "bertscore_f1": np.mean(bert_res['f1'])
    }

# --- PHẦN 2: LLM JUDGE (GROQ API) ---
def llm_judge_evaluate(input_data, golden, generated_text, report_type):
    prompt = f"""
    You are a strict QA Auditor. Evaluate the generated report based on the Input Data and Golden Reference.
    
    Report Type: {report_type}
    
    [INPUT DATA]
    {input_data}
    
    [GOLDEN REFERENCE (IDEAL STYLE)]
    {golden}
    
    [GENERATED REPORT (CANDIDATE)]
    {generated_text}
    
    Evaluation Criteria:
    1. FACTUALITY: Does it contain ANY information NOT present in Input Data? (Critical)
    2. FORMAT: Does it follow the exact format of the Report Type? (Email vs Note)
    3. COMPLETENESS: Does it cover the key task status?
    
    Output strictly in JSON format:
    {{
        "score": (integer 1-5),
        "reason": "Short explanation of the score, pointing out specific errors if any."
    }}
    """
    
    try:
        completion = client.chat.completions.create(
            model=JUDGE_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that outputs JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0, # Quan trọng: Nhiệt độ 0 để đảm bảo nhất quán
            response_format={"type": "json_object"}
        )
        return json.loads(completion.choices[0].message.content)
    except Exception as e:
        print(f"Error calling Groq: {e}")
        return {"score": 0, "reason": "API Error"}

# --- PHẦN 3: MAIN PIPELINE ---
def run_evaluation_pipeline(data_dict):
    results = []
    
    for report_type, content in data_dict.items():
        print(f"\n--- Đang đánh giá loại: {report_type} ---")
        
        golden = content['golden']
        generated_list = content['generated_list']
        input_data = content['input_json']
        
        # 1. Tính Metrics toán học (Batch processing)
        # Vì bạn có 1 Golden so với 10 Generated, ta phải duplicate Golden 10 lần
        refs = [golden] * len(generated_list)
        math_metrics = calculate_standard_metrics(refs, generated_list)
        
        # 2. Tính LLM Judge (Loop processing)
        judge_scores = []
        for idx, gen_text in enumerate(generated_list):
            # Gọi Groq API
            eval_result = llm_judge_evaluate(input_data, golden, gen_text, report_type)
            judge_scores.append(eval_result['score'])
            
            # Lưu chi tiết từng mẫu để debug
            results.append({
                "type": report_type,
                "sample_id": idx,
                "generated": gen_text[:50] + "...", # Preview
                "llm_score": eval_result['score'],
                "llm_reason": eval_result['reason']
            })
            
            time.sleep(0.5) 
            
        # 3. Tổng hợp cho loại report này
        avg_llm_score = np.mean(judge_scores)
        print(f"Kết quả {report_type}:")
        print(f"  - Avg LLM Score: {avg_llm_score}/5")
        print(f"  - BERTScore F1:  {math_metrics['bertscore_f1']:.4f}")
        print(f"  - ROUGE-L:       {math_metrics['rougeL']:.4f}")

    # Xuất báo cáo chi tiết ra DataFrame
    df_results = pd.DataFrame(results)
    return df_results

# --- RUN ---
df = run_evaluation_pipeline(data_samples)
print(df)
df.to_csv("evaluation_report.csv")