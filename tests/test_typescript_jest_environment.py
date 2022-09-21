from client_test import client

def testPassingTest():
  response = client.post('/', json={
    "testingEnvironment": "typescript-jest",
    "testCommand": "jest",
    "files": [
      {
        "name": "sum.ts",
        "content": "'use strict';\n\nexport function sum(a: number, b: number): number {\n  return a + b;\n}"
      },
      {
        "name": "sum.test.ts",
        "content": "import { sum } from './sum';\n\n'use strict';\n\ntest('should return proper result', () => {\n  expect(sum(1, 1)).toBe(2);\n});"
      }
    ]
  });

  responseBody = response.json()
  output = responseBody['output']

  assert "PASS" in output

def testFailingTest():
  response = client.post('/', json={
    "testingEnvironment": "typescript-jest",
    "testCommand":  "jest",
    "files": [
      {
        "name": "sum.ts",
        "content": "'use strict';\n\nexport function sum(a: number, b: number): number {\n  return a + b;\n}"
      },
      {
        "name": "sum.test.ts",
        "content": "import { sum } from './sum';\n\n'use strict';\n\ntest('should return proper result', () => {\n  expect(sum(1, 2)).toBe(2);\n});"
      }
    ]
  });

  responseBody = response.json()
  output = responseBody['output']

  assert "FAIL" in output
