from interfaces.test_verifier_interface import TestVerifierInterface

class TypescriptJestTestVerifier(TestVerifierInterface):
  def testPassed(self, testOutput: str) -> bool:
    return "PASS" in testOutput
