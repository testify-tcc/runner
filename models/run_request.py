from typing import List, Union
from pydantic import BaseModel
from models.docker_image_name import DockerImageName

class RunRequestFile(BaseModel):
  fileName: str
  content: str

class RunRequestBody(BaseModel):
  testCommand: str
  files: List[RunRequestFile]
  testingEnvironment: DockerImageName

  class Config():
    arbitrary_types_allowed = True

class RunRequestResponse(BaseModel):
  passed: Union[bool, None]
  output: str
