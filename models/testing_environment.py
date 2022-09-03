from enum import Enum


class TestingEnvironment(str, Enum):
  JAVASCRIPT_JEST = "javascript-jest"
  TYPESCRIPT_JEST = "typescript-jest"