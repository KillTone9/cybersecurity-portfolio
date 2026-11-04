# Mobile Forensics Evidence Handling Notes

This document outlines evidence-handling principles for the Mobile Forensic Suite project. It is not a claim that every control is implemented in the current codebase.

## Acquisition record

For each authorized acquisition, document:
- Case or exercise identifier (avoid personal identifiers in public examples).
- Device make/model and operating-system version, when relevant.
- Acquisition method and tool versions.
- Start/end timestamps and timezone.
- Operator and authorization basis.
- Any errors, interruptions, or limitations.

## Integrity

- Preserve the original acquisition output.
- Calculate cryptographic hashes for acquired files where supported.
- Record algorithm, digest, timestamp, and file identity.
- Recalculate hashes when verifying a copied or transferred artifact.
- Treat a matching hash as an integrity check, not proof that the source data was accurate or complete.

## Analysis and reporting

- Work from verified copies.
- Record parser/tool version and processing options.
- Keep source artifact references for each extracted item.
- Distinguish raw artifacts, parsed records, and analyst interpretation.
- Document unsupported formats and parsing errors.

## Privacy and publication

Never publish real messages, contact details, account identifiers, location history, credentials, or case evidence. Use synthetic datasets for screenshots and demonstrations.
