# sum - 1
data = (3, 5, 2, -5)

def sum_product(data):
    sum_result = 0
    product_result = 1
    
    for i in data:
        sum_result += i
        product_result *= i
    
    # Method 1
    print((sum_result, product_result))
    # Method 2
    x = (sum_result, product_result)
    print(x)

sum_product(data)


#sum - 2
def new_dict(fruits):
    result = {}
    for el in fruits:
        result[el["name"]] = {"color" : color, "type" : type}
        # name = el["name"]       
        # del el["name"]          
        # result[name] = el
    print(result)
    
new_dict(
    [{"name" : "apple", "color" : "red", "type" : "fruit"},
    {"name" : "banana", "color" : "yellow", "type" : "fruit"},
    {"name" : "grapes", "color" : "purple", "type" : "fruit"}]
    )