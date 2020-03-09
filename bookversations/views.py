from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from mailchimp3 import MailChimp
from .models import ReadingList, NewsletterUser
from .forms import NewsletterUserSignUpForm


def index(request):
    reading_list = ReadingList.objects.order_by('-book_title')[:6]
    context = {
        'reading_list': reading_list,
    }
    return render(request, 'bookversations/index.html', context)


def newsletter_signup(request):
    form = NewsletterUserSignUpForm(request.POST or None)
    api = settings.MAILCHIMP_API_KEY
    list_id = settings.MAILCHIMP_EMAIL_LIST_ID

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            return render(request, 'bookversations/existingmail.html')
        else:
            instance.save()
            client = MailChimp(mc_api=api, mc_user='suadolaps')
            client.lists.members.create(list_id, {'email_address': instance.email, 'status': 'subscribed'}, merge_fields={'FNAME': instance.fname, 'LNAME': instance.lname})

    context = {
        'form': form,
    }
    template = 'bookversations/success.html'
    return render(request, template, context)

