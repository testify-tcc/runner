from pydantic import BaseModel
from enum import Enum
from typing import List

class File(BaseModel):
  fileName: str
  content: str

class RunRequest(BaseModel):
  files: List[File]

  class Config():
    arbitrary_types_allowed = True