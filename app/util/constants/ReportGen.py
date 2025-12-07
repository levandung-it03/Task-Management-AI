
class CstModelCfg:
    APP_NAME = "Report Generation API"
    VERSION = "1.0.0"
    MODEL_NAME = "llama-3-8b-report-gen"
    DEF_PROMPT_TOKEN = "You are a helpful assistant generating concise work reports."
    DEF_TEMPERATURE = 0.6
    DEF_MAX_TOKENS = 200
    SYS_ROLE = "system"
    USR_ROLE = "user"

class CstModelReq:
    content = "content"
    role = "role"
    model = "model"
    messages = "messages"
    temperature = "temperature"
    max_tokens = "max_tokens"
    
class CstModelRes:
    report = "report"

class CstLog:
    res_success = "Report generated successfully by model: "
    res_error = "Model server error: "
    res_def_throw = "Failed to generate report from model API"