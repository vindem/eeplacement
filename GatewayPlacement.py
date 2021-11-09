import IoTSensor
import LORAGateway


class GatewayPlacement:
    def __init__(self, sensor_list):
        self._sensor_list = sensor_list
        self._gateway_list = []

    def add_gateway(self, gateway):
        self._gateway_list.append(gateway)

    def remove_gateway(self, gateway):
        self._gateway_list.remove(gateway)

    def sensors_covered(self):
        curr_placement_coverage = []
        for g in self._gateway_list:
            curr_gateway_coverage = g.get_coverage(self._sensor_list)
            for s in curr_gateway_coverage:
                if not s.get_id() in curr_placement_coverage:
                    curr_placement_coverage.append(s.get_id())

        covers = True
        for s in self._sensor_list:
            if not s.get_id() in curr_placement_coverage:
                covers = False
                break

        return covers

    def energy_consumption(self, time):
        energy = 0.0
        for s in self._sensor_list:
            energy = energy + s.get_total_consumption(time, s.get_closest_gateway(self._gateway_list))

        for g in self._gateway_list:
            energy = energy + g.get_energy_consumption(time)

        return energy

    def get_gateways_number(self):
        return len(self._gateway_list)
