import pyperclip
import re

text = str(pyperclip.paste())

phone_pattern = "\+91\d{10}"
phone_reg = re.compile(phone_pattern)

email_pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.[a-zA-Z]+"
email_reg = re.compile(email_pattern)

phone_matches = phone_reg.findall(text)
email_matches = email_reg.findall(text)

if len(phone_matches) != 0:
	print("List of phone numbers found:")
	for ph in phone_matches:
		print(ph)
else:
	print("No phone number found.")

if len(email_matches) != 0:
	print("List of emails found:")
	for em in email_matches:
		print(em)
else:
	print("No email found.")

matches = phone_matches + email_matches
pyperclip.copy("\n".join(matches))

print("All matches are copied to the clipboard.")




