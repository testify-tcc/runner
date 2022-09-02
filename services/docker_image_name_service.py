import env

from models.docker_image_name import DockerImageName

class DockerImageNameService():
  def getProcessedImageName(self, imageName: DockerImageName):
    return f"{env.DOCKER_HUB_PROFILE}/{imageName}:latest"

