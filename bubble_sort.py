def bubble_sort(arr):
    n = len(arr)
    print(f"Original array: {arr}")
    for i in range(n):
        swapped = False
        print(f"\nPass {i + 1}:")
        for j in range(0, n - i - 1):
            print(f"  Comparing {arr[j]} and {arr[j+1]}", end=' ')
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f"=> swapped => {arr}")
            else:
                print("=> no change")
        if not swapped:
            print("  No swaps in this pass, array is sorted.")
            break
    print(f"\nSorted array: {arr}")


# Example usage:
if __name__ == "__main__":
    # You can change the array below to test with different inputs
    user_input = input("Enter numbers separated by commas e.g. 7,14,11,8,9: ")
    arr = [int(x.strip()) for x in user_input.split(",")]
    bubble_sort(arr)
