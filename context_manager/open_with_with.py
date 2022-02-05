import os

if __name__ == '__main__':
    assets_path = os.path.dirname(__file__)
    filepath = os.path.join(assets_path, 'exercises', 'assets', 'test-file.txt')
    with open(filepath, 'w') as file:
        file.write('Ala ma kota')

