import json

class Organization:
    def __init__(self):
        self.buildings = {}
        self.networks = {}

    def add_building(self, building):
        self.buildings[building.name] = building

    def remove_building(self, name):
        del self.buildings[name]

    def add_network(self, network):
        self.networks[network.name] = network

    def remove_network(self, name):
        del self.networks[name]

    def generate_report_json(self):
        org_dict = {
            "Organization Report": {
                "Buildings": [
                    {
                        "name": building.name,
                        "Rooms": [
                            {
                                "name": room.name,
                                "Peripherals": [
                                    {
                                        "name": peripheral.name,
                                        "value": peripheral.value
                                    }
                                    for peripheral in room.peripherals.values()
                                ]
                            }
                            for room in building.rooms.values()
                        ]
                    }
                    for building in self.buildings.values()
                ],
                "Networks": [
                    {
                        "name": network.name,
                        "secure": network.secure,
                        "Servers": [
                            {
                                "name": server.name,
                                "version": server.version,
                                "Services": [
                                    {
                                        "name": service.name,
                                        "version": service.version
                                    }
                                    for service in server.services.values()
                                ]
                            }
                            for server in network.servers.values()
                        ]
                    }
                    for network in self.networks.values()
                ]
            }
        }

        return org_dict

    def generate_report(self):
        report = "Organization Report:\n\n"

        # List all buildings
        report += "Buildings:\n"
        for building in self.buildings.values():
            report += f"Building: {building.name}\n"

            # List all rooms in the building
            report += "\tRooms:\n"
            for room in building.rooms.values():
                report += f"\tRoom: {room.name}\n"

                # List all peripherals in the room
                report += "\t\tPeripherals:\n"
                for peripheral in room.peripherals.values():
                    report += f"\t\t\t{peripheral.name} (Value: {peripheral.value})\n"

        # List all networks
        report += "\nNetworks:\n"
        for network in self.networks.values():
            report += f"Network: {network.name} (Secure: {network.secure})\n"

            # List all servers in the network
            report += "\tServers:\n"
            for server in network.servers.values():
                report += f"\t\tOperating System:\n\t\t\t{server.name} (Version: {server.version})\n"

                # List all services on the server
                report += "\t\tServices:\n"
                for service in server.services.values():
                    report += f"\t\t\t{service.name} (Version: {service.version})\n"

        return report