# Postmortem

## Issue Summary:

- **Duration:** April 10, 2024, 9:00 AM to April 10, 2024, 1:00 PM (UTC)
- **Impact:** The authentication service for our mobile app experienced an outage, leading to users being unable to log in. Approximately 60% of users were affected by the service disruption.

## Timeline:

- **9:00 AM:** Issue detected through a surge in error logs from the authentication service.
  - **Actions taken:** Initial investigation focused on database connectivity and server health.
  - **Misleading investigation paths:** Assumed database overload or server misconfiguration as potential causes.
- **10:00 AM:** Incident escalated to the backend engineering team.
- **11:00 AM:** Root cause identified as a misconfigured firewall blocking authentication requests.
  - **Actions taken:** Firewall rules updated to allow proper authentication traffic.
- **12:00 PM:** Authentication service restored, users regained access.
- **1:00 PM:** Incident officially resolved.

## Root Cause and Resolution

### Root Cause:
- The authentication service outage stemmed from a misconfigured firewall blocking incoming authentication requests, preventing users from logging in.

### Resolution:
- The issue was resolved by updating the firewall rules to allow authentication traffic to reach the authentication service, restoring normal functionality.

## Corrective and Preventative Measures:

- Strengthen monitoring: Enhance monitoring to detect firewall misconfigurations promptly.
- Regular firewall audits: Implement regular audits of firewall configurations to prevent similar misconfigurations in the future.
- Automated firewall testing: Utilize automated tools to validate firewall rules and ensure they align with service requirements.
- Incident response training: Conduct training sessions to improve incident response capabilities and ensure swift resolution of future issues.

## Tasks to Address the Issue:

1. Update firewall rules: Ensure proper configuration to allow authentication traffic.
2. Enhance monitoring: Set up alerts to detect firewall-related issues.
3. Conduct firewall audit: Review existing firewall configurations for correctness and effectiveness.
4. Schedule incident response training: Organize sessions to educate team members on effective troubleshooting and escalation procedures.
