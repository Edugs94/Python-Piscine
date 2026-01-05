"""
Docstring for ex1.alien_contact
"""

from enum import Enum
from datetime import datetime
from typing import Optional, Dict, Any

try:
    from pydantic import BaseModel, Field, ValidationError, model_validator

except ImportError:
    print("Pydantic is not installed. Install it with: 'pip install pydantic'")
    exit()

class ContactType(str, Enum):
    """
    Docstring for ContactType
    """

    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """
    Docstring for AlienContact
    """

    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def check_contact_rules(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')
        if (
            self.contact_type == ContactType.PHYSICAL
            and self.is_verified is False
        ):
            raise ValueError("Physical contact reports must be verified")
        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )
        return self


def main():
    '''
    Docstring for main
    '''
    print("Alien Contact Log Validation")
    print("======================================")

    try:
        contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 1, 1, 10, 0, 0),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=False,
        )

        print("Valid contact report:")
        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type.value}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print(f"Witnesses: {contact.witness_count}")
        print(f"Message: '{contact.message_received}'")

    except ValidationError as e:
        for error in e.errors():
            err_dict: Dict[str, Any] = error
            print(err_dict["msg"])

    print()
    print("======================================")
    print("Expected validation error:")
    try:
        contact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 1, 1, 10, 0, 0),
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=1,
            message_received="Greetings from Zeta Reticuli",
            is_verified=False,
        )

        print("Valid contact report:")
        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type.value}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print(f"Witnesses: {contact.witness_count}")
        print(f"Message: '{contact.message_received}'")

    except ValidationError as e:
        for error in e.errors():
            err_dict: Dict[str, Any] = error
            print(err_dict["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
