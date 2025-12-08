def create_data() -> dict:

    #{'players': {'alice': {'level': 41, 'total_score': 2824, 'sessions_played': 13, 'favorite_mode': 'ranked', 'achievements_count': 5}, 'bob': {'level': 16, 'total_score': 4657, 'sessions_played': 27, 'favorite_mode': 'ranked', 'achievements_count': 2}, 'charlie': {'level': 44, 'total_score': 9935, 'sessions_played': 21, 'favorite_mode': 'ranked', 'achievements_count': 7}, 'diana': {'level': 3, 'total_score': 1488, 'sessions_played': 21, 'favorite_mode': 'casual', 'achievements_count': 4}, 'eve': {'level': 33, 'total_score': 1434, 'sessions_played': 81, 'favorite_mode': 'casual', 'achievements_count': 7}, 'frank': {'level': 15, 'total_score': 8359, 'sessions_played': 85, 'favorite_mode': 'competitive', 'achievements_count': 1}}, 'sessions': [{'player': 'bob', 'duration_minutes': 94, 'score': 1831, 'mode': 'competitive', 'completed': False}, {'player': 'bob', 'duration_minutes': 32, 'score': 1478, 'mode': 'casual', 'completed': True}, {'player': 'diana', 'duration_minutes': 17, 'score': 1570, 'mode': 'competitive', 'completed': False}, {'player': 'alice', 'duration_minutes': 98, 'score': 1981, 'mode': 'ranked', 'completed': True}, {'player': 'diana', 'duration_minutes': 15, 'score': 2361, 'mode': 'competitive', 'completed': False}, {'player': 'eve', 'duration_minutes': 29, 'score': 2985, 'mode': 'casual', 'completed': True}, {'player': 'frank', 'duration_minutes': 34, 'score': 1285, 'mode': 'casual', 'completed': True}, {'player': 'alice', 'duration_minutes': 53, 'score': 1238, 'mode': 'competitive', 'completed': False}, {'player': 'bob', 'duration_minutes': 52, 'score': 1555, 'mode': 'casual', 'completed': False}, {'player': 'frank', 'duration_minutes': 92, 'score': 2754, 'mode': 'casual', 'completed': True}, {'player': 'eve', 'duration_minutes': 98, 'score': 1102, 'mode': 'casual', 'completed': False}, {'player': 'diana', 'duration_minutes': 39, 'score': 2721, 'mode': 'ranked', 'completed': True}, {'player': 'frank', 'duration_minutes': 46, 'score': 329, 'mode': 'casual', 'completed': True}, {'player': 'charlie', 'duration_minutes': 56, 'score': 1196, 'mode': 'casual', 'completed': True}, {'player': 'eve', 'duration_minutes': 117, 'score': 1388, 'mode': 'casual', 'completed': False}, {'player': 'diana', 'duration_minutes': 118, 'score': 2733, 'mode': 'competitive', 'completed': True}, {'player': 'charlie', 'duration_minutes': 22, 'score': 1110, 'mode': 'ranked', 'completed': False}, {'player': 'frank', 'duration_minutes': 79, 'score': 1854, 'mode': 'ranked', 'completed': False}, {'player': 'charlie', 'duration_minutes': 33, 'score': 666, 'mode': 'ranked', 'completed': False}, {'player': 'alice', 'duration_minutes': 101, 'score': 292, 'mode': 'casual', 'completed': True}, {'player': 'frank', 'duration_minutes': 25, 'score': 2887, 'mode': 'competitive', 'completed': True}, {'player': 'diana', 'duration_minutes': 53, 'score': 2540, 'mode': 'competitive', 'completed': False}, {'player': 'eve', 'duration_minutes': 115, 'score': 147, 'mode': 'ranked', 'completed': True}, {'player': 'frank', 'duration_minutes': 118, 'score': 2299, 'mode': 'competitive', 'completed': False}, {'player': 'alice', 'duration_minutes': 42, 'score': 1880, 'mode': 'casual', 'completed': False}, {'player': 'alice', 'duration_minutes': 97, 'score': 1178, 'mode': 'ranked', 'completed': True}, {'player': 'eve', 'duration_minutes': 18, 'score': 2661, 'mode': 'competitive', 'completed': True}, {'player': 'bob', 'duration_minutes': 52, 'score': 761, 'mode': 'ranked', 'completed': True}, {'player': 'eve', 'duration_minutes': 46, 'score': 2101, 'mode': 'casual', 'completed': True}, {'player': 'charlie', 'duration_minutes': 117, 'score': 1359, 'mode': 'casual', 'completed': True}], 'game_modes': ['casual', 'competitive', 'ranked'], 'achievements': ['first_blood', 'level_master', 'speed_runner', 'treasure_seeker', 'boss_hunter', 'pixel_perfect', 'combo_king', 'explorer']}


    game_data = [
        {"name": "alice",   "score": 2300, "region": "north",
         "premium": True,  "sessions_duration": 45,
         "total_sessions": 153,   "last_login_days": 0},

        {"name": "bob",     "score": 1200, "region": "east",
         "premium": False, "sessions_duration": 20,
         "total_sessions": 12,    "last_login_days": 2},

        {"name": "charlie", "score": 2150, "region": "central",
         "premium": True,  "sessions_duration": 120,
         "total_sessions": 150,   "last_login_days": 12},

        {"name": "diana",   "score": 2050, "region": "east",
         "premium": True,  "sessions_duration": 60,
         "total_sessions": 180,   "last_login_days": 3},

        {"name": "eve",     "score": 1800, "region": "north",
         "premium": False, "sessions_duration": 35,
         "total_sessions": 125,   "last_login_days": 2},

        {"name": "frank",   "score": 1500, "region": "central",
         "premium": True,  "sessions_duration": 50,
         "total_sessions": 40,    "last_login_days": 5},

        {"name": "grace",   "score": 900,  "region": "north",
         "premium": True, "sessions_duration": 15,
         "total_sessions": 10,    "last_login_days": 1},

        {"name": "hank",    "score": 400,  "region": "east",
         "premium": False, "sessions_duration": 10,
         "total_sessions": 2,     "last_login_days": 60},

        {"name": "ivy",     "score": 1950, "region": "central",
         "premium": False, "sessions_duration": 40,
         "total_sessions": 65,    "last_login_days": 3},

        {"name": "jack",    "score": 100,  "region": "north",
         "premium": True, "sessions_duration": 5,
         "total_sessions": 1,     "last_login_days": 4},

        {"name": "maggie",    "score": 500,  "region": "north",
         "premium": True, "sessions_duration": 15,
         "total_sessions": 12,     "last_login_days": 0}
    ]
    return game_data


def performance_report(data: dict) -> None:
    print()
    print('=== Player Performance Report ===')
    high_scorers = [(player['name'], player['score']) for player in
                    data if player['score'] > 2000]
    high_scorers = dict(high_scorers)
    score_tuples = [(player['score'], player['name']) for player in data]
    top_performers = sorted(score_tuples, reverse=True)[:3]
    top_3 = [player for score, player in top_performers]
    active_regions = {player['region'] for player in data}

    print(f'Top performers: {top_3}')
    print(f'High scorers (2000+): {high_scorers}')
    print(f'Active regions: {active_regions}')


def revenue_analytics(data):
    print()
    print('=== Revenue Analytics ===')
    unique_regions = {player['region'] for player in data}
    revenue_by_region = {
        region: 117 * (sum(1 for player in data if player['premium'] is True
                           and region ==
                           player['region'])) for region in unique_regions}
    print(f'Revenue by region: {revenue_by_region}')
    premium_count = sum(1 for player in data if player['premium'] is True)
    print(f'Premium players: {premium_count}')
    conv_rate = premium_count * 100 / len(data)
    print(f'Conversion rate: {conv_rate:.1f}%')


def engagement_metrics(data):
    print()
    daily_active_users = [sum(1 for player in data if player[
        'last_login_days'] <= day) for day in range(5)]
    print(f"Daily active users: {daily_active_users}")
    max_session = max(player['sessions_duration'] for player in data)
    minutes_played = sum(player['sessions_duration'] * player[
        'total_sessions'] for player in data)
    sessions_played = sum(player['total_sessions'] for player in data)
    print(f'Session lengths: avg {minutes_played/sessions_played} min,'
          f' max {max_session} min')

    active_players = sum(1 for player in data if player[
        'last_login_days'] <= 2)
    retention_rate = active_players * 100 / len(data)
    print(f'Retention rate: {retention_rate:.1f}%')


def advanced_insights(data):
    print()
    print('=== Advanced Insights ===')
    categories = {'casual', 'hardcore', 'competitive'}
    player_clusters = {
        category: sum(1 for player in data if
                      (category == 'competitive' and
                       player['last_login_days'] == 0) or
                      (category == 'hardcore' and 0 <
                       player['last_login_days'] <= 2) or
                      (category == 'casual' and
                       player['last_login_days'] > 2)
                      )
        for category in categories
    }
    print(f'Player clusters: {player_clusters}')
    players_at_risk = sum(1 for player in data if
                          player["last_login_days"] > 10)
    print(f'Churn prediction: {players_at_risk} players at risk')
    matches_generated = sum(1
                            for player1 in data
                            for player2 in data
                            if player1['region'] == player2['region'] and
                            player1['name'] != player2['name']
                            )
    print(f'Recommendation engine: {matches_generated} matches generated')


if __name__ == "__main__":
    print('=== Game Analytics Dashboard ===')
    data: dict = create_data()
    performance_report(data)
    revenue_analytics(data)
    engagement_metrics(data)
    advanced_insights(data)
