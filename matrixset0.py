class Solution:
    def setZeroes(self,martrix):
        m=len(martrix)
        n=len(martrix[0])
        row=[0]*m
        line=[0]*n
        for i in range(m):
            for j in range(n):
                if martrix[i][j]==0:
                    row[i]=line[j]=1
        for i in range(m):
            for j in range(n):
                if row[i] or line[j]:
                    martrix[i][j]=0
