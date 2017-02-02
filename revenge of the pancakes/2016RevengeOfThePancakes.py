# Problem B: Revenge of the Pancakes
# CodeJam 2016 Qualification
# By: Richard Salas Chavez

def main():
    input = open('B-large-practice.in','r')
    output = open('B-output-large.txt', 'w')

    test_cases = int(input.readline()) # number of test cases
    #print test_cases

    case = 1
    # loop through cases
    while(case <= test_cases):
        pancakes = input.readline().strip()
        #print case
        #print pancakes
        working = True
        moves = 0 # how many moves/flips need to be made

        while (working):
            print pancakes
            happy = 0

            # check how many pancakes are happy
            for c in pancakes:
                if c == '+':
                    happy += 1

            # if they are all happy then you're done
            if happy == len(pancakes):
                print pancakes
                output.write("Case #%i: %i\n" % (case, moves))
                break

            # special case: if the first pancake is happy look for the next
            # unhappy one
            if pancakes[0] == '+':
                parts = pancakes.split('+-', 1)
                print "%i parts" % len(parts)
                # if found
                if len(parts) > 1:
                    parts[0] += '+'
                    parts[1] = '-' + parts[1]
                pancakes = '-' * len(parts[0]) # flip pancakes
                moves += 1

            # if the first pancake is not happy then look for the first unhappy one
            else:
                parts = pancakes.split('-+', 1)
                print "%i parts" % len(parts)
                # if found
                if len(parts) > 1:
                    parts[0] += '-'
                    parts[1] = '+' + parts[1]
                pancakes = '+' * len(parts[0]) # flip pancakes
                moves += 1

            if len(parts) > 1:
                pancakes += parts[1]
            print
        case += 1

    input.close()
    output.close()

main()
