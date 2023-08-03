from organization import Organization
from building import Building
from room import Room
from peripheral import Peripheral
from network import Network
from server import Server
from service import Service
from items import peripherals, servers, services, long_wordlist
from random import Random

def generate_word_name(N, rng):
    # Sample N words from the wordlist
    sampled_words = rng.sample(long_wordlist, N)

    # Join the sampled words with dashes between them
    word_name = "-".join(sampled_words)

    return word_name


def generate_organization(num_buildings, num_rooms, peripherals_list, servers_list, services_list, seed):
    rng = Random(seed)
    """Generate a unique organization with the given number of buildings and rooms."""
    # Create an organization
    org = Organization()

    for _ in range(num_buildings):
        # Generate a unique ID for the building
        building_id = generate_word_name(N=4, rng=rng)

        # Add a building to the organization
        building = Building(building_id)
        org.add_building(building)

        for _ in range(num_rooms):
            # Generate a unique ID for the room
            room_id = generate_word_name(N=4, rng=rng)

            # Add a room to the building
            room = Room(room_id)
            building.add_room(room)

            # Add a random number of peripherals to the room
            num_peripherals = rng.randint(1, len(peripherals_list) // 4)
            for _ in range(num_peripherals):
                peripheral_name, peripheral_cost = rng.choice(peripherals_list)
                peripheral = Peripheral(peripheral_name, peripheral_cost)
                room.add_peripheral(peripheral)

        # Add a random number of networks to the organization
        num_networks = rng.randint(1, 3)
        for _ in range(num_networks):
            network_id = generate_word_name(N=4, rng=rng)
            network = Network(network_id, f'Network-{network_id}')
            network.set_secure(rng.choice([True, False]))
            org.add_network(network)

            # Add a random number of servers to the network
            num_servers = rng.randint(1, 4)
            for _ in range(num_servers):
                server_name, server_version = rng.choice(servers_list)
                server = Server(server_name, server_version)
                network.add_server(server)

                # Add a random number of services to the server
                num_services = rng.randint(5, 10)
                for _ in range(num_services):
                    service_name, service_version = rng.choice(services_list)
                    service = Service(service_name, service_version)
                    server.add_service(service)

    return org