from geopy.distance import great_circle


class NetworkNode:
    def __init__(self, latitude, longitude, elevation):
        self._latitude = latitude
        self._longitude = longitude
        self._elevation = elevation

    def get_latitude(self):
        return self._latitude

    def get_longitude(self):
        return self._longitude

    def get_elevation(self):
        return self._elevation

    def set_latitude(self, latitude):
        self._latitude = latitude

    def set_longitude(self, longitude):
        self._longitude = longitude

    def set_elevation(self, altitude):
        self._altitude = altitude

    def get_coordinates(self):
        return (self._latitude, self._longitude)

    def distance(self, node):
        return great_circle(self.get_coordinates(), node.get_coordinates()).meters



