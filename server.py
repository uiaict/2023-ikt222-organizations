class Server:
    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.services = {}

    def add_service(self, service):
        self.services[service.name] = service

    def remove_service(self, name):
        del self.services[name]
