from pydantic import BaseSettings


class Config(BaseSettings):
    MYSQL_USER: str = "user"
    MYSQL_PASSWORD: str = "password"
    MYSQL_DATABASE: str = "poll_service"
    MYSQL_HOST: str = "poll-db"
    MYSQL_PORT: str = "3306"

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"mysql+aiomysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}"
            f"@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DATABASE}"
        )

    USER_SERVICE_BASE_URL: str = "http://user-service:8000"

    class Config:
        env_file = ".env"
