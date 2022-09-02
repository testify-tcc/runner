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
      self.createFile(file.name, file.content)

  def deleteFile(self, fileName: str) -> None:
    file = Path(f"{env.PROJECT_TMP_DIRECTORY}/{fileName}");
    file.unlink()

  def deleteFiles(self, files: List[RunRequestFile]) -> None:
    for file in files:
      self.deleteFile(file.name)

  def deleteDirectory(self, filesToDelete: List[RunRequestFile]) -> None:
    self.deleteFiles(filesToDelete)
    pathClient = Path(env.PROJECT_TMP_DIRECTORY)
    pathClient.rmdir()
