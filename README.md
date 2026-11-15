# IOC Enricher

A Python tool for validating and enriching **Indicators of Compromise (IOCs)**,
such as IP addresses, domains and file hashes, to support SOC investigations.

> Learning project, built while preparing to contribute to
> [The Honeynet Project](https://www.honeynet.org/) for GSoC 2027.

## Why

Analysts receive IOCs from alerts, reports and threat feeds. Before looking them
up in threat-intelligence services, the tool should:

- reject invalid input (e.g. `999.1.1.1` is not a real IP)
- skip private and internal IPs (e.g. `192.168.1.10`), which waste API calls
  and can leak internal network details to third parties

## Current features

- `is_ip()`: checks whether a value is a valid IPv4 or IPv6 address
- `is_public_ip()`: checks whether an IP is publicly routable

## Planned

- Detect domains and file hashes (MD5, SHA-1, SHA-256)
- Handle defanged IOCs such as `evil[.]com`
- Query threat-intelligence sources and produce JSON reports

## Setup (Windows / PowerShell)

```
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run the tests

```
pytest
```