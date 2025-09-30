# Tier 2: Close Collaboration

## What is a Tier 2 Project?

A **Tier 2** project is a **collaborative effort** that typically occurs within a team or operational division (OpDiv). The project follows an **innersource working style**, where internal teams collaborate using open source best practices but within the confines of a private or internal environment. The project is not meant for broad public contribution but rather for **internal collaboration**.

Innersource projects often allow different teams within the same organization to contribute, fostering collaboration and code-sharing internally while maintaining control over external access.

> The Tier 2 repository template can be found in [`{{cookiecutter.project_slug}}`](./{{cookiecutter.project_slug}}/) and is offered as a GitHub template repository: https://github.com/DSACMS/tier2

### Key Characteristics of a Tier 2 Project:

- Focuses on **collaborating within a smaller team** or internal group.
- Utilizes **innersource practices**, where internal teams work collaboratively on code, borrowing from open source workflows but keeping the work within the organization.
- Projects may be shared among internal stakeholders or divisions.
- **Not necessarily accepting contributions** from the broader community.

---

## Files for a Tier 2 Project

There are specific files that are required and recommended to include in the repository as part of the CMS Open Source Program Office's repository hygiene guidelines and standards.

| **File**             | **Requirement** | **Description**                                                                                                                                          |
| -------------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `LICENSE`            | Mandatory       | Defines the licensing terms under which the project is distributed.                                                                                      |
| `code.json`          | Mandatory       | Contains project metadata following government requirements.                                                                                             |
| `README.md`          | Mandatory       | Provides a comprehensive overview of the project, including its purpose, how to install or use it, and any relevant information for users or developers. |
| `COMMUNITY.md`       | Mandatory       | Lists project team members and points of contact.                                                                                                        |
| `SECURITY.md`        | Mandatory       | Outlines the agency's security policies, including how to report security issues or vulnerabilities in the code.                                         |
| `CONTRIBUTING.md`    | Mandatory       | Offers guidelines for contributing to the project, including code standards, how to submit issues, and creating pull requests.                           |
| `CODE_OF_CONDUCT.md` | Mandatory       | Establishes guidelines for professional and respectful behavior to foster a collaborative environment.                                                   |

For more information about required sections and content within the files above, please visit [maturity-model-tiers.md](https://github.com/DSACMS/repo-scaffolder/blob/main/maturity-model-tiers.md).

## .github directory

The .github directory includes various files such as GitHub action workflows, code.json metadata cookiecutter creation, and issue templates. For more information, please visit the [.github-directory.md]([../docs/.github-directory.md).

## Repository Hygiene using repolinter

As part of maintaining repository hygiene, repolinter is used to identify missing files and information. `repolinter.json` defines a set of checks that verify the existence of these files in your repository. To run repolinter, execute the following command from the root directory:

```
repolinter lint .
```

A GitHub action is also available for running repolinter checks. For more information, please visit [README.md](https://github.com/DSACMS/repo-scaffolder?tab=readme-ov-file#identify-missing-files-and-information-using-repolinter).
