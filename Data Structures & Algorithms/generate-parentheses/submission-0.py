class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def genSets(left, right, subsets):
            if right < left:
                return
            if left == 0 and right == 0:
                res.append("".join(subsets))
                return
            if left == right:
                subsets.append("(")
                genSets(left-1, right, subsets)
                subsets.pop()
                return
            elif left > 0:
                subsets.append("(")
                genSets(left-1, right, subsets)
                subsets.pop()
            subsets.append(")")
            genSets(left, right-1, subsets)
            subsets.pop()
        genSets(n,n,[])
        return res