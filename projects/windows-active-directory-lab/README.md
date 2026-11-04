# Windows Server and Active Directory Lab

**Project type:** Windows infrastructure / identity and access management  
**Status:** Lab documentation draft — topology and configuration evidence pending

## Overview

This project documents hands-on learning with Windows Server and Active Directory in a virtualized environment. The focus is domain fundamentals, identity administration, Group Policy, and authentication concepts relevant to IT support and security operations.

## Topics covered in the lab work

- Domain and directory-service fundamentals.
- User and group administration.
- Organizational Units (OUs).
- Group Policy Objects (GPOs).
- Kerberos and NTLM authentication concepts.
- Windows event review and basic troubleshooting.

## Suggested lab workflow

1. Build an isolated virtual network.
2. Install and configure a Windows Server domain controller.
3. Create a test domain and organizational structure.
4. Create test users and security groups.
5. Apply a GPO to a controlled test OU.
6. Join a Windows client to the domain.
7. Validate policy application and authentication.
8. Review relevant logs and document results.

This workflow is a reproducible plan; configuration screenshots and command output should be added after the environment is available.

## Planned evidence

- [ ] Network and virtual-machine diagram.
- [ ] Domain and OU structure (using fictional names).
- [ ] Example user/group configuration.
- [ ] GPO settings and client-side validation.
- [ ] Authentication event examples.
- [ ] Troubleshooting notes.

## Skills demonstrated

Windows Server fundamentals, Active Directory, identity administration, Group Policy, authentication concepts, virtualization, and technical documentation.

## Security considerations

Use test identities and an isolated lab. Apply least privilege, avoid reusing personal passwords, and never publish real domain credentials, private IP details tied to a live network, or sensitive organizational data.
