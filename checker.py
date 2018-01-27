import logging, yaml
from ldap3 import Server, Connection, ALL
from slackclient import SlackClient 

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

if cfg['slack']['enabled'] == True:
    channel = cfg['slack']['channel']
    token = cfg['slack']['key']

logging.basicConfig(filename='mylog.log',level=logging.DEBUG)
servers = cfg['ldap']['host']
timeout = connect_timeout=cfg['ldap']['timeout']

def notify(message,channel,token):

    sc = SlackClient(token)

    sc.api_call(
            "chat.postMessage",
            channel=channel,
            text=message
    )



def check(server, timeout):
    
    server = Server(server, connect_timeout=timeout)
    conn = Connection(server)
    
    try:
        a = conn.bind()
        if a == True:
            logging.info('successful connection to %s' % server)
    except Exception as e:
        logging.error(e)
        if cfg['slack']['enabled'] == True:
            message = "Unable ro connect to %s : " % server + str(e) 
            notify(message,channel,token)



for server in servers:
    
    check(server, timeout)
