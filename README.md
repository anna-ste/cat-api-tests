# Testing API with pytest 

## Setup execution environment
1. Install Python 3.9 

The most reliable way of python3 installation is by downloading relevant python installer for your platform from the official site.
It supports all existing and popular platforms. Go to https://www.python.org/downloads/ and find platform specific installer.
It will handle all the system links, paths, pip linking automatically.

2. To install dependencies run `pip install -r requirements.txt`

## Global variables

* Ways of setting variables: 
    1. In `config` create file `settings_local.json` and copy content of `settings.json`. In `settings_local.json` you can set necessary values for variables used in framework such as `api_key`.
    2. Set environment variables. Use same naming as in `settings.json`, but capital letters, for example, if in `settings.json` we have `api_key`, environment variable should be named `API_KEY`.
   

* Priority of execution:
    1. `settings.json` will be overwritten by `settings_local.json`.
    2. `settings_local.json` will be overwritten by environment variables.


## API selected for testing 

https://docs.thecatapi.com/


## Implemented tests
Tests in `test_categories.py` check list categories api, validate list category json schema  (GET method)

Tests in `test_votes.py` check delete categories api (DELETE method)


## Execution

To execute tests run:

$ pytest

## CI Integration
Tests are integrated into Travis CI: (see `.travis.yml`)  

Tests are integrated into GitHub Actions (see `.github/worklows/python-yaml.app`)
