"""
Docstring for ex2.space_crew
"""

from datetime import datetime
from enum import Enum

try:
    from pydantic import BaseModel, Field, ValidationError, model_validator

except ImportError:
    print("Pydantic is not installed. Install it with: 'pip install pydantic'")
    exit()


class Rank(str, Enum):
    """
    Docstring for Rank
    """

    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """
    Docstring for CrewMember
    """

    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_crew_needs(self):
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')
        leadership = any(
            member.rank in (Rank.COMMANDER, Rank.CAPTAIN)
            for member in self.crew
        )
        if leadership is False:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )
        if self.duration_days > 365:
            experienced = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced += 1

            if experienced < len(self.crew) / 2:
                raise ValueError(
                    "Crew must be more experienced for +1 years expeditions"
                )

        if any(member.is_active is False for member in self.crew):
            raise ValueError("One or more crewmates are not active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2026, 2, 1),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="kner",
                    name="Sarah Connor",
                    rank=Rank.COMMANDER,
                    age=27,
                    specialization="Mission Command",
                    years_experience=6,
                    is_active=True,
                ),
                CrewMember(
                    member_id="24ggrtg",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=43,
                    specialization="Navigation",
                    years_experience=18,
                    is_active=True,
                ),
                CrewMember(
                    member_id="46yyhr",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=31,
                    specialization="Engineering",
                    years_experience=8,
                    is_active=True,
                ),
            ],
            budget_millions=2500.0,
        )
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            print(
                f"- {member.name} ({member.rank.value})"
                f" - {member.specialization}"
            )
    except ValidationError as e:
        for error in e.errors():
            if error["type"] == "value_error":
                print(error["msg"][13:])
            else:
                loc = ".".join(str(item) for item in error["loc"])
                print(f"{loc}: {error['msg']}")

    print("\n=========================================")
    print("Expected validation error:")
    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2026, 2, 1),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="wrfwfw",
                    name="Sarah Connor",
                    rank=Rank.LIEUTENANT,
                    age=27,
                    specialization="Mission Command",
                    years_experience=6,
                    is_active=True,
                ),
                CrewMember(
                    member_id="efeeea",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=43,
                    specialization="Navigation",
                    years_experience=18,
                    is_active=True,
                ),
                CrewMember(
                    member_id="efde",
                    name="Alice Johnson",
                    rank=Rank.LIEUTENANT,
                    age=31,
                    specialization="Engineering",
                    years_experience=8,
                    is_active=True,
                ),
            ],
            budget_millions=2500.0,
        )
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            print(
                f"- {member.name} ({member.rank.value})"
                f" - {member.specialization}"
            )
    except ValidationError as e:
        for error in e.errors():
            if error["type"] == "value_error":
                print(error["msg"][13:])
            else:
                loc = ".".join(str(item) for item in error["loc"])
                print(f"{loc}: {error['msg']}")


if __name__ == "__main__":
    main()
