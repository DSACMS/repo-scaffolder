<!--- # NOTE: Modify sections marked with `TODO` -->

# How to Contribute

<!-- Basic instructions about where to send patches, check out source code, and get development support.-->

We're so thankful you're considering contributing to an [open source project of
the U.S. government](https://code.gov/)! If you're unsure about anything, just
ask -- or submit the issue or pull request anyway. The worst that can happen is
you'll be politely asked to change something. We appreciate all friendly
contributions.

We encourage you to read this project's CONTRIBUTING policy (you are here), its
[LICENSE](LICENSE.md), and its [README](README.md).

## Getting Started

<!--- TODO: If you have 'good-first-issue' or 'easy' labels for newcomers, mention them here.-->

### Team Specific Guidelines

<!-- TODO: This section helps contributors understand any team structure in the project (formal or informal.) Encouraged to point towards the COMMUNITY.md file for further details.-->

### Building dependencies

<!--- TODO: This step is often skipped, so don't forget to include the steps needed to install on your platform. If you project can be multi-platform, this is an excellent place for first time contributors to send patches!-->

### Building the Project

<!--- TODO: Be sure to include build scripts and instructions, not just the source code itself! -->

### Workflow and Branching

<!--- TODO: Workflow Example
We follow the [GitHub Flow Workflow](https://guides.github.com/introduction/flow/)

1.  Fork the project
2.  Check out the `main` branch
3.  Create a feature branch
4.  Write code and tests for your change
5.  From your branch, make a pull request against `{{ cookiecutter.project_org }}/{{ cookiecutter.project_repo_name }}/main`
6.  Work with repo maintainers to get your change reviewed
7.  Wait for your change to be pulled into `{{ cookiecutter.project_org }}/{{ cookiecutter.project_repo_name }}/main`
8.  Delete your feature branch
-->

### Testing Conventions

<!--- TODO: Discuss where tests can be found, how they are run, and what kind of tests/coverage strategy and goals the project has. -->

### Coding Style and Linters

<!--- TODO: HIGHLY ENCOURAGED. Specific tools will vary between different languages/frameworks (e.g. Black for python, eslint for JavaScript, etc...)

1. Mention any style guides you adhere to (e.g. pep8, etc...)
2. Mention any linters your project uses (e.g. flake8, jslint, etc...)
3. Mention any naming conventions your project uses (e.g. Semantic Versioning, CamelCasing, etc...)
4. Mention any other content guidelines the project adheres to (e.g. plainlanguage.gov, etc...)

-->

### Writing Issues

<!--- TODO: Example Issue Guides

When creating an issue please try to adhere to the following format:

    module-name: One line summary of the issue (less than 72 characters)

    ### Expected behavior

    As concisely as possible, describe the expected behavior.

    ### Actual behavior

    As concisely as possible, describe the observed behavior.

    ### Steps to reproduce the behavior

    List all relevant steps to reproduce the observed behavior.

    see our .github/ISSUE_TEMPLATE.md for more examples.
-->

### Writing Pull Requests

<!-- TODO: Make a brief statement about where to file pull/merge requests, and conventions for doing so. Link to PULL_REQUEST_TEMPLATE.md file.

Comments should be formatted to a width no greater than 80 columns.

Files should be exempt of trailing spaces.

We adhere to a specific format for commit messages. Please write your commit
messages along these guidelines. Please keep the line width no greater than 80
columns (You can use `fmt -n -p -w 80` to accomplish this).

    module-name: One line description of your change (less than 72 characters)

    Problem

    Explain the context and why you're making that change.  What is the problem
    you're trying to solve? In some cases there is not a problem and this can be
    thought of being the motivation for your change.

    Solution

    Describe the modifications you've done.

    Result

    What will change as a result of your pull request? Note that sometimes this
    section is unnecessary because it is self-explanatory based on the solution.

Some important notes regarding the summary line:

* Describe what was done; not the result
* Use the active voice
* Use the present tense
* Capitalize properly
* Do not end in a period — this is a title/subject
* Prefix the subject with its scope

    see our .github/PULL_REQUEST_TEMPLATE.md for more examples.
-->

## Reviewing Pull Requests

<!--- TODO: Make a brief statement about how pull-requests are reviewed, and who is doing the reviewing. Linking to COMMUNITY.md can help.

Code Review Example

The repository on GitHub is kept in sync with an internal repository at
github.cms.gov. For the most part this process should be transparent to the
project users, but it does have some implications for how pull requests are
merged into the codebase.

When you submit a pull request on GitHub, it will be reviewed by the project
community (both inside and outside of github.cms.gov), and once the changes are
approved, your commits will be brought into github.cms.gov's internal system for
additional testing. Once the changes are merged internally, they will be pushed
back to GitHub with the next sync.

This process means that the pull request will not be merged in the usual way.
Instead a member of the project team will post a message in the pull request
thread when your changes have made their way back to GitHub, and the pull
request will be closed.

The changes in the pull request will be collapsed into a single commit, but the
authorship metadata will be preserved.

-->

## Shipping Releases

<!-- TODO: What cadence does your project ship new releases? (e.g. one-time, ad-hoc, periodically, upon merge of new patches) Who does so? Below is a sample template you can use to provide this information.

{{ cookiecutter.project_repo_name }} will see regular updates and new releases. This section describes the general guidelines around how and when a new release is cut.

-->

<!-- ### Table of Contents

- [Versioning](#versioning)
  - [Breaking vs. non-breaking changes](#breaking-vs-non-breaking-changes)
  - [Ongoing version support](#ongoing-version-support)
- [Release Process](#release-process)
  - [Goals](#goals)
  - [Schedule](#schedule)
  - [Communication and Workflow](#communication-and-workflow)
  - [Beta Features](#beta-features)
- [Preparing a Release Candidate](#preparing-a-release-candidate)
  - [Incorporating feedback from review](#incorporating-feedback-from-review)
- [Making a Release](#making-a-release)
- [Auto Changelog](#auto-changelog)
- [Hotfix Releases](#hotfix-releases) -->

<!-- ### Versioning

{{ cookiecutter.project_repo_name }} uses [Semantic Versioning](https://semver.org/). Each release is associated with a [`git tag`](github.com/{{ cookiecutter.project_org }}/{{ cookiecutter.project_repo_name }}/tags) of the form `X.Y.Z`.

Given a version number in the `MAJOR.MINOR.PATCH` (eg., `X.Y.Z`) format, here are the differences in these terms:

- **MAJOR** version - make breaking/incompatible API changes
- **MINOR** version - add functionality in a backwards compatible manner
- **PATCH** version - make backwards compatible bug fixes -->

<!-- ### Breaking vs. non-breaking changes

TODO: Examples and protocol for breaking changes

Definitions for breaking changes will vary depending on the use-case and project but generally speaking if changes break standard workflows in any way then they should be put in a major version update.
-->

<!-- #### Ongoing version support

TODO: Explanation of general thought process

Explain the project’s thought process behind what versions will and won’t be supported in the future.
-->

<!-- TODO: List of supported releases

This section should make clear which versions of the project are considered actively supported.
-->

<!-- ### Release Process

The sections below define the release process itself, including timeline, roles, and communication best practices. -->

<!-- #### Goals

TODO: Explain the goals of your project’s release structure

This should ideally be a bulleted list of what your regular releases will deliver to key users and stakeholders
-->

<!-- #### Schedule

TODO: Communicate the timing of the regular release structure

For example, if you plan on creating regular releases on a weekly basis you should communicate that as well as the typical days upcoming releases will become tagged.

You should also communicate special cases such as security updates or critical bugfixes and how they would likely be released earlier than what is usually scheduled.
-->

<!-- #### Communication and Workflow

TODO: Communicate proper channels to be notified about releases

Communicate the slack channels, mailing lists, or other means of pushing out release notifications.
-->

<!-- TODO: (OPTIONAL) Support beta feature testing
## Beta Features

When a new beta feature is created for a release, make sure to create a new Issue with a '[Feature Name] - Beta [X.X.x] - Feedback' title and a 'beta' label. Update the spec text for the beta feature with 'Beta feature: Yes (as of X.X.x). Leave feedback' with a link to the new feature Issue.

Once an item is moved out of beta, close its Issue and change the text to say 'Beta feature: No (as of X.X.x)'.
-->

<!-- ### Preparing a Release Candidate

The following steps outline the process to prepare a Release Candidate of {{ cookiecutter.project_repo_name }}. This process makes public the intention and contents of an upcoming release, while allowing work on the next release to continue as usual in `dev`.

1. Create a _Release branch_ from the tip of `dev` named `release-x.y.z`, where `x.y.z` is the intended version of the release. This branch will be used to prepare the Release Candidate. For example, to prepare a Release Candidate for `0.5.0`:

   ```bash
   git fetch
   git checkout origin/dev
   git checkout -b release-0.5.0
   git push -u origin release-0.5.0
   ```

   Changes generated by the steps below should be committed to this branch later.

2. Create a tag like `x.y.z-rcN` for this Release Candidate. For example, for the first `0.5.0` Release Candidate:

   ```bash
   git fetch
   git checkout origin/release-0.5.0
   git tag 0.5.0-rc1
   git push --tags
   ```

3. Publish a [pre-Release in GitHub](proj-releases-new):

   ```md
   Tag version: [tag you just pushed]
   Target: [release branch]
   Release title: [X.Y.Z Release Candidate N]
   Description: [copy in ReleaseNotes.md created earlier]
   This is a pre-release: Check
   ```

4. Open a Pull Request to `main` from the release branch (eg. `0.5.0-rc1`). This pull request is where review comments and feedback will be collected.

5. Conduct Review of the Pull Request that was opened. -->

<!-- #### Incorporating feedback from review

The review process may result in changes being necessary to the release candidate.

For example, if the second Release Candidate for `0.5.0` is being prepared, after committing necessary changes, create a tag on the tip of the release branch like `0.5.0-rc2` and make a new [GitHub pre-Release](proj-releases-new) from there:

```bash
git fetch
git checkout origin/release-0.5.0
# more commits per OMF review
git tag 0.5.0-rc2
git push --tags
```

Repeat as-needed for subsequent Release Candidates. Note the release branch will be pushed to `dev` at key points in the approval process to ensure the community is working with the latest code. -->

<!-- ### Making a Release

The following steps describe how to make an approved [Release Candidate](#preparing-a-release-candidate) an official release of {{ cookiecutter.project_repo_name }}:

1. **Approved**. Ensure review has been completed and approval granted.

2. **Main**. Merge the Pull Request created during the Release Candidate process to `main` to make the release official.

3. **Dev**. Open a Pull Request from the release branch to `dev`. Merge this PR to ensure any changes to the Release Candidate during the review process make their way back into `dev`.

4. **Release**. Publish a [Release in GitHub](proj-releases-new) with the following information

   - Tag version: [X.Y.Z] (note this will create the tag for the `main` branch code when you publish the release)
   - Target: main
   - Release title: [X.Y.Z]
   - Description: copy in Release Notes created earlier
   - This is a pre-release: DO NOT check

5. **Branch**. Finally, keep the release branch and don't delete it. This allows easy access to a browsable spec. -->

<!-- ### Auto Changelog

It is recommended to use the provided auto changelog github workflow to populate the project’s CHANGELOG.md file:

```yml
name: Changelog
on:
  release:
    types:
      - created
jobs:
  changelog:
    runs-on: ubuntu-latest
    steps:
      - name: "Auto Generate changelog"
        uses: heinrichreimer/action-github-changelog-generator@v2.3
        with:
          token: ${{ '{{ secrets.GITHUB_TOKEN }}' }}
```

This provided workflow will automatically populate the CHANGELOG.md with all of the associated changes created since the last release that are included in the current release.

This workflow will be triggered when a new release is created.

If you do not wish to use automatic changelogs, you can delete the workflow and update the CHANGELOG.md file manually. Although, this is not recommended.

For best practices on writing changelogs, see: https://keepachangelog.com/en/1.1.0/#how -->

<!-- ### Hotfix Releases

In rare cases, a hotfix for a prior release may be required out-of-phase with the normal release cycle. For example, if a critical bug is discovered in the `0.3.x` line after `0.4.0` has already been released.

1. Create a _Support branch_ from the tag in `main` at which the hotfix is needed. For example if the bug was discovered in `0.3.2`, create a branch from this tag:

   ```bash
   git fetch
   git checkout 0.3.2
   git checkout -b 0.3.x
   git push -u origin 0.3.x
   ```

2. Merge (or commit directly) the hotfix work into this branch.

3. Tag the support branch with the hotfix version. For example if `0.3.2` is the version being hotfixed:

   ```bash
   git fetch
   git checkout 0.3.x
   git tag 0.3.3
   git push --tags
   ```

4. Create a [GitHub Release](proj-releases-new) from this tag and the support branch. For example if `0.3.3` is the new hotfix version:

   ```md
   Tag version: 0.3.3
   Target: 0.3.x
   Release title: 0.3.3
   Description: [copy in ReleaseNotes created earlier]
   This is a pre-release: DO NOT check
   ```

[proj-releases-new]: https://github.com/{{ cookiecutter.project_org }}/{{ cookiecutter.project_repo_name }}/releases/new
-->

## Documentation

<!-- TODO: Documentation Example

We also welcome improvements to the project documentation or to the existing
docs. Please file an [issue](https://github.com/{{ cookiecutter.project_org }}/{{ cookiecutter.project_repo_name }}/issues).
-->

## Policies

### Open Source Policy

We adhere to the [CMS Open Source
Policy](https://github.com/CMSGov/cms-open-source-policy). If you have any
questions, just [shoot us an email](mailto:opensource@cms.hhs.gov).

### Security and Responsible Disclosure Policy

_Submit a vulnerability:_ Vulnerability reports can be submitted through [Bugcrowd](https://bugcrowd.com/cms-vdp). Reports may be submitted anonymously. If you share contact information, we will acknowledge receipt of your report within 3 business days.

For more information about our Security, Vulnerability, and Responsible Disclosure Policies, see [SECURITY.md](SECURITY.md).

## Public domain

This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0 dedication. By submitting a pull request or issue, you are agreeing to comply with this waiver of copyright interest.
