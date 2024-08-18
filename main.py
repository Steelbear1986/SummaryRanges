class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result=[]
        pom=-1000
        for i in range(len(nums)):
            if str(nums[i]) not in result and  nums[i]-pom!=1:
                result.append(str(nums[i]))
                pom=nums[i]
            if str(nums[i]) not in result and nums[i] - pom == 1:
                if len(result[-1])==len(str(pom)):
                      result[-1] = result[-1]+ '->' + str(nums[i])
                      pom = nums[i]
                if len(result[-1]) >= len(str(pom)) and nums[i]!=pom:
                       result[-1]=result[-1][:len(str(nums[i]))]+'->'+str(nums[i])
                       pom = nums[i]
        return result