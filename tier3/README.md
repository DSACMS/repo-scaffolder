# Tier 3: Working in Public

## What is a Tier 3 Project?

A **Tier 3** project is an **open collaboration** effort where the work is conducted in public. The project is led by smaller, semi-open teams but encourages **limited external contributions**. The work is typically **open source**, but the direction and maintenance of the project are CMS-led, controlled by a smaller group or team, rather than a large, decentralized community. Tier 3 projects may be public-facing tools, utilities, or websites, where external contributions are welcomed but managed closely by the core team.

> The Tier 3 repository template can be found in [`{{cookiecutter.project_slug}}`](./{{cookiecutter.project_slug}}/) and is offered as a GitHub template repository: https://github.com/DSACMS/tier3

### Key Characteristics of a Tier 3 Project:

- **Collaborative in public**, where the work is open to external stakeholders.
- Led by a **CMS team** (often organizational or tool-specific).
- Accepts **limited contributions from external sources**, typically following specific guidelines.
- Publicly accessible code and documentation.
- Maintenance and decision-making are generally led by CMS.

---

## Files for a Tier 3 Project

There are specific files that are required and recommended to include in the repository as part of the CMS Open Source Program Office's repository hygiene guidelines and standards.

| **File**             | **Requirement** | **Description**                                                                                                                                                          |
| -------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `LICENSE`            | Mandatory       | Defines the licensing terms under which the project is distributed.                                                                                                      |
| `code.json`          | Mandatory       | Contains project metadata following government requirements.                                                                                                             |
| `README.md`          | Mandatory       | Provides a comprehensive overview of the project, including its purpose, how to install or use it, and any relevant information for users or developers.                 |
| `COMMUNITY.md`       | Mandatory       | Lists project team members and points of contact with detailed roles and responsibilities.                                                                               |
| `SECURITY.md`        | Mandatory       | Outlines the agency's security policies, including how to report security issues or vulnerabilities in the code.                                                         |
| `CONTRIBUTING.md`    | Mandatory       | Offers guidelines for contributing to the project, including code standards, how to submit issues, and creating pull requests.                                           |
| `CODE_OF_CONDUCT.md` | Mandatory       | Establishes guidelines for acceptable behavior within the community, setting expectations for how contributors should interact in a respectful and collaborative manner. |
| `GOVERNANCE.md`      | Recommended     | Describes the governance model of the project, such as decision-making processes and rules for contributing. It ensures a transparent process for managing the project.  |
| `.gitignore` | Optional     | Lists intentionally untracked files that Git should ignore.                           |

For more information about required sections and content within the files above, please visit [maturity-model-tiers.md](https://github.com/DSACMS/repo-scaffolder/blob/main/maturity-model-tiers.md).

## .github directory

The .github directory includes various files such as GitHub action workflows, code.json metadata cookiecutter creation, and issue templates. For more information, please visit the [.github-directory.md](../docs/.github-directory.md).

## Repository Hygiene using repolinter

As part of maintaining repository hygiene, repolinter is used to identify missing files and information. `repolinter.json` defines a set of checks that verify the existence of these files in your repository. To run repolinter, execute the following command from the root directory:

```
repolinter lint .
```

A GitHub action is also available for running repolinter checks. For more information, please visit [README.md](https://github.com/DSACMS/repo-scaffolder?tab=readme-ov-file#identify-missing-files-and-information-using-repolinter).
