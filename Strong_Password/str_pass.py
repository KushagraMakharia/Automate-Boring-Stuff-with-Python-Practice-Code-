import re

password = "AbC1@2853"

def password_critera_check(password):
	len_pattern = "[\d\w@$!%*?&]{8,}"
	uc_pattern = "[A-Z]"
	lc_pattern = "[a-z]"


	len_check = re.compile(len_pattern)
	uc_check = re.compile(uc_pattern)
	lc_check = re.compile(lc_pattern)


	if len_check.search(password) and uc_check.search(password) and lc_check.search(password):
		print("Password passed the criteria.")
	else:
		print("Password needs to be more stronger.") 

password_critera_check(password)

