import docker

from services.docker_service import DockerService
from services.runner_service import RunnerService
from services.runner_file_service import RunnerFileService
from services.docker_image_name_service import DockerImageNameService
from builders.docker_container_builder import DockerContainerBuilder

dockerClient = docker.from_env()
dockerImageNameService = DockerImageNameService()
dockerContainerBuilder = DockerContainerBuilder()
dockerService = DockerService(dockerClient, dockerImageNameService, dockerContainerBuilder)

runnerFileService = RunnerFileService()
runnerService = RunnerService(dockerService, runnerFileService)
