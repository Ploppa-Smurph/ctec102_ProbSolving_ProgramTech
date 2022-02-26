# Bakery Project from Bill Barry Youtube -- link to part01: https://www.youtube.com/watch?v=yj5wzfSO_rs&list=PLrCtLWOL70NSmuUs4D0jzOJr3yQ1jSRBw&index=17

# customer enters # of pies they wish to order and the order is formatted for display
# calculate order based on quantity totals for pie or cake; price per pie ($17.99) and price per cake ($24.99)
# calculates tax of 9.5% - display order summary with totals and tax

#call Hierarchy== Main -> will call: Input order Data; Price order, Display summary.
# Price order will call: -> Price pie; Price Cakes; Calculate Tax; Calculate Total

# - annotate the Hierarchy and find out what DATA each Function needs to complete it's job
# our input order data will not need any data from Main, but it is important that it 'Returns' it's inputted data back to Main so the program can work properly
# Price order needs the cake and pie count from Main, then Price Order will pass that information on for pricing
# price pies receives # of pies from Price Order and 'returns' the total pie price 
# price cakes receives the # of cakes from Price Order and returns the total cake price
# Calculate Tax then receives the current price order <sub-total> (including the current pie and cake count) and calculates tax based on that subtotal - the tax is returned to price order
# Calculate Total receives the price total of pies, price total of cakes, and tax total and calculates the total order and returns the total to Price Order
# Price Order Returns information to Main
# Main calls Display Summary and delivers the pie quantity and price, the cake quantity and price, the tax, and the order total to display as a void function - it outputs and returns nothing.

#when we pass the information to the function we do that as parameters

#declare Constants pie and cake price as variables for ease later
#------------------------------------------------------------------------------
# CONSTANTS
#-------------------------------------------------------------------------------
PIE_PRICE = 17.99
CAKE_PRICE = 24.99
TAX_RATE = .095

#------------------------------------------------------------------------------
# MAIN
#-------------------------------------------------------------------------------
def main():
    numPies, numCakes = inputOrderData() # can set multiple variables to store values, which is unique to python, unlike most other languages, is storing pieCount and cakeCount as numPies and numCakes
    piePrice, cakePrice, orderSubtotal, orderTax, orderTotal = priceOrder(numPies, numCakes)
    displaySummary(numPies, numCakes, piePrice, cakePrice, orderSubtotal, orderTax, orderTotal)

#------------------------------------------------------------------------------
# INPUT
#-------------------------------------------------------------------------------    
# inputOrderData function
def inputOrderData():  # no parameters because there is no input from main
    pieCount = int(input('How many pies in the order? '))
    cakeCount = int(input('How many cakes?'))
    return pieCount, cakeCount  

#------------------------------------------------------------------------------
# CALCULATIONS
#-------------------------------------------------------------------------------
#priceOrder function which has sub-functions that it calls upon
def priceOrder(pieCount, cakeCount):
    pieTotal = pricePies(pieCount)
    cakeTotal = priceCakes(cakeCount)
    subTotal = pieTotal + cakeTotal  # simple calculation to find subtotal 
    tax = calcTax(subTotal)
    total = calcTotal(subTotal, tax)
    return pieTotal, cakeTotal, subTotal, tax, total
    
#pricePies function    
def pricePies(pieCount): 
    pieTotal = round(pieCount * PIE_PRICE, 2)
    return pieTotal

#priceCakes function    
def priceCakes(cakeCount):
    cakeTotal = round(cakeCount * CAKE_PRICE, 2)
    return cakeTotal

#calcTax function
def calcTax(subTotal):
    tax = round(subTotal * TAX_RATE, 2)  # round to 2 digits
    return tax

#calcTotal function    
def calcTotal(subtotal, tax):
    total = round(subtotal + tax, 2)
    return total

#------------------------------------------------------------------------------
#  DISPLAY
#-------------------------------------------------------------------------------
#displaySummary function  -- void function - no return  
def displaySummary(numPies, numCakes, pieTotal, cakeTotal, subTotal, tax, total):  
    print('*'*60)
    print('Beth''s Bakery Order Summary\n')    # return extra space
    print('Item            ', 'Count', format('Price',         '>8s'))   # format the price to show the difference of how formatting works -- right allign with >
    print('----------------', '-----', '-----')   
    print('Number of Pies: ', format(numPies, '5d'), format(pieTotal, '>8,.2f'))  # formatting so the numPies cell always takes '5 digits'  and the pieTotal has floating point decimal  
    print('Number of Cakes:', format(numCakes, '5d'), cakeTotal) 
    print('----------------', '-----', '-----')    
    print('Subtotal:       ', '     ', subTotal)    
    print('Tax:            ', '     ', tax)  
    print('                ', '     ', '-----') 
    print('the Total is:   ', '     ', total)  
    print('*'*60 )
    
# call main to execute the program
main()                  
