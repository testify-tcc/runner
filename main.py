from fastapi import FastAPI
from models import RunRequest
from utils.file import createFiles, deleteDirectory
import docker
import os

DEBUG = False

DOCKER_JAVASCRIPT_JEST_IMAGE_NAME = 'vinigpereira/javascript-jest:latest'
DOCKER_JAVASCRIPT_JEST_TEST_COMMAND = 'jest'
DOCKER_CONTAINER_WORKDIR = '/sandbox'
TMP_DIRECTORY_NAME = 'tmp'
TMP_SANDBOX_DIRECTORY_PATH = f"{DOCKER_CONTAINER_WORKDIR}/tmp"

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Welcome to Testity!"}

@app.post("/run")
async def run(runRequest: RunRequest):
  currentPath = os.path.dirname(os.path.abspath(__file__))
  tmpDirectoryPath = f"{currentPath}/{TMP_DIRECTORY_NAME}"

  createFiles(tmpDirectoryPath, runRequest.files);

  logStream = None

  try:
    if DEBUG: print("Creating docker client")
    client = docker.from_env()
    if DEBUG: print("Pulling images")
    client.images.pull(DOCKER_JAVASCRIPT_JEST_IMAGE_NAME)
    if DEBUG: print("Running javascript container")
    container = client.containers.run(
      DOCKER_JAVASCRIPT_JEST_IMAGE_NAME,
      DOCKER_JAVASCRIPT_JEST_TEST_COMMAND,
      detach=True,
      working_dir=DOCKER_CONTAINER_WORKDIR,
      volumes=[f"{tmpDirectoryPath}:{TMP_SANDBOX_DIRECTORY_PATH}"]
    )
    if DEBUG: print("Saving the logstream")
    logStream = container.logs(stream=True);
    if DEBUG: print("Stopping container")
    container.stop()
    if DEBUG: print("Removing container")
    container.remove()    
  finally:
    if DEBUG: print("Deleting tmp directory")
    deleteDirectory(tmpDirectoryPath, runRequest.files)
  
  finalLog = ""

  try:
    while True:
      finalLog += next(logStream).decode("utf-8")
  except StopIteration:
    if DEBUG: print("log iteration stopped")

  return finalLog