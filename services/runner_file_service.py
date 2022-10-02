import env

from typing import List
from pathlib import Path
from models.run_request import RunRequestFile

class RunnerFileService():
  def createFile(self, filename: str, content: str) -> None:
    file = Path(f"{env.PROJECT_TMP_DIRECTORY}/{filename}");
    file.parent.mkdir(exist_ok=True, parents=True);
    file.write_text(content)

  def createFiles(self, files: List[RunRequestFile]) -> None:
    for file in files:
      self.createFile(file.fileName, file.content)

  def deleteFile(self, fileName: str) -> None:
    file = Path(f"{env.PROJECT_TMP_DIRECTORY}/{fileName}");
    file.unlink()

  def deleteFiles(self, files: List[RunRequestFile]) -> None:
    for file in files:
      self.deleteFile(file.fileName)
