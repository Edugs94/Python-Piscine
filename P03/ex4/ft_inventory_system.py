"""Exercise 4: Inventory System"""


def create_inventories() -> dict:
    '''Creates a general data_base named inventories based on
    data_generator given on the exercise'''

    inventories = {
        'players': {
            'alice': {
                'items': {
                    'pixel_sword': 1,
                    'code_bow': 1,
                    'health_byte': 1,
                    'quantum_ring': 3
                },
                'total_value': 1875,
                'item_count': 6
            },
            'bob': {
                'items': {
                    'code_bow': 3,
                    'pixel_sword': 2
                },
                'total_value': 900,
                'item_count': 5
            },
            'charlie': {
                'items': {
                    'pixel_sword': 1,
                    'code_bow': 1
                },
                'total_value': 350,
                'item_count': 2
            },
            'diana': {
                'items': {
                    'code_bow': 3,
                    'pixel_sword': 3,
                    'health_byte': 3,
                    'data_crystal': 3
                },
                'total_value': 4125,
                'item_count': 12
            }
        },
        'catalog': {
            'pixel_sword':
                {'type': 'weapon', 'value': 150, 'rarity': 'common'},
            'quantum_ring':
                {'type': 'accessory', 'value': 500, 'rarity': 'rare'},
            'health_byte': {'type': 'consumable', 'value': 25,
                            'rarity': 'common'},
            'data_crystal': {'type': 'material', 'value': 1000,
                             'rarity': 'legendary'},
            'code_bow': {'type': 'weapon', 'value': 200, 'rarity': 'uncommon'}
        }
    }
    return inventories


def update_gold_and_qty(inventories: dict, player: str) -> tuple[int, int]:
    '''Returns the current value of gold_value and item_count for a player'''

    players_db = inventories.get('players')
    catalog_db = inventories.get('catalog')
    player_data = players_db.get(player)
    player_items: dict = player_data.get('items')
    gold_value = 0
    item_count = 0

    for item_name, qty in player_items.items():
        item_details = catalog_db.get(item_name)

        price = item_details.get('value')
        total_price = qty * price
        gold_value += total_price
        item_count += qty

    return gold_value, item_count


def display_inventory(inventories: dict, player: str) -> None:
    '''Displays all players items, rarities, categories...'''

    players_db = inventories.get('players')
    catalog_db = inventories.get('catalog')
    player_data = players_db.get(player)
    if player_data is None:
        print(f"{player} not found")
        return
    print(f"=== {player.capitalize()}'s Inventory ===")
    category_counts = {}

    player_items = player_data.get('items')

    for item_name, qty in player_items.items():
        item_details = catalog_db.get(item_name)

        price = item_details.get('value')
        category = item_details.get('type')
        rarity = item_details.get('rarity')
        total_price = qty * price

        curr_cat_count = category_counts.get(category, 0)
        category_counts.update({category: curr_cat_count + qty})

        print(f"{item_name} ({category}, {rarity}): "
              f"{qty}x @ {price} gold each = {total_price} gold")
    gold_value = player_data.get('total_value')
    item_count = player_data.get('item_count')

    print()
    print(f'Inventory value: {gold_value} gold')
    print(f'Item count: {item_count} items')

    print('Categories: ', end='')
    i = 0
    for cat, qty in category_counts.items():
        if (i != len(category_counts) - 1):
            print(f'{cat} ({qty}), ', end='')
        else:
            print(f'{cat} ({qty})')
        i += 1


def ft_transaction(inventories: dict, player1: str, player2: str,
                   item_name: str, qty: int):

    '''Performs item trade between 2 different players'''

    print()
    if qty == 1:
        print(f"=== Transaction: {player1.capitalize()} "
              f"gives {player2.capitalize()} {qty} {item_name} ===")
    else:
        print(f"=== Transaction: {player1.capitalize()} "
              f"gives {player2.capitalize()} {qty} {item_name}s ===")

    players_db = inventories.get('players')
    p1_data = players_db.get(player1)
    p2_data = players_db.get(player2)

    if p1_data is None:
        print(f"Error: Player {player1.capitalize()} does not exist. "
              "Aborting transaction")
        return inventories
    if p2_data is None:
        print(f"Error: Player {player2.capitalize()} does not exist. "
              "Aborting transaction")
        return inventories

    if player1 == player2:
        print("Transaction failure: Player 1 and Player 2 must "
              "be distinct entities.")
        return inventories

    p1_items = p1_data.get('items')
    if p1_items.get(item_name) is None or p1_items.get(item_name) < qty:
        print(f"Error: {player1} does not have enough {item_name}s. Aborting.")
        return inventories

    current_qty_p1 = p1_items.get(item_name)
    p1_items.update({item_name: current_qty_p1 - qty})
    total_value, item_count = update_gold_and_qty(inventories, player1)
    p1_data['total_value'] = total_value
    p1_data['item_count'] = item_count

    p2_items = p2_data.get('items')
    current_qty_p2 = p2_items.get(item_name, 0)
    p2_items.update({item_name: current_qty_p2 + qty})
    total_value, item_count = update_gold_and_qty(inventories, player2)
    p2_data['total_value'] = total_value
    p2_data['item_count'] = item_count

    print('Transaction successful!')
    print()

    print('=== Updated Inventories ===')
    print(f'{player1.capitalize()} {item_name}s: {p1_items.get(item_name)}')
    print(f'{player2.capitalize()} {item_name}s: {p2_items.get(item_name)}')

    return inventories


def print_analytics(inventories: dict):
    '''Calculate and prints richest player,
    the player with more items and rarest_item'''
    print()
    print('=== Inventory Analytics ===')

    players_db = inventories.get('players')
    catalog_db = inventories.get('catalog')

    richest_player = None
    highest_value = -1

    most_items_player = None
    most_items_amount = -1

    rarity_tier = {'common': 0, 'uncommon': 1, 'rare': 2,
                   'epic': 3, 'legendary': 4}

    max_rarity_found_value = -1
    rarest_items_list = []

    for player_name, player_data in players_db.items():

        p_value = player_data.get('total_value', 0)
        p_qty = player_data.get('item_count', 0)

        if p_value > highest_value:
            highest_value = p_value
            richest_player = player_name

        if p_qty > most_items_amount:
            most_items_amount = p_qty
            most_items_player = player_name

        p_items = player_data.get('items')

        for item_name, qty in p_items.items():
            if qty > 0:
                item_details = catalog_db.get(item_name)

                r_str = item_details.get('rarity')
                r_val = rarity_tier.get(r_str, 0)

                if r_val > max_rarity_found_value:
                    max_rarity_found_value = r_val
                    rarest_items_list = [item_name]

                elif r_val == max_rarity_found_value:
                    if item_name not in rarest_items_list:
                        rarest_items_list.append(item_name)

    print(f'Most valuable player: {richest_player.capitalize()} '
          f'({highest_value} gold)')
    print(f'Most items: {most_items_player.capitalize()} '
          f'({most_items_amount} items)')

    print('Rarest items: ', end='')
    print(*rarest_items_list, sep=', ')


if __name__ == "__main__":
    '''Main program workflow'''

    player1 = 'alice'
    player2 = 'bob'

    print('=== Player Inventory System ===')
    print()
    inventories = create_inventories()

    display_inventory(inventories, player1.lower())

    inventories = ft_transaction(inventories, player1.lower(), player2.lower(),
                                 'quantum_ring', 1)

    print_analytics(inventories)
