def achievement_hunter(set1, set2, set3):
    unique_achievements = set1.union(
        set2.union(set3))
    print(f'All unique achievements: {unique_achievements}')
    print(f'Total unique achievements: {len(unique_achievements)}')
    print()
    common = set1.intersection(
        set2.intersection(set3))
    print(f'Common to all players: {common}')
    rare_set1 = set1.difference(
        set2.union(set3))
    rare_set2 = set2.difference(
        set1.union(set3))
    rare_set3 = set3.difference(
        set2.union(set1))
    rare = rare_set1.union(
        rare_set2.union(rare_set3))
    print(f'Rare achievements (1 player): {rare}')
    print()
    print(f"Alice vs Bob common: {set1.intersection(set2)}")
    print(f"Alice unique: {set1.difference(set2)}")
    print(f"Bob unique: {set2.difference(set1)}")


def main():
    alice_achievements = {'first_kill', 'level_10', 'treasure_hunter',
                          'speed_demon'}
    bob_achievements = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie_achievements = {'level_10', 'treasure_hunter', 'boss_slayer',
                            'speed_demon', 'perfectionist'}
    print('=== Achievement Tracker System ===')
    print()
    print(f'Player alice achievements: {alice_achievements}')
    print(f'Player bob achievements: {bob_achievements}')
    print(f'Player charlie achievements: {charlie_achievements}')
    print()
    achievement_hunter(
        alice_achievements, bob_achievements, charlie_achievements)


if __name__ == "__main__":
    main()
