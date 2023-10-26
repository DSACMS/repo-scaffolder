import subprocess

subprocess.call(["git", "submodule", "init"], cwd="./cookiecutter-django")
subprocess.call(["git", "submodule", "update"], cwd="./cookiecutter-django")
