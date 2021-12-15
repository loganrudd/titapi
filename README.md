## Synopsis

A simple FastAPI to predict passenger survival aboard the Titanic.

## Installation

Creat a [Conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html) 
environment from environment.yml file:

`conda env create -n <name_of_env> -f environment.yml`

## Code Example

After activating the Conda environment, from the root of the project run the 
app with `uvicorn main:app` and then in another terminal run the test_request.py
to send test data to the API and return a prediction:

`python test_request.py`

## API Reference

https://fastapi.tiangolo.com/
