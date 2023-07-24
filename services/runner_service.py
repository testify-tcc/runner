from types import NoneType
from builders.test_verifier_builder import TestVerifierBuilder
from models.docker_image_name import DockerImageName
from models.run_request import RunRequestBody, RunRequestResponse
from services.docker_service import DockerService
from services.runner_file_service import RunnerFileService
from services.docker_image_map_service import DockerImageMapService

class RunnerService():
  def __init__(
    self,
    dockerService: DockerService,
    runnerFileService: RunnerFileService,
    dockerImageMapService: DockerImageMapService,
    testVerifierBuider: TestVerifierBuilder,
  ) -> None:
    self.dockerService = dockerService
    self.runnerFileService = runnerFileService
    self.dockerImageMapService = dockerImageMapService
    self.testVerifierBuider = testVerifierBuider

  def run(self, body: RunRequestBody) -> RunRequestResponse:
    files = body.files
    testCommand = body.testCommand
    dockerImageName = self.dockerImageMapService.getDockerImageFromTestingEnvironment(body.testingEnvironment)
    testVerifier = self.testVerifierBuider.build(body.testingEnvironment)

    self.runnerFileService.createFiles(files)

    dockerContainerOutput = self.runTestAndGetOutput(dockerImageName, testCommand)

    testPassed = None

    if testVerifier is not None:
      testPassed = testVerifier.testPassed(dockerContainerOutput);

    self.runnerFileService.deleteFiles(files)

    return { 'passed': testPassed, 'output': dockerContainerOutput }

  def runTestAndGetOutput(self, dockerImageName: DockerImageName, testCommand: str) -> str:
    dockerContainer = self.dockerService.runAndGetContainer(dockerImageName, testCommand)
    dockerContainerLogStream = dockerContainer.logs()
    
    dockerContainerOutput = ""

    try:
      while True:
        dockerContainerOutput += next(dockerContainerLogStream).decode("utf-8")
    except StopIteration:
      pass

    return dockerContainerOutput