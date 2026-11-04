# SOC Monitoring Home Lab

**Project type:** Blue Team / Security Operations  
**Status:** Lab documentation draft — configurations, sample logs, and screenshots pending

## Overview

This project documents a learning environment for practicing security monitoring, log review, and initial alert triage using Wazuh and Splunk.

The intended workflow reflects entry-level SOC responsibilities: understand the alert, validate the underlying events, gather context, determine whether escalation is warranted, and document the decision.

## Tools and concepts

- Wazuh — security monitoring and log analysis.
- Splunk — search and investigation using SPL.
- Windows Event Viewer and Sysmon — endpoint telemetry.
- MITRE ATT&CK — technique classification.
- Incident triage — distinguish events, alerts, and confirmed incidents.

## Investigation workflow

1. Identify the alert source, timestamp, host, and user.
2. Review the raw event and relevant surrounding events.
3. Validate whether the activity is expected or suspicious.
4. Correlate endpoint, identity, and network context where available.
5. Map relevant behavior to MITRE ATT&CK when justified.
6. Record evidence, confidence, impact, and recommended next steps.
7. Escalate when the available evidence supports further investigation.

## Example investigation topics

- Repeated failed logons and Windows Event ID 4625.
- Successful logons and Windows Event ID 4624.
- Sysmon process creation events (Event ID 1).
- Suspicious parent-child process relationships.
- Unusual PowerShell execution.
- Persistence-related registry or scheduled-task activity.

These are proposed practice scenarios, not claims of detections already implemented in a running lab.

## Planned evidence

- [ ] Lab architecture diagram.
- [ ] Wazuh agent and manager configuration (sanitized).
- [ ] Splunk searches and dashboards.
- [ ] Sample Windows and Sysmon events.
- [ ] Alert triage case notes.
- [ ] Screenshots showing investigation steps.
- [ ] Detection logic with false-positive considerations.

## Skills demonstrated

Log analysis, alert triage, SIEM fundamentals, Windows telemetry, event correlation, MITRE ATT&CK mapping, and incident documentation.

## Disclaimer

Generate test events only in an isolated lab or systems you are authorized to monitor. Remove hostnames, usernames, IPs, tokens, and other sensitive data before publication.
