class Solution:
    def merge(self, nums1, nums2):
        result = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] is not None and nums2[j] is not None:
                if nums1[i] <= nums2[j]:
                    if nums1[i] not in [None]:
                        result.append(nums1[i])
                        i += 1
                else:
                    if nums2[j] not in [None]:
                        result.append(nums2[j])
                        j += 1
        while i < len(nums1):
            if nums1[i] is not None:
                result.append(nums1[i])
            i += 1
        while j < len(nums2):
            if nums2[j] is not None:
                result.append(nums2[j])
            j += 1
        return result
