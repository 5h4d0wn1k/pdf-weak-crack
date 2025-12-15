# PDF Weak Password Cracker

⚠️ **EDUCATIONAL PURPOSE ONLY** - This tool is designed for authorized security testing and educational purposes. Only use on PDF files you own or have explicit written authorization to test.

## Overview

A PDF password cracking tool that attempts to crack weak passwords using wordlists. Designed for security audits and educational purposes to demonstrate the importance of strong passwords.

## Features

- **Wordlist-Based Cracking**: Uses wordlists to attempt password cracking
- **Weak Password Detection**: Demonstrates vulnerability of weak passwords
- **Educational**: Learn about password security and PDF encryption
- **Simple Interface**: Easy-to-use command-line tool

## Installation

### Requirements

- Python 3.8+
- PyPDF2 library

### Setup

```bash
# Clone the repository
git clone https://github.com/5h4d0wn1k/pdf-weak-crack.git
cd pdf-weak-crack

# Install dependencies
pip install PyPDF2

# Verify installation
python pdf_weak_crack.py --help
```

## Usage

### Basic Usage

```bash
# Attempt to crack PDF password
python pdf_weak_crack.py \
  --pdf protected.pdf \
  --wordlist passwords.txt
```

## Command-Line Options

| Option | Description |
|--------|-------------|
| `--pdf` | Protected PDF file (required) |
| `--wordlist` | Password wordlist file (required) |

## Wordlist Format

The wordlist file should contain one password per line:

```
password
123456
admin
letmein
password123
SecurePassword123!
```

## Output Format

```
⚠️  Authorized use only. Crack only PDFs you own/control.
[*] Trying password: password
[*] Trying password: 123456
[+] Password found: password123
```

## Examples

### Example 1: Basic Cracking

```bash
# Crack PDF with wordlist
python pdf_weak_crack.py \
  --pdf protected.pdf \
  --wordlist common_passwords.txt
```

### Example 2: Using Large Wordlist

```bash
# Use comprehensive wordlist
python pdf_weak_crack.py \
  --pdf protected.pdf \
  --wordlist rockyou.txt
```

## Security Implications

This tool demonstrates:
- **Weak Passwords**: Easy to crack with wordlists
- **Password Strength**: Importance of strong, unique passwords
- **Brute Force**: How attackers attempt to crack passwords

## Password Security Best Practices

1. **Length**: Use at least 12 characters (preferably 16+)
2. **Complexity**: Include uppercase, lowercase, numbers, and symbols
3. **Uniqueness**: Don't reuse passwords
4. **Avoid Common Patterns**: Don't use dictionary words or common patterns

## Use Cases

- **Security Audits**: Test password strength of protected PDFs
- **Penetration Testing**: Authorized security assessments
- **Educational Purposes**: Learn about password security and cracking
- **Password Policy Testing**: Verify password policies are effective

## Legal Disclaimer

⚠️ **IMPORTANT**: This tool is for authorized security testing and educational purposes only.

- Only crack PDFs you own or have explicit written authorization to test
- Never use on PDFs you don't own
- Follow responsible disclosure practices
- Comply with all applicable laws and regulations

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is for educational purposes only. Use responsibly and ethically.

---

**Remember**: Only use on PDFs you own or have explicit authorization to test!
