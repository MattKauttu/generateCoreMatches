def get_weaknesses(member):
    member_defenses = member._defenses.__dict__
    weaknesses = {}

    for key in member_defenses:
        if member_defenses[key] == 2 or member_defenses[key] == 4:
            weaknesses[key] = member_defenses[key]

    return weaknesses
