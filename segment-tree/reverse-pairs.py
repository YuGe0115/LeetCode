class Solution:
    def reversePairs(self, nums: list[int]) -> int:
                
        def mergeSort(arr):
            # 1. Base case
            if len(arr) <= 1:
                return arr, 0

            # 2. Divide
            mid = len(arr) // 2

            # 3. Conquer
            left, count_left = mergeSort(arr[:mid])
            right, count_right = mergeSort(arr[mid:])

            # 4. Count crossed reverse pairs
            count_cross = 0
            j = 0

            for i in range(len(left)):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1

                count_cross += j




            # 5. merge
            merged = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])

            # 6. Return sorted array + number of pairs
            total = count_left + count_right + count_cross
            return merged, total

        _, count = mergeSort(nums)
        return count
        