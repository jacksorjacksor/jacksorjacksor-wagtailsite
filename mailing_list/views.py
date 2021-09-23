from django.http import JsonResponse
import json

from mailing_list.models import MailingListForm


def mailing_list(request):
    print("received!")
    data_from_post = json.load(request)["post_data"]

    if request.method == "POST":
        if len(data_from_post) > 0:
            print("here though?")
            print(data_from_post)
            f = MailingListForm({"email_address": data_from_post})
            f.save()
            #     MailingListForm(data_from_post).save()

        # code that generates "output" variable
        output = "YOU'RE MY WIFE NOW DAVE!"
        data = {
            "output": output,
        }
        return JsonResponse(data)
