from allauth.socialaccount.signals import social_account_added, social_account_updated
from allauth.socialaccount.models import SocialToken, SocialApp
from django.dispatch import receiver
from django.contrib.auth import get_user_model
import requests
import pprint
User = get_user_model()

@receiver(social_account_added)
@receiver(social_account_updated)
def almacenar_tokens(sender, request, sociallogin, **kwargs):
    # Obtener el id_token y access_token de la respuesta
    id_token = sociallogin.token.token
    access_token = sociallogin.token.token_secret

    # Verificar si los tokens están presentes
    if id_token and access_token:
        # Crear o actualizar el SocialToken
        social_app = SocialApp.objects.get(id=sociallogin.token.app_id)
        token, created = SocialToken.objects.get_or_create(
            app=social_app,
            account=sociallogin.account,
            defaults={
                'token': id_token,
                'token_secret': access_token,
                'expires_at': sociallogin.token.expires_at
            }
        )

        if not created:
            token.token = id_token
            token.token_secret = access_token
            token.expires_at = sociallogin.token.expires_at
            token.save()

        # Almacenar el id_token en la sesión
        request.session['id_token'] = id_token
