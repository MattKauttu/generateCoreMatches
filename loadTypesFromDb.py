import pymongo

from models.BaseType import BaseType
from models.DualType import DualType
from models.TypeRelationships import Relationships


def load_types_from_db():
    client = pymongo.MongoClient("mongodb://localhost:27017")

    # Database Name
    db = client["pkmn_analytics"]

    base_types = load_base_types_from_db(db)
    dual_types = load_dual_types_from_db(db)

    return base_types, dual_types


def load_base_types_from_db(db):
    # Collection Name
    coll = db["base_types"]

    x = coll.find()

    base_types = {}

    for data in x:
        identifier = data["_id"]
        name = data["name"]
        attacking = Relationships(normal=data['attacking']['normal'],
                                  fire=data['attacking']['fire'],
                                  water=data['attacking']['water'],
                                  electric=data['attacking']['electric'],
                                  grass=data['attacking']['grass'],
                                  ice=data['attacking']['ice'],
                                  fighting=data['attacking']['fighting'],
                                  poison=data['attacking']['poison'],
                                  ground=data['attacking']['ground'],
                                  flying=data['attacking']['flying'],
                                  psychic=data['attacking']['psychic'],
                                  bug=data['attacking']['bug'],
                                  rock=data['attacking']['rock'],
                                  ghost=data['attacking']['ghost'],
                                  dragon=data['attacking']['dragon'],
                                  dark=data['attacking']['dark'],
                                  steel=data['attacking']['steel'],
                                  fairy=data['attacking']['fairy'])
        defending = Relationships(normal=data['defending']['normal'],
                                  fire=data['defending']['fire'],
                                  water=data['defending']['water'],
                                  electric=data['defending']['electric'],
                                  grass=data['defending']['grass'],
                                  ice=data['defending']['ice'],
                                  fighting=data['defending']['fighting'],
                                  poison=data['defending']['poison'],
                                  ground=data['defending']['ground'],
                                  flying=data['defending']['flying'],
                                  psychic=data['defending']['psychic'],
                                  bug=data['defending']['bug'],
                                  rock=data['defending']['rock'],
                                  ghost=data['defending']['ghost'],
                                  dragon=data['defending']['dragon'],
                                  dark=data['defending']['dark'],
                                  steel=data['defending']['steel'],
                                  fairy=data['defending']['fairy'])
        has_immunities = data["hasImmunities"]

        base_type = BaseType(_id=identifier,
                             _name=name,
                             _attacking=attacking,
                             _defending=defending,
                             _has_immunities=has_immunities)

        base_types[name] = base_type

    return base_types


def load_dual_types_from_db(db):
    # Collection Name
    coll = db["dual_types"]

    x = coll.find()

    dual_types = {}

    for data in x:
        identifier = data["_id"]
        type1name = data['_type1name']
        type2name = data['_type2name']
        defenses = Relationships(normal=data['_defenses']['normal'],
                                 fire=data['_defenses']['fire'],
                                 water=data['_defenses']['water'],
                                 electric=data['_defenses']['electric'],
                                 grass=data['_defenses']['grass'],
                                 ice=data['_defenses']['ice'],
                                 fighting=data['_defenses']['fighting'],
                                 poison=data['_defenses']['poison'],
                                 ground=data['_defenses']['ground'],
                                 flying=data['_defenses']['flying'],
                                 psychic=data['_defenses']['psychic'],
                                 bug=data['_defenses']['bug'],
                                 rock=data['_defenses']['rock'],
                                 ghost=data['_defenses']['ghost'],
                                 dragon=data['_defenses']['dragon'],
                                 dark=data['_defenses']['dark'],
                                 steel=data['_defenses']['steel'],
                                 fairy=data['_defenses']['fairy'])

        dual_type = DualType(_id=identifier,
                             _type1name=type1name,
                             _coverage=None,
                             _defenses=defenses,
                             _type2name=type2name)

        dual_types[type1name + "_" + type2name] = dual_type

    return dual_types
