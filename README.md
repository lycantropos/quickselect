quickselect
===========

[![](https://travis-ci.com/lycantropos/quickselect.svg?branch=master)](https://travis-ci.com/lycantropos/quickselect "Travis CI")
[![](https://dev.azure.com/lycantropos/quickselect/_apis/build/status/lycantropos.quickselect?branchName=master)](https://dev.azure.com/lycantropos/quickselect/_build/latest?definitionId=24&branchName=master "Azure Pipelines")
[![](https://readthedocs.org/projects/quickselect/badge/?version=latest)](https://quickselect.readthedocs.io/en/latest "Documentation")
[![](https://codecov.io/gh/lycantropos/quickselect/branch/master/graph/badge.svg)](https://codecov.io/gh/lycantropos/quickselect "Codecov")
[![](https://img.shields.io/github/license/lycantropos/quickselect.svg)](https://github.com/lycantropos/quickselect/blob/master/LICENSE "License")
[![](https://badge.fury.io/py/quickselect.svg)](https://badge.fury.io/py/quickselect "PyPI")

In what follows
- `python` is an alias for `python3.5` or any later
version (`python3.6` and so on),
- `pypy` is an alias for `pypy3.5` or any later
version (`pypy3.6` and so on).

Installation
------------

Install the latest `pip` & `setuptools` packages versions:
- with `CPython`
  ```bash
  python -m pip install --upgrade pip setuptools
  ```
- with `PyPy`
  ```bash
  pypy -m pip install --upgrade pip setuptools
  ```

### User

Download and install the latest stable version from `PyPI` repository:
- with `CPython`
  ```bash
  python -m pip install --upgrade quickselect
  ```
- with `PyPy`
  ```bash
  pypy -m pip install --upgrade quickselect
  ```

### Developer

Download the latest version from `GitHub` repository
```bash
git clone https://github.com/lycantropos/quickselect.git
cd quickselect
```

Install dependencies:
- with `CPython`
  ```bash
  python -m pip install --force-reinstall -r requirements.txt
  ```
- with `PyPy`
  ```bash
  pypy -m pip install --force-reinstall -r requirements.txt
  ```

Install:
- with `CPython`
  ```bash
  python setup.py install
  ```
- with `PyPy`
  ```bash
  pypy setup.py install
  ```

Usage
-----
```python
>>> from quickselect import floyd_rivest, hoare
>>> sequence = list(range(-100, 101))
>>> key = abs
>>> (floyd_rivest.nth_largest(sequence, 0, key=key)
...  == hoare.nth_largest(sequence, 0, key=key)
...  == max(sequence, key=key))
True
>>> (floyd_rivest.nth_smallest(sequence, 0, key=key)
...  == hoare.nth_smallest(sequence, 0, key=key)
...  == min(sequence, key=key))
True

```

Development
-----------

### Bumping version

#### Preparation

Install
[bump2version](https://github.com/c4urself/bump2version#installation).

#### Pre-release

Choose which version number category to bump following [semver
specification](http://semver.org/).

Test bumping version
```bash
bump2version --dry-run --verbose $CATEGORY
```

where `$CATEGORY` is the target version number category name, possible
values are `patch`/`minor`/`major`.

Bump version
```bash
bump2version --verbose $CATEGORY
```

This will set version to `major.minor.patch-alpha`. 

#### Release

Test bumping version
```bash
bump2version --dry-run --verbose release
```

Bump version
```bash
bump2version --verbose release
```

This will set version to `major.minor.patch`.

### Running tests

Install dependencies:
- with `CPython`
  ```bash
  python -m pip install --force-reinstall -r requirements-tests.txt
  ```
- with `PyPy`
  ```bash
  pypy -m pip install --force-reinstall -r requirements-tests.txt
  ```

Plain
```bash
pytest
```

Inside `Docker` container:
- with `CPython`
  ```bash
  docker-compose --file docker-compose.cpython.yml up
  ```
- with `PyPy`
  ```bash
  docker-compose --file docker-compose.pypy.yml up
  ```

`Bash` script (e.g. can be used in `Git` hooks):
- with `CPython`
  ```bash
  ./run-tests.sh
  ```
  or
  ```bash
  ./run-tests.sh cpython
  ```

- with `PyPy`
  ```bash
  ./run-tests.sh pypy
  ```

`PowerShell` script (e.g. can be used in `Git` hooks):
- with `CPython`
  ```powershell
  .\run-tests.ps1
  ```
  or
  ```powershell
  .\run-tests.ps1 cpython
  ```
- with `PyPy`
  ```powershell
  .\run-tests.ps1 pypy
  ```
