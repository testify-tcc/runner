from models.docker_image_name import DockerImageName
from models.testing_environment import TestingEnvironment

class DockerImageMap(dict):
  def __setitem__(self, key: TestingEnvironment, value: DockerImageName) -> None:
    return super().__setitem__(TestingEnvironment(key), value)

  def __getitem__(self, key: TestingEnvironment) -> DockerImageName:
    return super().__getitem__(TestingEnvironment(key))

class TestingEnvironmentService():
  def __init__(self) -> None:
    self.dockerImagesMap = DockerImageMap()
    self.dockerImagesMap[TestingEnvironment.JAVASCRIPT_JEST] = DockerImageName.JAVASCRIPT_JEST

  def getDockerImageFromTestingEnvironment(self, testingEnvironment: TestingEnvironment) -> DockerImageName:
    return self.dockerImagesMap[testingEnvironment]
