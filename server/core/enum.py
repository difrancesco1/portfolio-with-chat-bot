from enum import Enum

class BulletPointType(str, Enum):
    BIOGRAPHY = "biography"
    EDUCATION = "education"
    EMPLOYMENT = "employment"
    EXPERIENCE = "experience"