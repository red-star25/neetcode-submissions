class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            print(left, right)
            sumOfNum = numbers[left] + numbers[right]
            if sumOfNum == target:
                return [left + 1, right + 1]
            elif sumOfNum > target:
                right -= 1
            elif sumOfNum < target:
                left += 1
        return []