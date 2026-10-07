import subprocess
import shutil
import os
import re

REPO_NAME = '{{ cookiecutter.project_repo_name }}'
ORG_NAME = '{{ cookiecutter.project_org }}'
VISIBILITY = '{{cookiecutter.project_visibility}}'
DESCRIPTION = '{{cookiecutter.project_description}}'
CREATE_REPO = '{{cookiecutter.create_repo}}'
EXTRA_REPO_TOPICS = '{{cookiecutter.extra_repo_topics}}'
ADD_TEAM = '{{cookiecutter.add_team}}'
MATURITY_TIER = "tier1"

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

def normalize_topic(topic):
    topic = topic.strip().lower()
    topic = re.sub(r"[\s_]+", "-", topic)
    topic = re.sub(r"[^a-z0-9-]", "", topic)
    topic = re.sub(r"-+", "-", topic)

    return topic.strip("-")


def get_repo_topics():
    org_topic = normalize_topic(
        f"{ORG_NAME}-{MATURITY_TIER}"
    )

    topics = [org_topic]

    for topic in EXTRA_REPO_TOPICS.split(","):
        normalized_topic = normalize_topic(topic)

        if normalized_topic and normalized_topic not in topics:
            topics.append(normalized_topic)

    return topics

def addTopics():
    topics = get_repo_topics()
    gh_cli_command = [
        "gh", "repo", "edit",
        f"{ORG_NAME}/{REPO_NAME}",
    ]
    for topic in topics:
        gh_cli_command.append(f"--add-topic={topic}")
    subprocess.call(gh_cli_command)

def addTeam():
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
        team_table += f"""| {member["role"]} | {member["name"]} | {member["affiliation"]} |\n"""

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

    moveCookiecutterFile()
    
    subprocess.call(["git", "init", "-b", "main"])
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-m", "initial commit"])
    
    if CREATE_REPO == "True":
        createGithubRepo()
        addTopics()
        
    
    print(f"\n****************************************")
    print(f"\n✅ {REPO_NAME} has successfully been created!\n")
    
if __name__ == "__main__":
    main()
