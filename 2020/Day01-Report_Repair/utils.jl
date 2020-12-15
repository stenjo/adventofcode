# Multiply all items of a list (array) 
# with each other and return product
function multiplyArray(list)
    product = 1
    for i in list
        product = product * i
    end
    product
end
