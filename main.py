from IoTSensor import IoTSensor
from LORAGateway import LORAGateway
from PlacementAlgorithms import AllGatewaysPlacement
from PlacementAlgorithms import RandomPlacement


def degrees_to_decimal(in_string):
    degrees = in_string[:in_string.index("°")]
    minutes = in_string[in_string.index("°")+1:in_string.index("'")]
    seconds = in_string[in_string.index("'")+1:in_string.index("\"")]
    return float(degrees) + float(minutes)/60.0 + float(seconds)/3600.0


def parse_sensor(in_string):
    splitted = in_string.split("\t")
    id = splitted[0]
    latitude = degrees_to_decimal(splitted[1])
    longitude = degrees_to_decimal(splitted[2])
    altitude = float(splitted[3])
    return IoTSensor(id, latitude, longitude, altitude, 10.0, 13.0)

def parse_gateway(id, in_string):
    splitted = in_string.split(",")
    threshold = float(splitted[0])
    latitude = float(splitted[3])
    longitude = float(splitted[4])
    altitude = float(splitted[5])
    return LORAGateway(id, latitude, longitude, altitude, threshold)

def read_sensors(in_file):
    sensor_list = []
    file = open(in_file, 'r')
    lines = file.readlines()
    for line in lines[1:]:
        sensor_list.append(parse_sensor(line))

    return sensor_list

def read_gateway(in_file):
    gateway_list = []
    file = open(in_file, 'r')
    lines = file.readlines()
    id = 0
    for line in lines[1:]:
        gateway_list.append(parse_gateway("g"+str(id),line))
        id = id + 1

    return gateway_list


if __name__ == '__main__':
    S = read_sensors('datasets/sensor_locations.tsv')
    G = read_gateway('datasets/gateway_locations.csv')

    agp = AllGatewaysPlacement(S, G)
    P0 = agp.generate_gateway_placement()

    rp = RandomPlacement(S, G)
    P1 = rp.generate_gateway_placement()

    print(P0.sensors_covered())
    print(P0.get_gateways_number())
    print(P0.energy_consumption(3600))

    print(P1.sensors_covered())
    print(P1.get_gateways_number())
    print(P1.energy_consumption(3600))



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
