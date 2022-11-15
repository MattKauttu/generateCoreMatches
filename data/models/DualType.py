from dataclasses import dataclass
from models.TypeRelationships import Relationships


@dataclass
class DualType:
    _id: str
    _type1name: str
    _coverage: Relationships
    _defenses: Relationships
    _type2name: str = ""
