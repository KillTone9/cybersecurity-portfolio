# Mobile Forensic Suite

**Project type:** Software development / digital forensics  
**Status:** Project documentation draft — source code and test evidence pending

## Overview

Mobile Forensic Suite is a command-line project intended to support a structured mobile-forensics workflow covering acquisition, analysis, and report generation.

The project notes available for this portfolio describe Android Debug Bridge (ADB) and iOS backup acquisition workflows, parsing of mobile application artifacts, and integrity-focused handling of collected data.

## Capabilities described in project notes

- CLI workflow organized around acquisition, analysis, and reporting.
- Android acquisition workflows involving ADB.
- iOS backup acquisition workflow.
- Review of messaging artifacts such as WhatsApp, SMS, and Telegram, subject to source availability and supported formats.
- SQLite-based artifact storage or migration work.
- HMAC-SHA256 and PBKDF2 concepts for integrity and key derivation.

These are based on prior project discussions. Exact implementation details, supported device versions, and feature completeness must be verified against the source before being advertised as released functionality.

## Forensic principles

- Preserve original evidence and work from copies.
- Record acquisition method, timestamps, and tool versions.
- Calculate and verify cryptographic hashes where applicable.
- Maintain an auditable chain-of-custody record.
- Distinguish parsed artifacts from validated conclusions.
- Avoid exposing personal or sensitive data in public examples.

## Planned repository structure

```text
mobile-forensic-suite/
├── README.md
├── docs/
│   ├── architecture.md
│   ├── acquisition-workflows.md
│   └── evidence-handling.md
├── src/
├── tests/
├── samples/
└── reports/
```

This is a proposed structure, not a representation of files currently published.

## Validation checklist

- [ ] Publish source code and dependency manifest.
- [ ] Document supported operating systems and device workflows.
- [ ] Add unit and integration test results.
- [ ] Verify hash generation and integrity checks.
- [ ] Document SQLite schema and migration behavior.
- [ ] Add sanitized sample data and example reports.
- [ ] Document known limitations.

## Skills demonstrated

CLI application design, digital-forensics workflow concepts, mobile artifact analysis, SQLite, cryptographic integrity concepts, and technical documentation.

## Disclaimer

Use only devices and data you own or are explicitly authorized to examine. Do not publish private messages, personal identifiers, credentials, or real case evidence.
