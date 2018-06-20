import datetime
import os

from django.conf import settings
from django.contrib.auth.models import User
from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase

from registration import forms
from registration.models import RegistrationProfile


class RegistrationViewTests(TestCase):
    """
    Test the registration views.
    """
    urls = 'registration.tests.urls'

    def setUp(self):
        self.old_activation = getattr(settings, 'ACCOUNT_ACTIVATION_DAYS', None)

        if self.old_activation is None:
            settings.ACCOUNT_ACTIVATION_DAYS = 7 # pragma: no cover
        
        settings.TEMPLATES += (os.path.join(os.path.dirname(__file__), 'templates'),)

    def tearDown(self):
        if self.old_activation is None:
            settings.ACCOUNT_ACTIVATION_DAYS = self.old_activation # pragma: no cover

    def test_registration_view_initial(self):
        response = self.client.get(reverse('registration_register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'registration/registration_form.html')
        self.failUnless(isinstance(response.context['form'],
                                   forms.RegistrationForm))

    def test_registration_view_success(self):
        """
        A ``POST`` to the ``register`` view with valid data properly
        creates a new user and issues a redirect.
        """
        response = self.client.post(reverse('registration_register'),data={'username': 'alice','email': 'alice@example.com','password1': 'swordfish','password2': 'swordfish'})
        self.assertRedirects(response,
                             'http://testserver%s' % reverse('registration_complete'))

    def test_registration_view_failure(self):
        response = self.client.post(reverse('registration_register'),
                                    data={'username': 'bob',
                                            'email': 'bobe@example.com',
                                            'password1': 'foo',
                                            'password2': 'bar'})
        self.assertEqual(response.status_code, 200)
        self.failIf(response.context['form'].is_valid())
        # self.assertFormError(response, 'form', field=None,
        #                         errors=u"The two password fields didn't match.")


