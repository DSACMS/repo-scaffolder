CONTRIBUTORS = '{{ cookiecutter.greater_one_contributors }}'
RELEASE = '{{cookiecutter.greater_one_release}}'
WORK = '{{cookiecutter.work_as_team}}'
MAINTAIN = '{{cookiecutter.maintain_as_team}}'
ROADMAP = '{{cookiecutter.roadmap_as_team}}'

if CONTRIBUTORS == "no":
    # tier 0
    print("We suggest using the tier 0 template for your project.  Run: ")
    print("cookiecutter https://github.com/DSACMS/repo-scaffolder/scaffold-templates/tier0")
elif RELEASE == "no":
    #tier 1
    print("We suggest using the tier 1 template for your project.  Run: ")
    print("cookiecutter https://github.com/DSACMS/repo-scaffolder/scaffold-templates/tier1")
elif WORK == "no":
    #tier 1
    print("We suggest using the tier 1 template for your project.  Run: ")
    print("cookiecutter https://github.com/DSACMS/repo-scaffolder/scaffold-templates/tier1")
elif MAINTAIN == "no":
    # tier 2
    print("We suggest using the tier 2 template for your project.  Run: ")
    print("cookiecutter https://github.com/DSACMS/repo-scaffolder/scaffold-templates/tier2")
elif ROADMAP == "no":
    # tier 3
    print("We suggest using the tier 3 template for your project.  Run: ")
    print("cookiecutter https://github.com/DSACMS/repo-scaffolder/scaffold-templates/tier3")
else:
    # tier 4
    print("We suggest using the tier 4 template for your project.  Run: ")
    print("cookiecutter https://github.com/DSACMS/repo-scaffolder/scaffold-templates/tier4")