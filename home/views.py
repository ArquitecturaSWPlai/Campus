import json
from django.http import JsonResponse,  HttpResponseRedirect
import concurrent.futures as thread_request
from django.shortcuts import render, redirect
from .models import UserProfile, UsuarioAcademic, ConfigApisMoodle, Inscripciones
import requests as fetch
from django.core.exceptions import MultipleObjectsReturned
from campusVirtual import settings
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp
from django.contrib.auth.models import User

def home(request):
    usr, perfilAprender, inscripciones = buscar_alumno(request)
    configApisMoodle = ConfigApisMoodle.objects.all()
    return render(request, 'dist/index.html', {"lista_configuracion_moodle":configApisMoodle,"perfil":perfilAprender, "usuario": usr, "inscripciones": inscripciones})

def salir(request):
    redirect_url = '/'
    keycloak_url = settings.SOCIALACCOUNT_PROVIDERS["keycloak"]["KEYCLOAK_URL"]
    keycloak_realm = settings.SOCIALACCOUNT_PROVIDERS["keycloak"]["KEYCLOAK_REALM"]
    KEYCLOAK_LOGOUT_URL = f"{keycloak_url}/realms/{keycloak_realm}/protocol/openid-connect/logout"
    
    user_id = request.user.id
    user = User.objects.get(id=request.user.id)
    # Cerrar sesión en Django
    logout(request)
    social_account = SocialAccount.objects.filter(user=user).first()
    social_app = SocialApp.objects.first()
    if social_account:
        # Si se encuentra una cuenta social, obtener el token social asociado
        token = social_account.socialtoken_set.first()
        if token:
            # Si se encuentra un token, obtener el id_token
            id_token = token.token_secret
            # Construir la URL de logout de Keycloak con redirect_uri e id_token_hint
            data = {
                'refresh_token': id_token,
                'client_id': social_app.client_id,
                'client_secret': social_app.secret,
            }
            response = fetch.post(KEYCLOAK_LOGOUT_URL, data=data)
            return redirect(redirect_url)
    # Si no se encontró ninguna cuenta social o token, redirigir a la URL predeterminada
    return redirect(redirect_url)


def buscar_alumno(request):
    if request.user.is_authenticated:
        usr = User.objects.get(id=request.user.id)
        if UserProfile.objects.filter(user=usr).exists():
            perfil, created = UserProfile.objects.get_or_create(user=usr)
            inscripciones = Inscripciones.objects.filter(usuario=perfil)
            return usr, perfil, inscripciones
    else:
        return None, None, None
def redirect_moodle(request):
    return HttpResponseRedirect('https://cursos.plai.mx/')

