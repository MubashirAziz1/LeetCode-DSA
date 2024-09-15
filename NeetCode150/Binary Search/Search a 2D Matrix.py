class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Search a row in which target is present.
        top = 0
        bot = len(matrix)-1
        while top<=bot:
            m = top+((bot-top)//2)
            if matrix[m][0] <= target and matrix[m][-1] >= target:
                row_numb = m
                break
            elif matrix[m][0] > target:
                bot = m-1
            elif matrix[m][-1] < target:
                top = m+1

        # Search a target in the known row
        try:
            l = 0
            h = len(matrix[0])-1
            while l <= h:
                m = l+((h-l)//2)
                if matrix[row_numb][m] == target:
                    return True
                elif matrix[row_numb][m] > target:
                    h = m-1
                elif matrix[row_numb][m] < target:
                    l = m+1
        except NameError:
            return False
        
