class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        for i in range(0,numRows):
            if(i==0):
                ans.append([1])
            elif (i==1):
                ans.append([1,1])
            else:
                temp=[1]
                for j in range(1,i):
                    temp.append(ans[i-1][j-1]+ans[i-1][j])
                temp.append(1)
                ans.append(temp)
        return ans