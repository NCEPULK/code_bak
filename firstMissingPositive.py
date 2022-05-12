


class Solution():
    def firstMissingPositive(self,nums):
        i=0
        while i<len(nums):
            print(i,nums)
            if nums[i]!=i+1 and nums[i]>0 and nums[i]<len(nums):
                a=nums[i]
                nums[i]=nums[a-1]
                nums[a-1]=a
                i-=1
            i+=1
        print(nums)
        for i in range(1,len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1
if __name__=='__main__':
    print(Solution().firstMissingPositive([-1,4,2,1,9,10]))
