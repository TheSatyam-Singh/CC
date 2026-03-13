class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def solve(i, target, path):
            if target == 0:
                ans.append(path.copy())
                return
            if i >= len(candidates) or target < 0:
                return
            path.append(candidates[i])
            solve(i + 1, target - candidates[i], path)
            path.pop()
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            solve(j, target, path)
        solve(0, target, [])
        return ans
