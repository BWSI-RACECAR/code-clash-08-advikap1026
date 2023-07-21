class Solution:    
    def optimizescan(self, battcap):
        # Input type: Integer
        # return type: float

        #TODO: Write code below to return a float with the solution to the prompt.
         meters = float(battcap/250)
        # maxArea = 0
        # length = 0 
        # width = 0 
        # count = 1 
        # for i in range(int(meters)):
        #     width = meters - count 
        #     length = meters - 2*(width)
        #     if width > 0 and length > 0: 
        #         area = width *length 
        #         if area > maxArea:
        #             maxArea = area
        #     count = count + 1
        # return maxArea
        # pass 
         return float(((meters*meters)/4)-2*((meters/4)(meters/4)))
         #return float((battcap/500)*(battcap/1000))
    
        #A = P^2/4 - 2(p/4)^2
        #A = p - 4tdist 
        #tdist = P/4
def main():
    battcap = int(input())

    tc1 = Solution()
    ans = tc1.optimizescan(battcap)
    print("%.2f" % ans)

if __name__ and "__main__":
    main()