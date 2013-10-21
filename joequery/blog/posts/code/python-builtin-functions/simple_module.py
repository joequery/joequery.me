import json

def myfn(mydict):
    return json.dumps(mydict)

def myfn2():
    return myfn({"x": 30})

print(myfn2())
