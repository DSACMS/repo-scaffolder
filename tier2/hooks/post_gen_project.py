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
        "--add-topic=dsacms-tier2",
    ]
    subprocess.call(gh_cli_command)

def addMaintainer():
    maintainers = []
    add_maintainer = True
    while add_maintainer:
        maintainer = {}
        maintainer["role"] = input("Maintainer's Role (Reviewer, Approver, Maintainer): ").strip()
        maintainer["name"] = input("Maintainer's Name: ").strip()
        github_username = input("Maintainer's GitHub Username: ").strip()
        maintainer["github_username"] = github_username if github_username.startswith('@') else f'@{github_username}'
        maintainer["affiliation"] = input("Maintainer's Affiliation (DSAC, CCSQ, CMMI, etc...): ").strip()
        maintainers.append(maintainer)

        while True:
            add_maintainer_input = input("Would you like to add another maintainer? [Y/n]: ").strip().lower()
            if add_maintainer_input in ("y", "yes", ""):
                add_maintainer = True
                break
            elif add_maintainer_input in ("n", "no"):
                add_maintainer = False
                break
            else:
                print("\nInvalid response, please respond with: 'y', 'yes', 'n', 'no', or just press Enter for yes")

    maintainers_table = ""
    for maintainer in maintainers:
        maintainers_table += f"| {maintainer["role"]} | {maintainer["name"]}| {maintainer["github_username"]} | {maintainer["affiliation"]} |\n"

    proj_name = "{{ cookiecutter.project_name }}"
    maintainers_file_path = f"../{proj_name}/MAINTAINERS.md"

    with open(maintainers_file_path, "r") as f:
        lines = f.readlines()

    with open(maintainers_file_path, "w") as f:
        for line in lines:
            if "| {role} | {names} | {github usernames} | {affiliations}|" in line:
                f.write(maintainers_table)  # Replace placeholder line with new table of maintainers
            else:
                f.write(line)

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