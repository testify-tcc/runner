from typing import List, Tuple
from models.docker_image_name import DockerImageName
from models.testing_environment import TestingEnvironment

class DockerImageMap(dict):
  def __init__(self):
    self.map = dict()

  def set(self, key: TestingEnvironment, value: DockerImageName) -> None:
    self.map[TestingEnvironment(key)] = value

  def get(self, key: TestingEnvironment) -> DockerImageName:
    return self.map[TestingEnvironment(key)]

class DockerImageMapService():
  def __init__(self, mappings: List[Tuple[TestingEnvironment, DockerImageName]]) -> None:
    self.dockerImageMap = DockerImageMap()

    for mapping in mappings:
      self.dockerImageMap.set(mapping[0], mapping[1])

  def getDockerImageFromTestingEnvironment(
    self,
    testingEnvironment: TestingEnvironment
  ) -> DockerImageName:
    return self.dockerImageMap.get(testingEnvironment)
