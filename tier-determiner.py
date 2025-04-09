from dataclasses import dataclass

@dataclass
class Prompt:
    question: str
    answer: bool = None

def main():
    # Intro text to repo-scaffolder
    print("\n👋  Welcome to the repo-scaffolder cookiecutter CLI.")
    print("⚙️   We will assist you with creating a repository.")
    print("📝  Answer the following questions to identify the maturity model tier of your project.")
    print("ℹ️   Visit https://github.com/DSACMS/repo-scaffolder/blob/main/maturity-model-tiers.md for more information.\n")
    print("****************************************\n")

    prompts = {
        "CONTRIBUTORS": Prompt("Does your project have more than one contributor?"),
        "RELEASE": Prompt("Do you plan on cutting more than one release?"),
        "WORK": Prompt("Do you plan on having other individuals/teams outside the agency work with you?"),
        "MAINTAIN": Prompt("Do you plan on having other individuals/teams outside the agency maintain the project with you?"),
        "ROADMAP": Prompt("Do you plan on having other individuals/teams outside the agency plan the development roadmap with you?")
    }

    # Obtain answers
    for key, prompt in prompts.items():
        while True:
            response = input(f"{prompt.question} [y/n]: ").strip().lower()
            if response in ["y", "yes"]:
                prompt.answer = True
                break
            elif response in ["n", "no"]:
                prompt.answer = False
                break
            else:
                print("Please answer y or n.")

    # Determine tier
    if not prompts["CONTRIBUTORS"].answer:
        tier = 0
    elif not prompts["RELEASE"].answer:
        tier = 0
    elif not prompts["WORK"].answer:
        tier = 1
    elif not prompts["MAINTAIN"].answer:
        tier = 2
    elif not prompts["ROADMAP"].answer:
        tier = 3
    else:
        tier = 4

    print(f"\n****************************************")
    print(f"\n📚 Your project is classified as: Tier {tier}")
    print(f"ℹ️  Visit https://github.com/DSACMS/repo-scaffolder/blob/main/tier{tier} for more information about the maturity model tier.")
    print(f"⚙️  Next, create your Tier {tier} repository by running the command below:")
    print(f"   cookiecutter https://github.com/DSACMS/repo-scaffolder --directory=tier{tier}\n")
    

if __name__ == "__main__":
    main()