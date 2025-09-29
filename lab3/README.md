**Assembly Reflections**

- We noticed that the registers arte very limited in numbers.
- Instructions are low-level, requiring explicit steps for simple tasks.

- Coding in assembly is different as it is very low level language and requires multiple lines of code to execute basic operations.
- Debugging assembly language is significantlty harder than python due to its syntax.


**Python Reflections**

- Python has built-in functions making programs easier to write and debug.
- No need to woory about register or memory management.

- *Variables:* Easily declared and reassigned.  
- *Functions:* Allow code reuse and modular design.  
- *Loops:* Handle repetition without manually managing jump instructions.  
- *Libraries:* Provide built-in support for I/O, math, etc.


**Comparison Table**

## 3. Comparison Table

| Feature             | Assembly Example       | Python Example              | Notes                                      |
|---------------------|------------------------|-----------------------------|--------------------------------------------|
| **Variable storage** | MOV AX, 5            | x = 5                     | Assembly uses registers; Python uses memory. |
| **Printing output**  | INT 21h               | print("Hello")            | Python abstracts away system-level details. |
| **Arithmetic**       | ADD AX, BX           | z = x + y                 | Assembly requires register ops, Python is direct. |
