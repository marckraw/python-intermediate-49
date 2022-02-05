def load_data(filepath):
    with open(filepath) as in_file:
        return json.load(in_file)


def evaluate_attribute(attribute_value, expected_value, operator):
    if operator == 'eq':
        return attribute_value == expected_value
    if operator == 'gt':
        return attribute_value > expected_value
    if operator == 'lt':
        return attribute_value < expected_value
    return False
    # expression = f'{attribute_value} {operator} {expected_value}'
    # return eval(expression)


def search_data(data, attribute, value, operator='eq'):
    filtered_data = []

    for obj in data:
        if evaluate_attribute(
                attribute_value=obj.get(attribute),
                expected_value=value,
                operator=operator,
        ):
            filtered_data.append(obj)
    return filtered_data
    # return [obj for obj in data if obj.get(attribute) == value]