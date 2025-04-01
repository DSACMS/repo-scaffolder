import subprocess
import shutil
import os

REPO_NAME = '{{ cookiecutter.project_repo_name }}'
ORG_NAME = '{{ cookiecutter.project_org }}'
VISIBILITY = '{{cookiecutter.project_visibility}}'
DESCRIPTION = '{{cookiecutter.project_description}}'
CREATE_REPO = '{{cookiecutter.create_repo}}'
RECEIVE_UPDATES = '{{cookiecutter.receive_updates}}'
ADD_TEAM = '{{cookiecutter.add_team}}'
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
    print("ℹ️ Creating a list of maintainers, approvers, and reviewers")
    maintainers = getUsernames("MAINTAINERS")
    approvers = getUsernames("APPROVERS")
    reviewers = getUsernames("REVIEWERS")

    community_file_path = "COMMUNITY.md"

    with open(community_file_path, "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.strip() == "### Maintainers:" and i + 2 < len(lines) and lines[i + 2].strip() == "-":
            lines[i + 2] = formatUsernames(maintainers)
        elif line.strip() == "### Approvers:" and i + 2 < len(lines) and lines[i + 2].strip() == "-":
            lines[i + 2] = formatUsernames(approvers)
        elif line.strip() == "### Reviewers:" and i + 2 < len(lines) and lines[i + 2].strip() == "-":
            lines[i + 2] = formatUsernames(reviewers)

    with open(community_file_path, "w") as f:
        f.writelines(lines)

def addTeam():
    print("ℹ️ Creating a table of project team members")
    team = []
    add_member = True
    while add_member:
        member = {}
        member["role"] = input("Project Member's Role (Engineer, Project Lead, COR, etc...): ").strip()
        member["name"] = input("Project Member's Name: ").strip()
        member["affiliation"] = input("Project Member's Affiliation (DSAC, CCSQ, CMMI, etc...): ").strip()
        team.append(member)

        while True:
            add_member_input = input("Would you like to add another project member? [Y/n]: ").strip().lower()
            if add_member_input in ("y", "yes", ""):
                add_member = True
                break
            elif add_member_input in ("n", "no"):
                add_member = False
                break
            else:
                print("\nInvalid response, please respond with: 'y', 'yes', 'n', 'no', or just press Enter for yes")

    team_table = ""
    for member in team:
        team_table += f"| {member["role"]} | {member["name"]} | {member["affiliation"]} |\n"

    community_file_path = f"COMMUNITY.md"

    with open(community_file_path, "r") as f:
        lines = f.readlines()

    with open(community_file_path, "w") as f:
        for line in lines:
            if "| {role} | {names} | {affiliations} |" in line:
                f.write(team_table)  # Replace placeholder line with new table of project team members
            else:
                f.write(line)

def moveCookiecutterFile(): 
    original_dir = os.getcwd()

    try:
        github_dir = os.path.join(original_dir, ".github")
        os.chdir(github_dir)

        source_path = "cookiecutter.json"
        destination_dir = "codejson"
        destination_path = os.path.join(destination_dir, "cookiecutter.json")

        shutil.move(source_path, destination_path)
    
    finally:
        # Moves back to project dir
        os.chdir(original_dir)

def main():
    if ADD_TEAM == "True":
        addTeam()

    if ADD_MAINTAINER == "True":
        addMaintainer()

    moveCookiecutterFile()
        
    subprocess.call(["git", "init", "-b", "main"])
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-m", "initial commit"])

    if CREATE_REPO == "True":
        createGithubRepo()

    if RECEIVE_UPDATES == "True":
        addTopic()
    
if __name__ == "__main__":
    main()
