<!--- # NOTE: Modify sections marked with `TODO` and then rename the file.-->

# How to Contribute

We're so thankful you're considering contributing to an [open source project of
the U.S. government](https://code.gov/)! If you're unsure about anything, just
ask -- or submit the issue or pull request anyway. The worst that can happen is
you'll be politely asked to change something. We appreciate all friendly
contributions.

We encourage you to read this project's CONTRIBUTING policy (you are here), its
[LICENSE](LICENSE.md), and its [README](README.md).

## Getting Started

<!--- ### TODO: If you have 'good-first-issue' or 'easy' labels for newcomers, mention them here.-->

### Building dependencies

In the root directory of the project,
`pip install -r requirements.txt`

### Building the Project

<!--- ### TODO -->

### Workflow and Branching

We follow the [GitHub Flow Workflow](https://guides.github.com/introduction/flow/)

1.  Fork the project
2.  Check out the `main` branch
3.  Create a feature branch
4.  Write code and tests for your change
5.  From your branch, make a pull request against `cmsgov/cmsgov-example-repo/main`
6.  Work with repo maintainers to get your change reviewed
7.  Wait for your change to be pulled into `cmsgov/cmsgov-example-repo/main`
8.  Delete your feature branch

### Coding Style and Linters

This project strives to adhere to the Python Style Guide (http://peps.python.org/pep-0008/). We would recommend using a linter such as pyflakes, flake8, black, or other plugin for your editor or IDE of choice.

-->

### Issues

When creating an issue please try to adhere to the following format:

    module-name: One line summary of the issue (less than 72 characters)

    ### Expected behavior

    As concisely as possible, describe the expected behavior.

    ### Actual behavior

    As concisely as possible, describe the observed behavior.

    ### Steps to reproduce the behavior

    List all relevant steps to reproduce the observed behavior.

    see our .github/ISSUE_TEMPLATE.md for more examples.

### Pull Requests

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

## Reviewing Pull Requests

When you submit a pull request on GitHub, it will be reviewed by the project
community, and once the changes are approved, your commits will be brought into
a development branch for additional testing. Once the changes are merged, they will
be pushed back to the main branch.

If the issue the pull request is addressing is particularly urgent, the pull request
will be merged directly into the main branch. 

## Documentation

We also welcome improvements to the project documentation or to the existing
docs. Please file an [issue](https://github.com/DSACMS/repo-scaffolder/issues).

## Policies

### Open Source Policy

We adhere to the [CMS Open Source
Policy](https://github.com/CMSGov/cms-open-source-policy). If you have any
questions, just [shoot us an email](mailto:opensource@cms.hhs.gov).

### Security and Responsible Disclosure Policy

*Submit a vulnerability:* Vulnerability reports can be submitted through [Bugcrowd](https://bugcrowd.com/cms-vdp). Reports may be submitted anonymously. If you share contact information, we will acknowledge receipt of your report within 3 business days.

For more information about our Security, Vulnerability, and Responsible Disclosure Policies, see [SECURITY.md](SECURITY.md).

## Public domain

This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0 dedication. By submitting a pull request or issue, you are agreeing to comply with this waiver of copyright interest.
