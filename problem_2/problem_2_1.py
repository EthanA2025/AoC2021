# Depending on what direction given at that line the horizontal and vertical values change
# Up decreases vertical while Down increases vertical, fowards always increases horizontal 

def dive(filename):
    horizontal = 0
    depth = 0
    with open(filename) as file:
        for line in file:
            splt = line.lower().split()    
            if splt[0] == 'up':
                depth -= int(splt[1]) # Takes split line and sees what operation it must do
            elif splt[0] == 'down':
                depth += int(splt[1])            
            elif splt[0] == 'forward':
                horizontal += int(splt[1])
    
    return horizontal * depth

# --------part 2-------------

def dive_accurate(filename, aim=0):
    horizontal = 0
    depth = 0
    with open(filename) as file:
        for line in file:
            splt = line.lower().split()    
            if splt[0] == 'up':
                aim -= int(splt[1]) # Takes split line and sees what operation it must do
            elif splt[0] == 'down': # Instead of adding to vertical 
                aim += int(splt[1])  
            elif splt[0] == 'forward':
                horizontal += int(splt[1])
                depth += aim * int(splt[1])       
            
    return horizontal * depth

def main():
    print(dive("puzzle_2.txt"))
    print(dive_accurate("puzzle_2.txt"))

if __name__ == "__main__":
    main()