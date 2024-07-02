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
def get_usernames(role):
    while True:
        usernames = input(f"Enter the GitHub usernames of {role} (comma-separated): ").strip()
        if usernames:
            return [username.strip() for username in usernames.split(',')]
        print("Please enter at least one username.")

# Helper function for addMaintainer() to format list of usernames
def format_usernames(usernames):
    return "".join(f"- @{username}\n" for username in usernames)

def addMaintainer():
    maintainers = get_usernames("MAINTAINERS")
    approvers = get_usernames("APPROVERS")
    reviewers = get_usernames("REVIEWERS")

    maintainers_file_path = "MAINTAINERS.md"

    with open(maintainers_file_path, "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if i + 1 < len(lines):
            if line.strip() == "## Maintainers:" and lines[i+1].strip() == "-":
                lines[i+1] = format_usernames(maintainers)
            elif line.strip() == "## Approvers:" and lines[i+1].strip() == "-":
                lines[i+1] = format_usernames(approvers)
            elif line.strip() == "## Reviewers:" and lines[i+1].strip() == "-":
                lines[i+1] = format_usernames(reviewers)

    with open(maintainers_file_path, "w") as f:
        f.writelines(lines)

    print("Maintainers, Approvers, and Reviewers have been added to MAINTAINERS.md")

if CREATE_REPO == "True":
    createGithubRepo()

if RECEIVE_UPDATES == "True":
    addTopic()

if ADD_MAINTAINER == "True":
    addMaintainer()
