from django.conf import settings
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render
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

    if form.is_valid():
        instance = form.save(commit=False)
        context = {
            'instance': instance,
        }
        if NewsletterUser.objects.filter(email=instance.email).exists():
            return render(request, 'bookversations/existingmail.html', context)
        else:
            instance.save()

    context = {
        'form': form,
    }

    template = 'bookversations/success.html'

    return render(request, template, context)


