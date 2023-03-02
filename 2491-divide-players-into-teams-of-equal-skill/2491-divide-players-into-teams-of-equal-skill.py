class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if(len(skill) == 2):
            return skill[1] * skill[0]
        eq = len(skill) // 2
        eqsum = sum(skill) // eq
        count = Counter(skill)
        res = 0
        for i, k in count.items():
            if(count[eqsum - i] == k):
                res += k*(i * (eqsum - i))
            else:
                return -1
        return res //2
                