from django.http import JsonResponse
import json

from mailing_list.models import MailingListForm


def mailing_list(request):
    data_from_post = json.load(request)["post_data"]
    # Then add validation etc.
    if request.method == "POST":
        f = MailingListForm({"email_address": data_from_post})
        f.save()

        # code that generates "output" variable
        output = "YOU'RE MY WIFE NOW DAVE!"
        data = {
            "output": output,
        }
        return JsonResponse(data)