
from django.shortcuts import render


def renderTemplate(request):
    myDict={"name":"Alon"}
    return render(request, 'templatesApp/firstTemplate.html',context=myDict)


def renderEmployee(request):
    myDict={"id":123,"name":"Alon","sal":10000}
    return render(request, 'templatesApp/employeeTemplate.html',context=myDict)