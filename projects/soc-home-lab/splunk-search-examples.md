# Splunk Search Examples for a SOC Practice Lab

These are illustrative SPL starting points. Field names depend on the data source and sourcetype configured in the lab. They have not been validated against a particular dataset in this repository.

## Failed Windows logons (Event ID 4625)

```spl
index=windows EventCode=4625
| stats count by host, Account_Name, Source_Network_Address
| sort - count
```

## Successful Windows logons (Event ID 4624)

```spl
index=windows EventCode=4624
| stats count by host, Account_Name, Logon_Type
| sort - count
```

## Sysmon process creation (Event ID 1)

```spl
index=sysmon EventCode=1
| table _time host User Image ParentImage CommandLine
| sort - _time
```

## Triage notes

- Confirm the actual field names with `| fieldsummary` or `| table *` on a small sample.
- Establish a baseline before treating volume as suspicious.
- Correlate events by host, user, timestamp, and process context.
- A failed logon or unusual process is an event to investigate, not automatically a confirmed incident.
- Record false-positive explanations and evidence gaps.

Use only logs from systems you own or are authorized to monitor. Sanitize hostnames, usernames, and addresses before publishing screenshots.
