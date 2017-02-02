# Problem A: Counting Sheep
# CodeJam 2016 Qualification
# By: Richard Salas Chavez

path = "C:\Users\risal\PycharmProjects\codejam" # path of folder where this file is stored
digits = [0,1,2,3,4,5,6,7,8,9] # numbers the Bleatrix Trotter the sheep keeps track of

def main():
    input = open('A-large-practice.in','r') # input file
    output = open('output-large.txt', 'w')  # output file

    test_cases = int(input.readline())      # gets number of test cases

    case = 1

    while(case <= test_cases):
        digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        number = input.readline().strip()
        print "Input: %i" % int(number)

        # special case in which Bleatrix will never see any digit other than 0
        if int(number) == 0:
            output.write("Case #%i: " % case)
            output.write("INSOMNIA\n")
            case += 1

        else:
            i = 1           # start with 1 x N, the 2 x N
            working = True
            num = number    # N

            while working:
                #print num
                # iterate through every digit in the number
                # c for character
                # notice num is a string
                for c in num:
                    #print c
                    #check if any of the digits in the number has been seen before
                    for d in digits:
                        # if it has, then remove it from the list
                        if int(c) == int(d):
                            digits.remove(int(c))
                            break
                    # keep looping until Bleatrix has seen all digits
                    if len(digits) == 0:
                        # outputs last number Bleatrix will see before she falls asleep
                        working = False
                        output.write("Case #%i: " % case)
                        output.write(num + "\n")
                        print "Output: %s" % num
                        print
                        break
                i += 1
                num = str(int(number)*i)
            case += 1
    input.close()
    output.close()

main();
