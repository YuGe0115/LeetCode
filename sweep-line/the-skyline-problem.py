class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        def divide(buildings):
            # Base case
            if len(buildings) == 1:
                L, R, H = buildings[0]
                return [[L, H], [R, 0]]

            # Divide
            mid = len(buildings) // 2
            left_buildings = buildings[:mid]
            right_buildings = buildings[mid:]

            # Conquer
            left_skyline = divide(left_buildings)
            right_skyline = divide(right_buildings)

            merged = []

            i = 0
            j = 0

            left_height = 0
            right_height = 0

            while i < len(left_skyline) and j < len(right_skyline):

                # Left skyline changes first
                if left_skyline[i][0] < right_skyline[j][0]:
                    x = left_skyline[i][0]
                    left_height = left_skyline[i][1]
                    i += 1

                # Right skyline changes first
                elif left_skyline[i][0] > right_skyline[j][0]:
                    x = right_skyline[j][0]
                    right_height = right_skyline[j][1]
                    j += 1

                # Both skylines change at the same x
                else:
                    x = left_skyline[i][0]
                    left_height = left_skyline[i][1]
                    right_height = right_skyline[j][1]
                    i += 1
                    j += 1

                # Actual visible height
                height = max(left_height, right_height)

                if not merged or merged[-1][1] != height:
                    merged.append([x, height])

        
            while i < len(left_skyline):
                x, height = left_skyline[i]

                if not merged or merged[-1][1] != height:
                    merged.append([x, height])

                i += 1

            while j < len(right_skyline):
                x, height = right_skyline[j]

                if not merged or merged[-1][1] != height:
                    merged.append([x, height])

                j += 1

            return merged

        return divide(buildings)
        