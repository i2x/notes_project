from django.shortcuts import render
from django.http import JsonResponse


def calculator_v1(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('num2', 0))
        operator = request.POST.get('operator')

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/' and num2 != 0:
            result = num1 / num2
        elif operator == '/' and num2 == 0:
            result = "Cannot divide by zero"

    return render(request, 'calculator_v1.html', {'result': result})


def calculator_v2(request):
    if request.method == 'POST':
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('num2', 0))
        operator = request.POST.get('operator')
        result = "Invalid input"

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/' and num2 != 0:
            result = num1 / num2
        elif operator == '/' and num2 == 0:
            result = "Cannot divide by zero"

        return JsonResponse({'result': result})
    return render(request, 'calculator_v2.html')


def calculator_v3(request):
    return render(request, 'calculator_v3.html')