# Reusable Actions

This repository contains resusable actions and workflow to push updates to repositories.

## Finding Repos (Action)
The [find repos action](https://github.com/DSACMS/repo-scaffolder/blob/main/.github/findRepos/action.yml) takes a [github topic](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics) and a [github org](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/about-organizations) as input.  It 
then queries the github apis with these values to find the repos.

## Updating Files
The [updateStringInRepos](https://github.com/DSACMS/repo-scaffolder/blob/main/.github/workflows/updateStringInRepos.yml) workflow takes a github topic, github org, a string to find, a string to replace the found string with, and a file to find that string in.  Then it raises a pull request in the repos it finds with the string in that file.  It can be triggered from this repo using the [workflow dispatch](https://docs.github.com/en/actions/using-workflows/manually-running-a-workflow#running-a-workflow).  This workflow can be used as a reusable workflow.

## Adding Files
The [addFilesToRepos](https://github.com/DSACMS/repo-scaffolder/blob/main/.github/workflows/addFilesToRepos.yml) workflow takes a github topic, github org, and a file to add to the repo.  It then raises a pull request in the repos it finds with the file to add.  It can be triggered from this repo using the [workflow dispatch](https://docs.github.com/en/actions/using-workflows/manually-running-a-workflow#running-a-workflow).  This workflow can be used as a reusable workflow.

## Resolve Extended JSON Files 