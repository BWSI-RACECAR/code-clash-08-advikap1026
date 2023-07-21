class Solution:    
    def optimizescan(self, battcap):
        # Input type: Integer
        # return type: float

        #TODO: Write code below to return a float with the solution to the prompt.
        meters = battcap/250 
        maxArea = 0
        length = 0 
        width = 0 
        count = 1 
        for i in range(meters):
            width = meters -1 
            length = meters - 2(width)
            if width > 0 and length > 0: 
                area = width *length 
                if area > maxArea:
                    maxArea = area
        return maxArea
        pass 

def main():
    battcap = int(input())

    tc1 = Solution()
    ans = tc1.optimizescan(battcap)
    print("%.2f" % ans)

if __name__ and "__main__":
    main()