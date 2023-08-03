class Network:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.servers = {}
        self.secure = False

    def set_secure(self, secure):
        self.secure = secure

    def add_server(self, server):
        self.servers[server.name] = server

    def remove_server(self, name):
        del self.servers[name]
