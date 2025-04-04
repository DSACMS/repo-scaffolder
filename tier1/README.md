# Tier 1: One-Time Release

## What is a Tier 1 Project?

A **Tier 1** project refers to an **informational or historical** project that has been **released publicly**. However, it does **not** have planned future updates or maintenance by the original authors or contributors. These projects typically include code samples, prototypes, public documentation, or other types of resources that are made available for use but won't receive ongoing updates or active development.

The main purpose of a Tier 1 project is to share knowledge and provide information from past work. Though available for public consumption, the project is **not expected to evolve or expand** in the future. Contributors may not engage in continuous development or issue resolution.

### Key Characteristics of a Tier 1 Project:

- **Publicly released** without planned future development or maintenance.
- Primarily **informational or historical** in nature.
- May still provide value to the community, but it is not actively worked on.

---

## Files for a Tier 1 Project

There are specific files that are required and recommended to include in the repository as part of the CMS Open Source Program Office's repository hygiene guidelines and standards.

| **File**          | **Requirement** | **Description**                                                                                                                                          |
| ----------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `LICENSE`         | Mandatory       | Defines the licensing terms under which the project is distributed.                                                                                      |
| `code.json`       | Mandatory       | Contains project metadata following government requirements.                                                                                             |
| `README.md`       | Mandatory       | Provides a comprehensive overview of the project, including its purpose, how to install or use it, and any relevant information for users or developers. |
| `COMMUNITY.md`    | Mandatory       | Lists project team members and points of contact.                                                                                                        |
| `SECURITY.md`     | Mandatory       | Outlines the agency's security policies, including how to report security issues or vulnerabilities in the code.                                         |
| `CONTRIBUTING.md` | Recommended     | Offers guidelines for contributing to the project, including code standards, how to submit issues, and creating pull requests.                           |

For more information about required sections and content within the files above, please visit [maturity-model-tiers.md](https://github.com/DSACMS/repo-scaffolder/blob/main/maturity-model-tiers.md).

## .github directory

The .github directory includes various files such as GitHub action workflows, code.json metadata cookiecutter creation, and issue templates. For more information, please visit the [.github-directory.md]([../docs/.github-directory.md).

## Repository Hygiene using repolinter

As part of maintaining repository hygiene, repolinter is used to identify missing files and information. `repolinter.json` defines a set of checks that verify the existence of these files in your repository. To run repolinter, execute the following command from the root directory:

```
repolinter lint .
```

A GitHub action is also available for running repolinter checks. For more information, please visit [README.md](https://github.com/DSACMS/repo-scaffolder?tab=readme-ov-file#identify-missing-files-and-information-using-repolinter).
