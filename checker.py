import logging, yaml
from ldap3 import Server, Connection, ALL
from slackclient import SlackClient 

with open("config.yml", 'r') as ymlfile:
    cfg= yaml.load(ymlfile)

if cfg['slack']['enabled'] == True:
    channel = cfg['slack']['channel']
    token = cfg['slack']['key']

logging.basicConfig(filename='mylog.log',level=logging.DEBUG)
server = Server(cfg['ldap']['host'], connect_timeout=cfg['ldap']['timeout'])
conn = Connection(server)


def notify(message,channel,token):

    sc = SlackClient(token)

    sc.api_call(
            "chat.postMessage",
            channel=channel,
            text=message
    )


try:
    a = conn.bind()
    if a == True:
        logging.info('successful connection')
except Exception as e:
    logging.error(e)
    if cfg['slack']['enabled'] == True:
        message = "Unable ro connect to " + cfg['ldap']['host']+ ": " + str(e)
        notify(message,channel,token)


