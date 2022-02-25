#this is the main
#modify it to make it work
import area_module_starter
def main():
    
    #input validation function.
    # greets the user and asks for shape.if shape is not in ['triangle','rectangle','square','circle']
    #says that this shape is not implemented,asks again.
    shape=valid_input()

    #takes shape,asks aditional questions and returns the area 
    area=compute_area(shape)
    #Displays results 
    display_results(shape, area)

    
    
main()
