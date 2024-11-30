from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
import re
from django.http import HttpResponse

# Criação da tarefa
def home(request):
    if request.method == "POST":
        entrada = request.POST.get("entrada")
        categoria = request.POST.get("categoria")
        
        if entrada and categoria:  # Verifica se ambos os campos são preenchidos
            print(f"Criando tarefa com nome: {entrada} e categoria: {categoria}")
            Task.objects.create(name=entrada, category=categoria)  # Cria uma nova tarefa no banco de dados
        else:
            print("Entrada ou categoria vazia")
        return redirect('home')  # Redireciona para a página inicial após criar a tarefa
    
    tasks = Task.objects.all()  # Pega todas as tarefas do banco de dados
    return render(request, 'home.html', {'tasks': tasks})

# Validação de entrada (exemplo adicional)
def validar(request):
    if request.method == "POST":
        entrada = request.POST.get("entrada")
        # Verifica se a entrada contém apenas letras
        if re.fullmatch(r"[a-zA-Z]+", entrada):
            return HttpResponse(f"Entrada válida: {entrada}")
        else:
            return HttpResponse("Entrada inválida. Use apenas letras.")
    return render(request, "form.html")

# Exclusão de tarefa
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()  # Exclui a tarefa do banco de dados
    return redirect('home')  # Redireciona de volta para a home
