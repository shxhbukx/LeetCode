def numJewelsInStones(self, jewels, stones):
    count = Counter(jewels)
    ans = 0
    for stone in stones:
        ans += count[stone]
    return ans    