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
    def __get(url):
        with request.urlopen(url) as req:
            return req.read().decode('utf-8')

    @staticmethod
    def get_people_in_space():
        data = OpenNotify.__get(URLS['ASTROS'])
        data = json.loads(data)
        return data

    @staticmethod
    def get_ISS_location():
        data = OpenNotify.__get(URLS['ISS_NOW'])
        data = json.loads(data)
        return data

    @staticmethod
    async def get_people_in_space_async():
        return OpenNotify.get_people_in_space()

    @staticmethod
    async def get_ISS_location_async():
        return OpenNotify.get_ISS_location_async()


