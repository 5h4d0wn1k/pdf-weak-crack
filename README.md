> **⚠️ EDUCATIONAL USE ONLY — AUTHORIZED TESTING ONLY.**
> This project exists for education, research, and **defense of systems you own
> or hold explicit written authorization to assess**. Unauthorized use is
> prohibited and may be illegal. Read [ETHICS.md](ETHICS.md) and
> [SCOPE.md](SCOPE.md) before use. Use at your own risk; **AS IS**, no warranty.
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
- **Security Awareness**: Educational tool for understanding password security

## Use Cases

- **Security Audits**: Test PDF password strength
- **Penetration Testing**: Authorized security assessments
- **Educational Purposes**: Learn about password security

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## ⚠️ Legal Disclaimer

### Educational Purpose Only
This tool is provided strictly for **educational purposes** and **authorized security testing** only. It is intended to help security professionals and students learn about security concepts in controlled environments.

### Authorized Use Only
- You must have **explicit written authorization** before testing any system you do not own
- Unauthorized access to computer systems is **illegal** and punishable under laws including but not limited to the Computer Fraud and Abuse Act (CFAA), Computer Misuse Act, and similar legislation worldwide
- Only use this tool on systems you own, have permission to test, or in isolated lab environments

### No Warranty
This software is provided "AS IS" without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. The author makes no representations or warranties regarding the accuracy, completeness, or reliability of this software.

### Limitation of Liability
**In no event shall the author (Nikhil Nagpure) be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.**

### User Responsibility
- The user assumes **full responsibility** for any consequences resulting from the use of this tool
- The author is **not responsible** for any misuse, damage, or illegal activities performed with this software
- Users are solely responsible for ensuring compliance with all applicable local, state, national, and international laws and regulations

### Indemnification
By using this software, you agree to **indemnify, defend, and hold harmless** the author from and against any and all claims, liabilities, damages, losses, costs, and expenses (including reasonable attorneys fees) arising from or related to your use of this software.

### Responsible Disclosure
If you discover vulnerabilities using this tool, please follow responsible disclosure practices and report them to the affected parties through appropriate channels.

---

**By using this software, you acknowledge that you have read, understood, and agree to be bound by this disclaimer.**
## License

This project is for educational purposes only. Use responsibly and ethically.

---

**Remember**: Always use strong passwords when protecting PDFs!
