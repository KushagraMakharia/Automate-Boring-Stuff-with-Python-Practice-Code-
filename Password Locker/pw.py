#! python3

# pw.py - An insecure password locker program.

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
'luggage': '12345'}

import sys
import pyperclip

if len(sys.agrv) < 2:
	print("Please provide the account you want password for")
	sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print("Password for "+ account + " has been copied into clipboard.")
else:
	print("Password for "+ account + " hasn't been found.")
	
