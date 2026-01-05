# Scenario 02 – SSH Activity Review (No New Events Observed)

## Objective
The objective of this scenario was to monitor SSH-related activity and identify any new authentication failures, brute force attempts, or suspicious login behavior using Wazuh SIEM.

This scenario focuses on validating current activity, not historical events.

---

## Environment
- **SIEM:** Wazuh 4.14.0 OVA  
- **Node analyzed:** Wazuh Manager  
- **Monitored service:** SSH (`sshd`)  
- **Time range analyzed:** Last 24 hours  

---

## Detection Approach
The following steps were performed during the analysis:

- Review of SSH-related events in **Threat Hunting → Events**
- Keyword-based filtering using `ssh`
- Review of authentication-related alerts (PAM / SSH rules)
- Validation of event timestamps to differentiate historical vs current activity

---

## Findings
During the selected time window:

- No **new** SSH authentication events were generated
- No new authentication failures were observed
- No brute force or suspicious SSH patterns were detected

SSH-related alerts visible in the SIEM correspond to **previous activity generated during Scenario 01** and fall outside the scope of this scenario.

No additional events were recorded during the analysis period.

---

## Conclusion
This scenario resulted in **no new SSH-related security activity** being detected during the analyzed time range.

The absence of alerts indicates that:
- No authentication attempts occurred during this period
- The monitoring pipeline was operational
- Historical alerts were correctly retained and distinguishable from current activity

---

## Status
**Scenario completed – No new activity observed**

