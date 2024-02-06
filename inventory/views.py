from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render
from . models import Inventory
from . forms import InventoryForm

# Create your views here.
def index(request):
    return render(request, 'inventory/index.html', {'inventory': Inventory.objects.all()})

def view_item(request, id):
    item = Inventory.objects.get(pk=id)
    return HttpResponse(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            new_inventory_name = form.cleaned_data.get('name')
            new_inventory_lot_number = form.cleaned_data.get('lot_number')
            new_inventory_expiration_date = form.cleaned_data.get('expiration_date')

            new_inventory_item = Inventory(
                name=new_inventory_name, 
                lot_number=new_inventory_lot_number, 
                expiration_date=new_inventory_expiration_date
            )
            new_inventory_item.save()
            return render(request, 'inventory/add.html', {'form': InventoryForm(), 'success': True})
    else:
        form = InventoryForm()
    return render(request, 'inventory/add.html', {'form': InventoryForm()})

def edit(request, id):
    if request.method == 'POST':
        item = Inventory.objects.get(pk=id)
        form = InventoryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return render(request, 'inventory/edit.html', {'form': form,'success': True})
    else:
        item = Inventory.objects.get(pk=id)
        form = InventoryForm(instance=item)
    return render(request, 'inventory/edit.html', {'form': form})

def delete_item(request, id):
    if request.method == 'POST':
        item = Inventory.objects.get(pk=id)
        item.delete()
        return render(request, 'inventory/index.html', {'inventory': Inventory.objects.all()})


