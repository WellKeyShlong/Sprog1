def quick(n):
    arr = n[:]

    def partition(left, right, n, count):
        pivot = n[(left + right) // 2]

        while left <= right:
            while n[left] < pivot:
                count += 1
                left += 1
            count += 1 

            while n[right] > pivot:
                count += 1
                right -= 1
            count += 1 

            if left <= right:
                count += 1 
                n[left], n[right] = n[right], n[left]
                left += 1
                right -= 1

        return left, count

    def quicksort(left, right, n, count=0):
        if left < right:
            mid, count = partition(left, right, n, count)
            count = quicksort(left, mid - 1, n, count)
            count = quicksort(mid, right, n, count)
        return count

    count = quicksort(0, len(arr) - 1, arr)
    return count

