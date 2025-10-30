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
            else:
                arr[k] = p_arr[j]
                j += 1
            k += 1 
        
        while i < len(l_arr):
            arr[k] = l_arr[i]
            i += 1
            k += 1

        while j < len(p_arr):
            arr[k] = p_arr[j]
            j += 1
            k += 1


arr_test = [1, 7, 8, 2, 4, 7, 2, 3, 8, 5, 6]
merge_sort(arr_test)

