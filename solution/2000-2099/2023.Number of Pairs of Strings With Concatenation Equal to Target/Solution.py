class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        cnt = Counter(nums)
        ans = 0
        for i in range(1, len(target)):
            a, b = target[:i], target[i:]
            ans += cnt[a] * cnt[b] if a != b else cnt[a] * (cnt[a] - 1)
        return ans
