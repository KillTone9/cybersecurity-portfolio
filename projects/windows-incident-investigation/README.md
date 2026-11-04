# Windows Incident Investigation Exercises

**Project type:** Blue Team / Endpoint investigation  
**Status:** Exercise documentation draft — event samples and case reports pending

## Overview

This project collects controlled Windows investigation exercises focused on understanding endpoint telemetry and recognizing behaviors that may warrant further investigation.

The intended approach is evidence-led: an event or unusual process is a lead, not automatically a confirmed security incident.

## Tools and data sources

- Windows Event Viewer.
- Sysmon.
- Autoruns.
- Process Monitor (Procmon).
- PowerShell.
- MITRE ATT&CK knowledge base.

## Investigation topics

- Failed and successful logons.
- Process creation and parent-child relationships.
- PowerShell command-line review.
- Scheduled tasks and Run-key persistence locations.
- Unusual executable paths and process behavior.
- Correlation of endpoint events with network activity.

## Selected event references

| Source | Event ID | Meaning |
|---|---:|---|
| Windows Security | 4624 | Successful logon |
| Windows Security | 4625 | Failed logon |
| Sysmon | 1 | Process creation |
| Sysmon | 3 | Network connection |
| Sysmon | 22 | DNS query |

Event interpretation depends on configuration, log availability, and surrounding context. Event IDs alone do not establish malicious activity.

## Investigation workflow

1. Establish the system, time range, and exercise scope.
2. Collect relevant event records.
3. Build a process timeline.
4. Inspect command lines, parent processes, paths, and signatures.
5. Correlate logon, process, DNS, and network events.
6. Identify benign explanations and possible false positives.
7. Document supporting evidence and confidence.
8. Recommend containment or escalation only when justified.

## Planned evidence

- [ ] Sanitized EVTX or exported event samples.
- [ ] Sysmon configuration used for the exercise.
- [ ] Process tree screenshots.
- [ ] Timeline of relevant events.
- [ ] MITRE ATT&CK technique mapping with rationale.
- [ ] Short incident-investigation reports.

## Skills demonstrated

Windows event analysis, Sysmon telemetry, process investigation, persistence concepts, timeline development, false-positive awareness, and technical reporting.

## Disclaimer

Perform exercises only on systems you own or are authorized to investigate. Use benign test activity and sanitize all evidence before publication.
