from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    bot_token: str
    database_url: str
    redis_url: str = "redis://localhost:6379/0"

    yukassa_shop_id: str = ""
    yukassa_secret_key: str = ""

    audd_api_token: str = ""

    vk_access_token: str = ""
    yandex_music_token: str = ""
    soundcloud_client_id: str = ""
    spotify_client_id: str = ""
    spotify_client_secret: str = ""

    price_month: int = Field(default=108, description="Цена подписки на месяц (руб)")
    price_6months: int = Field(default=300)
    price_year: int = Field(default=500)
    price_lifetime: int = Field(default=10000)
    referral_commission: int = Field(default=20, description="Процент реферальных выплат")


settings = Settings()
