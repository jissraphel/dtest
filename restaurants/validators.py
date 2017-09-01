from django.core.exceptions import ValidationError

def validate_email(value):
	email=value
	if ".edu" in email:
		raise ValidationError("email error")
	return email 

CATEGORIES=['non','veg','nml']

 def validate_category(value):
 	if not value in CATEGORIES:
 		raise ValidationError(f"{value} is not valid")
 		