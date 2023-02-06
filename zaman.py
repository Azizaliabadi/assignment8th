def jam(t1 , t2):
    result = {}
    result["h"] = t1["h"] + t2["h"]
    result["m"] = t1["m"] + t2["m"]
    result["s"] = t1["s"] + t2["s"]
    if result["s"] >= 60:
        result["s"] -= 60
        result["m"] += 1
    if result["m"] >= 60:
        result["m"] -= 60
        result["h"] += 1
    if result["h"] > 23:
        result["h"] -= 24
    return result

def kam(t1 , t2):
    result = {}
    result["h"] = t1["h"] - t2["h"]
    result["m"] = t1["m"] - t2["m"]
    result["s"] = t1["s"] - t2["s"]
    if result["s"] >= 60:
        result["s"] -= 60
        result["m"] += 1
    if result["s"] < 0:
        result["s"] += 60
        result["m"] -= 1
    if result["m"] >= 60:
        result["m"] -= 60
        result["h"] += 1
    if result["m"] < 0:
        result["m"] += 60
        result["h"] -= 1
    if result["h"] > 23:
        result["h"] -= 24
    if result["h"] < 23:
        result["h"] += 24
    return result

def show(zaman):
    print(zaman["h"],":",zaman["m"],":",zaman["s"])
zaman1 = {"h":4,"m":30,"s":20}
zaman2 = {"h":20,"m":45,"s":40}
result_jam = jam(zaman1,zaman2)
result_kam = kam(zaman1,zaman2)
print("jam satha")
show(result_jam)
print("kame satha")
show(result_kam)