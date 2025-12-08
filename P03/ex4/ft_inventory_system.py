def create_inventories() -> dict:
    print('=== Player Inventory System ==')
    print()
    inventories = {
        'Alice': {
            'sword': {
                'category': 'weapon',
                'rarity': 'rare',
                'qty': 1,
                'price': 500
            },
            'potion': {
                'category': 'consumable',
                'rarity': 'common',
                'qty': 5,
                'price': 50
            },

            'shield': {
                'category': 'armor',
                'rarity': 'uncommon',
                'qty': 1,
                'price': 200
            }
        },
        'Bob': {
            'magic ring': {
                'category': 'armor',
                'rarity': 'rare',
                'qty': 1,
                'price': 300
            }
        }
    }
    return inventories


def display_inventory(inventories: dict, player: str) -> None:
    inventory = inventories.get(player)
    if inventory is None:
        print(f"{player} not found")
        return
    gold_value = 0
    item_count = 0
    category_counts = {}
    print(f"=== {player}'s Inventory ===")
    for name, details in inventory.items():
        qty = details.get('qty')
        category = details.get('category')
        rarity = details.get('rarity')
        price = details.get('price')

        total_price = qty * price
        gold_value += total_price
        item_count += qty
        category_total = category_counts.get(category, 0)
        category_counts.update({category: category_total + qty})

        print(f"{name} ({category}, {rarity}):"
              f" {qty}x @ {price} gold each = {total_price} gold")
    print()
    print(f'Inventory value: {gold_value}')
    print(f'Item count: {item_count} items')
    print('Categories: ', end='')
    text = [f"{category}({quantity})" for category, quantity
            in category_counts.items()]
    print(*text, sep=', ')


def display_update(inventories: dict, player1, player2, item_name):
    print('=== Updated Inventories ===')
    print(f'{player1} {item_name}s: {inventories.get(
        player1).get(item_name).get('qty')}')
    print(f'{player2} {item_name}s: {inventories.get(
        player2).get(item_name).get('qty')}')
    print()


def ft_transaction(inventories: dict, player1: str,
                   player2: str, item_name: str, qty: int):

    print(f"=== Transaction: {player1} gives {player2} {qty} {item_name}s ===")
    if inventories.get(player1) is None:
        print(f"Error: Player {player1} does not exist. Aborting transaction")
        return
    if inventories.get(player2) is None:
        print(f"Error: Player {player2} does not exist. Aborting transaction")
        return

    inventory_p1: dict = inventories.get(player1)
    item_details_p1: dict = inventory_p1.get(item_name)
    current_qty = item_details_p1.get('qty', 0)
    item_details_p1.update({'qty': (current_qty - qty)})

    inventory_p2: dict = inventories.get(player2)
    item_details_p2: dict = inventory_p2.get(item_name)
    if item_details_p2 is None:
        item_details_p2 = dict(item_details_p1)
        inventory_p2.update({item_name: item_details_p2})
        item_details_p2.update({'qty': 0})
    current_qty = item_details_p2.get('qty', 0)
    item_details_p2.update({'qty': current_qty + qty})
    print('Transaction successful!')
    print()

    display_update(inventories, player1, player2, item_name)

    return inventories


def print_analytics(inventories: dict):
    print('=== Inventory Analytics ===')
    richest_player: str = None
    highest_value: int = -1
    most_items_player = None
    most_items_amount = -1
    rarity_tier = {'common': 0, 'uncommon': 1, 'rare': 2, 'epic': 3,
                   'legendary': 4}
    unique_items = {}
    rarest_items = {}
    for player, item in inventories.items():
        item_total = 0
        item_qty = 0
        for item_name, details in item.items():
            item_total += details.get('qty') * details.get('price')
            item_qty += details.get('qty')
        if item_total > highest_value:
            highest_value = item_total
            richest_player = player
        if item_qty > most_items_amount:
            most_items_amount = item_qty
            most_items_player = player
    print(f'Most valuable player: {richest_player} ({highest_value} gold)')
    print(f'Most items: {most_items_player} ({most_items_amount} items)')

    max_rarity = -1
    for player, item in inventories.items():
        for item_name, details in item.items():
            rarity_value = rarity_tier[details['rarity']]
            unique_items.update({item_name: rarity_value})
            if rarity_value > max_rarity:
                max_rarity = rarity_value
    for item_name, rarity in unique_items.items():
        if unique_items.get(item_name) == max_rarity:
            rarest_items.update({item_name: rarity})

    print('Rarest items: ', end='')

    text = [f"{item_name}" for item_name, rarity
            in rarest_items.items()]
    print(*text, sep=', ')


if __name__ == "__main__":
    player1 = 'Alice'
    player2 = 'Bob'
    inventories = create_inventories()
    display_inventory(inventories, player1)
    print()
    inventories = ft_transaction(inventories, player1, player2, 'potion', 2)
    print_analytics(inventories)
