import json
from typing import List
from urllib import request
from types import MappingProxyType
from datetime import datetime
from dataclasses import dataclass

URLS = MappingProxyType(
    {
        "ASTROS": "http://api.open-notify.org/astros.json",
        "ISS_NOW": "http://api.open-notify.org/iss-now.json",
    }
)


@dataclass
class Location:
    latitude: float
    longitude: float


@dataclass
class ISSLocation:
    message: str
    date_time: datetime
    utc_date_time: datetime
    location: Location


@dataclass
class People:
    name: str
    craft: str


@dataclass
class PeopleInSpace:
    number: int
    message: str
    people: List[People]


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
    def get_ISS_location() -> ISSLocation:
        data = OpenNotify.__get(URLS['ISS_NOW'])
        data = json.loads(data)
        unix = data['timestamp']

        message = data['message']
        date_time = datetime.fromtimestamp(unix)
        utc_date_time = datetime.utcfromtimestamp(unix)
        latitude = data['iss_position']['latitude']
        longitude = data['iss_position']['longitude']
        location = Location(latitude=latitude, longitude=longitude)
        del data
        return ISSLocation(
            location=location, message=message,
            date_time=date_time, utc_date_time=utc_date_time
        )

    @staticmethod
    async def get_people_in_space_async():
        return OpenNotify.get_people_in_space()

    @staticmethod
    async def get_ISS_location_async():
        return OpenNotify.get_ISS_location_async()


