import subprocess

subprocess.call(["git", "submodule", "init", "-b", "main"], cwd="./cookiecutter-django")
