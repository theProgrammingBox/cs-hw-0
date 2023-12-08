def mid_coverage(x, y, z):
    """
    Function to determine the path and branches taken in the mid function for given x, y, z.
    Returns the list of statement numbers executed and branches taken.
    """
    executed_lines = []
    branches_taken = []
    
    m = z
    executed_lines.append(1)
    
    if y < z:
        executed_lines.append(2)
        branches_taken.append('2T')
        if x < y:
            executed_lines.append(3)
            branches_taken.append('3T')
            m = y
            executed_lines.append(4)
        elif x < z:
            executed_lines.append(5)
            branches_taken.append('5T')
            m = x
            executed_lines.append(6)
        else:
            branches_taken.append('3F')
            branches_taken.append('5F')
    else:
        executed_lines.append(7)
        branches_taken.append('2F')
        if x > y:
            executed_lines.append(8)
            branches_taken.append('8T')
            m = y
            executed_lines.append(9)
        elif x > z:
            executed_lines.append(10)
            branches_taken.append('10T')
            m = x
            executed_lines.append(11)
        else:
            branches_taken.append('8F')
            branches_taken.append('10F')

    executed_lines.append(12)
    return executed_lines, branches_taken

# Main loop to receive inputs and display results
while True:
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    z = int(input("Enter z: "))
    executed_lines, branches_taken = mid_coverage(x, y, z)
    print("Executed lines: ", executed_lines)
    print("Branches taken: ", branches_taken)
