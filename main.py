def hanoi_solver(n):
    # Initialize the three rods
    rod_1 = list(range(n, 0, -1))
    rod_2 = []
    rod_3 = []
    
    # Store the initial state of the rods
    states = [f"{rod_1} {rod_2} {rod_3}"]
    
    def move_disk(source, target):
        # Pop from the source rod and append to the target rod
        disk = source.pop()
        target.append(disk)
        # Record the updated state of all three rods
        states.append(f"{rod_1} {rod_2} {rod_3}")

    def solve(disks, source, target, auxiliary):
        if disks == 1:
            move_disk(source, target)
            return
        
        # Move top n-1 disks from source to auxiliary rod
        solve(disks - 1, source, auxiliary, target)
        # Move the largest remaining disk from source to target rod
        move_disk(source, target)
        # Move the n-1 disks from auxiliary to target rod
        solve(disks - 1, auxiliary, target, source)

    # Begin the recursive puzzle solution moving from rod_1 to rod_3
    solve(n, rod_1, rod_3, rod_2)
    
    # Return all moves joined by a newline character
    return "\n".join(states)
