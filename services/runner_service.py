from models.docker_image_name import DockerImageName
from models.run_request import RunRequestBody, RunRequestResponse
from services.docker_service import DockerService
from services.runner_file_service import RunnerFileService

class RunnerService():
  def __init__(
    self,
    dockerService: DockerService,
    runnerFileService: RunnerFileService,
  ) -> None:
    self.dockerService = dockerService
    self.runnerFileService = runnerFileService

  def run(self, body: RunRequestBody) -> RunRequestResponse:
    files = body.files
    testCommand = body.testCommand
    dockerImageName = body.testingEnvironment

    self.runnerFileService.createFiles(files)

    dockerContainerOutput = self.runTestAndGetOutput(dockerImageName, testCommand)

    self.runnerFileService.deleteDirectory(files)

    return { 'passed': True, 'output': dockerContainerOutput }

  def runTestAndGetOutput(self, dockerImageName: DockerImageName, testCommand: str) -> str:
    self.dockerService.pullImage(dockerImageName)
    dockerContainer = self.dockerService.runAndGetContainer(dockerImageName, testCommand)
    dockerContainerLogStream = dockerContainer.logs()
    dockerContainer.stop()
    dockerContainer.remove()
    
    dockerContainerOutput = ""

    try:
      while True:
        dockerContainerOutput += next(dockerContainerLogStream).decode("utf-8")
    except StopIteration:
      pass

    return dockerContainerOutput