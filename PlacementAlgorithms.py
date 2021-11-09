import abc
from GatewayPlacement import GatewayPlacement
import random


class PlacementAlgorithm(metaclass=abc.ABCMeta):
    def __init__(self, sensors_list, gateways_list):
        self._sensors = sensors_list
        self._gateways = gateways_list

    @abc.abstractmethod
    def generate_gateway_placement(self):
        pass

class AllGatewaysPlacement(PlacementAlgorithm):
    def __init__(self, sensors_list, gateways_list):
        super().__init__(sensors_list, gateways_list)

    def generate_gateway_placement(self):
        placement = GatewayPlacement(self._sensors)
        for p in self._gateways:
            placement.add_gateway(p)

        return placement

class RandomPlacement(PlacementAlgorithm):
    def __init__(self, sensors_list, gateways_list):
        super().__init__(sensors_list, gateways_list)

    def generate_gateway_placement(self):
        placement = GatewayPlacement(self._sensors)
        while not placement.sensors_covered():
            g = random.choice(self._gateways)
            placement.add_gateway(g)

        return placement