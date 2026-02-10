from pydantic import BaseSettings


class Config(BaseSettings):
    # DB
    MYSQL_USER: str = "user"
    MYSQL_PASSWORD: str = "password"
    MYSQL_DATABASE: str = "poll_service"

    # 👇 חשוב מאוד: שם ה־service ב־docker-compose
    MYSQL_HOST: str = "poll-db"

    # 👇 בתוך Docker תמיד 3306
    MYSQL_PORT: str = "3306"

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"mysql+aiomysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}"
            f"@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DATABASE}"
        )

    # Internal API (גם זה בתוך Docker)
    USER_SERVICE_BASE_URL: str = "http://user-service:8000"

    class Config:
        env_file = ".env"
