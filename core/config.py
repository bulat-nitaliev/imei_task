from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
from pathlib import Path

class AccessToken(BaseModel):
    lifetime_seconds:int = 3600
    reset_password_token_secret:str
    verification_token_secret:str

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    api_v1_prefix:str = '/api/v1'
    db_url: str = 'postgresql+asyncpg://postgres:SA-testing-1@localhost/imei_db' 
    echo: bool = True
    url_api:str = 'https://api.imeicheck.net/v1/checks' 
    timeout:int = 30
    api_key:str = 'e4oEaZY1Kom5OXzybETkMlwjOCy3i8GSCGTHzWrhd4dc563b'
    # api_key:str = 'sy5woSxuac7xKalljXFjgbB2hCRw7GQLueRtGp1974d8fe72'

    access_token:AccessToken





settings = Settings()
