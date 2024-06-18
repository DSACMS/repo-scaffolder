# Code Owners
<!-- TODO: Who are the points of contact in your project who are responsible/accountable for the project? This can often be an engineering or design manager or leader, who may or may not be the primary maintainers of the project. List them by GitHub Username-->
{% set code_owners = cookiecutter.code_owners.split(',') %}
{% for item in code_owners %}- {{ item }}
{% endfor %}

## Repo Domains

<!-- TODO: List out the various domains of the project or teams of owners for that domain (e.g. Frontend, Backend, Documentation)-->
documentation/* {usernames of documentation owners}  
frontend/* {usernames of frontend owners}
