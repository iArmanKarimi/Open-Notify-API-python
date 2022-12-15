import json
from urllib import request
from types import MappingProxyType

URLS = MappingProxyType(
    {
        "ASTROS": "http://api.open-notify.org/astros.json",
        "ISS_NOW": "http://api.open-notify.org/iss-now.json",
    }
)


class OpenNotify:
    @staticmethod
    def get_people_in_space():
        pass

    @staticmethod
    def get_ISS_location():
        pass

    @staticmethod
    async def get_people_in_space_async():
        pass

    @staticmethod
    async def get_ISS_location_async():
        pass

