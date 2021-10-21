[![Build Status](https://travis-ci.com/OleBo/MathSo.svg?branch=main)](https://travis-ci.com/OleBo/MathSo)
[![Binder](http://mybinder.org/badge_logo.svg)](http://mybinder.org/v2/gh/OleBo/MathSo/main)
# MathSo
Lecture on numeric

## Prerequisit

[GitHub CLI](https://github.com/cli/cli) is required to clone repositories hosted on GitHub.com. [Poetry](https://python-poetry.org) is used for python packaging and dependency management. [Pyenv](https://github.com/pyenv/pyenv) lets you easily switch between multiple versions of Python.

### macOS

via [Homebrew](https://brew.sh/)

```console
brew install gh
brew install poetry
brew install pyenv
```

## Install

Our project is using python 3.9.7, so let's install it:

```console
pyenv install 3.9.7
```

Go to your project folder and clone a GitHub repository locally.

```console
gh repo clone OleBo/MathSo & cd MathSo
poetry install & poetry shell
```

The 'poetry install' reads the poetry.lock file from the current directory, processes it, and downloads and installs all the libraries and dependencies outlined in that file. If the file does not exist it will look for pyproject.toml and do the same.

The 'shell' command spawns a shell, according to the $SHELL environment variable, within the virtual environment. If one doesn’t exist yet, it will be created.

## Using Notebooks

The notebook extensions can be installed. They need to be copied to the Jupyter data directory. Then, the installed notebook extensions can be enabled, either by using built-in Jupyter commands, or more conveniently by using the 'jupyter_nbextensions_configurator' server extension, which is installed as a dependency of this repo.

```console
jupyter contrib nbextension install --user
jupyter nbextensions_configurator enable --user
jupyter nbextension enable toc2/main
jupyter nbextension enable collapsible_headings/main
jupyter nbextension enable highlight_selected_word/main
jupyter nbextension enable execute_time/ExecuteTime
```

Go to the notebooks folder and start Jupyter

```console
jupyter notebook
```

## Template and CI

The software development principles for this project are drawn from a [medium article by Trace Smith](https://medium.com/python-template-for-machine-learning-projects/integrating-software-development-principles-with-ml-projects-95c17794a561) and its [template repository](https://github.com/mleng-shared/python-ml-template).

In the project root, the project code is organized into the [main module](https://github.com/OleBo/MathSo/blob/main), [notebooks/](https://github.com/OleBo/MathSo/blob/main/notebooks), [math_so/](https://github.com/OleBo/MathSo/blob/main/math_so), additional executable scripts or helpers, [scripts/](https://github.com/OleBo/MathSo/blob/main/scripts), and unit or integration tests in [tests/](https://github.com/OleBo/MathSo/blob/main/tests). We generally follow the convention of placing our main shared executable code within the main module. Scripts are meant to be ad-hoc utilities run from the command line which may be used in setting up datasets or otherwise. An additional directory could also be added here containing infrastructure specific code (e.g. AzureML, AWS, Airflow, etc.).

### configuring the environment
In order to repoduce this framework we use
- [pyenv](https://github.com/pyenv/pyenv) - for managing the Python environment
- [poetry](https://github.com/python-poetry/poetry) - for managing required dependencies
### continuous integration (CI)
The [integration pipeline is configured](https://travis-ci.com/dashboard) to only run if code changes are being merged into the master branch. Thus, once a pull request is opened, the build will kick-off and the status of the run will be provided in the PR window opened in GitHub.

The build step will run the .travis.yml file located in the project repository which contains a series of commands to execute. Within this job, there are three tasks that will be checked:
- unit tests,
- code formatting and
- code linting.
Once the build is initiated from the opened pull request, you can monitor the runs in real-time.

### unit tests
We will utilize [pytest](https://docs.pytest.org/en/stable/) for writing and maintaining tests. The testing scripts should reside in the [tests](https://github.com/OleBo/MathSo/blob/main/tests/) directory within the project root. pytest expects the file names to begin with `test_` or end with `_test.py`. [Here](https://github.com/OleBo/MathSo/blob/main/tests/test_utils.py), we've adopted the naming convention `test_<name-of-task>.py`.

We will utilize [pytest-cov](https://pypi.org/project/pytest-cov/) to produce coverage results of your unit tests. Here, we can measure the percentage of the source code that the tests cover. To run pytest and pass the cov flag to output the coverage in order to have an idea on the completeness of the tests:

`pytest cov=python_ml_template/utils/ tests/`

### auto formating
To make sure code being merged into the master branch is maintaining [pep8](https://www.python.org/dev/peps/pep-0008/) standards, we use [autopep8](https://pypi.org/project/autopep8/). To format the source code files within the project, you can run this command:

`vautopep8 --in-place --aggressive --recursive <path>`

### linting
We use [flake8](https://pypi.org/project/flake8/) to identify syntactical and stylistic problems in your source code.

`flake8 path_to_check/`
