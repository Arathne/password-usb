# sorts file
#
if __name__ == '__main__':
    data = []

    with open('./.password', 'r') as passwordFile:
        for line in passwordFile:
            data.append(line)
    
    data.sort()
    
    with open('./.password', 'w') as passwordFile:
        output = ''
        for line in data:
            output += line
        
        print(output)
        passwordFile.write(output)
