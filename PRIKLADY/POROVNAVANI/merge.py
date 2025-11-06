def merge_sort(arr):
    if len(arr) > 1:
        l_arr = arr[:len(arr)//2]
        p_arr = arr[len(arr)//2:]

        merge_sort(l_arr)
        merge_sort(p_arr)

        i = 0
        j = 0
        k = 0

        while i < len(l_arr) and j < len(p_arr):
            if l_arr[i] < p_arr[j]:
                arr[k] = l_arr[i]
                i += 1
            

