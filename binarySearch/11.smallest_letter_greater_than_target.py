class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        for i in letters:
            if target != i and sorted([target, i])[1] == i:
                return i

        return letters[0]

letters = ["c","f","j"]
target = "a"
sol = Solution()
print(sol.nextGreatestLetter(letters, target))