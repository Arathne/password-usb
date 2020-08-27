import random
import string



# generates password
#
def gen_password(length):
    password = ''
    regen = ''
    characters = string.ascii_letters + string.digits + string.punctuation

    while regen == 'Y' or regen == 'y' or regen == '':
        password = ''.join(random.choice(characters) for i in range(length))
        print('\n' + password)
        regen = input('regenerate? Y/n: ')

    return password



# gets integer input or exits program if invalid
#
def int_input(msg):
    number = input(msg)
    
    try: 
        number = abs(int(number))
    except:
        print('input a valid number')
        exit(-1)
    
    return number



# main program
#
if __name__ == '__main__':
    domain = input('domain: ')
    email = input('@: ')
    twoStep = input('two step auth? y/N: ')


    if twoStep == 'y' or twoStep == 'Y':
        password = 'two-step-authentication'
    else:
        length = int_input('length: ')
        password = gen_password(length)


    with open( './.password', 'a' ) as outputFile:
        outputFile.write( '{:<12} {:<12} {}\n'.format(domain, email, password) )
        print('\nsuccessfully appended to file')

