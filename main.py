from getDualTypeFromUser import get_dual_type_from_user
from getIdealCoreMatches import get_ideal_core_matches
from getWeaknesses import get_weaknesses
from loadTypesFromDb import load_types_from_db


def main():
    base_types, dual_types = load_types_from_db()

    highest_synergies = []

    for key in dual_types:
        # key = get_dual_type_from_user().lower()

        member = dual_types[key]

        weaknesses = get_weaknesses(member)

        matches = get_ideal_core_matches(weaknesses, dual_types)

        possible_core_matches = {}

        for match in matches:
            mate = dual_types[match]

            mate_weaknesses = get_weaknesses(mate)

            mate_matches = get_ideal_core_matches(mate_weaknesses, dual_types)

            if key in mate_matches:
                possible_core_matches[match] = mate_matches[key]

        core_matches = {}

        for match in matches:
            if match in possible_core_matches:
                core_matches[match] = matches[match] + possible_core_matches[match]

        core_matches_list = list(reversed(sorted(core_matches.items(), key=lambda x: x[1])))

        # core_matches = list(reversed(sorted(possible_core_matches.items(), key=lambda x: x[1])))
        # my_matches = list(reversed(sorted(matches.items(), key=lambda x: x[1])))

        highest_synergies.append((key, core_matches_list[0][0], core_matches_list[0][1]))

    highest_synergies = list(reversed(sorted(highest_synergies, key=lambda x: x[2])))
    pass


if __name__ == '__main__':
    main()
