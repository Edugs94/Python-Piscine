"""
Docstring for ex0.space_station
"""

from datetime import datetime
from typing import Optional

try:
    from pydantic import BaseModel, Field, ValidationError

except ImportError:
    print("Pydantic is not installed. Install it with: 'pip install pydantic'")
    exit()


class SpaceStation(BaseModel):
    """
    Pydantic model for Space Station validation.
    """

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main():
    '''
    Docstring for main
    '''
    print("Space Station Data Validation")
    print("========================================")

    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=15,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2026, 1, 2, 2, 0, 0),
            is_operational=True,
        )
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        status = "Operational" if station.is_operational else "Non-Operational"
        print(f"Status: {status}")

    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])

    print()
    print("========================================")
    print("Expected validation error:")

    try:
        _ = SpaceStation(
            station_id="ISS002",
            name="Overcrowded Station",
            crew_size=25,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
