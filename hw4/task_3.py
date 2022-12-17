class Solution(object):
    def minDistance(self, word1, word2):
        """Сложность функции O(n*m)"""
        w1Len = len(word1)
        w2Len = len(word2)
        dp = [[0 for n in range(w2Len+1)] for n in range(w1Len+1)]
        for i in range(w1Len+1):
            for j in range(w2Len+1):
                if(i == 0 and j == 0):  # Если строки пустые
                    dp[i][j] = 0
                elif(i == 0):  # Левый вертикальный край
                    dp[i][j] = dp[i][j-1]+1
                elif(j == 0):  # Верхний горизонтальный край
                    dp[i][j] = dp[i-1][j]+1
                elif(word1[i-1] == word2[j-1]):  # Когда буквы в словах совпадают
                    #print("+++", word1[i-1],"+++",word2[j-1],"+++")
                    dp[i][j] = dp[i-1][j-1]
                else:  # Когда буквы в словах не совпали
                    # print("***",i,"***",j,"***")
                    #print("+++", word1[i-1],"+++",word2[j-1],"+++")
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1])+1
        return dp[w1Len][w2Len]
