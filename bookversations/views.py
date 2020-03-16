from django.conf import settings
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


username = 'suadolaps'
MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_LIST_ID = settings.MAILCHIMP_LIST_ID


def newsletter_signup(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            return render(request, 'bookversations/existingmail.html', {'form': form})
        else:
            instance.save()
            client = MailChimp(mc_api=MAILCHIMP_API_KEY, mc_user='suadolaps')
            client.lists.members.create(MAILCHIMP_LIST_ID, {'email_address': instance.email, 'status': 'subscribed',
                                                            'merge_fields': {'FNAME': instance.first_name, 'LNAME':
                                                                instance.last_name}})

    return render(request, 'bookversations/success.html', {'form': form})


def failure_retry(request):
    return render(request, 'bookversations/index.html')
