# Twenty Questions

A fun project to teach programming in python. See the lessons at https://racingtadpole.github.io/twenty-questions/.

## Quick start

If you get stuck doing this, you can search for an online python interpreter and use it, eg. https://repl.it/languages/Python3.

### Install Visual Studio Code

Install Visual Studio Code, PyCharm or a similar editor.

### Install Python and pipenv

See the [pipenv documentation](https://docs.pipenv.org/install/) for the steps to install python 3, pip and pipenv.

On a Mac, you will need to install python 3 as described above (python 2 is the default).
The simplest way to install `pipenv` is to install homebrew, and then type `brew install pipenv`.
 
On linux, this [link](https://packaging.python.org/install_requirements_linux/#installing-pip-setuptools-wheel-with-linux-package-managers)
may be helpful.

### Install the Required Packages

Enter the `twenty-questions` directory, and type:

```
pipenv install --dev
```

This creates an environment containing the required packages, which you enter by typing:

```
pipenv shell
```

### Run the tests

In the pipenv environment, make sure this command runs without error:

```
bin/check_code
```
