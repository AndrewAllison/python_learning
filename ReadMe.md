# Project Name

## Overview
This project demonstrates a lot of learning for python aimed at node developers. It has the use of pre-commit hooks for code formatting and linting with `black`, `flake8`, and `pylint`.

## Requirements

- Python 3.9+
- Virtual environment tool like `venv`
- `pip` for package management

## Prerequisites

Ensure that you have the following installed on your local machine:

- Python 3.9.6
- Git

Also, make sure you have a virtual environment tool like `venv`.

## Installation

Clone the repository:

Create and activate the virtual environment:

For macOS/Linux:
```bash
python3 -m venv venv source venv/bin/activate
```
For Windows:
```bash
py -m venv venv .\venv\Scripts\activate
```

Install the dependencies:
```bash
pip install -r requirements.txt
```

### Running the tests

```bash
pytest
```

### Running the pre-commit hook

```bash
pre-commit run --all-files
```
