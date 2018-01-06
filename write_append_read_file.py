'''

var_name = open('file_name', intetion)
           'file_name' can be file_path

intention ---> 'w' = write
          ---> 'a' = append
          ---> 'r' = read



var_name.write(text_to_write)

var_name.close()


var_name = open('file-name', 'r').read()
        ---> reads whole file
var_name = open('file-name', 'r').readlines()
        ---> reads line by line (to a list)
    ---> no need to close file if reading (saves a list/string)
'''

writeMe = 'Sample Text to Save\nNew line!'

saveFile = open('exampleFile.txt','w')
saveFile.write(writeMe)
saveFile.close()

appendMe = '\nNew bit of information'

appendFile = open('exampleFile.txt', 'a')
appendFile.write(appendMe)
appendFile.close()


readMe = open('exampleFile.txt', 'r').read()
print(readMe)

readMe = open('exampleFile.txt', 'r').readlines()
print(readMe)
