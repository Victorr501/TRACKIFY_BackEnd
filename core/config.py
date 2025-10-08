#Configuracion para la base de datos

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Trackify API"
    DB_USER: str = "root"
    DB_PASSWORD: str = "1234"
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_NAME: str = "TRACKIFY"
    
    @property
    def DATABASE_URL(self):
        return(
            f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@"
            f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )
    
    
    class Config:
        env_file = ".env"
        
settings = Settings()