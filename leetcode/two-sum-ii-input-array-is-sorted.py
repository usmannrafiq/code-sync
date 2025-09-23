class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Time: O(n)
        # Space: O(1)

        # initialize left and right pointers
        left = 0
        right = len(numbers) - 1

        # loop through the list until target is found
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1

            elif numbers[left] + numbers[right] > target:
                right -= 1

            else: 
                return left + 1 , right + 1