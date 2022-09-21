from typing import Optional
from models.testing_environment import TestingEnvironment
from interfaces.test_verifier_interface import TestVerifierInterface
from services.test_verifiers.javascript_jest_test_verifier import JavascriptJestTestVerifier
from services.test_verifiers.typescript_jest_test_verifier import TypescriptJestTestVerifier


class TestVerifierBuilder():
  def build(self, testingEnvironment: TestingEnvironment) -> Optional[TestVerifierInterface]:
    if testingEnvironment == TestingEnvironment.JAVASCRIPT_JEST:
      return JavascriptJestTestVerifier()
    elif testingEnvironment == TestingEnvironment.TYPESCRIPT_JEST:
      return TypescriptJestTestVerifier()
    else:
      return None
