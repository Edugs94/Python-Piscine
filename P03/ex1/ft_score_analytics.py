"""Exercise 1: Score Analytics."""
import sys


def create_list(score_list) -> list:
    """Creates a list 2nd command-line argument to the last one."""

    for arg in sys.argv[1:]:
        try:
            score_list.append(int(arg))
        except ValueError:
            pass

    return score_list


def main():
    "Main workflow to print requested data from list data"

    argc = len(sys.argv)
    print("=== Player Score Analytics ===")
    if argc < 2:
        print(f"No scores provided. Usage: python3 {sys.argv[0]}"
              " <score1> <score2> ...")
        return
    score_list = []
    score_list = create_list(score_list)
    print('Scores processed: [', end='')
    i = 0
    while i < argc - 1:
        if i != argc - 2:
            print(f'{score_list[i]}, ', end='')
        else:
            print(f'{score_list[i]}]')
        i += 1
    print(f'Total players: {len(score_list)}')
    print(f'Total score: {sum(score_list)}')
    print(f'Average score: {sum(score_list)/len(score_list)}')
    print(f'High score: {max(score_list)}')
    print(f'Low score: {min(score_list)}')
    print(f'Score range: {max(score_list) - min(score_list)}')
    print()


if __name__ == '__main__':
    main()
