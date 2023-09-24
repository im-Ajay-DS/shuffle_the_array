class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled_array=[]
        i=0
        while n<len(nums):
            shuffled_array.append(nums[i])# append the x element
            shuffled_array.append(nums[n])# append the y element
            i=i+1 #increament x elements
            n=n+1 #increament y elements
        return shuffled_array
