from client_test import client

def testPassingTest():
  response = client.post('/', json={
    "testingEnvironment": "typescript-jest",
    "testCommand": "jest",
    "files": [
      {
        "fileName": "sum.ts",
        "content": "\"use strict\";\n\nexport function sum(a: number, b: number): number {\n  return a + b;\n}\n"
      },
      {
        "fileName": "sum.test.ts",
        "content": "\"use strict\";\n\nimport { sum } from \"./sum\";\n\ntest(\"should return proper result\", "
                   "() => {\n  expect(sum(1, 1)).toBe(2);\n  expect(sum(-1, 1)).toBe(0);\n  expect(sum(-1, "
                   "-1)).toBe(-2);\n});"
      }
    ]
  })

  responseBody = response.json()
  output = responseBody['output']

  assert "PASS" in output

def testFailingTest():
  response = client.post('/', json={
    "testingEnvironment": "typescript-jest",
    "testCommand": "jest",
    "files": [
      {
        "fileName": "sum.ts",
        "content": "\"use strict\";\n\nexport function sum(a: number, b: number): number {\n  return a + b;\n}\n"
      },
      {
        "fileName": "sum.test.ts",
        "content": "\"use strict\";\n\nimport { sum } from \"./sum\";\n\ntest(\"should return proper result\", "
                   "() => {\n  expect(sum(1, 1)).toBe(3);\n  expect(sum(-1, 1)).toBe(2);\n  expect(sum(-1, "
                   "-1)).toBe(-1);\n});"
      }
    ]
  })

  responseBody = response.json()
  output = responseBody['output']

  assert "FAIL" in output
