
class CstModelConfig:
    APP_NAME = "Report Generation API"
    VERSION = "1.0.0"
    MODEL_NAME = "llama-3-8b-report-gen"
    DEF_PROMPT_TOKEN = "You are a helpful assistant generating concise work reports."
    DEF_TEMPERATURE = 0.6
    DEF_MAX_TOKENS = 200
    SYS_ROLE = "system"
    USR_ROLE = "user"

    @classmethod
    def generate_request_json(cls, prompt: str):
        return {
        "model": cls.MODEL_NAME,
        "messages": [
            {"role": cls.SYS_ROLE, "content": cls.DEF_PROMPT_TOKEN},
            {"role": cls.USR_ROLE, "content": prompt}
        ],
        "temperature": cls.DEF_TEMPERATURE,
        "max_tokens": cls.DEF_MAX_TOKENS
    }

class CstModelRes:
    Choices = "choices"
    Message = "message"
    Content = "content"

class CstLog:
    res_success = "Report generated successfully by model: "
    res_error = "Model server error: "
    res_def_throw = "Failed to generate report from model API"