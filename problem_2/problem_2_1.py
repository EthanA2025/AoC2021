# Depending on what direction given at that line the horizontal and vertical values change
# Up decreases vertical while Down increases vertical, fowards always increases horizontal 

def dive(filename):
    horizontal = 0
    vertical = 0
    with open(filename) as file:
        for line in file:
            splt = line.lower().split()    
            if splt[0] == 'up':
                vertical -= int(splt[1]) # Takes split line and sees what operation it must do
            elif splt[0] == 'down':
                vertical += int(splt[1])            
            elif splt[0].lower() == 'forward':
                horizontal += int(splt[1])
    
    return horizontal * vertical

def main():
    print(dive("puzzle_2.txt"))

if __name__ == "__main__":
    main()