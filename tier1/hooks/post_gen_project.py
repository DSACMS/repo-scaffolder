import subprocess
import shutil
import os

REPO_NAME = '{{ cookiecutter.project_repo_name }}'
ORG_NAME = '{{ cookiecutter.project_org }}'
VISIBILITY = '{{cookiecutter.project_visibility}}'
DESCRIPTION = '{{cookiecutter.project_description}}'
CREATE_REPO = '{{cookiecutter.create_repo}}'
RECEIVE_UPDATES = '{{cookiecutter.receive_updates}}'

def createGithubRepo():
    gh_cli_command = [
        "gh", "repo", "create",
        f"{ORG_NAME}/{REPO_NAME}",
        "--source=.",
        f"--{VISIBILITY}",
        "--push",
        f"--description={DESCRIPTION}",
    ]
    subprocess.call(gh_cli_command)
    subprocess.call(["git", "push", "--set-upstream", "origin", "main"])

def addTopic():
    gh_cli_command = [
        "gh", "repo", "edit",
        f"{ORG_NAME}/{REPO_NAME}",
        "--add-topic=dsacms-tier1",
    ]
    subprocess.call(gh_cli_command)

def moveCookiecutterFile(): 
    github_dir = os.path.join(os.getcwd(), ".github")
    os.chdir(github_dir)

    source_path = "cookiecutter.json"
    destination_dir = "codejson"
    destination_path = os.path.join(destination_dir, "cookiecutter.json")

    shutil.move(source_path, destination_path)

def main():
    subprocess.call(["git", "init", "-b", "main"])
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-m", "initial commit"])
    
    if CREATE_REPO == "True":
        createGithubRepo()

    if RECEIVE_UPDATES == "True":
        addTopic()
    
    moveCookiecutterFile()
    
if __name__ == "__main__":
    main()
