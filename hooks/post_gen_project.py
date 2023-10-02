import re
import sys
import subprocess

REPO_NAME = '{{ cookiecutter.project_repo_name }}'
VISIBILITY = '{{cookiecutter.project_visibility}}'
DESCRIPTION = '{{cookiecutter.project_description}}'

if not re.match(r'^[-._a-zA-Z0-9]+$', REPO_NAME):
    print(f'ERROR: {REPO_NAME} is not a valid Python module name!')
    sys.exit(1)

if VISIBILITY not in ["public", "private", "internal"]:
    print(f'ERROR: {VISIBILITY} is not a valid visibility for github, it must be one of "public", "private" or "internal"')
    sys.exit(1)

def check_dependencies() -> bool:
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
    except subprocess.CalledProcessError as exception:
        print(f"ERROR: git failed with exit code: {exception.returncode}. (is git installed?)")
        return False
    try:
        subprocess.run(["gh", "--version"], capture_output=True, check=True)
        return True
    except subprocess.CalledProcessError as exception:
        print(f"ERROR: gh failed with exit code {exception.returncode}. (is gh installed? gh is github CLI)")
        return False

if not check_dependencies():
    sys.exit(1)

subprocess.call(["git", "init", "-b", "main"])
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "first commit"])

gh_cli_command = [
    "gh", "repo", "create",
    f"{REPO_NAME}",
    f"--{VISIBILITY}",
    f"--description={DESCRIPTION}",
]
subprocess.call(gh_cli_command)

subprocess.call(["git", "push", "--set-upstream", "origin", "main"])
