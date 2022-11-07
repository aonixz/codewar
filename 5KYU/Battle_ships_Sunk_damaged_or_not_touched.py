def damaged_or_sunk(board, attacks) -> dict:
    game_results = {
        'sunk': 0,
        'damaged': 0,
        'not_touched': 0,
        'points': 0
    }

    boats = {
        '1': [],
        '2': [],
        '3': []
    }
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                boats[str(board[i][j])].append({'cord': [j + 1, len(board) - i], 'is_attacked': False})

    for boat_key in boats:
        for boat_path in boats[boat_key]:
            for attack in attacks:
                if boat_path['cord'] == attack:
                    boat_path['is_attacked'] = True

    for boat_key in boats:
        damaged_path_count = sum([1 for item in boats[boat_key] if item['is_attacked']])
        boat_length = len(boats[boat_key])

        if boat_length > 0:
            if damaged_path_count == 0:
                game_results['not_touched'] += 1
            elif damaged_path_count < boat_length:
                game_results['damaged'] += 1
            elif damaged_path_count == boat_length:
                game_results['sunk'] += 1
    game_results['points'] = game_results['sunk'] * 1 + game_results['damaged'] * 0.5 + game_results['not_touched'] * -1

    return game_results