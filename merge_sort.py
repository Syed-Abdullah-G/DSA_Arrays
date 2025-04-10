def merge_sort(arr, depth=0):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        print("  " * depth + f"Dividing: {arr} -> {L} & {R}")
        merge_sort(L, depth + 1)
        merge_sort(R, depth + 1)

        i = j = k = 0

        print("  " * depth + f"Merging: {L} & {R}")
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                print("  " * depth + f"Placing {L[i]}")
                i += 1
            else:
                arr[k] = R[j]
                print("  " * depth + f"Placing {R[j]}")
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            print("  " * depth + f"Placing {L[i]}")
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            print("  " * depth + f"Placing {R[j]}")
            j += 1
            k += 1

        print("  " * depth + f"Result after merge: {arr}")


# Example usage
if __name__ == "__main__":
    user_input = input("Enter numbers separated by commas e.g. 7,14,11,8,9: ")
    arr = [int(x.strip()) for x in user_input.split(",")]
    print(f"Original array: {arr}")
    merge_sort(arr)
    print(f"\nSorted array: {arr}")
