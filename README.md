[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/b3KS_NjW)
# 🧠 Brainfuck Scanner Assignment

## 📜 Overview
In this assignment, you will implement a **scanner (lexer)** for the Brainfuck programming language. The scanner should:
- Accept a **command-line argument file path**.
- Read the **Brainfuck source file byte by byte**.
- **Extract only the valid Brainfuck commands** (ignoring whitespace, comments, and invalid characters).
- **Continue scanning** even if an invalid token is encountered.
- Output **both valid and invalid tokens** in a structured format.
- **Write the output to `output0.txt`.**

---

## ❓ Help
If you're new to Brainfuck, here are some resources to help you understand the language:

- 📺 **Brainfuck Explained (YouTube Video)** – [Watch here](https://www.youtube.com/watch?v=hdHjjBS4cs8)  
- 🔗 **Brainfuck Online Interpreter** – [Try it here](https://copy.sh/brainfuck/)  

These resources will give you a solid understanding of **how Brainfuck works** and allow you to **test your programs online**.

---

## 📖 Brainfuck EBNF Grammar
The **Extended Backus-Naur Form (EBNF)** for Brainfuck is as follows:

```ebnf
program      ::= { command } ;
command      ::= ">" | "<" | "+" | "-" | "." | "," | "[" | "]" ;
```

### 🔍 Explanation:
- A **program** consists of **zero or more** (`{}`) `command`s.
- A **command** is one of the following:
  - `>`: Move the pointer to the right  
  - `<`: Move the pointer to the left  
  - `+`: Increment the byte at the pointer  
  - `-`: Decrement the byte at the pointer  
  - `.`: Output the byte at the pointer  
  - `,`: Input a byte and store it at the pointer  
  - `[`: Jump past the matching `]` if the byte at the pointer is `0`  
  - `]`: Jump back to the matching `[` if the byte at the pointer is **not** `0`  

---

## 🎯 Task
Your task is to write a **scanner (lexer)** that:
1. **Accepts a file path** as a command-line argument.
2. Reads the **Brainfuck source file byte by byte**.
3. **Extracts only the valid Brainfuck commands** (ignoring whitespace, comments, and invalid characters).
4. Outputs **valid tokens** in the following format:

   ```
   term:">"
   term:"+"
   term:"["
   term:"-"
   term:"]"
   ```

5. **Detects invalid characters** and reports them in the format:

   ```
   <invalid_token>: error, invalid term
   ```

   - The invalid token is prefixed with its **actual value** from the input.
   - **Scanning should continue** even after encountering an invalid token.

6. **Writes the output to `output0.txt`.**

---

## 🛠️ Steps to Complete the Assignment

### **📂 Step 1: Accept File Path from Command Line**
- The program should accept a file path as a **command-line argument**.
- Example usage:
  ```
  python brainfuck_scanner.py input.bf
  ```

### **📜 Step 2: Read the Input Byte by Byte**
- Open the file **in binary mode** to read **byte by byte**.
- Ensure the input is **not empty**.

### **🧮 Step 3: Tokenization**
- Scan the file **byte by byte**.
- Keep only the valid Brainfuck commands (`><+-.,[]`).
- Ignore **whitespace** and any other characters.

### **🚨 Step 4: Handle Invalid Tokens**
- If a character is **not** in `><+-.,[]`, print it in the format:

  ```
  <invalid_token>: error, invalid term
  ```

  - Example:
    ```
    2a: error, invalid term
    ```

- **The program should NOT stop execution** if an invalid token is encountered.

### **📝 Step 5: Format Tokens**
- For each valid Brainfuck command, output it in this format:

  ```
  term:"<command>"
  ```

  Example:
  ```
  term:">"
  term:"+"
  term:"["
  term:"-"
  term:"]"
  ```

### **📄 Step 6: Write to `output0.txt`**
- Write both **valid tokens** and **invalid token errors** into a file named **`output0.txt`**.

---

## 📥 Example Input Files

Below are three sample **Brainfuck programs** that contain both **valid and invalid** tokens.

### **📌 Example 1: Simple Brainfuck Program (Valid)**
#### **File: `input.bf`**
```brainfuck
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.
>++.<<+++++++++++++++.>.+++.------.--------.>+.>.
```
#### **📝 Expected Output (`output0.txt`)**
(Valid tokens in **Brainfuck format**)

---

### **📌 Example 2: Nested Loops (Mostly Valid)**
#### **File: `input2.bf`**
```brainfuck
[+[-->+<]>>.,] Python Code?
```
#### **📝 Expected Output (`output0.txt`)**
(Valid tokens and invalid character errors for non-Brainfuck text)

---

### **📌 Example 3: Invalid Characters Mixed with Valid Brainfuck**
#### **File: `input3.bf`**
```brainfuck
+?@> -a#b .%c
```
#### **📝 Expected Output (`output0.txt`)**
(Brainfuck tokens extracted, with errors for invalid characters)

---

## 🚀 **How to Run the Scanner**
1. Save one of the above Brainfuck programs as a file, e.g., `input.bf`.
2. Run the scanner using the command:
   ```
   python brainfuck_scanner.py input1.bf
   ```
3. The results will be written to `output0.txt`.

---

## 🔧 **Makefile**
- You should also provide a Makefile, which will specify how to compile or run your program.
- Please note that this part is also **VERY IMPORTANT**, so please make sure to submit your Makefile.

Good luck! 🚀
