import docker
from models.docker_image_name import DockerImageName
from models.testing_environment import TestingEnvironment

from services.docker_service import DockerService
from services.runner_service import RunnerService
from services.runner_file_service import RunnerFileService
from services.docker_image_name_service import DockerImageNameService
from services.docker_image_map_service import DockerImageMapService
from builders.docker_container_builder import DockerContainerBuilder

dockerClient = docker.from_env()
dockerImageNameService = DockerImageNameService()
dockerContainerBuilder = DockerContainerBuilder()
dockerService = DockerService(dockerClient, dockerImageNameService, dockerContainerBuilder)

dockerImageMapService = DockerImageMapService([
  (TestingEnvironment.JAVASCRIPT_JEST, DockerImageName.JAVASCRIPT_JEST),
  (TestingEnvironment.TYPESCRIPT_JEST, DockerImageName.TYPESCRIPT_JEST),
])

runnerFileService = RunnerFileService()
runnerService = RunnerService(dockerService, runnerFileService, dockerImageMapService)
