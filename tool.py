import yaml

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

edc = load_yaml("stuff.yml")

def list_weights(yaml):
    weights = []
    for i in yaml.keys():
        var = yaml[i]
        if type(var) is int:
            weights.append(var)
        else:
            weights += list_weights(var)
    return(weights)


def total_weight(yaml):
    return(sum(list_weights(yaml)))

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

print(total_weight(edc))
