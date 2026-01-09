# Tier 4: Community Governance

## What is a Tier 4 Project?

A **Tier 4** project is a fully **open and collaborative** project that operates under a **community governance model**. In Tier 4 projects, the focus is on **collaborating broadly with the public**, and the project is often either **donated** to or **stewarded** by an external community. The governance structure is **open** and welcomes input from a wide range of contributors, typically from outside the original development team.

> The Tier 4 repository template can be found in [`{{cookiecutter.project_slug}}`](./{{cookiecutter.project_slug}}/) and is offered as a GitHub template repository: https://github.com/DSACMS/tier4

### Key Characteristics of a Tier 4 Project:

- **Broad public collaboration** with contributions welcomed from the community.
- **Community-led governance**, where decisions are made transparently, often with input from various stakeholders.
- **Mature open-source project**, typically with a well-defined governance structure to guide development, maintenance, and project direction.

---

## Files for a Tier 4 Project

There are specific files that are required to include in the repository as part of the CMS Open Source Program Office's repository hygiene guidelines and standards.

| **File**             | **Requirement** | **Description**                                                                                                                                                          |
| -------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `LICENSE`            | Mandatory       | Defines the licensing terms under which the project is distributed.                                                                                                      |
| `code.json`          | Mandatory       | Contains project metadata following government requirements.                                                                                                             |
| `README.md`          | Mandatory       | Provides a comprehensive overview of the project, including its purpose, how to install or use it, and any relevant information for users or developers.                 |
| `COMMUNITY.md`       | Mandatory       | Lists project team members and points of contact with detailed roles and responsibilities.                                                                               |
| `SECURITY.md`        | Mandatory       | Outlines the agency's security policies, including how to report security issues or vulnerabilities in the code.                                                         |
| `CONTRIBUTING.md`    | Mandatory       | Offers guidelines for contributing to the project, including code standards, how to submit issues, and creating pull requests.                                           |
| `CODE_OF_CONDUCT.md` | Mandatory       | Establishes guidelines for acceptable behavior within the community, setting expectations for how contributors should interact in a respectful and collaborative manner. |
| `GOVERNANCE.md`      | Mandatory       | Describes the governance model of the project, such as decision-making processes and rules for contributing. It ensures a transparent process for managing the project.  |
| `.gitignore` | Optional     | Lists intentionally untracked files that Git should ignore.                           |

For more information about required sections and content within the files above, please visit [maturity-model-tiers.md](https://github.com/DSACMS/repo-scaffolder/blob/main/maturity-model-tiers.md).

## .github directory

The .github directory includes various files such as GitHub action workflows, code.json metadata cookiecutter creation, and issue templates. For more information, please visit the [.github-directory.md]([../docs/.github-directory.md).

## Repository Hygiene using repolinter

As part of maintaining repository hygiene, repolinter is used to identify missing files and information. `repolinter.json` defines a set of checks that verify the existence of these files in your repository. To run repolinter, execute the following command from the root directory:

```
repolinter lint .
```

A GitHub action is also available for running repolinter checks. For more information, please visit [README.md](https://github.com/DSACMS/repo-scaffolder?tab=readme-ov-file#identify-missing-files-and-information-using-repolinter).
