import threading
import mailchimp
from django.conf import settings

class SendSubscribeMail(object):
    def __init__(self, email):
        self.email = email
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        API_KEY = settings.api_key
        LIST_ID = settings.list_id
        api = mailchimp.Mailchimp(API_KEY)
        api.lists.subscribe(LIST_ID, {'email': self.email})

