# Windows and Sysmon Event Reference

Quick reference for controlled investigation exercises.

| Log source | Event ID | Meaning | Investigation context |
|---|---:|---|---|
| Windows Security | 4624 | Successful logon | Account, logon type, source context |
| Windows Security | 4625 | Failed logon | Failure reason, account, source context |
| Sysmon | 1 | Process creation | Image, command line, parent process, user |
| Sysmon | 3 | Network connection | Process, destination, protocol |
| Sysmon | 22 | DNS query | Query name, process, result |

## Important interpretation notes

- Event availability depends on audit policy and Sysmon configuration.
- Event IDs are context, not verdicts.
- Correlate timestamps and host identity across data sources.
- Consider normal administrative activity and software updates as possible benign explanations.
- Preserve original event records and document the time zone.

This reference is educational and does not claim that the listed events were collected in a completed investigation.
