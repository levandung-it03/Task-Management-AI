
class CstModelCfg:
    APP_NAME = "Report Generation API"
    VERSION = "1.0.0"
    MODEL_NAME = "llama-3-8b-report-gen"
    DEF_DAILY_REPORT_TOKEN = "You are a team leader writing internal daily progress notes."
    DEF_DAILY_REPORT_TEMPERATURE = 0.1
    DEF_DAILY_REPORT_TOP_P = 0.95
    DEF_DAILY_REPORT_MAX_TOKENS = 400
    DEF_PROCESSING_REPORT_TOKEN = "You are a software engineer reporting task progress to your manager."
    DEF_PROCESSING_REPORT_TEMPERATURE = 0.1
    DEF_PROCESSING_REPORT_TOP_P = 0.95
    DEF_PROCESSING_REPORT_MAX_TOKENS = 350
    DEF_COMPLETED_REPORT_TOKEN = "You are a software engineer writing completion reports."
    DEF_COMPLETED_REPORT_TEMPERATURE = 0.4
    DEF_COMPLETED_REPORT_TOP_P = 0.9
    DEF_COMPLETED_REPORT_MAX_TOKENS = 400
    SYS_ROLE = "system"
    USR_ROLE = "user"

class CstModelReq:
    content = "content"
    role = "role"
    model = "model"
    messages = "messages"
    temperature = "temperature"
    max_tokens = "max_tokens"
    top_p = "top_p"
    
class CstModelRes:
    report = "report"

class CstLog:
    res_success = "Report generated successfully by model: "
    res_error = "Model server error: "
    res_def_throw = "Failed to generate report from model API"