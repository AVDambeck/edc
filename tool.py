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

yaml = load_yaml("stuff.yml")


