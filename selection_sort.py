def selection_sort(arr):
    n = len(arr)
    print(f"Original array: {arr}")
    for i in range(n):
        min_index = i
        print(f"\nPass {i + 1}:")
        for j in range(i + 1, n):
            print(f"  Comparing {arr[min_index]} and {arr[j]}", end=' ')
            if arr[j] < arr[min_index]:
                min_index = j
                print("=> new minimum found")
            else:
                print("=> no change")
        if min_index != i:
            print(f"  Swapping {arr[i]} and {arr[min_index]}")
            arr[i], arr[min_index] = arr[min_index], arr[i]
        else:
            print(f"  No swap needed for index {i}")
        print(f"  Array after pass {i + 1}: {arr}")
    print(f"\nSorted array: {arr}")


# Example usage:
if __name__ == "__main__":
    user_input = input("Enter numbers separated by commas e.g. 7,14,11,8,9: ")
    arr = [int(x.strip()) for x in user_input.split(",")]
    selection_sort(arr)
