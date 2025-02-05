from config_reader import read_config

config = read_config('./config.ini')

db_host = config['database']['host']
db_port = config['database']['port']
db_user = config['database']['user']
db_password = config['database']['password']

server_host = config['server']['host']
server_port = config['server']['port']

print(f"Database Host: {db_host}")
print(f"Database Port: {db_port}")
print(f"Database User: {db_user}")
print(f"Database Password: {db_password}")

print(f"Server Host: {server_host}")
print(f"Server Port: {server_port}")
