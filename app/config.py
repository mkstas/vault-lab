from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    environment: str
    app_name: str
    database_url: str
    jwt_secret: str
    jwt_algorithm: str
    access_token_ttk_min: int
    password_pepper: str
    password_min_lenght: int

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
