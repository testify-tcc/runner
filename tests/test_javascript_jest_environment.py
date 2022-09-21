from client_test import client

def testPassingTest():
  response = client.post('/', json={
    "testingEnvironment": "javascript-jest",
    "testCommand": "jest",
    "files": [
      {
        "name": "sum.js",
        "content": "'use strict';\n\nfunction sum(a, b) {\n  return a + b;\n}\n\nmodule.exports = { sum };"
      },
      {
        "name": "sum.test.js",
        "content": "const { sum } = require('./sum.js');\n\n'use strict';\n\ntest('should return proper result', () => {\n  expect(sum(1, 1)).toBe(2);\n});"
      }
    ]
  });

  responseBody = response.json()
  output = responseBody['output']

  assert "PASS" in output

def testFailingTest():
  response = client.post('/', json={
    "testingEnvironment": "javascript-jest",
    "testCommand": "jest",
    "files": [
      {
        "name": "sum.js",
        "content": "'use strict';\n\nfunction sum(a, b) {\n  return a + b;\n}\n\nmodule.exports = { sum };"
      },
      {
        "name": "sum.test.js",
        "content": "const { sum } = require('./sum.js');\n\n'use strict';\n\ntest('should return proper result', () => {\n  expect(sum(1, 2)).toBe(2);\n});"
      }
    ]
  });

  responseBody = response.json()
  output = responseBody['output']

  assert "FAIL" in output