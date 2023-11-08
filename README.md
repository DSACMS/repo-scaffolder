# Repo Scaffolder

## Prerequisites
- python
- github cli
- cookiecutter

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

## Existing Projects
You can update existing projects with the repo scaffolder.  Using the `-s` flag on cookiecutter will not overwrite existing files.  Follow these steps:
1. Create a new branch in your repo
2. cd into folder above
3. run: `cookiecutter -f -s https://github.com/DSACMS/repo-scaffolder --directory=tierX`
4. Make sure when answering the questions you use the existing folder/project name
5. Raise pr into main

## Updating Projects
When creating projects, if you want to receive updates then add `dsacms-tierX` as a github topic to the repo.  The scaffolder repo includes github workflows that will find all repos with that tag and can raise a pull request with an updated string or adding a file.
