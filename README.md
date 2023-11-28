# Educational Ransomware Simulation

## Overview
This repository contains two Python scripts for simulating ransomware encryption and decryption processes for educational purposes. The `ransom.py` script encrypts files in its directory, while `ransomdecrypter.py` decrypts them. This simulation is designed to provide practical insights into how ransomware operates and to enhance understanding of file encryption and decryption.

**Disclaimer:** This code is strictly for educational purposes. Creating, distributing, or using ransomware for malicious purposes is illegal and unethical.

## Requirements
- Python 3
- `cryptography` Python library

To install the required library, run: `pip install cryptography`

## Files
1. `ransom.py` - Encrypts files in its directory.
2. `ransomdecrypter.py` - Decrypts files encrypted by `ransom.py`.
3. `generatedkey.key` - Stores the encryption key (created by `ransom.py`).

## Usage

### Encryption
1. Place the `ransom.py` script in a directory with files you wish to encrypt.
2. Run the script: `python3 ransom.py`
3. Encrypted files and the `generatedkey.key` will be generated in the same directory.

### Decryption
1. Ensure `ransomdecrypter.py` and `generatedkey.key` are in the same directory as the encrypted files.
2. Run the script: `python3 ransomdecrypter.py`
3. Files will be decrypted and restored to their original state.

## Important Note
- Use this script only in a controlled, secure environment and never on personal, sensitive, or critical files.
- The author is not responsible for any misuse of this educational tool or any damage incurred.

## Recommended Courses
Enhance your knowledge in ethical hacking and cybersecurity with these Udemy courses:
1. [Etik Hacker Olma Kursu](https://www.udemy.com/course/etik-hacker-olma-kursu/) - Learn the latest tools and software in ethical hacking with practical examples.
2. [Etik Hacker Olma Kursu - Seviye 2 : Ağ İçi Saldırılar](https://www.udemy.com/course/etik-hacker-olma-kursu-seviye-2-ag-ici-saldirilar/) - Discover how ethical hackers execute network attacks and write their own attacks using the latest techniques.
3. [Python : Sıfırdan İleri Seviyeye - Etik Hacker Örnekleriyle](https://www.udemy.com/course/python-sifirdan-ileri-seviyeye/) - Master Python from beginner to advanced level with ethical hacking examples.
4. [Etik Hacker Olmak: Web Sızma Testleri ve Bug Bounty](https://www.udemy.com/course/web-pentesting/) - Learn Web Penetration Testing & Bug Bounty operations with hundreds of different examples using the latest technology tools.
5. [Etik Hacker İleri Seviye: Sızma Testleri & Yetki Yükseltme](https://www.udemy.com/course/sizma-testleri/) - Advance your journey as a Cybersecurity Expert with Penetration Testing and Privilege Escalation Techniques.