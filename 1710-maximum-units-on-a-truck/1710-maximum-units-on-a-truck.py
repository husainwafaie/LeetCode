class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        count = 0
        boxes = 0
        box = sorted(boxTypes, key = lambda x:-x[1])
        for i in range(len(box)):
            if box[i][0] + boxes > truckSize:
                return count + (box[i][1] * (truckSize - boxes))
            elif box[i][0] + boxes == truckSize:
                return count + (box[i][1] * box[i][0]) 
            else:
                count += box[i][0] * box[i][1]
                boxes += box[i][0]
        return count