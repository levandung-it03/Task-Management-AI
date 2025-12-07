from pydantic import BaseModel

class Settings(BaseModel):
    app_name: str = "Report Generation API"
    version: str = "1.0.0"

    # endpoint
    ngrok_url: str = "https://myxoid-giftedly-pok.ngrok-free.dev/generate-report"

    model_name: str = "llama-3-8b-report-gen"

    # Optional Hugging Face fallback 
    # hf_model_url: Optional[str] = None
    # hf_token: Optional[str] = None

    # App behavior
    temperature: float = 0.6
    max_tokens: int = 200

settings = Settings()
