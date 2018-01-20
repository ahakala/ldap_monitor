import logging, yaml
from ldap3 import Server, Connection, ALL

with open("config.yml", 'r') as ymlfile:
    cfg= yaml.load(ymlfile)

logging.basicConfig(filename='mylog.log',level=logging.DEBUG)
server = Server(cfg['ldap']['host'], connect_timeout=cfg['ldap']['timeout'])
conn = Connection(server)
try:
    a = conn.bind()
    if a == True:
        logging.info('successful connection')
except Exception as e:
    logging.error(e)

#print(conn)
