from lib2to3.pytree import Base
from pydantic import BaseSettings


class Settings(BaseSettings):
    db_path = "../data/test.db"


settings = Settings()
