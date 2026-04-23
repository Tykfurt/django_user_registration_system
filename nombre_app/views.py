from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Validar contraseñas
        if password != confirm_password:
            return render(request, 'registro_app/register.html', {
                'error': 'Las contraseñas no coinciden'
            })

        # Crear usuario
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()

        return redirect('/')  # o a login

    return render(request, 'registro_app/register.html')