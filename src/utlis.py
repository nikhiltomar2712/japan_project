def load_yaml(file_path):
    import yaml
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def save_yaml(data, file_path):
    import yaml
    with open(file_path, 'w') as file:
        yaml.dump(data, file)

def format_place_name(place_name):
    return place_name.title()  # Capitalizes each word in the place name

def calculate_distance(coord1, coord2):
    from geopy.distance import geodesic
    return geodesic(coord1, coord2).kilometers

def is_valid_coordinate(coord):
    return isinstance(coord, (list, tuple)) and len(coord) == 2 and all(isinstance(x, (int, float)) for x in coord)
