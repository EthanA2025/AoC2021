def rates(filename):
    espilon = ""
    counter = 0
    gamma = ""
    with open(filename) as file:
        content = file.readlines()
        bits = len(content[0]) - 1 # Gets number of bits in the file that each line has
        while counter < bits: # While counter is less than bits, the number of bits in a line
            zeros = 0
            ones = 0 # reset variables 
            with open(filename) as file:
                for line in file:
                    line = line.strip().split() # line formatting
                    for num in line:
                        if num[counter] == '1':
                            ones += 1
                        else:
                            zeros += 1 # For each line in the file if the number at counter is 1 then add 1 to our binary number output
                if zeros > ones: # if there are more zeros then add 0 to our binary number we will convert, for espillon do the oppositer
                    gamma += "0"
                    espilon += "1"
                else:
                    gamma += "1"
                    espilon += "0"

                counter += 1

        decimal = 0 # converting binary to decimal 
        for num in gamma:
            decimal = decimal*2 + int(num)
        dec = 0
        for n in espilon:
            dec = dec*2 + int(n)
    
    return decimal * dec # Multiply gamma and espillon decimal values

#----------part 2---------#


def main():
    print(rates("puzzle.txt"))

if __name__ == "__main__":
    main()