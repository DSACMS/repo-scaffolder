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
        "--add-topic=dsacms-tier0",
    ]
    subprocess.call(gh_cli_command)

def addMaintainer():
    maintainers = []
    add_maintainer = True
    while add_maintainer:
        maintainer = {}
        maintainer["role"] = input("Maintainer's Role (Reviewer, Approver, Maintainer): ").strip()
        maintainer["name"] = input("Maintainer's Name: ").strip()
        maintainer["github_username"] = input("Maintainer's GitHub Username: ").strip()
        maintainer["affiliation"] = input("Maintainer's Affiliation (DSAC, CCSQ, CMMI, etc...): ").strip()
        maintainers.append(maintainer)

        while True:
            add_maintainer_input = input("Would you like to add another maintainer? (yes/no): ").strip().lower()
            if add_maintainer_input in ("yes", "y", "no", "n"):
                # If input is "yes" or "y", then add_maintainer is True and main loop continues, vise versa
                add_maintainer = add_maintainer_input in ("yes", "y")
                break
            else:
                print("\nInvalid response, please respond with: 'yes', 'y', 'no', or 'n'")

    maintainers_table = ""
    for maintainer in maintainers:
        maintainers_table += f"| {maintainer["role"]} | {maintainer["name"]}| {maintainer["github_username"]} | {maintainer["affiliation"]} |\n"

    proj_name = "{{ cookiecutter.project_name }}"
    maintainers_file_path = f"../{proj_name}/MAINTAINERS.md"

    with open(maintainers_file_path, "r") as f:
        lines = f.readlines()

    with open(maintainers_file_path, "w") as f:
        in_table = False
        for line in lines:
            if "| {role} | {names} | {github usernames} | {affiliations}|" in line:
                in_table = True
                f.write(maintainers_table)  # Replace placeholder line with new table of maintainers
            elif in_table and line.strip() == "":
                in_table = False
            if not in_table:
                f.write(line)

if CREATE_REPO == "True":
    createGithubRepo()

if RECEIVE_UPDATES == "True":
    addTopic()

if ADD_MAINTAINER == "True":
    addMaintainer()