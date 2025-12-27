class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=len(nums)
        i=0
        j=1
        if not nums:
            return 0
        while(j<l):
            if nums[i]==val and nums[j]!=val:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            elif nums[j]==val:
                pass
            else:
                nums[i+1],nums[j]=nums[j],nums[i+1]
                i+=1
            j+=1
        print(i)
        if nums[i]==val:
            return i
        else:
            return i+1

