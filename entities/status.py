from enum import Enum

class Status(Enum):
    VALID = 200, 'Valid'
    BANNED = 404, 'Banned'

    def __new__(cls, code, description):
        obj = object.__new__(cls)
        obj._value_ = code
        obj.description = description
        return obj

    @classmethod
    def from_code(cls, code):
        for member in cls:
            if member.value == code:
                return member
        raise ValueError(f"No matching Status for code: {code}")