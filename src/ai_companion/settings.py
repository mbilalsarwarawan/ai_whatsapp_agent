from pydantic_settings import BaseSettings, SettingsConfigDict
import os

print(f"Current working directory: {os.getcwd()}")
print(f".env file exists: {os.path.exists('.env')}")

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_file_encoding="utf-8")

    GROQ_API_KEY: str
    ELEVENLABS_API_KEY: str
    ELEVENLABS_VOICE_ID: str
    TOGETHER_API_KEY: str

    QDRANT_API_KEY: str | None
    QDRANT_URL: str
    QDRANT_PORT: str = "6333"
    QDRANT_HOST: str | None = None

    TEXT_MODEL_NAME: str = "llama-3.3-70b-versatile"
    SMALL_TEXT_MODEL_NAME: str = "gemma2-9b-it"
    STT_MODEL_NAME: str = "whisper-large-v3-turbo"
    TTS_MODEL_NAME: str = "eleven_flash_v2_5"
    TTI_MODEL_NAME: str = "black-forest-labs/FLUX.1-schnell-Free"
    ITT_MODEL_NAME: str = "llama-3.2-90b-vision-preview"

    MEMORY_TOP_K: int = 3
    ROUTER_MESSAGES_TO_ANALYZE: int = 3
    TOTAL_MESSAGES_SUMMARY_TRIGGER: int = 20
    TOTAL_MESSAGES_AFTER_SUMMARY: int = 5

    SHORT_TERM_MEMORY_DB_PATH: str = "D:/learning/automation/ava-whatsapp-agent-course/short_term_memory/memory.db"


settings = Settings()
print("Settings object created")
print(f"GROQ_API_KEY from settings: {settings.GROQ_API_KEY[:5] if settings.GROQ_API_KEY else 'Not loaded'}")