class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        poss=[]
        for i in range(1,area+1):
            if area%i==0:
                if i>=area/i:
                    poss.append([i,area//i])
                if int(area/i)==i:
                    return [i,area//i]
        min=0
        for i in range(len(poss)):
            if (poss[i][0]-poss[i][1])<(poss[min][0]-poss[min][1]):
                min=i
        return poss[min]