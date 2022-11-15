def get_ideal_core_matches(weaknesses, dual_types):
    matches = {}

    for weakness in weaknesses:

        multiplier = weaknesses[weakness]

        for key in dual_types:
            defensive_relationship = dual_types[key]._defenses.__dict__[weakness]

            if defensive_relationship == 0 or defensive_relationship == 0.25 or defensive_relationship == 0.5:
                if key not in matches:
                    matches[key] = 0

                match defensive_relationship:
                    case 0:
                        matches[key] += (10 * multiplier)
                    case 0.25:
                        matches[key] += (6 * multiplier)
                    case 0.5:
                        matches[key] += (2 * multiplier)

    #matches = list(reversed(sorted(matches.items(), key=lambda x:x[1])))

    return matches