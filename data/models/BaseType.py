from dataclasses import dataclass
from models.TypeRelationships import Relationships


@dataclass
class BaseType:
    _id: str
    _name: str
    _attacking: Relationships
    _defending: Relationships
    _has_immunities: bool
