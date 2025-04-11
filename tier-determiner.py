from dataclasses import dataclass

@dataclass
class Prompt:
    question: str
    answer: bool = None

def print_tier_description(tier=None):
    tier_descriptions = {
        0: "💡 Tier 0 - Private Repository: Private, experimental projects typically maintained by a single developer; often prototypes or example code",
        1: "💡 Tier 1 - One-Time Release: A project with no plans for updates or ongoing maintenance from its original author(s).",
        2: "💡 Tier 2 - Close Collaboration: Collaborative project shared across small teams or departments, typically using innersource practices.",
        3: "💡 Tier 3 - Working in Public: Public-facing project open to external contributions, developed by CMS or its contractors for official use",
        4: "💡 Tier 4 - Community Governance: Fully open-source project with community-led governance and broad public collaboration."
    }

    if tier is None:
        for description in tier_descriptions.values():
            print(description)
    elif tier in tier_descriptions:
        print(tier_descriptions[tier])
    else:
        print(f"Invalid tier number: {tier}")

def main():
    # Intro text to repo-scaffolder
    print("\n👋 Welcome to the repo-scaffolder CLI.")
    print("⚙️  We will assist you with creating a repository.\n")

    print("🌱 The OSPO follows a maturity model framework to classify projects according to their open source journey:")
    print_tier_description()
    print("ℹ️  Visit https://github.com/DSACMS/repo-scaffolder/blob/main/maturity-model-tiers.md for more information.\n")

    print("\n📝 Answer the following questions to identify the maturity model tier of your project.")

    print("****************************************\n")

    prompts = {
        "CONTRIBUTORS": Prompt("Does your project have more than one contributor?"),
        "RELEASE": Prompt("Do you plan on shipping more than one release?"),
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

    # Output results
    print(f"\n****************************************")
    print(f"\n📚 Your project is classified as: Tier {tier}")
    print_tier_description(tier)
    print(f"ℹ️  Visit https://github.com/DSACMS/repo-scaffolder/blob/main/tier{tier} for more information about the maturity model tier.")

    # Provide next steps
    print(f"⚙️  Next, create your Tier {tier} repository by running the command below:")
    print(f"   cookiecutter https://github.com/DSACMS/repo-scaffolder --directory=tier{tier}\n")
    

if __name__ == "__main__":
    main()