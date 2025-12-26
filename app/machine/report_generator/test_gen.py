import requests
import json
import time
import re
import os
from datasets import load_dataset

# ========================================
# CẤU HÌNH
# ========================================
SERVER_URL = "https://myxoid-giftedly-pok.ngrok-free.dev/generate-report"
OUTPUT_GEN_FILE = "generated_reports.jsonl"
OUTPUT_GROUND_TRUTH_FILE = "ground_truth_reports.jsonl"

# 1. Load và Split Dataset
huggingface_user = "PLKhang"
dataset_name = "report-finetuning-prompts"

full_dataset = load_dataset(f"{huggingface_user}/{dataset_name}", split="train")
dataset_split = full_dataset.train_test_split(test_size=0.1, seed=42)
test_dataset = dataset_split["test"]

print(f"✅ Đã chuẩn bị {len(test_dataset)} mẫu thử nghiệm.")

# 2. Hàm extract thông tin an toàn (Regex linh hoạt)
def extract_info(prompt_text):
    # Tìm nội dung giữa các thẻ, chấp nhận mọi biến thể của dấu xuống dòng
    system = re.search(r"<\|start_header_id\|>system<\|end_header_id\|>\s+(.*?)\s+<\|eot_id\|>", prompt_text, re.DOTALL)
    user = re.search(r"<\|start_header_id\|>user<\|end_header_id\|>\s+(.*?)\s+<\|eot_id\|>", prompt_text, re.DOTALL)
    assistant = re.search(r"<\|start_header_id\|>assistant<\|end_header_id\|>\s+(.*?)\s+<\|eot_id\|>", prompt_text, re.DOTALL)
    
    get_val = lambda m: m.group(1).strip().strip('"') if m else "N/A"
    
    return {
        "system": get_val(system),
        "user": get_val(user),
        "truth": get_val(assistant)
    }

# Xóa file cũ nếu có để ghi mới từ đầu
for f in [OUTPUT_GEN_FILE, OUTPUT_GROUND_TRUTH_FILE]:
    if os.path.exists(f): os.remove(f)

print("🚀 Bắt đầu Inference tuần tự (Ghi file tức thì)...")

# 3. Vòng lặp Inference và Append file
with open(OUTPUT_GEN_FILE, "a", encoding="utf-8") as f_gen, \
     open(OUTPUT_GROUND_TRUTH_FILE, "a", encoding="utf-8") as f_truth:

    for i, item in enumerate(test_dataset):
        info = extract_info(item["prompt"])
        
        payload = {
            "messages": [
                {"role": "system", "content": info["system"]},
                {"role": "user", "content": info["user"]}
            ],
            "max_tokens": 300,
            "temperature": 0.01,
            "top_p": 0.95
        }
        
        try:
            start_time = time.time()
            response = requests.post(SERVER_URL, json=payload, timeout=40) # timeout tránh treo
            res_json = response.json()
            latency = time.time() - start_time
            
            # Ghi dòng kết quả Generator
            gen_data = {
                "id": i,
                "generated_report": res_json.get("report", ""),
                "latency": f"{latency:.2f}s"
            }
            f_gen.write(json.dumps(gen_data, ensure_ascii=False) + "\n")
            f_gen.flush() # Ép ghi xuống ổ đĩa ngay lập tức

            # Ghi dòng kết quả Ground Truth
            truth_data = {
                "id": i,
                "input_context": info["user"],
                "expected_report": info["truth"]
            }
            f_truth.write(json.dumps(truth_data, ensure_ascii=False) + "\n")
            f_truth.flush()

            print(f"✔️ [{i+1}/{len(test_dataset)}] - {latency:.2f}s - Đã lưu")
            
        except Exception as e:
            print(f"❌ Lỗi tại mẫu {i+1}: {str(e)}")
            continue # Tiếp tục mẫu tiếp theo nếu mẫu này lỗi

print(f"\n✨ Hoàn thành! Dữ liệu đã được lưu an toàn tại {OUTPUT_GEN_FILE} và {OUTPUT_GROUND_TRUTH_FILE}")