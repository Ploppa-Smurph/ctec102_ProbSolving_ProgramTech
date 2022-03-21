# open() with error handling
file_name= input('enter the file name with extension: ')
try:
    f=open(file_name, 'r')
    print(f.read())
    f.close()
except FileNotFoundError as var_err:
    print('File not found;', var_err)
