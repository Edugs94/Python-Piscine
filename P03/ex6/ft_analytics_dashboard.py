"""Exercise 6: Analytics Dashboard"""


def create_data() -> dict:
    """
    Data extracted from example given on data_generator
    """
    data = {
        "players": {
            "alice": {
                "level": 41,
                "total_score": 2824,
                "sessions_played": 13,
                "favorite_mode": "ranked",
                "achievements_count": 5,
            },
            "bob": {
                "level": 16,
                "total_score": 4657,
                "sessions_played": 27,
                "favorite_mode": "ranked",
                "achievements_count": 2,
            },
            "charlie": {
                "level": 44,
                "total_score": 9935,
                "sessions_played": 21,
                "favorite_mode": "ranked",
                "achievements_count": 7,
            },
            "diana": {
                "level": 3,
                "total_score": 1488,
                "sessions_played": 21,
                "favorite_mode": "casual",
                "achievements_count": 4,
            },
            "eve": {
                "level": 33,
                "total_score": 1434,
                "sessions_played": 81,
                "favorite_mode": "casual",
                "achievements_count": 7,
            },
            "frank": {
                "level": 15,
                "total_score": 8359,
                "sessions_played": 85,
                "favorite_mode": "competitive",
                "achievements_count": 1,
            },
        },
        "sessions": [
            {
                "player": "bob",
                "duration_minutes": 94,
                "score": 1831,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "bob",
                "duration_minutes": 32,
                "score": 1478,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "diana",
                "duration_minutes": 17,
                "score": 1570,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 98,
                "score": 1981,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "diana",
                "duration_minutes": 15,
                "score": 2361,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "eve",
                "duration_minutes": 29,
                "score": 2985,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 34,
                "score": 1285,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "alice",
                "duration_minutes": 53,
                "score": 1238,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "bob",
                "duration_minutes": 52,
                "score": 1555,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "frank",
                "duration_minutes": 92,
                "score": 2754,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 98,
                "score": 1102,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "diana",
                "duration_minutes": 39,
                "score": 2721,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 46,
                "score": 329,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "charlie",
                "duration_minutes": 56,
                "score": 1196,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 117,
                "score": 1388,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "diana",
                "duration_minutes": 118,
                "score": 2733,
                "mode": "competitive",
                "completed": True,
            },
            {
                "player": "charlie",
                "duration_minutes": 22,
                "score": 1110,
                "mode": "ranked",
                "completed": False,
            },
            {
                "player": "frank",
                "duration_minutes": 79,
                "score": 1854,
                "mode": "ranked",
                "completed": False,
            },
            {
                "player": "charlie",
                "duration_minutes": 33,
                "score": 666,
                "mode": "ranked",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 101,
                "score": 292,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 25,
                "score": 2887,
                "mode": "competitive",
                "completed": True,
            },
            {
                "player": "diana",
                "duration_minutes": 53,
                "score": 2540,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "eve",
                "duration_minutes": 115,
                "score": 147,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "frank",
                "duration_minutes": 118,
                "score": 2299,
                "mode": "competitive",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 42,
                "score": 1880,
                "mode": "casual",
                "completed": False,
            },
            {
                "player": "alice",
                "duration_minutes": 97,
                "score": 1178,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 18,
                "score": 2661,
                "mode": "competitive",
                "completed": True,
            },
            {
                "player": "bob",
                "duration_minutes": 52,
                "score": 761,
                "mode": "ranked",
                "completed": True,
            },
            {
                "player": "eve",
                "duration_minutes": 46,
                "score": 2101,
                "mode": "casual",
                "completed": True,
            },
            {
                "player": "charlie",
                "duration_minutes": 117,
                "score": 1359,
                "mode": "casual",
                "completed": True,
            },
        ],
        "game_modes": ["casual", "competitive", "ranked"],
        "achievements": [
            "first_blood",
            "level_master",
            "speed_runner",
            "treasure_seeker",
            "boss_hunter",
            "pixel_perfect",
            "combo_king",
            "explorer",
        ],
        "regions": [
            "north",
            "east",
            "central"
        ]
    }

    return data


def list_comp_ex(data: dict) -> None:
    """
    Displays info requested by exercise working with dict comprehensions
    """
    print()
    print("=== List Comprehension Examples ===")

    players_data = data.get("players")

    high_scorers: list = [
        player
        for player, details in players_data.items()
        if details["total_score"] > 2000
    ]
    scores_doubled: list = [
        details["total_score"] * 2 for player, details in players_data.items()
    ]
    active_players: list = [player for player, details in players_data.items()]

    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}")


def dict_com_ex(data: dict) -> None:
    """
    Displays info requested by exercise working with lists comprehensions
    """
    print()
    print("=== Dict Comprehension Examples ===")

    players_data = data.get("players")
    player_scores = {
        player: details["total_score"] for player, details
        in players_data.items()
    }

    scores_tuples = [
        ("low", -1, 1999),
        ("medium", 2000, 2999),
        ("high", 3000, 99999),
    ]

    score_categories = {
        cat: sum(
            1 for stats in data["players"].values()
            if min_s < stats.get('total_score') <= max_s
        )
        for cat, min_s, max_s in scores_tuples
    }

    achievements = {
        player: details["achievements_count"]
        for player, details in players_data.items()
    }

    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievements}")


def set_comp_ex(data: dict) -> None:
    """
    Displays info requested by exercise working with sets comprehensions
    """
    print()
    print('=== Set Comprehension Examples ===')

    players_data = data.get("players")

    unique_players = {player for player, details in players_data.items()}
    unique_achievements = set(data.get("achievements"))

    regions_set = set(data.get("regions"))
    print(f'Unique players: {unique_players}')
    print(f'Unique achievements: {unique_achievements}')
    print(f'Active regions: {regions_set}')


def combined_analysis(data: dict) -> None:
    """
    Displays info requested by exercise working with different comprehensions
    """
    print()
    print('=== Combined Analysis ===')

    players_data = data.get("players")
    active_players = set([player for player, details in players_data.items()])
    total_players = sum(1 for player in active_players)
    print(f'Total players: {total_players}')

    unique_achievements = set(data.get("achievements"))
    unique_achievements_count = sum(1 for achievement in unique_achievements)
    print(f'Total unique achievements: {unique_achievements_count}')

    avg_score = sum(players_data.get(player).get('total_score') for
                    player, details in players_data.items()) / total_players
    print(f'Average score: {avg_score:.1f}')

    scores_list = [(details['total_score'], name) for name,
                   details in players_data.items()]
    max_score, top_performer = max(scores_list)
    top_achievements = players_data.get(
        top_performer).get('achievements_count')
    print(f'Top performer: {top_performer} ({max_score} points,'
          f' {top_achievements} achievements)')


if __name__ == "__main__":
    """
    Main workflow of the program
    """
    data = create_data()
    list_comp_ex(data)
    dict_com_ex(data)
    set_comp_ex(data)
    combined_analysis(data)
