from django.conf import settings
from django.template.loader import render_to_string

from dora.core.emails import send_mail


def send_suggestion_validated_new_structure_email(email, structure):
    params = {
        "structure": structure,
        "cta_link": f"{settings.FRONTEND_URL}/?nom=&commune",  # TODO
        "cta_text": "Rejoindre cette structure",
        "homepage_url": settings.FRONTEND_URL,
    }
    body = render_to_string("new_structure.html", params)

    send_mail(
        "[DORA] Des acteurs de l’insertion sont intéressées par vos services !",
        email,
        body,
        tags=["validate_new_structure"],
    )


def send_suggestion_validated_existing_structure_email(to, service):
    params = {
        "cta_link": service.get_frontend_url(),
        "cta_text": "Voir la suggestion",
        # "more_details_link": "",
    }
    body = render_to_string("existing_structure.html", params)

    send_mail(
        "[DORA] Vous avez reçu une nouvelle suggestion de service ! 🥳 🎉",
        to,
        body,
        tags=["suggestion_existing_structure"],
    )
