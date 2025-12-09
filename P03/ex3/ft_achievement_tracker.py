def format_output(data):
    '''Helper to print "None" if set is empty, otherwise print the set'''
    if not data:
        return "None"
    return data


def achievement_hunter(set1, set2, set3):
    '''Gets and displays all the information
    required regaring players achivements'''

    unique_achievements = set1.union(
        set2.union(set3))
    print(f'All unique achievements: {format_output(unique_achievements)}')
    print(f'Total unique achievements: {len(unique_achievements)}')
    print()
    common = set1.intersection(
        set2.intersection(set3))
    print(f'Common to all players: {format_output(common)}')
    rare_set1 = set1.difference(
        set2.union(set3))
    rare_set2 = set2.difference(
        set1.union(set3))
    rare_set3 = set3.difference(
        set2.union(set1))
    rare = rare_set1.union(
        rare_set2.union(rare_set3))
    print(f'Rare achievements (1 player): {format_output(rare)}')
    print()
    print(f"Alice vs Bob common: {format_output(set1.intersection(set2))}")
    print(f"Alice unique: {format_output(set1.difference(set2))}")
    print(f"Bob unique: {format_output(set2.difference(set1))}")


def process_achievements(set1, set2, set3):
    '''Displays all info about players achievements requested'''

    print('=== Achievement Tracker System ===')
    print()
    print(f'Player alice achievements: {set1}')
    print(f'Player bob achievements: {set2}')
    print(f'Player charlie achievements: {set3}')
    print()
    achievement_hunter(set1, set2, set3)


def main():
    '''Main worklow of the program. Establishes achievements and
    calls function achievement hunter'''

    alice_data = ['first_blood', 'pixel_perfect', 'speed_runner',
                  'first_blood', 'first_blood']
    bob_data = ['level_master', 'boss_hunter', 'treasure_seeker',
                'level_master', 'level_master']
    charlie_data = ['treasure_seeker', 'boss_hunter', 'combo_king',
                    'first_blood', 'boss_hunter', 'first_blood',
                    'boss_hunter', 'first_blood']
    diana_data = ['first_blood', 'combo_king', 'level_master',
                  'treasure_seeker', 'speed_runner', 'combo_king',
                  'combo_king', 'level_master']
    eve_data = ['level_master', 'treasure_seeker', 'first_blood',
                'treasure_seeker', 'first_blood', 'treasure_seeker']
    frank_data = ['explorer', 'boss_hunter', 'first_blood', 'explorer',
                  'first_blood', 'boss_hunter']

    alice_achievements = set(alice_data) # noqa
    bob_achievements = set(bob_data) # noqa
    charlie_achievements = set(charlie_data) # noqa
    diana_achievements = set(diana_data) # noqa
    eve_achievements = set(eve_data) # noqa
    frank_achievements = set(frank_data) # noqa

    process_achievements(alice_achievements, bob_achievements,
                         charlie_achievements)


if __name__ == "__main__":
    main()
