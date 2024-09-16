# DSAC OSPO Outbound Review Checklist
## Tier 1: One-Time Release

### State the Benefit(s) of Sourcing the Project

- [ ] **Cost Savings** 
by making the project freely availbale, this reduces licensing and acquisition costs.
- [ ] **Ease of Repurposing**
The open nature of the code allows users to modify and adapt the software to suit their specific needs, fostering customization and flexibility.
- [ ] **Minimization of Vendor Lock-in/Flexibility of Vendor Choice**
Users are not tied to a single vendor, providing the freeman to choose between different vendors.
- [ ] **Enable Transparency**
The source code is accessible and visible to anyone, promoting transparency in how the software functions, which helps build trust.
- [ ] **Enable Extension/Extensibility**
Users can extend and enhance the functionality of the software by adding their own features.
- [ ] **Increase Interoperability**
Planning in the open enables future compatibility and interoperability between different systems and software applications.
- [ ] **Facilitate Experimentation/Early Adoption**
Working in the open encourages experimentation and early adoption of cutting-edge technologies,leading to faster innovation and improvemnet in software capabilities.

### State3 the Risk(s) of Open Sourcing the Porject, if any

- [ ] **Security Risks**
Vulnerabilities may be exposed if the code is not thoroughly reviewed, potentially leading to security breaches or exploitation.(See: SECURITY.md)Does this project connect to any CMS-internal only systems? Does this project require authorization or authentication to operate? Does this project detail any non-public directories of CMS/HHS systems or people?
- [ ] **Financial Risks**
Costs may arise from maintaining code, community engagemnet, addressing security concerns, or subscription costs, hardware costs, specialized tooling or infrastructure costs, among others. Does this project require any ongoing financial costs or subscription fees?
(e.g. - Cloud Hosting, Specialized build systems, paid maintainers, paid libraries or dependencies.)
- [ ] **Privacy Risks**
Does this project require access to non-public, non synthetic PII,PHI, or other internal-only CMS Systems containing such data or information?

---

### Questions

- Does the code contain or touch any private information such as Personal Identifiable Information (PII) or Protected Health Information (PHI)?
  - Can it be removed? Is it absolutely needed to function? Can it be shipped with synthetic data instead?
 - Does the code interface with any CMS' internal-only systems(e.g. mainframes,JIRA instances, databases, etc..)?
 - Does the repository contain any keys or credentials to access or authenticate with CMS' systems?
   - Can it be removed or is it needed?

   If you answered "yes" to any of the above  questions, your project may be 'sensitive' in nature, and require a more thorough review before sharing publicly. Please reach out to opensource@cms.hhs.gov for guidance. If you answer yes to any of these questions above, it is best to seek quidance **before** releasing open source.

   **Results** 

   *Insert Review Here*




   ---




   ### Code Review

   The existing codebase should be given a one time, top-to-bottom code quality and security vulnerability review by two (or more) engineers who have written production code within the path two years, in the languages used in the project.Engineers should review credential management practices with the development team to ensure that any keys, passwords, or other sensitive configurations are not checked into source code or in the git history.

   The engineers can be federal government employees or trusted partners from outside the agency from other contracts, or form independent testing contracts.Their names, organizations, comments and approval/disapproval on the overall codebase should be tracked in the documents.

   To provide independent review, ideally the engineers should not have been involved in the development of the software product.This includes engineers who wrote part of the software or who direclty provided technical direction and oversight in the creation of the software.

   As part of the code review, engineers should reference modern listings of the most significant software security vulnerabilities. For instance, an acceptable description would be that the engineers showed how they used automated tools and manual review to check each item in __OWASP's current 10 Most Critical Web Application Security Risks.__




   **Results**

   *Insert Review Here*


   ---


   ### Code Analysis 

   A best practice and a requirement for releasing a repository open source at many parts of CMS is to run at least one automated tool for code analysis (such as static code analysis,repolinters, secret scanners) on the codebase to detect for security vulnerabilities or sensitive information, and results have been appropriately addressed. Even if all findings are eventually fixed, if the initial scans revealed significant, severe vulnerabilities(such as SQL injection vulnerabilities),this may indicate that the software development team was not adhering to the best practices required for open source public release, and should be given additional review.

   Ideally, automated tooling for code analysis should be incorporated as a regularly scheduled part of the software development lifecycle. The development team should briefly document how frequently they commit to running these automated scanning tools, and how they will be running these tests, and who will be monitoring, interpreting,and acting upon the results.


   #### Toolkit
   Below is a list of suggested tools to run for code analysis:

| **Tool** |  **Description** |  **Link**   |
:-------| :-------------: | :------: |
| Repo Linter  | Lint repositories for common issues such as missing files etc.| https://github.com/todogroup/repolinter |
|  gitleaks  | Protect and discover secrets using Gitleaks :key:  |  https://github.com/gitleaks/gitleaks
| git filter-repo |  Entirely remove unwanted files / files with sensitive data from a repository's history   |  https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository


**Results**

*Insert Review Here*

----