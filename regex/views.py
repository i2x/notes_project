from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Regex App!")


def article_by_year(request, year):
    return HttpResponse(f"Articles from the year {year}")

def profile(request, username):
    return HttpResponse(f"Profile page of user: {username}")
