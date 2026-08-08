
class Numbers:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __add__(self, other):
        return Numbers(self.data + other.data)

nums1 = Numbers([1, 2, 3])
nums2 = Numbers([4, 5])
result = nums1 + nums2

print(len(nums1))
print(result.data)

