# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

def climbingLeaderboard(ranked, player):
    # get numbers for each position in the current leaderboard
    numbers = []
    cur_number, cur_score = 1, ranked[0]
    for i, score in enumerate(ranked):
        if score < cur_score:
            cur_number += 1
            cur_score = score
        numbers.append(cur_number)
    # print(numbers)

    result = []
    for player_score in player:
        # print(f'\n\nStarting with {player_score}')

        # binary search of player_score in the ranked
        cur_min, cur_max = 0, len(ranked) - 1
        cur_idx = cur_min + (cur_max - cur_min) // 2

        while True:
            # print(f'{cur_min}, {cur_max} => {cur_idx}')

            if cur_min + 1 >= cur_max:
                # print(f'Shortened {cur_min}, {cur_max}, {cur_idx}')
                
                if player_score >= ranked[cur_min]: result.append(numbers[cur_min])
                elif player_score == ranked[cur_max]: result.append(numbers[cur_max])
                elif player_score < ranked[cur_max]: result.append(numbers[cur_max] + 1)
                else: result.append(numbers[cur_max])
                # print(f'Ranked at min, max: {ranked[cur_min]}, {ranked[cur_max]}; player_score {player_score}')
                break

            elif player_score < ranked[cur_idx]:
                cur_min = cur_idx
                cur_idx = cur_min + (cur_max - cur_min) // 2
            else:
                cur_max = cur_idx
                cur_idx = cur_min + (cur_max - cur_min) // 2


    # print('Result', result)
    return result

assert climbingLeaderboard([100, 90, 90, 80], [70, 80, 105]) == [4, 3, 1]
assert climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]) == [6, 5, 4, 2, 1]