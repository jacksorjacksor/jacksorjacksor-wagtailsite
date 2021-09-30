from django.http import JsonResponse
import json

from mailing_list.models import MailingList, MailingListForm

from django.core.mail import send_mail


def send_email_to_new_mailing_list_sign_up(email_input):
    send_mail(
        "jacksorjacksor - mailing list sign-up",
        'Welcome to the mailing list! Thanks for signing up! To unsubscribe just reply to this email saying "unsubscribe".',
        "rich@jacksorjacksor.xyz",
        [email_input],
        fail_silently=False,
    )


def mailing_list(request):
    json_output = json.loads(request.body)  # Get ALL the json!
    print(f"{json_output=}")
    email_input = json_output["email_input"]
    name_input = json_output["name_input"]

    # Then add validation etc.
    if request.method == "POST":
        if len(name_input) > 0:  # Robot captcha test
            output_message = "Please try again"

        # If the email address isn't already added then add it
        # if not MailingList.objects.filter(email_address=email_input).exists():
        f = MailingListForm({"email_address": email_input})
        f.save()
        # send_email_to_new_mailing_list_sign_up(email_input)

        output_message = f"{email_input} has been added to the mailing list!"

        # code that generates "output" variable
        data = {
            "output_message": output_message,
        }
        return JsonResponse(data)
