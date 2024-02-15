# Create XDR Incidents from apache log

This use case is about creating Incidents and attached sigthings within XDR from apache web server logs analysis

When you expose a Web server on the INTERNET this one is rapidly discovered ( in 4 hours max ) and then we start to see Web Attacks attempts.

A lot of these attacks are clearly visible in the apache logs.

The rationnal for this use case is to analyse any apache logs and automatically create Incidents within SecureX for every discovered attack. 

- Create Incident within XDR
- Send Alerts to the Security Operators
- And then populate XDR blocking Feeds with ip addresses of Hackers.

After that, every company firewall block these bad guys

# The Use Cases.

2 use case were builted upon this idea

They were published here :

- [Create an XDR incident from Attack Detection into apache log](https://github.com/pcardotatgit/XDR_demo_-_create_incident_from_apache_log_threat_analysis)

- [Create an XDR incident from real time Attack Detection on XAMPP Apache Web Server](Create an XDR incident from real time Attack Detection on XAMPP Apache Web Server)