import yaml

def parse_config(path):
    with open(path, 'r') as file:
        if path.endswith('.yaml') or path.endswith('.yml'):
            return yaml.safe_load(file)
        else:
            raise ValueError("File format not supported yet")
