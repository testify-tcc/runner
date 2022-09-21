from interfaces.test_verifier_interface import TestVerifierInterface

class JavascriptJestTestVerifier(TestVerifierInterface):
  def testPassed(self, testOutput: str) -> bool:
    return "PASS" in testOutput
