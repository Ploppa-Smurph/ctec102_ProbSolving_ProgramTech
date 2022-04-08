#pickle ex: save and load
import pickle

example_dict={1:2, "hello": "world"}
example_list=['joker says ha', 'batman says grrrr', 'superman says hello']

# wb is writing binary
# in save the function takes an argument
def save(x):
    filename= input('enter a name for the save file, with NO extension: ')
    f = open(filename+'.dat', 'wb')  ## take string 'filename' and concatenate with '.dat'
    pickle.dump(x,f)
    f.close()

# rb is reading binary
# in load the function returns an arugument (from a created and named variable we create)
def load():
    filename= input('enter a filename to load with NO extension: ')
    f = open(filename+'.dat', 'rb')
    x=pickle.load(f)
    f.close()
    return x

## for the final we will have to set a variable equal to load() and call that variable
