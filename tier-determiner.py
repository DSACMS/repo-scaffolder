def main():
    # Intro text to repo-scaffolder
    print("\n👋  Welcome to the repo-scaffolder cookiecutter CLI.")
    print("⚙️   We will assist you with creating a repository.")
    print("📝  Answer the following questions to identify the maturity model tier of your project.")
    print("ℹ️   Visit https://github.com/DSACMS/repo-scaffolder/blob/main/maturity-model-tiers.md for more information.\n")
    print("****************************************\n")

    prompts = {
        "CONTRIBUTORS": "Does your project have more than one contributor?",
        "RELEASE": "Do you plan on cutting more than one release?",
        "WORK": "Do you plan on having other individuals/teams outside the agency work with you?",
        "MAINTAIN": "Do you plan on having other individuals/teams outside the agency maintain the project with you?",
        "ROADMAP": "Do you plan on having other individuals/teams outside the agency plan the development roadmap with you?"
    }

    answers = {}

    # Obtain answers
    for key, question in prompts.items():
        while True:
            answer = input(f"{question} [y/n]: ").strip().lower()
            if answer in ["y", "yes"]:
                answers[key] = True
                break
            elif answer in ["n", "no"]:
                answers[key] = False
                break
            else:
                print("Please answer y or n.")

    # Determine tier
    if not answers.get("CONTRIBUTORS"):
        tier = 0
    elif not answers.get("RELEASE"):
        tier = 0
    elif not answers.get("WORK"):
        tier = 1
    elif not answers.get("MAINTAIN"):
        tier = 2
    elif not answers.get("ROADMAP"):
        tier = 3
    else:
        tier = 4

    print(f"\n****************************************")
    print(f"\n📚 Your project is classified as: Tier {tier}")
    print(f"ℹ️  Visit https://github.com/DSACMS/repo-scaffolder/blob/main/tier{tier} for more information about the maturity model tier.")
    print(f"🔨 Next, create your Tier {tier} repository by running the command below:")
    print(f"   cookiecutter https://github.com/DSACMS/repo-scaffolder --directory=tier{tier}\n")
    

if __name__ == "__main__":
    main()