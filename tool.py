import yaml

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def filter_items(data, include_tags=["basic"], exclude_tags=[]):
    include_tags = set(include_tags)
    exclude_tags = set(exclude_tags)

    return [
            item for item in data
            if include_tags.issubset(set(item['tags'].split(', '))) and not exclude_tags.intersection(set(item['tags'].split(', ')))
    ]

def sort_items_alpha(data):
    sorted_items = sorted(data, key=lambda x: x['name'])
    return sorted_items

class item:
    def __init__(self, name, stuff=[], weight=None):
        self.name = name
        self.stuff = stuff
        self.weight = weight

    def add(self, item):
        self.stuff += item

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

print(total_weight(edc))


