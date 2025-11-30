import yaml

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

edc = load_yaml("stuff.yml")

def total_weight(yaml):
    weight = 0
    for i in yaml.keys():
        var = yaml[i]
        if type(var) is int:
            weight += var
        else:
            weight += total_weight(var)
    return(weight)

def list_items_by_weight(yaml):
    itemSet = set()
    for i in yaml.keys():
        var = yaml[i]
        if type(var) is int:
            itemSet.add((str(i), var))
        else:
            itemSet = itemSet.union(list_items_by_weight(var))
    sortedSet = sorted(itemSet, key=lambda x: x[1])
    return(sortedSet)

ls = list_items_by_weight(edc)
for i in ls:
    print(i)

