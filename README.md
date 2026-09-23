> **⚠️ EDUCATIONAL USE ONLY — AUTHORIZED TESTING ONLY.**
> This project exists for education, research, and **defense of systems you own
> or hold explicit written authorization to assess**. Unauthorized use is
> prohibited and may be illegal. Read [ETHICS.md](ETHICS.md) and
> [SCOPE.md](SCOPE.md) before use. Use at your own risk; **AS IS**, no warranty.

# PDF Weak Crack

![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)
![GitHub Stars](https://img.shields.io/github/stars/5h4d0wn1k/pdf-weak-crack)
![Last Commit](https://img.shields.io/github/last-commit/5h4d0wn1k/pdf-weak-crack)
![GitHub Issues](https://img.shields.io/github/issues/5h4d0wn1k/pdf-weak-crack)

> **PDF weak password cracker for authorized security testing and education** —
> a wordlist-driven audit tool that tests password-protected PDFs against
> candidate passwords using PyPDF2.

## Why

PDF documents are routinely "protected" with weak, dictionary-word owner and
user passwords that offer a false sense of security. This tool demonstrates
that reality in a controlled, authorized way: it feeds a candidate wordlist to
`PyPDF2.PdfReader.decrypt()` and reports the first password that unlocks the
file. It exists so security teams and students can measure real-world PDF
password strength, prove why strong passphrases and modern encryption settings
matter, and validate DLP/document-protection policies — strictly on PDFs they own.

## Features

- **Wordlist-driven PDF audit** — `--pdf` + `--wordlist` (one candidate per
  line) until a hit or exhaustion.
- **Clear triage output** — reports `[+] Password found`,
  `[-] PDF is not password protected`, or `[-] No password found in list`.
- **Graceful dependency check** — exits cleanly with a hint if PyPDF2 is missing.
- **Minimal footprint** — small, focused CLI; Python 3.8+.

## Quickstart

```bash
pip install PyPDF2
python pdf_weak_crack.py --help

# Audit a protected lab PDF
python pdf_weak_crack.py --pdf protected.pdf --wordlist passwords.txt
```

`--pdf` and `--wordlist` are both required. Example wordlist format (one per
line): `password`, `123456`, `admin`, `letmein`, `password123`.

## Project structure

```
pdf_weak_crack.py   # CLI + PDF audit engine (PyPDF2)
requirements.txt    # PyPDF2 dependency
ETHICS.md           # ethics/authorized-use policy (read first)
SCOPE.md            # defined assessment scope
```

## Documentation

- [ETHICS.md](ETHICS.md) — ethical-use policy, read first
- [SCOPE.md](SCOPE.md) — authorized-scope definition
- [CONTRIBUTING.md](CONTRIBUTING.md) — how to contribute
- [SECURITY.md](SECURITY.md) — vulnerability reporting
- [CHANGELOG.md](CHANGELOG.md) — version history

## Contributing

Wordlist tooling, PDF-encryption analysis, and reporting improvements are
welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT — see [LICENSE](LICENSE).