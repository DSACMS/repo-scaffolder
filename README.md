# repo-scaffolder

Templates and commandline tools for creating repositories for US Federal open source projects

## About the Project

The CMS Open Source Program Office developed a [maturity model framework](https://github.com/DSACMS/repo-scaffolder/blob/main/maturity-model-tiers.md) to classify federal open source projects based on their maturity level. Each tier outlines specific files and content that are required or recommended to be included in the repository.

repo-scaffolder assists project teams with creating repositories that adhere to repository hygiene standards. It provides file templates detailing project information, contributing guidance, maintainer roles, project metadata, community involvement, feedback mechanisms, governance, security policies, which teams can easily fill out and customize. In turn, this provides the project sufficient structure and foundation to promote a healthy open source ecosystem.

<!-- TODO: Include more information on outbound checklists -->

<!---
### Project Vision
**{project vision}** -->

<!--
### Project Mission
**{project mission}** -->

<!--
### Agency Mission
TODO: Good to include since this is an agency-led project -->

<!--
### Team Mission
TODO: Good to include since this is an agency-led project -->

## Core Team

An up-to-date list of core team members can be found in [MAINTAINERS.md](MAINTAINERS.md). At this time, the project is still building the core team and defining roles and responsibilities. We are eagerly seeking individuals who would like to join the community and help us define and fill these roles.

## Documentation Index

- [Using repo-scaffolder](#Using-repo-scaffolder)
- [Documentation (coming soon!)](./docs)

- [CONTRIBUTING.md](./CONTRIBUTING.md)
- [MAINTAINERS.md](./MAINTAINERS.md)
- [CODEOWNERS.md](./CODEOWNERS.md)
- [COMMUNITY_GUIDELINES.md](./COMMUNITY_GUIDELINES.md)
- [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)
- [SECURITY.md](./SECURITY.md)
- [LICENSE](./LICENSE)

## Repository Structure

<!-- TODO: Using the 'tree -d' command can be a helpful way to generate this information, but, be sure to update it as the project evolves and changes over time. -->
 <!--TREE START--><!--TREE END-->

## Using repo-scaffolder

### Create a new repository using repo-scaffolder

The Open Source Program Office follows a maturity model framework to classify federal repositories according to their level of maturity: https://github.com/DSACMS/repo-scaffolder/blob/main/maturity-model-tiers.md.

There are 4 tiers in the maturity model framework. The `/tier*` directory consists of templates, files, and scripts for each respective tier:

- `{{cookiecutter.project_slug}}` is the directory containing templates and files to be generated upon repository creation. This serves as your repository starting point.
- `cookiecutter.json` defining the questions cookiecutter asks.
- `hooks`, a folder containing scripts to be run upon repository creation.
- `checklist.md` & `checklist.pdf` is the outbound review checklist with guidelines on releasing the repository as open source.
- `README.md` with more information about the maturity tier and file contents.

#### Prerequisites

- python
- github cli
- cookiecutter
- [repolinter](https://github.com/todogroup/repolinter)

#### Need help picking a maturity tier?

If you do not know what tier your project is, the cookiecutter will walk you through questions to figure out what tier you need. Run:

```
cookiecutter https://github.com/DSACMS/repo-scaffolder
```

#### Know what maturity tier you need?

If you know what tier you need, you can run the cookiecutter for an individual tier. Use the below command with `X` substituted for the tier number.

```
cookiecutter https://github.com/DSACMS/repo-scaffolder --directory=tierX
```

### Update an existing repository using repo-scaffolder

You can update existing projects with repo-scaffolder. Using the `-s` flag on cookiecutter will not overwrite existing files. Follow these steps:

1. Create a new branch in your repo
2. cd into folder above
3. run: `cookiecutter -f -s https://github.com/DSACMS/repo-scaffolder --directory=tierX`
4. Make sure when answering the questions you use the existing folder/project name
5. Raise pr into main

### Metadata collection using code.json

<!-- TODO: Add text here about code.json and link code.json docs -->

#### Add code.json to your project

Each repository should contain a code.json file with metadata about the project.

To add code.json into your project, navigate to your project's `.github` directory and run the following cookiecutter command. You will be asked questions about the project (see cookiecutter.json) in order to collect and store this metadata in code.json.

```
cookiecutter . --directory=codejson
```

### Maintaining your repository using repo-scaffolder

#### Updating projects with new repo-scaffolder upstream file changes

When creating projects, if you want to receive updates then add `dsacms-tierX` as a github topic to the repo. The scaffolder repo includes github workflows that will find all repos with that tag and can raise a pull request with an updated string or adding a file. See [actions.md](https://github.com/DSACMS/repo-scaffolder/blob/main/.github/actions.md) for more information.

### Identify missing files and information using repolinter

<!-- TODO: Revise once repolinter GH actions are up and link to it-->

Repolinter is a tool maintained by the [TODOGroup](https://todogroup.org/) for checking repositories for common open source issues, using pre-defined rulesets. This can be run stand-alone as a script, pre-commit in your IDE, or post-commit or within CI/CD systems!

✔    =  Pass

✖    =  Fail

⚠  =  Warn

Tiers of level 1 thru 4 have repolinter.json file in their projects. Tier1 has detailed configuration of all the rules. All the other tiers extends their previous tiers and has only the `rule` and the `level` configuration.

Sample commands to run with the given repolinter.json path:

```
repolinter lint .

repolinter lint tier4/\{\{cookiecutter.project_slug\}\}
```

# Development and Software Delivery Lifecycle

The following guide is for members of the project team who have access to the repository as well as code contributors. The main difference between internal and external contributions is that external contributors will need to fork the project and will not be able to merge their own pull requests. For more information on contributing, see: [CONTRIBUTING.md](./CONTRIBUTING.md).

## Local Development

This project contains several different features.

- `/tier*` contains file templates for repository creation and metadata collection using cookiecutter. Refer to the README.mds to learn more about the file contents.
- `/.github` contains GitHub actions to update repositories contents across the ecosystem.
- `checklist.md` & `checklist.pdf` is the outbound review checklist with guidelines on releasing the repository as open source.
- `maturity-model-tiers.md` & `maturity-model-tiers.pdf` contain information about our maturity model framework.

### Editing/adding tiers and template contents in repo-scaffolder

At a top level, each tier consists of a folder for `hooks`, a folder containing the files to be added (`{{cookiecutter.project_slug}}`), and a `cookiecutter.json` defining the questions cookiecutter asks. These naming conventions must be followed as that is what cookiecutter picks up. The `hooks` folder needs to be duplicated in each tier. The folder containing the files to be added can include slugged out variables such as `{{ cookiecutter.project_name }}` that can be filled in by the answers to `cookiecutter.json`.
For example, `{{ cookiecutter.project_name }}` will be filled in by this question - `"project_name": "My Project",`.

See the [cookiecutter docs](https://cookiecutter.readthedocs.io/en/stable/)
for more information.

<!-- TODO: Add guidance on updating repolinter -->

## Coding Style and Linters

<!-- TODO - Add the repo's linting and code style guidelines -->

Each application has its own linting and testing guidelines. Lint and code tests are run on each commit, so linters and tests should be run locally before commiting.

## Branching Model

This project follows [trunk-based development](https://trunkbaseddevelopment.com/), which means:

- Make small changes in [short-lived feature branches](https://trunkbaseddevelopment.com/short-lived-feature-branches/) and merge to `dev` frequently.
- Be open to submitting multiple small pull requests for a single ticket (i.e. reference the same ticket across multiple pull requests).
- Treat each change you merge to `dev` as immediately deployable to production. Do not merge changes that depend on subsequent changes you plan to make, even if you plan to make those changes shortly.
- Ticket any unfinished or partially finished work.
- Tests should be written for changes introduced, and adhere to the text percentage threshold determined by the project.

This project uses **continuous deployment** using [Github Actions](https://github.com/features/actions) which is configured in the [./github/workflows](.github/workflows) directory.

Pull-requests are merged to `dev` and the changes are immediately deployed to the development environment. Releases are created to push changes to production in the `main` branch.

## Contributing

Thank you for considering contributing to an Open Source project of the US Government! For more information about our contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Codeowners

The contents of this repository are managed by the CMS Open Source Program Office. Those responsible for the code and documentation in this repository can be found in [CODEOWNERS.md](CODEOWNERS.md).

## Community

The repo-scaffolder team is taking a community-first and open source approach to the product development of this tool. We believe government software should be made in the open and be built and licensed such that anyone can download the code, run it themselves without paying money to third parties or using proprietary software, and use it as they will.

We know that we can learn from a wide variety of communities, including those who will use or will be impacted by the tool, who are experts in technology, or who have experience with similar technologies deployed in other spaces. We are dedicated to creating forums for continuous conversation and feedback to help shape the design and development of the tool.

We also recognize capacity building as a key part of involving a diverse open source community. We are doing our best to use accessible language, provide technical and process documents, and offer support to community members with a wide variety of backgrounds and skillsets.

### Community Guidelines

Principles and guidelines for participating in our open source community are can be found in [COMMUNITY_GUIDELINES.md](COMMUNITY_GUIDELINES.md). Please read them before joining or starting a conversation in this repo or one of the channels listed below. All community members and participants are expected to adhere to the community guidelines and code of conduct when participating in community spaces including: code repositories, communication channels and venues, and events.

## Feedback

If you have ideas for how we can improve or add to our capacity building efforts and methods for welcoming people into our community, please let us know at opensource@cms.hhs.gov. If you would like to comment on the tool itself, please let us know by filing an **issue on our GitHub repository.**

## Acknowlegements

This project was developed as a collaboration between the United States Digital
Service ([USDS.gov](https://usds.gov)), The Department of Health and Human
Services ([HHS.gov](https://hhs.gov)), The Digital Service at the Centers for
Medicare & Medicaid Services ([CMS.gov](https://cms.gov)) and The
[USDigitalResponse.org](https://usdigitalresponse.org).

## Policies

### Open Source Policy

We adhere to the [CMS Open Source
Policy](https://github.com/CMSGov/cms-open-source-policy). If you have any
questions, just [shoot us an email](mailto:opensource@cms.hhs.gov).

### Security and Responsible Disclosure Policy

_Submit a vulnerability:_ Vulnerability reports can be submitted through [Bugcrowd](https://bugcrowd.com/cms-vdp). Reports may be submitted anonymously. If you share contact information, we will acknowledge receipt of your report within 3 business days.

For more information about our Security, Vulnerability, and Responsible Disclosure Policies, see [SECURITY.md](SECURITY.md).

### Software Bill of Materials (SBOM)

A Software Bill of Materials (SBOM) is a formal record containing the details and supply chain relationships of various components used in building software.

In the spirit of [Executive Order 14028 - Improving the Nation’s Cyber Security](https://www.gsa.gov/technology/it-contract-vehicles-and-purchasing-programs/information-technology-category/it-security/executive-order-14028), a SBOM for this repository is provided here: https://github.com/DSACMS/repo-scaffolder/network/dependencies.

For more information and resources about SBOMs, visit: https://www.cisa.gov/sbom.

## Public domain

This project is in the public domain within the United States, and copyright
and related rights in the work worldwide are waived through the [CC0 1.0
Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/) as indicated in [LICENSE](LICENSE).

All contributions to this project will be released under the CC0 dedication. By
submitting a pull request or issue, you are agreeing to comply with this waiver
of copyright interest.
