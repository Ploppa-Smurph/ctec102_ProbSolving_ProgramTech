# compute_area(shape) is a function which calls on of the
# circle(), rectangle(), square(),triangle()
# each function asks for appropriate variables to compute
#the answer and display it
  
def compute_area(shape):
    if shape=='circle':
        area=circle()
    #elif other cases    
    return area    



def circle():
    import math
    radius=float(input('enter the radius of the circle'))
    area= math.pi*radius**2
    return area
    
def rectangle():
    pass
    #area =length*width
    
def  square():
    #area=length**2
    pass
def triangle():    
    #area=base*height/2
    pass
def display_results(shape, area):
    pass

def valid_input():
    pass
