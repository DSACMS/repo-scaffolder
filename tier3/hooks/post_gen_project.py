import subprocess
import shutil
import os

REPO_NAME = '{{ cookiecutter.project_repo_name }}'
ORG_NAME = '{{ cookiecutter.project_org }}'
VISIBILITY = '{{cookiecutter.project_visibility}}'
DESCRIPTION = '{{cookiecutter.project_description}}'
CREATE_REPO = '{{cookiecutter.create_repo}}'
RECEIVE_UPDATES = '{{cookiecutter.receive_updates}}'
ADD_MAINTAINER = '{{cookiecutter.add_maintainer}}'

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
        "--add-topic=dsacms-tier3",
    ]
    subprocess.call(gh_cli_command)

# Helper function for addMaintainer() to get user input of usernames for Maintainer, Approver, and Reviewer
def getUsernames(role):
    while True:
        usernames = input(f"Enter the GitHub usernames of {role} (comma-separated): ").strip()
        if usernames:
            return [username.strip() for username in usernames.split(',')]
        print("Please enter at least one username.")

# Helper function for addMaintainer() to format list of usernames
def formatUsernames(usernames):
    return "".join(f"- @{username.lstrip('@')}\n" for username in usernames)

def addMaintainer():
    maintainers = getUsernames("MAINTAINERS")
    approvers = getUsernames("APPROVERS")
    reviewers = getUsernames("REVIEWERS")

    maintainers_file_path = "MAINTAINERS.md"

    with open(maintainers_file_path, "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.strip() == "## Maintainers:" and i + 2 < len(lines) and lines[i + 2].strip() == "-":
            lines[i + 2] = formatUsernames(maintainers)
        elif line.strip() == "## Approvers:" and i + 1 < len(lines) and lines[i + 1].strip() == "-":
            lines[i + 1] = formatUsernames(approvers)
        elif line.strip() == "## Reviewers:" and i + 1 < len(lines) and lines[i + 1].strip() == "-":
            lines[i + 1] = formatUsernames(reviewers)

    with open(maintainers_file_path, "w") as f:
        f.writelines(lines)

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
    
    if ADD_MAINTAINER == "True":
        addMaintainer()
    
    moveCookiecutterFile()
    
if __name__ == "__main__":
    main()
