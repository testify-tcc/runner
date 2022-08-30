from pathlib import Path
from models import File
from typing import List

def createFile(path: str, fileName: str, content: str):
  file = Path(f"{path}/{fileName}");
  file.parent.mkdir(exist_ok=True, parents=True);
  file.write_text(content)

def createFiles(path: str, files: List[File]):
  for file in files:
    createFile(path, file.fileName, file.content)

def deleteFile(path: str, fileName: str):
  file = Path(f"{path}/{fileName}");
  file.unlink()

def deleteFiles(path: str, files: List[File]):
  for file in files:
    deleteFile(path, file.fileName)

def deleteDirectory(path: str, filesToDelete: List[File]):
  deleteFiles(path, filesToDelete)
  pathClient = Path(path)
  pathClient.rmdir()

def createFilesRunCallbackAndDeleteThem(directoryPath: str, files: List[File], callback):
  createFiles(directoryPath, files);

  try:
    callback()
  finally:
    deleteDirectory(directoryPath, files)
