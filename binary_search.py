def binary_search(arr, target):
    print(f"Searching for {target} in {arr}")
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        print(f"Checking middle index {mid}: {arr[mid]}")
        if arr[mid] == target:
            print(f"Found {target} at index {mid}")
            return mid
        elif arr[mid] < target:
            print(f"{arr[mid]} < {target}, searching right half")
            left = mid + 1
        else:
            print(f"{arr[mid]} > {target}, searching left half")
            right = mid - 1
    print(f"{target} not found in the array.")
    return -1


# Example usage
if __name__ == "__main__":
    user_input = input("Enter numbers separated by commas e.g. 7,14,11,8,9: ")
    arr = sorted([int(x.strip()) for x in user_input.split(",")])  # must be sorted
    target = int(input("Enter the number to search for: "))
    binary_search(arr, target)
