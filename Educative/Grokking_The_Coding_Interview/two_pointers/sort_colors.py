"""
"""

def sort_colors(colors):

    left, center, right = 0, 0, len(colors) - 1

    while center <= right:
        if colors[center] == 1:
            center += 1
        elif colors[center] < 1:
            colors[left], colors[center] = colors[center], colors[left]
            left += 1
            center += 1
        else:
            colors[right], colors[center] = colors[center], colors[right]
            right -= 1
    return colors


# Driver code
def main():
    inputs = [[0, 1, 0], [1, 1, 0, 2], [2, 1, 1, 0, 0], [2, 2, 2, 0, 1, 0], [2, 1, 1, 0, 1, 0, 2]]

    # Iterate over the inputs and print the sorted array for each
    for i in range(len(inputs)):
        print(i + 1, ".\tcolors:", inputs[i].copy(),
              "\n\n\tThe sorted array is:", sort_colors(inputs[i]))
        print("-" * 100)

if __name__ == "__main__":
    main()