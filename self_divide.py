class Solution(object):
        def selfDividingNumbers(self, left, right):
            returnData = []
            for num in range(left,right + 1):
                temp = str(num)
                flag = 0
                for digit in temp:
                    id = int(digit)
                    if( id == 0 or (num%id) != 0 ):
                        flag = 1

                if( flag == 0 ):
                    returnData.append( num )

            return returnData
