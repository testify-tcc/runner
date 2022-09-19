import os

DOCKER_HUB_PROFILE = "vinigpereira"
CLIENT_DEV_ENDPOINT = "http://localhost:8080"
CLIENT_PROD_ENDPOINT = "https://imeusp-testify.netlify.app/"
PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
DOCKER_WORKDIR = "/sandbox"
DOCKER_TMP_DIRECTORY = f"{DOCKER_WORKDIR}/tmp"
PROJECT_TMP_DIRECTORY = f"{PROJECT_ROOT_PATH}/tmp"
