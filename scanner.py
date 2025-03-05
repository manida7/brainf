import sys


def brainfuck_scanner(file_path):
    valid_commands = {'>', '<', '+', '-', '.', ',', '[', ']'}
    output_lines = []

    try:
        with open(file_path, 'rb') as file:
            while True:
                byte = file.read(1)
                if not byte: 
                    break
                char = byte.decode('utf-8', errors='ignore')

                if char in valid_commands:
                    output_lines.append(f'term: "{char}"')
                elif char.strip() == '': 
                    continue
                else:
                    output_lines.append(
                        f'"{char}": error, invalid term')

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    with open('output0.txt', 'w') as output_file:
        for line in output_lines:
            output_file.write(line + '\n')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scanner.py input.bf")
    else:
        brainfuck_scanner(sys.argv[1])
