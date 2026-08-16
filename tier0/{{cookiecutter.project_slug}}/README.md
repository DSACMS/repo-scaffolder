# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## About the Project

**{project_statement}**

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

<!--
## Core Team

A list of core team members responsible for the code and documentation in this repository can be found in [COMMUNITY.md](COMMUNITY.md).
-->

<!--
## Repository Structure

TODO: Including the repository structure helps viewers quickly understand the project layout. Using the "tree -d" command can be a helpful way to generate this information, but, be sure to update it as the project evolves and changes over time.

**{list directories and descriptions}**

TODO: Add a 'table of contents" for your documentation. Tier 0/1 projects with simple README.md files without many sections may or may not need this, but it is still extremely helpful to provide "bookmark" or "anchor" links to specific sections of your file to be referenced in tickets, docs, or other communication channels.

**{list of .md at top directory and descriptions}**

-->

<!---
## Local Development

 TODO - with example below:
This project is monorepo with several apps. Please see the [api](./api/README.md) and [frontend](./frontend/README.md) READMEs for information on spinning up those projects locally. Also see the project [documentation](./documentation) for more info.
-->

<!--
## Coding Style and Linters

TODO - Add the repo's linting and code style guidelines

Each application has its own linting and testing guidelines. Lint and code tests are run on each commit, so linters and tests should be run locally before committing.
 -->

<!---
## Branching Model

TODO - with example below:
This project follows [trunk-based development](https://trunkbaseddevelopment.com/), which means:

* Make small changes in [short-lived feature branches](https://trunkbaseddevelopment.com/short-lived-feature-branches/) and merge to `main` frequently.
* Be open to submitting multiple small pull requests for a single ticket (i.e. reference the same ticket across multiple pull requests).
* Treat each change you merge to `main` as immediately deployable to production. Do not merge changes that depend on subsequent changes you plan to make, even if you plan to make those changes shortly.
* Ticket any unfinished or partially finished work.
* Tests should be written for changes introduced, and adhere to the text percentage threshold determined by the project.

This project uses **continuous deployment** using [Github Actions](https://github.com/features/actions) which is configured in the [./github/workflows](.github/workflows) directory.

Pull-requests are merged to `main` and the changes are immediately deployed to the development environment. Releases are created to push changes to production.
-->

## Policies

### Open Source Policy

We adhere to the [CMS Open Source Policy](https://github.com/CMSGov/cms-open-source-policy). If you have any questions, just [shoot us an email](mailto:opensource@cms.hhs.gov).

### Security and Responsible Disclosure Policy

_Submit a vulnerability:_ Vulnerability reports can be submitted through [Bugcrowd](https://bugcrowd.com/cms-vdp). Reports may be submitted anonymously. If you share contact information, we will acknowledge receipt of your report within 3 business days.

### Software Bill of Materials (SBOM)

A Software Bill of Materials (SBOM) is a formal record containing the details and supply chain relationships of various components used in building software.

In the spirit of [Executive Order 14028 - Improving the Nation's Cyber Security](https://www.gsa.gov/technology/it-contract-vehicles-and-purchasing-programs/information-technology-category/it-security/executive-order-14028), a SBOM for this repository is provided here: https://github.com/{{ cookiecutter.project_org }}/{{ cookiecutter.project_repo_name }}/network/dependencies.

For more information and resources about SBOMs, visit: https://www.cisa.gov/sbom.

### Paperwork Reduction Act

If this project collects information from the public, the [Paperwork Reduction Act](https://pra.digital.gov/)
may apply. It is triggered by collecting standardized information from ten or more members of the
public within a twelve month period, which includes forms, surveys, and some kinds of user research,
and it requires OMB clearance before the collection begins rather than after.

See [pra.digital.gov](https://pra.digital.gov/) for what counts as a collection and how the review
works, and talk to your agency's PRA contact early, since clearance takes time to obtain.

### Plain Language

Public-facing content in this project follows the [Federal Plain Language Guidelines](https://www.plainlanguage.gov/guidelines/),
as required by the [Plain Writing Act of 2010](https://www.plainlanguage.gov/law/). The test is
whether a reader can find what they need, understand it the first time they read it, and use it.

This applies to documentation as much as to interface text. A README is often the first thing a
member of the public reads about a government project.

### Accessibility

This project follows [Section 508 of the Rehabilitation Act](https://www.section508.gov/), which
requires that information and communication technology developed, procured, maintained, or used by
federal agencies be accessible to people with disabilities. The Revised 508 Standards incorporate
[WCAG 2.0](https://www.w3.org/TR/WCAG20/) Level A and AA by reference, and many teams now target
[WCAG 2.1](https://www.w3.org/TR/WCAG21/) Level AA.

Automated checkers find only a portion of accessibility defects. Test with a keyboard, and with a
screen reader, as part of normal development rather than as a release gate.

## Public domain

This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/) as indicated in [LICENSE](LICENSE).

All contributions to this project will be released under the CC0 dedication. By submitting a pull request or issue, you are agreeing to comply with this waiver of copyright interest.
