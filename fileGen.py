import os

def convert_size_to_bytes(size, unit):
    units = {
        'b': 1,
        'kb': 1024,
        'mb': 1024 * 1024,
        'gb': 1024 * 1024 * 1024
    }
    return int(size * units[unit.lower()])

def generate_file(file_name, size, unit):
    size_bytes = convert_size_to_bytes(size, unit)
    with open(file_name, 'wb') as f:
        f.write(os.urandom(size_bytes))
    print(f'File "{file_name}" of size {size} {unit.upper()} ({size_bytes} bytes) has been created.')
    print(f'Output file path: {os.path.abspath(file_name)}')

def print_instructions():
    print("Instructions:")
    print("1. Enter the file name you want to create.")
    print("2. Enter the size of the file.")
    print("3. Enter the unit of the size (b for bytes, kb for kilobytes, mb for megabytes, gb for gigabytes).")

if __name__ == "__main__":
    print_instructions()
    
    file_name = input("Enter the file name: ")
    size = float(input("Enter the size of the file: "))
    unit = input("Enter the unit (b, kb, mb, gb): ").strip().lower()
    
    if unit not in ['b', 'kb', 'mb', 'gb']:
        print("Invalid unit. Please enter one of the following units: b, kb, mb, gb.")
    else:
        generate_file(file_name, size, unit)

