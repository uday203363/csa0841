

def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
    else:
        tower_of_hanoi(n - 1, source, destination, auxiliary)
        
        print(f"Move disk {n} from {source} to {destination}")
          
        tower_of_hanoi(n - 1, auxiliary, source, destination)

num_disks = int(input("Enter the number of disks: "))

print("\nSteps to solve the Tower of Hanoi:\n")
tower_of_hanoi(num_disks, 'A', 'B', 'C')
