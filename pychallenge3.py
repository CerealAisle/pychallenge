file = open('C:\\Users\\hollmje\\Desktop\\chars4.txt')

def find_sequence(file):

    line = file.readline()
    sequence = ""
    
    while line != "":

        for index, letter in enumerate(line):

            # reached the end of a line or EOF
            if line == "":
                break
            elif line[index+9] == '\n':
                break
            
            # check for xXXXxXXXx pattern
            elif check_sequence(line[index:index + 9]):

                # found one
                print(line[index + 1:index + 8])
        
        line = file.readline()

    return sequence

def check_sequence(sequence):

    uppercase = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    lowercase = set('abcdefghijklmnopqrstuvwxyz')
    
    #print("checking %s...%s" % (sequence, sequence[0]))
    
    # if first char is not lowercase exit
    if sequence[0] in uppercase:
        return False

    # if next three characters are not uppercase, exit
    elif sequence[1] in lowercase:
        return False
    elif sequence[2] in lowercase:
        return False
    elif sequence[3] in lowercase:
        return False

    # if next character is not lowercase, exit
    elif sequence[4] in uppercase:
        return False

    # if next three characters are not uppercase, exit
    elif sequence[5] in lowercase:
        return False
    elif sequence[6] in lowercase:
        return False
    elif sequence[7] in lowercase:
        return False

    # if next character is not lowercase, exit
    elif sequence[8] in uppercase:
        return False
    else:
        return True

    
print(find_sequence(file))
file.close()
