data = [1,3,2,4,3,5,4,6,5,7,6,8,7,9,8,0]

def merge_sort(arr):
    def merge(A, B):
        C = []
        i, j = 0, 0
        while True:
            if i + j == len(A) + len(B):
                return C
            if i == len(A) or (j < len(B) and B[j] <= A[i]):
                C += [B[j]]
                j += 1
                continue
            if j == len(B) or A[i] <= B[j]:
                C += [A[i]]
                i += 1
    
    if len(arr) <= 1:
        return arr
    half_n = len(arr) // 2
    return merge(merge_sort(arr[:half_n]), merge_sort(arr[half_n:]))