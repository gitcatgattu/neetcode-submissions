class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # slow,fast=0,0
        # while True:
        #     slow=nums[slow]
        #     fast=nums[nums[fast]]
        #     if slow==fast:
        #         break
        # slow2=0
        # while True:
        #     slow=nums[slow]
        #     slow2=nums[slow2]
        #     if slow==slow2:
        #         return slow


        #modifying array

        i=0
        while True:
            if nums[i]<0:
                return -i
            nums[i]=-nums[i]
            i=nums[i]
