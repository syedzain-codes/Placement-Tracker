from pydantic import BaseModel, field_validator
from datetime import date


class Problem(BaseModel):

    name: str
    topic: str
    difficulty: str

    @field_validator("difficulty")
    @classmethod
    def validate_difficulty(cls, value):

        value = value.strip().capitalize()

        allowed = [
            "Easy",
            "Medium",
            "Hard"
        ]

        if value not in allowed:
            raise ValueError(
                "Difficulty must be Easy, Medium or Hard"
            )

        return value


class UpdateProblem(BaseModel):

    topic: str
    difficulty: str

    @field_validator("difficulty")
    @classmethod
    def validate_difficulty(cls, value):

        value = value.strip().capitalize()

        allowed = [
            "Easy",
            "Medium",
            "Hard"
        ]

        if value not in allowed:
            raise ValueError(
                "Difficulty must be Easy, Medium or Hard"
            )

        return value


class ProblemResponse(BaseModel):
    id: int
    name: str
    topic: str
    difficulty: str
    solved_date: date