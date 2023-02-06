
def zarb(f1,f2):
    result = {}
    result["s"] = f1["s"] * f2["s"]
    result["m"] = f1["m"] * f2["m"]
    return result
def jam(f1 , f2):
    result = {}
    result["s"] = (f1["s"])*f2["m"] + (f2["s"] * f1["m"])
    result["m"] = f1["m"] * f2["m"]
    return result
def kam(f1 ,f2):
    result = {}
    result["s"] = (f1["s"])*f2["m"] - (f2["s"] * f1["m"])
    result["m"] = f1["m"] * f2["m"]
    return result

def tagsim(f1 , f2):
    result = {}
    result["s"] = f1["s"] * f2["m"]
    result["m"] = f2["s"] * f1["m"]
    return result
a = {"s":2, "m":3}
b = {"s":5, "m":4}

zarb_result = zarbl(a ,b)
jam_result = jam(a ,b)
kam_result = kams(a ,b)
tagsim_result = tagsim(a ,b)
print("jam: ")
print(jam_result)
print("zarb: ")
print(zarb_result)
print("kam: ")
print(kam_result)
print("tagsim: ")
print(tagsim_result)