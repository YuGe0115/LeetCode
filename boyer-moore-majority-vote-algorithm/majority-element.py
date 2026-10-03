class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        def divide(left, right):
            # Base case
            if left == right:
                return nums[left]

            # Divide
            mid = (left + right) // 2

            # Conquer
            left_major = divide(left, mid)
            right_major = divide(mid + 1, right)

            # Combine
            if left_major == right_major:
                return left_major

            left_count = 0
            right_count = 0

            for i in range(left, right + 1):
                if nums[i] == left_major:
                    left_count += 1
                if nums[i] == right_major:
                    right_count += 1

            if left_count > right_count:
                return left_major
            else:
                return right_major

        return divide(0, len(nums) - 1)