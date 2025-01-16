from django.http import HttpResponse
import re

def index(request):
    return HttpResponse("Welcome to the Regex App!")

def article_by_year(request, year):
    return HttpResponse(f"Articles from the year {year}")

def check_email(request, email):
    # Updated Regex pattern for email validation
    pattern = r'^[\w\-\.]+@([\w\-]+\.)+[\w\-]{2,4}$'
    
    # Validate the email with the regex
    if re.fullmatch(pattern, email):
        return HttpResponse(f"The email '{email}' is valid and matches the correct email format.")
    else:
        return HttpResponse(f"The email '{email}' is invalid or does not match the correct email format.")
