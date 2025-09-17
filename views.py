from django.shortcuts import render, redirect
from .models import Entry, Category
from django.db.models import Sum
from .forms import EntryForm
from django.http import JsonResponse
import os
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from .forms import CategoryForm
from collections import OrderedDict

# Registo de utilizador
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


#mostra a página inicial do projeto
@login_required
def home(request):
    template_path = os.path.join(settings.BASE_DIR, 'templates', 'home.html')
    exists = os.path.exists(template_path)
    print("▶️ Template path:", template_path)
    print("✔️ Template exists?", exists)
    return render(request, 'home.html')


@login_required
@permission_required('mainapp.view_entry', raise_exception=True)
def entries_list(request):
    entry_type = request.GET.get('type')
    category = request.GET.get('category')
    order = request.GET.get('order', 'desc')

    entries = Entry.objects.all()

    if entry_type:
        entries = entries.filter(entry_type=entry_type)
    if category:
        entries = entries.filter(category__name__icontains=category)

    if order == 'asc':
        entries = entries.order_by('date')
    else:
        entries = entries.order_by('-date')

    return render(request, 'entries_list.html', {
        'entries': entries,
        'entry_type': entry_type,
        'category': category,
        'order': order,
        'categories': Category.objects.all(),
    })



# Criação de nova entrada
@login_required
@permission_required('mainapp.add_entry', raise_exception=True)
def new_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entries_list')
    else:
        form = EntryForm()
    return render(request, 'new_entry.html', {'form': form})


# Relatório de entradas, mostrando resumo por categoria e tipo
@login_required
@permission_required('mainapp.view_entry', raise_exception=True)
def report_view(request):
    entry_type = request.GET.get('type')
    category = request.GET.get('category')
    order = request.GET.get('order', 'desc')

    return render(request, 'report.html', {
        'entry_type': entry_type,
        'category': category,
        'order': order,
        'categories': Category.objects.all(),
    })

# Endpoint para obter dados do relatório em formato JSON
@login_required
@permission_required('mainapp.view_entry', raise_exception=True)
def report_data(request):
    from collections import OrderedDict

    entry_type = request.GET.get('type')
    category = request.GET.get('category')
    order = request.GET.get('order', 'desc')

    entries = Entry.objects.all()

    if entry_type:
        entries = entries.filter(entry_type=entry_type)
    if category:
        entries = entries.filter(category__name=category)

    if order == 'asc':
        entries = entries.order_by('date')
    else:
        entries = entries.order_by('-date')

    income = OrderedDict()
    expense = OrderedDict()

    for entry in entries:
        label = entry.date.strftime("%Y-%m-%d")
        if entry.entry_type == "income":
            income[label] = income.get(label, 0) + float(entry.value)
        elif entry.entry_type == "expense":
            expense[label] = expense.get(label, 0) + float(entry.value)

    return JsonResponse({'income': income, 'expense': expense})

#acesso negado 
def custom_permission_denied_view(request, exception=None):
    return render(request, "403.html", status=403)

from django.shortcuts import get_object_or_404
from .forms import CategoryForm

# Listagem de categorias e operações CRUD para categorias
@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form, 'title': 'Add Category'})

@login_required
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form, 'title': 'Edit Category'})

@login_required
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category_confirm_delete.html', {'category': category})
