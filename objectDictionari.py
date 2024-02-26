product = {
    "boys" : [1,2,3],
    "men" : {"name":"john"},
}

var_type = type(product)
var_producttype = type(product.get("sss"))
product["boys"].extend([4,5])

data = {
    "men" : {"name":"john"},
}

data.update({"name":"dddd"})

keys = list(data.keys())
values = data.values()

print(keys[0])