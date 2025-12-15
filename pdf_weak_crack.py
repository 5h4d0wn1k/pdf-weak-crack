"""
PDF weak password audit (lab PDFs only).
Uses a small wordlist to attempt opening a password-protected PDF.
Requires PyPDF2.
"""

from __future__ import annotations

import argparse
import sys
from typing import List, Optional


def load_words(path: str) -> List[str]:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return [line.strip() for line in f if line.strip()]


def try_open(pdf_path: str, passwords: List[str]) -> Optional[str]:
    try:
        from PyPDF2 import PdfReader  # type: ignore
    except Exception:
        print("PyPDF2 not installed. pip install PyPDF2", file=sys.stderr)
        sys.exit(1)

    reader = PdfReader(pdf_path)
    if not reader.is_encrypted:
        return "no_password"
    for pwd in passwords:
        if reader.decrypt(pwd):
            return pwd
    return None


def main() -> None:
    parser = argparse.ArgumentParser(description="PDF weak password audit (lab PDFs only).")
    parser.add_argument("--pdf", required=True, help="Protected PDF path.")
    parser.add_argument("--wordlist", required=True, help="Small wordlist to try.")
    args = parser.parse_args()

    print("⚠️  Authorized use only. Audit only PDFs you own/control.")
    words = load_words(args.wordlist)
    hit = try_open(args.pdf, words)
    if hit == "no_password":
        print("[-] PDF is not password protected.")
    elif hit:
        print(f"[+] Password found: {hit}")
    else:
        print("[-] No password found in provided list.")


if __name__ == "__main__":
    main()
