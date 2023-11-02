import subprocess

template = {{ cookiecutter.template }}

print(f"#################### {template}")

if "cookiecutter-django" in template:
    subprocess.call(["git", "submodule", "init"], cwd="./cookiecutter-django")
    subprocess.call(["git", "submodule", "update"], cwd="./cookiecutter-django")
