# About 
This is a simple Python script to check the functionality of an LDAP server. It attempts to establish a valid connection within a given amount of time. Success and failures are logged. 

Ideally, this could be the base of a more complex LDAP health monitor.

## Installation 
1. Clone this repository 
2. Run `pip install -r requirements.txt`
3. create a `config.yml` based on `config.yml.example`

If you wish to use Slack integration, follow their instructions about creating a bot user. You will put the `Key` and `channel` in the conifg file. If you do not wish to use Slack, simply set the `enabled` value to `False`. 


