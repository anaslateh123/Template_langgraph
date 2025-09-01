import os
from typing import List, Optional
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings  # Changed import

class Settings(BaseSettings):
    """
    Application settings and configuration.
    Values will be loaded from environment variables, with defaults provided.
    """
    
    LLM_MODEL_NAME: str = Field("gpt-4", description="Name of the LLM model to use")
    LLM_TEMPERATURE: float = Field(0.7, description="Temperature setting for the LLM model")
    LLM_MAX_TOKENS: int = Field(4000, description="Maximum number of tokens for LLM responses")
    
    MEMORY_DB_CONNECTION_STRING: str = Field(
        "postgresql://postgres:postgres@localhost:5432/memory_db",
        description="Connection string for memory database"
    )
    MEMORY_DB_POOL_SIZE: int = Field(5, description="Database connection pool size")
    
    EXTERNAL_SERVICES_ENDPOINTS: List[str] = Field(
        default_factory=lambda: ["https://api-service1.example.com", "https://api-service2.example.com"],
        description="List of external service endpoints"
    )
    
    LLM = None # Define for Langchain LLM instance
    
    ENVIRONMENT: str = Field("development", description="Application environment (development, testing, production)")
    DEBUG: bool = Field(True, description="Debug mode flag")
    
    @field_validator("EXTERNAL_SERVICES_ENDPOINTS", mode='before')  # Changed to field_validator
    @classmethod  
    def parse_endpoints(cls, v):
        """Parse endpoints from string if provided as comma-separated values in env var."""
        if isinstance(v, str):
            return [endpoint.strip() for endpoint in v.split(",")]
        return v
    
    model_config = {  
        "env_file": ".env",
        "case_sensitive": True
    }

settings = Settings()