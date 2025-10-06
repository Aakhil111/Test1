def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    low, high = 0, m

    while low <= high:
        i = (low + high) // 2
        j = (m + n + 1) // 2 - i

        A_left = float('-inf') if i == 0 else nums1[i - 1]
        A_right = float('inf') if i == m else nums1[i]
        B_left = float('-inf') if j == 0 else nums2[j - 1]
        B_right = float('inf') if j == n else nums2[j]

        if A_left <= B_right and B_left <= A_right:
            if (m + n) % 2 == 0:
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            else:
                return max(A_left, B_left)
        elif A_left > B_right:
            high = i - 1
        else:
            low = i + 1

nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))
