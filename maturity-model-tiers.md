# Maturity Model Tiers

This document outlines the maturity model tiers.

## Ordinality

| Level   | Description         |
|---------|---------------------|
| M | Mandatory         |
| R | Recommended       |
| N | Not Recommended   |


## Simplified

| File | Tier 0: Private Repository | Tier 1: One-Time Release | Tier 2: Close Collaboration | Tier 3: Working in Public | Tier 4: Community Governance |
|--------------------------|---|---|----|--|---|
| LICENSE                  | M | M | M | M | M |
| SECURITY.md              | N | M | M | M | M |
| README.md                | M | M | M | M | M |
| CONTRIBUTING.md          | R | R | M | M | M |
| MAINTAINERS.md           | N | N | R | M | M |
| GOVERNANCE.md            | N | N | N | R | M |
| CODEOWNERS.md            | N | N | R | M | M |
| COMMUNITY_GUIDELINES.md  | N | N | M | M | M |
| CODE_OF_CONDUCT.md       | N | N | M | M | M |

## Tier Ordinality

<table>
  <thead>
    <tr>
      <th>File</th>
      <th>Sections</th>
      <th>Tier 0: Private Repository</th>
      <th>Tier 1: One-Time Release</th>
      <th>Tier 2: Close Collaboration</th>
      <th>Tier 3: Working in Public</th>
      <th>Tier 4: Community Governance</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>LICENSE</td>
      <td>License</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>All repositories, whether private or public, must include authorship and copyright information. By default, work done by federal employees is not subject to copyright protections under Title 17 U.S. Code Sections 101 & 105, unless for security or contracting purposes.</td>
    </tr>
    <tr>
      <td>SECURITY.md</td>
      <td>Security & Responsible Disclosure Policy</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>This outlines the Security & Responsibility Disclosure policies including vulnerability submission, etc.</td>
    </tr>
    <tr>
      <td rowspan="22">README.md</td>
      <td>Project Description</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>This should be 1-3 sentence short description of the project that can be used as a 'one-liner' to describe the repo. A best practice is using this same language as the official 'description' on a GitHub repo landing page.</td>
    </tr>
    <tr>
      <!-- <td>README.md</td> -->
      <td>About the Project</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>This should be a longer-form description of the project. It can include history, background, details, problem statements, links to design documents or other supporting materials, or any other information/context that a user or contributor might be interested in.</td>
    </tr>
    <tr>
      <!-- <td>README.md</td> -->
      <td>Project Vision</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td>This should be a forward-looking statement that outlines the desired future state or long-term goals of the project.</td>
    </tr>
    <tr>
      <!-- <td>README.md</td> -->
      <td>Project Mission</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td>This should be a statement that defines the purpose, scope, and specific objectives of the project.</td>
    </tr>
    <tr>
      <!-- <td>README.md</td> -->
      <td>Agency Mission</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightcoral;">N</td>
      <td>Agency-led projects should include information about their agency mission. This should be taken directly from agency websites or wikis.</td>
    </tr>
    <tr>
      <!-- <td>README.md</td> -->
      <td>Team Mission</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightcoral;">N</td>
      <td>Agency-led projects should include information about the team executing on the mission. This should be taken directly from internal team charters and functional statements.</td>
    </tr>
    <tr>
      <!-- <td>README.md</td> -->
      <td>Core Team</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>This information helps with succession planning and provenance for security compliance and remediation. It helps future users and contributors understand where the code originated.</td>
    </tr>
    <tr>
      <!-- <td>README.md</td> -->
      <td>Documentation Index</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>This is a like a 'table of contents" for your documentation. Tier 0/1 projects with simple README.md files without many sections may or may not need this, but it is still extremely helpful to provide "bookmark" or "anchor" links to specific sections of your file to be referenced in tickets, docs, or other communication channels.</td>
    </tr>
    <tr>
      <!-- <td>README.md</td> -->
      <td>Repository Structure</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>Using the "tree" command can be a helpful way to generate this information, but, be sure to update it as the project evolves and changes over time.</td>
    </tr>
    <tr>
      <!-- <td>README.md</td> -->
      <td>Development and Software Delivery Lifecycle</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>Tier 1: Even if the lifecycle is "one-time release" being explicit is better than implicit.</td>
    </tr>
    <tr>
      <!-- <td>README.md</td> -->
      <td>Local Development</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>Use step by step instructions to get from 'zero' to 'running code.' Should include any system libraries or packages that are a 'pre-requisite' to installation of your project. When possible, including install instructions for multiple Operation Systems (or being explicit about which operating system the project was developed on) is a recommended practice.</td>
    </tr>
    <tr>
      <!-- <td>README.md</td> -->
      <td>Coding Style and Linters</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>This section outlines best practices contributors should follow to reduce friction and improve readability, functionality, and quality of contributions to a project. Oftentimes, these checks can be automated and run as part of a continuous integration and deployment pipeline.</td>
    </tr>
    <tr>
      <!-- <td>README.md</td> -->
      <td>Branching Model</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>Even for Tier 0/1 projects with one or a few contributors, branching models (such as git flow) are still recommended as a best practice for keeping feature development history clear, and to help reinforce development best practices.</td>
    </tr>
    <tr>
      <!-- <td>README.md</td> -->
      <td>Contributing</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>For projects that accept contributions, point towards the CONTRIBUTING.md file. For those that do not (tier0/1) not recommended to include this section, instead, mention one-time release, or private repo status instead.</td>
    </tr>
    <tr>
      <!-- <td>README.md</td> -->
      <td>Codeowners</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>Though all tiers have an 'implied' code-owner, since there is at least one author of the repo, explicit is better than implicit. In the case that a project may outlive the employment or contract of the original author, a shared inbox or alias is recommended for longer-lived projects (e.g. opensource@cms.hhs.gov).</td>
    </tr>
    <tr>
      <!-- <td>README.md</td> -->
      <td>Community</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>For projects that are higher tier than a one-time release, pointing your contributors towards wherever your community exists (e.g. email lists, online discussion boards or channels, project backlogs and documentation, etc...).</td>
    </tr>
    <tr>
      <!-- <td>README.md</td> -->
      <td>Community Guidelines</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>Project tiers above one-time release should point towards a CODE_OF_CONDUCT.md file or website providing information around acceptable conduct and reporting mechanisms and escalation strategies. It is better to have these processes defined before they are needed, so you can focus on support if/when there is an incident (e.g. Contributor-covenant.org).</td>
    </tr>
    <tr>
      <!-- <td>README.md</td> -->
      <td>Governance</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td>Make a short statement about how the project is governed (formally, or informally) and link to the GOVERNANCE.md file.</td>
    </tr>
    <tr>
      <!-- <td>README.md</td> -->
      <td>Feedback</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>Direct users towards the channel where they're encouraged to provide feedback, typically a github.com/$REPO/issue/new URL .</td>
    </tr>
    <tr>
      <!-- <td>README.md</td> -->
      <td>Glossary</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td>Even for early-tier projects, this documentation can be extremely valuable. Good candidate content includes any project-specific acronyms (esp applicable for Government projects) and any critical Subject Matter Expertise related vocabulary for people who are new to the domain your project is within.</td>
    </tr>
    <tr>
      <!-- <td>README.md</td> -->
      <td>Policies</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>This section is to explicitly link to Federal policies and guidelines that are required or recommended for Federal projects to comply with, such as  Accessibility (508) Interoperability, Anti-deficiency, Security, Licensing, and other policies that can vary between agencies and domains.</td>
    </tr>
    <tr>
      <!-- <td>README.md</td> -->
      <td>Public Domain</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>A best practice is to list the LICENSE under which a project is released at the bottom of the README. In most cases for Federal repos, we default to Creative Commons Zero 1.0 International (world-wide public domain).</td>
    </tr>
    <tr>
      <td rowspan="15">CONTRIBUTING.md</td>
      <td>How to Contribute</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>Basic instructions about where to send patches, check out source code, and get development support.</td>
    </tr>
    <tr>
      <!-- <td>CONTRIBUTING.md</td> -->
      <td>Getting Started</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightcoral;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>Often includes installation steps, pre-requisites for installation, and instuctions for working with the source code.</td>
    </tr>
    <tr>
      <!-- <td>CONTRIBUTING.md</td> -->
      <td>Team Specific Guidelines</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>This section helps contributors understand any team structure in the project (formal or informal.) Encouraged to point towards the MAINTAINERS.md file for further details.</td>
    </tr>
    <tr>
      <!-- <td>CONTRIBUTING.md</td> -->
      <td>Building dependencies</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightcoral;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>This step is often skipped, so don't forget to include the steps needed to install on your platform. If you project can be multi-platform, this is an excellent place for first time contributors to send patches!</td>
    </tr>
    <tr>
      <!-- <td>CONTRIBUTING.md</td> -->
      <td>Building the Project</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightcoral;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>Be sure to include build scripts and instructions, not just the source code itself!</td>
    </tr>
    <tr>
      <!-- <td>CONTRIBUTING.md</td> -->
      <td>Workflow and Branching</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>If your project has a preferred workflow or branching structure, mention it here. We recommend 'git flow' as a good default.</td>
    </tr>
    <tr>
      <!-- <td>CONTRIBUTING.md</td> -->
      <td>Testing Conventions</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>Discuss where tests can be found, how they are run, and what kind of tests/coverage strategy and goals the project has.</td>
    </tr>
    <tr>
      <!-- <td>CONTRIBUTING.md</td> -->
      <td>Coding Style and Linters</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>HIGHLY ENCOURAGED. Specific tools will vary between different languages/frameworks (e.g. Black for python, esliint for JavaScript, etc...)</td>
    </tr>
    <tr>
      <!-- <td>CONTRIBUTING.md</td> -->
      <td>Writing Issues</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightcoral;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>Make a brief statement about where to file issues, and conventions for doing so. Link to ISSUE_TEMPLATE.md file.</td>
    </tr>
    <tr>
      <!-- <td>CONTRIBUTING.md</td> -->
      <td>Writing Pull Requests</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>Make a brief statement about where to file pull/merge requests, and conventions for doing so. Link to PULL_REQUEST_TEMPLATE.md file.</td>
    </tr>
    <tr>
      <!-- <td>CONTRIBUTING.md</td> -->
      <td>Reviewing Pull Requests</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>Make a brief statement about how pull-requests are reviewed, and who is doing the reviewing. Linking to MAINTAINERS.md can help.</td>
    </tr>
    <tr>
      <!-- <td>CONTRIBUTING.md</td> -->
      <td>Shipping Releases</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td>What cadence does your project ship new releases? (e.g. one-time, ad-hoc, periodically, upon merge of new patches) Who does so?</td>
    </tr>
    <tr>
      <!-- <td>CONTRIBUTING.md</td> -->
      <td>Documentation Updates</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>Where is the documentation hosted? How is it updated? Who updates it?</td>
    </tr>
    <tr>
      <!-- <td>CONTRIBUTING.md</td> -->
      <td>Policies</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightcoral;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>This section is here to explicitly link to Federal policies and guidelines that are required or recommended for Federal projects to comply with, such as Accessibility (508) Interoperability, Anti-deficiency, Security, Licensing, and other policies that can vary between agencies and domains.</td>
    </tr>
    <tr>
      <!-- <td>CONTRIBUTING.md</td> -->
      <td>Public Domain</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightcoral;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>This section is to explicitly link to Federal policies and guidelines that are required or recommended for Federal projects to comply with, such as Accessibility (508) Interoperability, Anti-deficiency, Security, Licensing, and other policies that can vary between agencies and domains.</td>
    </tr>
    <tr>
      <td rowspan="2">MAINTAINERS.md</td>
      <td>Maintainers</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>Who are the project maintainers? List out @USERNAMES where possible so they can be tagged in issues/PRs directly.</td>
    </tr>
    <tr>
      <!-- <td>MAINTAINERS.md</td> -->
      <td>Maintainers Table</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>What groups/domains are maintainers a part of? Does your project have domains/areas that are maintained by specific people? List @USERNAMES directly, or any @ALIASES for groups/teams.</td>
    </tr>
    <tr>
      <td>GOVERNANCE.md</td>
      <td>Governance</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td>Starting at Tier 3 GOVERNANCE.md has basic language about early community governance, how the project make decisions, and how contirbutors are elevated through the leadership process if any (e.g. joining teams, getting maintainer status, etc...)</td>
    </tr>
    <tr>
      <td rowspan="2">CODEOWNERS.md</td>
      <td>List of Users</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>Who are the points of contact in your project who are responsible/accountable for the project? This can often be an engineering or design manager or leader, who may or may not be the primary maintainers of the project.</td>
    </tr>
    <tr>
      <!-- <td >CODEOWNERS.md</td> -->
      <td>List of Repo Domains by Owner</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>e.g. Frontend, Backend, Documentation</td>
    </tr>
    <tr>
      <td rowspan="3">COMMUNITY_GUIDELINES.md</td>
      <td>Principles</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>This section communicates to prospective contributors and users what the values of your community are. The examples provided in the template were established by the Justice40 project at USDS.</td>
    </tr>
    <tr>
      <!-- <td>COMMUNITY_GUIDELINES.md</td> -->
      <td>Community Guidelines</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>This section communicates specific norms and guidelines for how to participate and contribute positively to your community. The more explicit you can be about behaviors you'd like to encourage or discourage, the less friction new contributors will experience in onboarding and operating within your project.</td>
    </tr>
    <tr>
      <!-- <td>COMMUNITY_GUIDELINES.md</td> -->
      <td>Acknowledgements</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>This section recognizes previous work and best practices established by the other members of the federal open source community such as USDS, GSA, 18F, and the Justice40 Project.</td>
    </tr>
    <tr>
      <td rowspan="2">CODE_OF_CONDUCT.md</td>
      <td>Contributor Code of Conduct</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>Project tiers above one-time release should include a CODE_OF_CONDUCT.md file or website providing information around acceptable conduct and reporting mechanisms and escalation strategies. It is better to have these processes defined before they are needed, so you can focus on support if/when there is an incident. (e.g. Contributor-covenant.org)</td>
    </tr>
    <tr>
      <!-- <td>CODE_OF_CONDUCT.md</td> -->
      <td>Acknowledgements</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td>This section recognizes previous work and best practices established by the other members of the federal open source community such as USDS, GSA, 18F, and the Justice40 Project.</td>
    </tr>
  </tbody>
</table>

<!-- HTML table with Color
<table>
  <thead>
    <tr>
      <th>Level</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="background-color: lightgreen;">M</td>
      <td>Mandatory</td>
    </tr>
    <tr>
      <td style="background-color: lightblue;">R</td>
      <td>Recommended</td>
    </tr>
    <tr>
      <td style="background-color: lightcoral;">N</td>
      <td>Not Recommended</td>
    </tr>
  </tbody>
</table> -->

<!-- HTML Table with color -->
<!-- <table>
  <thead>
    <tr>
      <th>File</th>
      <th>Tier 0: Private Repository</th>
      <th>Tier 1: One-Time Release</th>
      <th>Tier 2: Close Collaboration</th>
      <th>Tier 3: Working in Public</th>
      <th>Tier 4: Community Governance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>LICENSE</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
    </tr>
    <tr>
      <td>SECURITY.md</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
    </tr>
    <tr>
      <td>README.md</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
    </tr>
    <tr>
      <td>CONTRIBUTING.md</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
    </tr>
    <tr>
      <td>MAINTAINERS.md</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
    </tr>
    <tr>
      <td>GOVERNANCE.md</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
    </tr>
    <tr>
      <td>CODEOWNERS.md</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightblue;">R</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
    </tr>
    <tr>
      <td>COMMUNITY_GUIDELINES.md</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
    </tr>
    <tr>
      <td>CODE_OF_CONDUCT.md</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightcoral;">N</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
      <td style="background-color: lightgreen;">M</td>
    </tr>
  </tbody>
</table> -->

<!-- Markdown Table -->
<!-- | File | Sections | Tier 0: Private Repository | Tier 1: One-Time Release | Tier 2: Close Collaboration | Tier 3: Working in Public | Tier 4: Community Governance | Notes |
|--------------------------|---|---|----|--|---|---|---|
| LICENSE                  | License | M | M | M | M | M | All repositories, whether private or public, must include authorship and copyright information. By default, work done by federal employees is not subject to copyright protections under Title 17 U.S. Code Sections 101 & 105, unless for security or contracting purposes. |
| SECURITY.md              | Security & Responsible Disclosure Policy | N | M | M | M | M | This outlines the Security & Responsibility Disclosure policies including vulnerability submission, etc. |
| README.md                | Project Description | M | M | M | M | M | This should be 1-3 sentence short description of the project that can be used as a 'one-liner' to describe the repo. A best practice is using this same language as the official 'description' on a GitHub repo landing page. |
| README.md                | About the Project | M | M | M | M | M | This should be a longer-form description of the project. It can include history, background, details, problem statements, links to design documents or other supporting materials, or any other information/context that a user or contributor might be interested in. |
| README.md                | Project Vision | R | N | M | R | R | This should be a forward-looking statement that outlines the desired future state or long-term goals of the project.|
| README.md                | Project Mission | R | R | M | R | R | This should be a statement that defines the purpose, scope, and specific objectives of the project.|
| README.md                | Agency Mission | R | R | M | R | N | Agency-led projects should include information about their agency mission. This should be taken directly from agency websites or wikis. |
| README.md                | Team Mission | R | R | M | R | N | Agency-led projects should include information about the team executing on the mission. This should be taken directly from internal team charters and functional statements. |
| README.md                | Core Team | R | M | M | M | M | This information helps with succession planning and provenance for security compliance and remediation. It helps future users and contributors understand where the code originated. |
| README.md                | Documentation Index | R | R | R | M | M | This is a like a 'table of contents" for your documentation. Tier 0/1 projects with simple README.md files without many sections may or may not need this, but it is still extremely helpful to provide "bookmark" or "anchor" links to specific sections of your file to be referenced in tickets, docs, or other communication channels. |
| README.md                | Repository Structure | R | R | R | M | M | Using the "tree" command can be a helpful way to generate this information, but, be sure to update it as the project evolves and changes over time. |
| README.md                | Development and Software Delivery Lifecycle | N | R | R | M | M | Tier 1: Even if the lifecycle is "one-time release" being explicit is better than implicit. |
| README.md                | Local Development | R | R | M | M | M | Use step by step instructions to get from 'zero' to 'running code.' Should include any system libraries or packages that are a 'pre-requisite' to installation of your project. When possible, including install instructions for multiple Operation Systems (or being explicit about which operating system the project was developed on) is a recommended practice. |
| README.md                | Coding Style and Linters | R | R | M | M | M | This section outlines best practices contributors should follow to reduce friction and improve readability, functionality, and quality of contributions to a project. Oftentimes, these checks can be automated and run as part of a continuous integration and deployment pipeline. |
| README.md                | Branching Model | R | R | R | M | M | Even for Tier 0/1 projects with one or a few contributors, branching models (such as git flow) are still recommended as a best practice for keeping feature development history clear, and to help reinforce development best practices. |
| README.md                | Contributing | N | R | M | M | M | For projects that accept contributions, point towards the CONTRIBUTING.md file. For those that do not (tier0/1) not recommended to include this section, instead, mention one-time release, or private repo status instead. |
| README.md                | Codeowners | N | R | M | M | M | Though all tiers have an 'implied' code-owner, since there is at least one author of the repo, explicit is better than implicit. In the case that a project may outlive the employment or contract of the original author, a shared inbox or alias is recommended for longer-lived projects (e.g. opensource@cms.hhs.gov). |
| README.md                | Community | R | R | M | M | M | For projects that are higher tier than a one-time release, pointing your contributors towards wherever your community exists (e.g. email lists, online discussion boards or channels, project backlogs and documentation, etc...). |
| README.md                | Community Guidelines | R | R | M | M | M | Project tiers above one-time release should point towards a CODE_OF_CONDUCT.md file or website providing information around acceptable conduct and reporting mechanisms and escalation strategies. It is better to have these processes defined before they are needed, so you can focus on support if/when there is an incident (e.g. Contributor-covenant.org). |
| README.md                | Governance | N | N | R | R | M | Make a short statement about how the project is governed (formally, or informally) and link to the GOVERNANCE.md file. |
| README.md                | Feedback | N | R | R | M | M | Direct users towards the channel where they're encouraged to provide feedback, typically a github.com/$REPO/issue/new URL . |
| README.md                | Glossary | R | R | R | R | M | Even for early-tier projects, this documentation can be extremely valuable. Good candidate content includes any project-specific acronyms (esp applicable for Government projects) and any critical Subject Matter Expertise related vocabulary for people who are new to the domain your project is within. |
| README.md                | Policies | M | M | M | M | M | This section is to explicitly link to Federal policies and guidelines that are required or recommended for Federal projects to comply with, such as  Accessibility (508) Interoperability, Anti-deficiency, Security, Licensing, and other policies that can vary between agencies and domains. |
| README.md                | Public Domain | M | M | M | M | M | A best practice is to list the LICENSE under which a project is released at the bottom of the README. In most cases for Federal repos, we default to Creative Commons Zero 1.0 International (world-wide public domain). |
| CONTRIBUTING.md                | How to Contribute | R | R | M | M | M | Basic instructions about where to send patches, check out source code, and get development support. |
| CONTRIBUTING.md                | Getting Started | R | M | M | M | M | Often includes installation steps, pre-requisites for installation, and instuctions for working with the source code. |
| CONTRIBUTING.md                | Team Specific Guidelines | N | N | R | M | M | This section helps contributors understand any team structure in the project (formal or informal.) Encouraged to point towards the MAINTAINERS.md file for further details. |
| CONTRIBUTING.md                | Building dependencies | R | M | M | M | M | This step is often skipped, so don't forget to include the steps needed to install on your platform. If you project can be multi-platform, this is an excellent place for first time contributors to send patches! |
| CONTRIBUTING.md                | Building the Project | R | M | M | M | M | Be sure to include build scripts and instructions, not just the source code itself! |
| CONTRIBUTING.md                | Workflow and Branching | R | R | M | M | M | If your project has a preferred workflow or branching structure, mention it here. We recommend 'git flow' as a good default. |
| CONTRIBUTING.md                | Testing Conventions | R | R | R | M | M | Discuss where tests can be found, how they are run, and what kind of tests/coverage strategy and goals the project has. |
| CONTRIBUTING.md                | Coding Style and Linters | R | R | M | M | M | HIGHLY ENCOURAGED. Specific tools will vary between different languages/frameworks (e.g. Black for python, esliint for JavaScript, etc...) |
| CONTRIBUTING.md                | Writing Issues | R | M | M | M | M | Make a brief statement about where to file issues, and conventions for doing so. Link to ISSUE_TEMPLATE.md file. |
| CONTRIBUTING.md                | Writing Pull Requests | N | N | R | M | M | Make a brief statement about where to file pull/merge requests, and conventions for doing so. Link to PULL_REQUEST_TEMPLATE.md file. |
| CONTRIBUTING.md                | Reviewing Pull Requests | N | N | R | M | M | Make a brief statement about how pull-requests are reviewed, and who is doing the reviewing. Linking to MAINTAINERS.md can help. |
| CONTRIBUTING.md                | Shipping Releases | N | N | R | R | M | What cadence does your project ship new releases? (e.g. one-time, ad-hoc, periodically, upon merge of new patches) Who does so? |
| CONTRIBUTING.md                | Documentation Updates | R | R | R | M | M | Where is the documentation hosted? How is it updated? Who updates it? |
| CONTRIBUTING.md                | Policies | R | M | M | M | M | This section is here to explicitly link to Federal policies and guidelines that are required or recommended for Federal projects to comply with, such as Accessibility (508) Interoperability, Anti-deficiency, Security, Licensing, and other policies that can vary between agencies and domains. |
| CONTRIBUTING.md                | Public Domain | R | M | M | M | M | This section is to explicitly link to Federal policies and guidelines that are required or recommended for Federal projects to comply with, such as Accessibility (508) Interoperability, Anti-deficiency, Security, Licensing, and other policies that can vary between agencies and domains. |
| MAINTAINERS.md                | Maintainers | N | N | R | M | M | Who are the project maintainers? List out @USERNAMES where possible so they can be tagged in issues/PRs directly. |
| MAINTAINERS.md                | Maintainers Table | N | N | R | M | M | What groups/domains are maintainers a part of? Does your project have domains/areas that are maintained by specific people? List @USERNAMES directly, or any @ALIASES for groups/teams. |
| GOVERNANCE.md                | Governance | N | N | N | R | M | Starting at Tier 3 GOVERNANCE.md has basic language about early community governance, how the project make decisions, and how contirbutors are elevated through the leadership process if any (e.g. joining teams, getting maintainer status, etc...) |
| CODEOWNERS.md                | List of Users | N | N | R | M | M | Who are the points of contact in your project who are responsible/accountable for the project? This can often be an engineering or design manager or leader, who may or may not be the primary maintainers of the project. |
| CODEOWNERS.md                | List of Repo Domains by Owner | N | N | R | M | M | e.g. Frontend, Backend, Documentation |
| COMMUNITY_GUIDELINES.md                | Principles | N | N | M | M | M | This section communicates to prospective contributors and users what the values of your community are. The examples provided in the template were established by the Justice40 project at USDS. |
| COMMUNITY_GUIDELINES.md                | Community Guidelines | N | N | M | M | M | This section communicates specific norms and guidelines for how to participate and contribute positively to your community. The more explicit you can be about behaviors you'd like to encourage or discourage, the less friction new contributors will experience in onboarding and operating within your project. |
| COMMUNITY_GUIDELINES.md                | Acknowledgements | N | N | M | M | M | This section recognizes previous work and best practices established by the other members of the federal open source community such as USDS, GSA, 18F, and the Justice40 Project. |
| CODE_OF_CONDUCT.md                | Contributor Code of Conduct | N | N | M | M | M | Project tiers above one-time release should include a CODE_OF_CONDUCT.md file or website providing information around acceptable conduct and reporting mechanisms and escalation strategies. It is better to have these processes defined before they are needed, so you can focus on suppport if/when there is an incident. (e.g. Contributor-covenant.org)  |
| CODE_OF_CONDUCT.md               | Acknowledgements | N | N | M | M | M | This section recognizes previous work and best practices established by the other members of the federal open source community such as USDS, GSA, 18F, and the Justice40 Project. | -->
