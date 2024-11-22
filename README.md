# Repo Scaffolder
Templates and commandline tools for creating repositories for US Federal open source projects

## Prerequisites
- python
- github cli
- cookiecutter
- [repolinter](https://github.com/todogroup/repolinter)

## Need help picking a tier?
If you do not know what tier your project is, the cookiecutter will walk you through questions to figure out what tier you need.  Run:
```
cookiecutter https://github.com/DSACMS/repo-scaffolder
```

## Know what tier you need?
If you know what tier you need, you can run the cookiecutter for an individual tier.  Use the below command with `X` substituted for the tier number.
```
cookiecutter https://github.com/DSACMS/repo-scaffolder --directory=tierX
```

## Add code.json to your project
To add code.json into your project, navigate to your project's `.github` directory and run the following cookiecutter command. You will be asked questions about the project (see cookiecutter.json) in order to collect and store this metadata in code.json.
```
cookiecutter . --directory=codejson
```

## Existing Projects
You can update existing projects with the repo scaffolder.  Using the `-s` flag on cookiecutter will not overwrite existing files.  Follow these steps:
1. Create a new branch in your repo
2. cd into folder above
3. run: `cookiecutter -f -s https://github.com/DSACMS/repo-scaffolder --directory=tierX`
4. Make sure when answering the questions you use the existing folder/project name
5. Raise pr into main

## Updating Projects
When creating projects, if you want to receive updates then add `dsacms-tierX` as a github topic to the repo.  The scaffolder repo includes github workflows that will find all repos with that tag and can raise a pull request with an updated string or adding a file.  See [actions.md](https://github.com/DSACMS/repo-scaffolder/blob/main/.github/actions.md) for more information.

## Editing or Adding Tiers
At a top level, each tier consists of a folder for `hooks`, a folder containing the files to be added (`{{cookiecutter.project_slug}}`), and a `cookiecutter.json` defining the questions cookiecutter asks.  These naming conventions must be 
followed as that is what cookiecutter picks up.  The `hooks` folder needs to be duplicated in each tier.  The folder 
containing the files to be added can include slugged out variables such as `{{ cookiecutter.project_name }}` that can 
be filled in by the answers to `cookiecutter.json`.  For example, `{{ cookiecutter.project_name }}` will be filled in by 
this question - `"project_name": "My Project",`.  See the [cookiecutter docs](https://cookiecutter.readthedocs.io/en/stable/) 
for more information.

## Repolinter

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

## Maturity Models
See our Maturity Model Tiers Document for reference: https://github.com/DSACMS/repo-scaffolder/blob/main/maturity-model-tiers.pdf

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

*Submit a vulnerability:* Vulnerability reports can be submitted through [Bugcrowd](https://bugcrowd.com/cms-vdp). Reports may be submitted anonymously. If you share contact information, we will acknowledge receipt of your report within 3 business days.

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

