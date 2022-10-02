from bootstrap import bootstrap
from dependency_container import runnerService
from models.run_request import RunRequestBody, RunRequestResponse

app = bootstrap()

@app.post("/", response_model=RunRequestResponse)
def run(body: RunRequestBody) -> RunRequestResponse:
  print(body)
  return runnerService.run(body)
