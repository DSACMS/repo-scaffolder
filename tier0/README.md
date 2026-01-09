# Tier 0: Private Repository

## What is a Tier 0 Project?

A **Tier 0** project is an **experimental or historical** repository that is **private** and generally used by a single developer or a small group. It typically includes working projects, example scripts, or early prototypes that serve as a foundation for future work or experimentation. This type of project is not shared publicly and often remains private due to its preliminary or incomplete nature.

The main purpose of a Tier 0 project is to provide a space for initial development, exploration, and testing. These repositories generally lack formal documentation or governance structures that are typical of more mature projects.

> The Tier 0 repository template can be found in [`{{cookiecutter.project_slug}}`](./{{cookiecutter.project_slug}}/) and is offered as a GitHub template repository: https://github.com/DSACMS/tier0

### Key Characteristics of a Tier 0 Project:

- **Private** and often limited to individual or small team access.
- Primarily **experimental or developmental** in nature.

---

## Files for a Tier 0 Project

Although these projects are private, there are specific files that are required and recommended to include in the repository as part of the CMS Open Source Program Office's repository hygiene guidelines and standards.

| **File**          | **Requirement** | **Description**                                                                                                             |
| ----------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `LICENSE`         | Mandatory       | Defines the licensing terms under which the project is distributed.                                                         |
| `code.json`       | Mandatory       | Contains project metadata following government requirements.                                                                |
| `README.md`       | Mandatory       | Provides an overview of the project, including its purpose, setup instructions, or any relevant notes for the developer(s). |
| `COMMUNITY.md`    | Mandatory       | Lists project team members and points of contact.                                                                           |
| `SECURITY.md`     | Recommended     | Outlines the agency's security policies, including how to report security issues or vulnerabilities in the code.            |
| `CONTRIBUTING.md` | Recommended     | Guidelines for contributing, useful if the project is later opened to collaborators or transitioned to a public repository. |
| `.gitignore` | Optional     | Lists intentionally untracked files that Git should ignore.                           |

For more information about sections and content within the files above, please visit [maturity-model-tiers.md](https://github.com/DSACMS/repo-scaffolder/blob/main/maturity-model-tiers.md).

## .github directory

The .github directory includes various files such as GitHub action workflows, code.json metadata cookiecutter creation, and issue templates. For more information, please visit the [.github-directory.md]([../docs/.github-directory.md).

## Repository Hygiene using repolinter

As part of maintaining repository hygiene, repolinter is used to identify missing files and information. `repolinter.json` defines a set of checks that verify the existence of these files in your repository. To run repolinter, execute the following command from the root directory:

```
repolinter lint .
```

A GitHub action is also available for running repolinter checks. For more information, please visit [README.md](https://github.com/DSACMS/repo-scaffolder?tab=readme-ov-file#identify-missing-files-and-information-using-repolinter).
