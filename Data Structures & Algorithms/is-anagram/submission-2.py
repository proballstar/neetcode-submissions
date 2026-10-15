class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorts = "".join(sorted(s))
        sortt = "".join(sorted(t))
        return sorts == sortt
        