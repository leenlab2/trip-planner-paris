"""This module contains the data structures we will use to store and use information about
points of interest. This includes the Location class, as well as all its subclasses.

This file is Copyright (c) 2021 Leen Al Lababidi, Michael Rubenstein, Maria Becerra and Nada Eldin
"""
from __future__ import annotations
from dataclasses import dataclass
import datetime


@dataclass
class Location:
    """A point of interest. This could be a landmark, restaurant, subway station, etc.

    Instance Attributes:
        - name: the name of the location
        - location: the geographical location in (latitude, longitude)

    Representation Invariants:
        - -90 <= self.location[0] <= 90
        - -180 <= self.location[1] <= 180
    """
    name: str
    location: tuple[float, float]


@dataclass
class Landmark(Location):
    """A historical landmark or popular form of entertainment in the city.

    Instance Attributes:
        - opening_times: a dictionary mapping from a day of the week to the range of time it is open
            for on that day. It only includes days the location is open on.
        - rating: the average rating given to this location by reviewers
        - time_spent: the average time spent at this location

    Representation Invariants:
        - all(day in {'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',\
            'Saturday'} for day in self.opening_times)
        - 0 <= self.rating <= 5
        - datetime.timedelta(0) <= self.time_spent <= datetime.timedelta(hours=24)
    """
    opening_times: dict[str, tuple[datetime.time, datetime.time]]
    rating: float
    time_spent: datetime.timedelta = datetime.timedelta(hours=2)


@dataclass
class Restaurant(Location):
    """A restaurant in the city

    Instance Attributes:
        - opening_times: a dictionary mapping from a day of the week to the range of time it is open
            for on that day. It only includes days the location is open on.
        - rating: the average rating given to this location by reviewers
        - time_spent: the average time spent at this location

    Representation Invariants:
        - all(day in {'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',\
            'Saturday'} for day in self.opening_times)
        - 0 <= self.rating <= 5
        - datetime.timedelta(0) <= self.time_spent <= datetime.timedelta(hours=24)
    """
    opening_times: dict[str, tuple[datetime.time, datetime.time]]
    rating: float
    time_spent: datetime.timedelta = datetime.timedelta(hours=1)


@dataclass
class Hotel(Location):
    """A hotel in the city

    Instance Attributes:
        - staying: whether the user is staying at this hotel
    """
    staying: bool = False


@dataclass
class SubwayStation(Location):
    """A subway station in the city

    Instance Attributes:
        - time_spent: the average time spent at this location

    Representation Invariants:
        - datetime.timedelta(0) <= self.time_spent <= datetime.timedelta(hours=24)
    """
    time_spent: datetime.timedelta = datetime.timedelta(minutes=5)


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['dataclasses', 'datetime'],
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 100,
        'disable': ['E1136']
    })

    import python_ta.contracts
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
