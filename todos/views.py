from django.shortcuts import render



def  todos_list(request):
    return render(request, "todos/todos_list.html")