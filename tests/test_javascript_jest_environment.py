from client_test import client

def testPassingTest():
  response = client.post('/', json={
    "testingEnvironment": "javascript-jest",
    "testCommand": "jest",
    "files": [
      {
        "fileName": "sum.js",
        "content": "\"use strict\";\n\nfunction sum(a, b) {\n  return a + b;\n}\n\nmodule.exports = { sum };\n"
      },
      {
        "fileName": "sum.test.js",
        "content": "\"use strict\";\n\nconst { sum } = require(\"./sum.js\");\n\ntest(\"should return proper "
                   "result\", () => {\n  expect(sum(1, 1)).toBe(2);\n  expect(sum(-1, 1)).toBe(0);\n  expect(sum(-1, "
                   "-1)).toBe(-2);\n});"
      }
    ]
  })

  responseBody = response.json()
  output = responseBody['output']

  assert "PASS" in output


def testFailingTest():
  response = client.post('/', json={
    "testingEnvironment": "javascript-jest",
    "testCommand": "jest",
    "files": [
      {
        "fileName": "sum.js",
        "content": "\"use strict\";\n\nfunction sum(a, b) {\n  return a + b;\n}\n\nmodule.exports = { sum };\n"
      },
      {
        "fileName": "sum.test.js",
        "content": "\"use strict\";\n\nconst { sum } = require(\"./sum.js\");\n\ntest(\"should return proper "
                   "result\", () => {\n  expect(sum(1, 1)).toBe(1);\n  expect(sum(-1, 1)).toBe(2);\n  expect(sum(-1, "
                   "-1)).toBe(-2);\n});"
      }
    ]
  })

  responseBody = response.json()
  output = responseBody['output']

  assert "FAIL" in output