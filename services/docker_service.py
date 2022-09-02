import env

from docker import DockerClient
from utils.docker_container import DockerContainer
from models.docker_image_name import DockerImageName
from builders.docker_container_builder import DockerContainerBuilder
from services.docker_image_name_service import DockerImageNameService

class DockerService():
  def __init__(
    self,
    dockerClient: DockerClient,
    dockerImageNameService: DockerImageNameService,
    dockerContainerBuilder: DockerContainerBuilder,
  ) -> None:
    self.dockerClient = dockerClient
    self.dockerImageNameService = dockerImageNameService
    self.dockerContainerBuilder = dockerContainerBuilder

  def pullImage(self, imageName: DockerImageName) -> None:
    processedImageName = self.dockerImageNameService.getProcessedImageName(imageName)
    self.dockerClient.images.pull(processedImageName)

  def runAndGetContainer(
    self,
    imageName: DockerImageName,
    testCommand: str
  ) -> DockerContainer:
    processedImageName = self.dockerImageNameService.getProcessedImageName(imageName)
    container = self.dockerClient.containers.run(
      processedImageName,
      testCommand,
      detach=True,
      working_dir=env.DOCKER_WORKDIR,
      volumes=[f"{env.PROJECT_TMP_DIRECTORY}:{env.DOCKER_TMP_DIRECTORY}"]
    )
    return self.dockerContainerBuilder.buildContainer(container)
