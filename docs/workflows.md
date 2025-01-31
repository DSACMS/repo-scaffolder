## Workflows

Located in .**github/workflows**, the OSPO has created GitHub Actions workflows to assist project teams with development and documentation upkeep for repository hygiene.

| File Name                                                                                                                                                      | Tier       | Description                                        |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------- | :------------------------------------------------- |
| [auto-changelog.yml](https://github.com/DSACMS/repo-scaffolder/blob/main/tier3/%7B%7Bcookiecutter.project_slug%7D%7D/.github/workflows/auto-changelog.yml)     | 2, 3, 4    | Auto-generates a CHANGELOG.md                      |
| [repoHygieneCheck.yml](https://github.com/DSACMS/repo-scaffolder/blob/main/tier3/%7B%7Bcookiecutter.project_slug%7D%7D/.github/workflows/repoHygieneCheck.yml) | 1, 2, 3, 4 | Performs repolinter checks                         |
| [contributors.yml](https://github.com/DSACMS/repo-scaffolder/blob/main/tier3/%7B%7Bcookiecutter.project_slug%7D%7D/.github/workflows/contributors.yml)         | 2, 3, 4    | Generates a list of contributors in MAINTAINERS.md |
| [gitleaks.yml](https://github.com/DSACMS/repo-scaffolder/blob/main/tier3/%7B%7Bcookiecutter.project_slug%7D%7D/.github/workflows/gitleaks.yml)                 | 1, 2, 3, 4 | Scans for secrets upon each push or PR             |
| [repoStructure.yml](https://github.com/DSACMS/repo-scaffolder/blob/main/tier3/%7B%7Bcookiecutter.project_slug%7D%7D/.github/workflows/repoStructure.yml)       | 3, 4       | Generates repo structure in README.md              |
