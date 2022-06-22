# to pass multiple data
def person(name, **data):

    print(name)
    print(data)

    for i ,j in data.items():
        print(i,j)

person("nikhil",age="24",location="Mangalore")