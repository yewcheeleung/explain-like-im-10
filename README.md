\# Explain Like I'm 10 🧸🧠



This is a Python project that takes a \*\*complicated sentence\*\* and explains it \*\*in simple language, like you're 10 years old\*\*.



It uses an AI model (a FLAN-T5 text-to-text model) from Hugging Face to rewrite text in a simpler way.



---



\## 🌟 What this project does



\- You type in a sentence or paragraph that is hard to understand  

\- The program sends it to an AI model  

\- The AI replies with a version that is:

&nbsp; - Simpler

&nbsp; - Shorter

&nbsp; - Easier to understand (like explaining to a 10-year-old)



Example:



> Input: "Explain quantum computing."  

> Output: "Quantum computers are special machines that can try many answers at once, so they can solve some problems much faster than normal computers."



---



\## 🧩 How it works (in simple terms)



1\. The program loads a \*\*pre-trained FLAN-T5 model\*\* from Hugging Face  

2\. It adds a prompt like:  

&nbsp;  > "Explain this like I'm 10 years old: \\<your text\\>"  

3\. The model generates a new sentence / paragraph  

4\. The program prints the AI’s answer to your screen



---



\## 📁 Project structure (example)



Your folder might look like this:



```text

explain-like-im-10/

├─ main.py                # Main Python file that runs the program

├─ requirements.txt       # Python packages needed for this project

└─ README.md              # This file



