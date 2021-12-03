def check_depth(filename):
    with open(filename) as file:
        depth_increase = 0
        last = int(next(file).strip())
        for line in file:
            if last < int(line.strip()):
                depth_increase += 1
            last = int(line.strip())

    return depth_increase

def main():
    print(check_depth(".\problem_1\problem_1.txt"))

main()