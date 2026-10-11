# 🔐 Password Strength Checker

A Python command-line application that checks password characteristics and suggests improvements.

## ✨ Features

- Check password length
- Check uppercase and lowercase letters
- Check numeric and special characters
- Detect long repeated-character sequences
- Display a strength category and improvement suggestions
- Hide password input in supported terminals

## 🛠️ Technologies

- Python
- Regular expressions (`re`)
- String processing (`string`)
- `getpass`

## 📂 Project Structure

```text
python-password-strength-checker/
├── main.py
├── password_checker.py
└── README.md
```

## 🚀 How to Run

1. Open a terminal in the project folder.
2. Run:

```bash
python main.py
```

3. Enter a test password when prompted.

## ⚙️ How It Works

The checker evaluates six conditions: length, uppercase letters, lowercase letters, digits, special characters, and repeated-character sequences. It counts the conditions passed and provides suggestions for failed checks.

## 📚 Concepts Learned

- Python functions and modules
- String methods and character checks
- Regular expressions
- Dictionaries and Boolean values
- List comprehensions
- Secure input handling with `getpass`

## ⚠️ Limitations

This educational checker uses a simple checklist. It does not detect breached passwords, estimate guessing time, or guarantee security. Do not enter real passwords into unfamiliar or untrusted programs.

## 👨‍💻 Author

Ayushman Tiwari

GitHub: https://github.com/ayushman-ece

---

*Built as a hands-on Python learning project.*