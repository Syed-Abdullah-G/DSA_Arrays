def insertion_sort(arr):
    print(f"Original array: {arr}")
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        print(f"\nInserting {key} at the correct position")

        while j >= 0 and key < arr[j]:
            print(f"  {key} < {arr[j]} => shifting {arr[j]} to the right")
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

        print(f"  Placed {key} at index {j + 1}")
        print(f"  Array after pass {i}: {arr}")

    print(f"\nSorted array: {arr}")


# Example usage:
if __name__ == "__main__":
    user_input = input("Enter numbers separated by commas e.g. 7,14,11,8,9: ")
    arr = [int(x.strip()) for x in user_input.split(",")]
    insertion_sort(arr)
