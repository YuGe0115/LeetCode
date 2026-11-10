class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:

        #get as many boxes with larger "units" number as possible
        boxTypes.sort(key = lambda x:x[1], reverse = True)

        result = 0
        actual_size = 0
        for i in range(len(boxTypes)):
            if actual_size == truckSize:
                break
            elif boxTypes[i][0] <= truckSize - actual_size :
                result += boxTypes[i][1] * boxTypes[i][0]
                actual_size += boxTypes[i][0]
            elif boxTypes[i][0] > truckSize - actual_size:
                result += (truckSize - actual_size) * boxTypes[i][1]
                actual_size = truckSize

        return result
        