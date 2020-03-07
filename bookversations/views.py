from django.conf import settings
from django.views import generic
from django.shortcuts import render
from .models import ReadingList, Subscribe


def index(request):
    reading_list = ReadingList.objects.order_by('-book_title')[:6]
    context = {
        'reading_list': reading_list,
    }
    return render(request, 'bookversations/index.html', context)



def subscribe(request):
    context = {
        'api_key': settings.MAILCHIMP_API_KEY,
    }
    if request.method == 'POST':
        email = request.POST['email']
        email_qs = Subscribe.objects.filter(email=email)

        if email_qs.exists():
            data = {"status": "404"}
            return render('bookversations/failure.html')
        else:
            Subscribe.objects.create(email=email)
            SendSubscribeMail(email)  # Send the Mail, Class available in utils.py

    return HttpResponse('bookversations/success.html', context)

