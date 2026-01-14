# HEP 0 - HEP Purpose, Policy, and Guidelines

<table>
<tr><td> Identifier </td><td> HEP 0 </td>
<tr><td> Title </td><td> HEP Purpose, Policy, and Guidelines </td>
<tr><td> Status </td><td> Accepted </td></tr>
<tr><td> Author(s) </td><td> Demetris Roumis </td></tr>
<tr><td> Created </td><td> March 18, 2024</td></tr>
<tr><td> Updated </td><td> April 15, 2024</td></tr>
<tr><td> Discussion </td><td> https://github.com/holoviz/holoviz/pull/395#issuecomment-2007702201 </td></tr>
<tr><td> Implementation </td><td> NA </td></tr>
</table>

## Summary

HEP 0 outlines the purpose, policy, and guidelines for future HEPs. This document aims to ensure that the process of proposing and implementing enhancements to the HoloViz ecosystem is clear, structured, and inclusive.

### What is a HEP?

A HEP is a HoloViz Enhancement Proposal, a design document requiring widespread attention and discussion that either proposes a specific change or else clarifies and codifies existing practice. These changes or codifications can be technical or address the social aspects of the organization, like governance or conduct. HEPs should provide a concise specification and rationale for the proposed change. HEPs serve as the principal means for proposing significant changes and formalizations for the HoloViz ecosystem, enabling the community to engage in informed decision-making while also documenting the proposals and the processes behind these decisions.

HEPs are maintained as text files using Markdown for formatting in the [HoloViz/HoloViz](https://github.com/holoviz/holoviz) repository. Their revision history is a historical record of the proposed change.

## Policy
### Core Developers
There are several references in this HEP to 'core developers'. This term refers to the currently active HoloViz core team members, collectively described by the combined MEMBERS.md files ([example](https://github.com/holoviz/holoviz/blob/main/doc/about/governance/project-docs/MEMBERS.md
)) in each of the HoloViz repositories. The core developers are reachable on HoloViz [GitHub](https://github.com/holoviz/holoviz) or [Discord](https://discord.gg/rb6gPXbdAr) with the handle: `@holoviz-dev`.

### Steering Committee
There are several references in this HEP to the 'steering committee'. The currently active HoloViz steering committee is listed in [STEERING-COMMITTEE.md](https://github.com/holoviz/holoviz/blob/main/doc/about/governance/org-docs/STEERING-COMMITTEE.md), and is governed by [CHARTER.md](https://github.com/holoviz/holoviz/blob/main/doc/about/governance/org-docs/CHARTER.md). The steering committee members are reachable on HoloViz [GitHub](https://github.com/holoviz/holoviz) or [Discord](https://discord.gg/rb6gPXbdAr) with the handle: `@steering-committee`.

### Workflow
#### Initiation
The HEP process begins with an idea for how HoloViz works or should work, whether that is a change from current practice or an explicit declaration of current practice. These enhancements can be technical or address the social aspects of the organization, such as governance or conduct. 

Before beginning to write a HEP, it is best to ascertain if the idea fits the intent of the HEP process and has a chance of acceptance. Informally vetting an idea publicly before going as far as writing a HEP is meant to save the potential proposer time. Small or uncontroversial changes often do not need a HEP and can be decided on in the [community channels](https://holoviz.org/community.html). Major or potentially controversial changes, such as those that require collaboration across multiple HoloViz projects, are expected to be submitted as HEPs. When it is unclear if an enhancement is suited for a HEP, ask HoloViz core developers to provide guidance. For example, the 'new-contributors' Discord channel is open to the public and a good place to ask.

#### Drafting
Once the proposer has confirmed with the HoloViz core developers that an idea has any chance of acceptance, a draft HEP should be written following the format described below. Drafting can take place in a pull request to the HoloViz/HoloViz repository, but the status should be changed to 'draft' while working.

HEPs should focus on a single issue; broad topics for discussion should be split into multiple well-focused HEPs.

#### Submission and Consensus-Building 
Once complete, the draft HEP should be submitted as a pull request to the HoloViz/HoloViz repository with the status changed to 'proposed'. At this point, all members of the HoloViz community are welcome and encouraged to participate in the review in a civil and respectful manner.

The HEP proposer is responsible for following the discussion on the pull request, answering questions, making updates to the proposal as part of the consensus-building process, and documenting dissenting opinions. In general, the goal is to make sure that the community reaches consensus, not to provide a rigid policy for people to try to game. When in doubt, err on the side of asking for more feedback and looking for opportunities to compromise.

When the proposer determines that the HEP is ready, they must notify the HoloViz core developers that it is ready for a formal review (e.g., in a comment on the pull request, using `@holoviz-dev`). This message must also describe any major points of contention and how they were resolved. 

#### Review and Resolution
A HoloViz core developer will then formally review the pull request for format, scope, and evidence of consensus. They may also notify other interested parties to weigh in on the HEP. If consensus has been reached, the HoloViz core developer will update the status of the pull request, assign a HEP number, add a link to the discussion in the [HEP table](index.md), and merge it. All HEPs will be resolved as either 'rejected', 'accepted', or 'deferred' depending on the consensus of the community.

In unusual and controversial cases where consensus has not been possible to achieve, a HoloViz core developer may ask the steering committee to take a HEP up for vote, following the policies described in [CHARTER.md](https://github.com/holoviz/holoviz/blob/main/doc/governance/org-docs/CHARTER.md).

#### Amending Existing HEPs
Once a HEP has been accepted, there may be cases where amendments are needed due to implementation challenges discovered after acceptance, community feedback during implementation, evolving requirements or best practices, error corrections or clarifications. For minor amendments (corrections, clarifications, or small adjustments that don't change the core intent), the original author or a core developer may submit a pull request with the changes and update the "Updated" date in the HEP table. For significant amendments that substantially alter the original proposal, a new HEP should be created that explicitly references and potentially supersedes the original. This ensures that major changes receive the same level of community review as the original proposal. In either case, the amendment process should follow similar community consensus principles as outlined in the original submission process.

## HEP Format


### Title
All HEPs should begin with markdown title-level heading in the format of '# HEP {Identifier} - {Title}'. The identifier should remain a placeholder until a core developer has reviewed the pull request and assigned a number. The `Title` should match the entry in the table below.

### Table
Next, each HEP should include a table with the following information:

<table>
<tr><td> Identifier </td><td> [Number to be assigned by HoloViz core developer upon HEP acceptance] </td>
<tr><td> Title </td><td> A short title of the proposal </td>
<tr><td> Status </td><td> Draft | Proposed | Accepted | Rejected | Deferred | Implemented | Superseded </td></tr>
<tr><td> Author(s) </td><td> Full Name [email is optional] </td></tr>
<tr><td> Created </td><td> March 15, 2024</td></tr>
<tr><td> Updated </td><td> March 15, 2024</td></tr>
<tr><td> Discussion </td><td> link to the issue where the HEP is being discussed, NA before submission </td></tr>
<tr><td> Implementation </td><td> link to the PR for the implementation, NA if not available </td></tr>
</table>

### Summary
A concise overview of the HEP's content.

### Resolution (if applicable)
A concise summary of the technical plan of action.

### Specification
If a HEP is perscriptive in nature (providing explicit guidelines or rules to follow), a **Specification** or **Policy** section is required to convey the technical details of the proposed enhancement.

### Optional Sections
Some sections that may be
included if appropriate for the proposal include:

- **Motivation/Background**: Why the proposed change or formalization is needed (beyond what is covered in the Summary).
- **Rationale**: Why particular decisions were made in the proposal.
- **Backwards Compatibility**: Will the proposed change break existing packages or workflows.
- **Alternatives**: Any alternatives considered during the design.
- **Sample Implementation/Illustration**: Links to prototype or a sample implementation of the proposed change.
- **FAQ**: Frequently asked questions (and answers to them).
- **Compliance**: Any mechanisms that promote adherence to HEP guidelines, favoring automation when possible.
- **Reference**: Any references used in the design of the HEP.

### Copyright
A final **Copyright** section is required.

## Pronunciation
HEP is to be pronounced `/hep/`.

## Reference
A significant portion of this document was adapted from [CEP 1](https://github.com/conda-incubator/ceps/blob/main/cep-0001.md) by the conda community. The [Numpy](https://numpy.org/neps/nep-0000.html) and [Python](https://peps.python.org/pep-0001/) versions of enhancement proposal guidelines were also referenced for inspiration.

## Copyright
This document is placed in the public domain or under the CC0-1.0-Universal license, whichever is more permissive.

