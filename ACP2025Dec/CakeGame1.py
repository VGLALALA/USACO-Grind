def that():
    import sys
    input = sys.stdin.readline

    def play_game(num_cakes, cake_sizes):
        bessie_share = 0
        max_elsie_share = 0
        left = 0
        right = num_cakes - 1

        turn = 0
        while left <= right:
            if turn == 0:
                if left + 1 == right:
                    bessie_share += cake_sizes[left] + cake_sizes[right]
                    break

                left_sum = cake_sizes[left] + cake_sizes[left + 1]
                right_sum = cake_sizes[right] + cake_sizes[right - 1]

                if left_sum >= right_sum:
                    bessie_share += left_sum
                    left += 2
                else:
                    bessie_share += right_sum
                    right -= 2
            else:
                if cake_sizes[left] >= cake_sizes[right]:
                    max_elsie_share += cake_sizes[left]
                    left += 1
                else:
                    max_elsie_share += cake_sizes[right]
                    right -= 1

            turn = 1 - turn

        return bessie_share, max_elsie_share

    data = input().split()
    index = 0
    num_cases = int(data[index])
    index += 1

    results = []
    for _ in range(num_cases):
        num_cakes = int(data[index])
        index += 1
        cake_sizes = list(map(int, data[index:index + num_cakes]))
        index += num_cakes
        bessie_share, max_elsie_share = play_game(num_cakes, cake_sizes)
        results.append((bessie_share, max_elsie_share))

    for bessie_share, max_elsie_share in results:
        print(f"{bessie_share} {max_elsie_share}")

that()