def check_depth(filename):
    with open(filename) as file:
        depth_increase = 0
        last = int(next(file).strip())
        for line in file:
            if last < int(line.strip()):
                depth_increase += 1 # If the last number in the file is less than the new one the depth increased so add 1 to the variable
            last = int(line.strip())

    return depth_increase

# Part 2

def check_sliding_depth(filename):
    with open(filename) as file:
        depth_increase = 0
        master_list = []
        for line in file:
            master_list.append(int(line.strip())) # For me it is easier to shove everything into a list
        for num in range(len(master_list) - 3):
            inital =  master_list[num] + master_list[num + 1] + master_list[num + 2] # Gets the first 3 indexes ex: 199, 200, 208 and adds them ex:607
            new = master_list[num + 1] + master_list[num + 2] + master_list[num + 3] # Gets the first 3 + 1 indexes ex: 200, 208, 210 ex: 618
            if inital < new:
                depth_increase += 1 # Compares new values ex: 607 < 618 so depth +1
            inital = new # test with the inital value now as the previous depth that was greater

    return depth_increase # returns count

def main():
    # print(check_depth("problem_1.txt"))
    print(check_sliding_depth("problem_1.txt"))

main()