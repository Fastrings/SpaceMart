import json, uuid, random

dict = {
    "products": []
}

for i in range(1000):
    product = {
        "reference": str(uuid.uuid4()),
        "name": "name" + str(i),
        "brand": "brand" + str(i),
        "type": "type"  + str(i),
        "price": random.randint(0, 1000)
    }
    dict["products"].append(product)

with open('products.json', 'w') as file:
    json.dump(dict, file, indent=4)