from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password  # To hash the password
from django.contrib import messages
from .models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Expense
from .forms import ExpenseForm


# List of expenses
def expense_list(request):
    expenses = Expense.objects.all().order_by('-date')
    return render(request, 'expense_list.html', {'expenses': expenses})

# Add new expense
def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})

# Edit an existing expense
from django.shortcuts import get_object_or_404

def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    
    else:
        form = ExpenseForm(instance=expense)

    return render(request, 'edit_expense.html', {'form': form})


# Delete an expense
def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)  # Use this for better error handling
    
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')  # Redirect to the expense list after deletion
    
    # Render a confirmation page if the request is not POST
    return render(request, 'expenses/delete_expense.html', {'expense': expense})

