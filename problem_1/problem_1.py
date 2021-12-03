def check_depth(filename):
    depth_increase = 0 
    with open(filename) as file:
        for line in file:
            print(line)

    return depth_increase

def main():
    check_depth("problem 1/problem1.txt")

main()