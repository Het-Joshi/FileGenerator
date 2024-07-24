Here's a structured README for your `fileGen.py` script that you can use on GitHub:

```markdown
# File Generator

`fileGen.py` is a Python script that generates a file of a specified size. The size can be specified in various units, including bytes (b), kilobytes (kb), megabytes (mb), and gigabytes (gb). The script creates a file filled with random data and displays the output file path.

## Features

- Generates a file of a specified size.
- Supports size units: bytes (b), kilobytes (kb), megabytes (mb), and gigabytes (gb).
- Provides user-friendly instructions and takes input interactively.

## Requirements

- Python 3.x

## Usage

1. **Clone the repository** and navigate to the directory:

    ```sh
    git clone https://github.com/Het-Joshi/file-generator.git
    cd file-generator
    ```

2. **Run the script** using the command:

    ```sh
    python3 fileGen.py
    ```

3. **Follow the on-screen instructions**:
    - Enter the desired file name when prompted.
    - Enter the size of the file.
    - Enter the unit of the size (b for bytes, kb for kilobytes, mb for megabytes, gb for gigabytes).

### Example

```sh
python3 fileGen.py
```

**Terminal Output:**
```
Instructions:
1. Enter the file name you want to create.
2. Enter the size of the file.
3. Enter the unit of the size (b for bytes, kb for kilobytes, mb for megabytes, gb for gigabytes).

Enter the file name: example.txt
Enter the size of the file: 10
Enter the unit (b, kb, mb, gb): mb
File "example.txt" of size 10 MB (10485760 bytes) has been created.
Output file path: /path/to/example.txt
```

## Script Details

### `convert_size_to_bytes(size, unit)`

Converts the size from the specified unit to bytes.

**Parameters:**
- `size` (float): The size of the file.
- `unit` (str): The unit of the file size (b, kb, mb, gb).

**Returns:**
- `int`: The size of the file in bytes.

### `generate_file(file_name, size, unit)`

Generates a file of the specified size filled with random data.

**Parameters:**
- `file_name` (str): The name of the file to be created.
- `size` (float): The size of the file.
- `unit` (str): The unit of the file size (b, kb, mb, gb).

### `print_instructions()`

Prints the instructions for using the script.

## Error Handling

The script checks if the unit entered by the user is valid and prompts an error message if it is not.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to contribute to this project by creating issues or submitting pull requests. Your contributions are welcome!
```

### Adding the Script to the Repository
Make sure your repository includes the following files:
- `fileGen.py`: The Python script.
- `README.md`: The documentation file with the content above.
- `LICENSE`: Your chosen license file (e.g., MIT License).

### Example Repository Structure
```
file-generator/
│
├── fileGen.py
├── LICENSE
└── README.md
```

By following this structure, you'll have a well-documented repository that is easy for others to understand and use.