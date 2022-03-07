# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import papermill as pm
import tempfile
import os.path
import tempfile

NB_URL = "{{cookiecutter.notebook_url}}"

def main(message) -> str:
    logging.info(
        "Notebook running activity function started."
    )
    logging.info(
        f"Message: {message}"
    )

    message_body = message

    input_path = NB_URL

    params = message_body.get("params")

    output_path = os.path.join(
        tempfile.gettempdir(), "output.ipynb"
    )

    returned_notebook = pm.execute_notebook(
        input_path=input_path,
        output_path=output_path,
        parameters=params
    )

    return returned_notebook
    


