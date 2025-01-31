# Tier 3: Working in Public

## What is a Tier 3 Project?

A **Tier 3** project is an **open collaboration** effort where the work is conducted in public. The project is led by smaller, semi-open teams but encourages **limited external contributions**. The work is typically **open source**, but the direction and maintenance of the project are CMS-led, controlled by a smaller group or team, rather than a large, decentralized community. Tier 3 projects may be public-facing tools, utilities, or websites, where external contributions are welcomed but managed closely by the core team.

### Key Characteristics of a Tier 3 Project:

- **Collaborative in public**, where the work is open to external stakeholders.
- Led by a **CMS team** (often organizational or tool-specific).
- Accepts **limited contributions from external sources**, typically following specific guidelines.
- Publicly accessible code and documentation.
- Maintenance and decision-making are generally led by CMS.

---

## Files for a Tier 3 Project

There are specific files that are required and recommended to include in the repository as part of the CMS Open Source Program Office's repository hygiene guidelines and standards.

| **File**                  | **Requirement** | **Description**                                                                                                                                                          |
| ------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `LICENSE`                 | Mandatory       | Defines the licensing terms under which the project is distributed.                                                                                                      |
| `SECURITY.md`             | Mandatory       | Outlines the agency's security policies, including how to report security issues or vulnerabilities in the code.                                                         |
| `README.md`               | Mandatory       | Provides a comprehensive overview of the project, including its purpose, how to install or use it, and any relevant information for users or developers.                 |
| `CONTRIBUTING.md`         | Mandatory       | Offers guidelines for contributing to the project, including code standards, how to submit issues, and creating pull requests.                                           |
| `MAINTAINERS.md`          | Recommended     | Lists the individuals responsible for maintaining the project as well as reviewing and approving pull requests.                                                          |
| `GOVERNANCE.md`           | Recommended     | Describes the governance model of the project, such as decision-making processes and rules for contributing. It ensures a transparent process for managing the project.  |
| `CODEOWNERS.md`           | Recommended     | Defines ownership of various sections of the repository.                                                                                                                 |
| `COMMUNITY_GUIDELINES.md` | Mandatory       | Defines expectations for interactions within the project's community, including how external contributors should engage and behave.                                      |
| `CODE_OF_CONDUCT.md`      | Mandatory       | Establishes guidelines for acceptable behavior within the community, setting expectations for how contributors should interact in a respectful and collaborative manner. |

For more information about required sections and content within the files above, please visit [maturity-model-tiers.md](https://github.com/DSACMS/repo-scaffolder/blob/main/maturity-model-tiers.md).

## Workflows

Located in the `.github` directory are [GitHub Action workflows](../docs/workflows.md) that can be used to regularly update your repository.
