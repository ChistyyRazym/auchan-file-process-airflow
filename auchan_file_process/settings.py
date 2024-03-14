from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    input_dir: List[str]
    output_dir: str
    file_name_mask: str
