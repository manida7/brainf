# Makefile for running the Brainfuck scanner program

# Variables
PYTHON = python
SCRIPT = brainfuck_scanner.py
INPUT = input3.bf
OUTPUT = output0.txt

# Default target: Run the program
run:
	@$(PYTHON) $(SCRIPT) $(INPUT)

# Clean target: Remove the output file
clean:
	@rm -f $(OUTPUT)

# Help target: Display usage information
help:
	@echo "Makefile Usage:"
	@echo "  make run    - Run the Brainfuck scanner with the default input file ($(INPUT))"
	@echo "  make clean  - Remove the output file ($(OUTPUT))"
	@echo "  make help   - Display this help message"
