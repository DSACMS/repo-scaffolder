import subprocess

REPO_NAME = '{{ cookiecutter.project_repo_name }}'
ORG_NAME = '{{ cookiecutter.project_org }}'
VISIBILITY = '{{cookiecutter.project_visibility}}'
DESCRIPTION = '{{cookiecutter.project_description}}'
CREATE_REPO = '{{cookiecutter.create_repo}}'
RECEIVE_UPDATES = '{{cookiecutter.receive_updates}}'
ADD_MAINTAINER = '{{cookiecutter.add_maintainer}}'

def createGithubRepo():
    subprocess.call(["git", "init", "-b", "main"])
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-m", "first commit"])
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

    in_maintainers, in_approvers, in_reviewers = False, False, False
    for i, line in enumerate(lines):
        if line.strip() == "## Maintainers:":
            in_maintainers = True
        elif line.strip() == "## Approvers:":
            in_approvers = True
        elif line.strip() == "## Reviewers:":
            in_reviewers = True
        elif in_maintainers and line.strip() == "-":
            lines[i] = formatUsernames(maintainers)
            in_maintainers = False
        elif in_approvers and line.strip() == "-":
            lines[i] = formatUsernames(approvers)
            in_approvers = False
        elif in_reviewers and line.strip() == "-":
            lines[i] = formatUsernames(reviewers)
            in_reviewers = False

    with open(maintainers_file_path, "w") as f:
        f.writelines(lines)

    print("Maintainers, Approvers, and Reviewers have been added to MAINTAINERS.md")

if CREATE_REPO == "True":
    createGithubRepo()

if RECEIVE_UPDATES == "True":
    addTopic()

if ADD_MAINTAINER == "True":
    addMaintainer()
