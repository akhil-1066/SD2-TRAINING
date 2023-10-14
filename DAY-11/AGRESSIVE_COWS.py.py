def aggressive_cows(stalls, cows):
    stalls.sort()

    def is_valid(mid):
        count = 1
        last_position = stalls[0]

        for i in range(1, len(stalls)):
            if stalls[i] - last_position >= mid:
                count += 1
                last_position = stalls[i]

        return count >= cows

    def binary_search():
        low, high = 0, stalls[-1] - stalls[0]

        while low < high:
            mid = (low + high) // 2
            if is_valid(mid):
                low = mid + 1
            else:
                high = mid

        return low - 1

    return binary_search()
stalls = [0,3,4,7,9,10]
num_cows = 4
result = aggressive_cows(stalls, num_cows)
print(f"The maximum minimum distance is: {result}")