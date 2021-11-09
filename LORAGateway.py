import NetworkNode


class LORAGateway(NetworkNode.NetworkNode):

    def __init__(self, id, latitude, longitude, altitude, threshold):
        self._id = id
        self._threshold = threshold
        self._base_power = 20.0
        super().__init__(latitude, longitude, altitude)

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_threshold(self):
        return self._threshold

    def set_threshold(self, threshold):
        self._threshold = threshold

    def get_energy_consumption(self, time):
        return self._base_power * (self._threshold / 500.0) * time

    # returns a list of sensors in sensor_list which are covered by current gateway
    def get_coverage(self, sensor_list):
        C = []
        for s in sensor_list:
            if self.distance(s) <= self.get_threshold():
                C.append(s)

        return C
