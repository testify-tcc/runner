from typing import Any
from utils.docker_container import DockerContainer

class DockerContainerBuilder():
  def buildContainer(self, container: Any) -> DockerContainer:
    return DockerContainer(container)
