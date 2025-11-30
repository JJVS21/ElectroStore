from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from django.urls import reverse
from .forms import SellerRegisterForm, ManagerRegisterForm
from django.conf import settings

# Ajusta estos valores si en tu proyecto el app_label o model name son diferentes
APP_LABEL = 'store'          # la app donde está el modelo (store)
MODEL_NAME = 'producto'      # nombre del modelo en minúsculas (ajústalo si es 'Product')

def create_group_with_permissions(group_name, perms_codenames):
    """
    Crea el grupo si no existe y le asigna las permissions cuyo codename se pasan en la lista.
    perms_codenames ejemplo: ['add_producto','change_producto','view_producto']
    """
    group, created = Group.objects.get_or_create(name=group_name)
    # obtener ContentType por app_label y model
    try:
        ct = ContentType.objects.get(app_label=APP_LABEL, model=MODEL_NAME)
    except ContentType.DoesNotExist:
        return group, f"ContentType {APP_LABEL}.{MODEL_NAME} no encontrado. Ajusta APP_LABEL/MODEL_NAME."

    # asignar permisos
    for codename in perms_codenames:
        try:
            perm = Permission.objects.get(content_type=ct, codename=codename)
            group.permissions.add(perm)
        except Permission.DoesNotExist:
            # si falta un permiso, lo ignoramos pero informamos
            continue
    return group, None

def register_seller(request):
    if request.method == 'POST':
        form = SellerRegisterForm(request.POST)
        if form.is_valid():
            u = form.save(commit=False)
            u.set_password(form.cleaned_data['password'])
            u.is_staff = True  # para permitir acceso al admin si quieres
            u.save()
            # crear/obtener grupo y permisos
            group, err = create_group_with_permissions(
                'Vendedores',
                [f'add_{MODEL_NAME}', f'change_{MODEL_NAME}', f'view_{MODEL_NAME}']
            )
            if err:
                messages.warning(request, err)
            else:
                u.groups.add(group)
            messages.success(request, 'Usuario vendedor creado correctamente.')
            return redirect(reverse('login'))  # o a donde prefieras
    else:
        form = SellerRegisterForm()
    return render(request, 'accounts/register_seller.html', {'form': form})

def register_manager(request):
    if request.method == 'POST':
        form = ManagerRegisterForm(request.POST)
        if form.is_valid():
            u = form.save(commit=False)
            u.set_password(form.cleaned_data['password'])
            u.is_staff = True
            u.is_superuser = False  # si quieres que no sea superuser
            u.save()
            group, err = create_group_with_permissions(
                'Supervisores',
                [f'add_{MODEL_NAME}', f'change_{MODEL_NAME}', f'delete_{MODEL_NAME}', f'view_{MODEL_NAME}']
            )
            if err:
                messages.warning(request, err)
            else:
                u.groups.add(group)
            messages.success(request, 'Usuario supervisor creado correctamente.')
            return redirect(reverse('login'))
    else:
        form = ManagerRegisterForm()
    return render(request, 'accounts/register_manager.html', {'form': form})

