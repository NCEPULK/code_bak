
import pdb

class Solution():
    def findMedianSortedArrays(self,nums1,nums2):
        len1=len(nums1)
        len2=len(nums2)
        p1=0
        p2=0
        group = []
        while(p1<len1 and p2<len2):
            if(nums1[p1]<nums2[p2]):
                group.append(nums1[p1])
                p1+=1
            else:    
                group.append(nums2[p2])
                p2+=1
        if p1==len1:
            group+=nums2[p2:]
        else:
            group+=nums1[p1:]
        length=len1+len2
        if (length)%2==0:
            group_out=(group[length//2-1]+group[length//2])/2
        else:
            group_out=group[(length-1)//2]
        print(group)
        print(group_out)

        return group_out 



if __name__=='__main__':
    nums1=[1,3]
    nums2=[2]
    Solution().findMedianSortedArrays(nums1,nums2)
