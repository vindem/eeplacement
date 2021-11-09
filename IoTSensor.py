import NetworkNode



class IoTSensor(NetworkNode.NetworkNode):
    def __init__(self, id, latitude, longitude, altitude, base_power, comm_power):
        self._id = id
        super().__init__(latitude, longitude, altitude)
        self._base_power = base_power
        self._comm_power = comm_power

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id
        
    def set_base_power(self, base_power):
        self._base_power = base_power

    def get_base_power(self):
        assert isinstance(self._base_power, float)
        return self._base_power

    def set_comm_power(self, comm_power):
        self._comm_power = comm_power

    def get_comm_power(self):
        assert isinstance(self._comm_power, float)
        return self._comm_power


    def get_closest_gateway(self, gateway_placement):
        min = float("inf")
        closest_gateway = None
        for g in gateway_placement:
            if super().distance(g) < min:
                closest_gateway = g
                min = super().distance(g)

        return closest_gateway

    def communication_energy(self, time, gateway):
        return ((self._comm_power - self._base_power) * (self.distance(gateway)/100.0)) * time

    def idle_energy(self, time):
        return self._base_power * time

    def get_total_consumption(self, time, closest_gateway):
        energy = self.idle_energy(time) + self.communication_energy(time, closest_gateway)
        return energy
