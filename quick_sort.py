def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        print(f"Array after partitioning with pivot index {pi}: {arr}")
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    pivot = arr[high]
    print(f"\nPartitioning with pivot {pivot} (index {high})")
    i = low - 1
    for j in range(low, high):
        print(f"  Comparing {arr[j]} with pivot {pivot}", end=' ')
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            print(f"=> swap {arr[i]} and {arr[j]} (i={i}, j={j})")
        else:
            print("=> no swap")
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    print(f"  Swapping pivot: {arr[i + 1]} with {arr[high]} => {arr}")
    return i + 1


# Example usage:
if __name__ == "__main__":
    user_input = input("Enter numbers separated by commas e.g. 7,14,11,8,9: ")
    arr = [int(x.strip()) for x in user_input.split(",")]
    print(f"Original array: {arr}")
    quick_sort(arr, 0, len(arr) - 1)
    print(f"\nSorted array: {arr}")
