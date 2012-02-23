#!/usr/bin/env python
# vim: set fileencoding=utf8:
"""
Base backends of django-inspecional-registration

All backends of django-inspectional-registration should be a subclass
of the ``BackendBase``


AUTHOR:
    lambdalisue[Ali su ae] (lambdalisue@hashnote.net)
    
Copyright:
    Copyright 2011 Alisue allright reserved.

License:
    Licensed under the Apache License, Version 2.0 (the "License"); 
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unliss required by applicable law or agreed to in writing, software
    distributed under the License is distrubuted on an "AS IS" BASICS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
__AUTHOR__ = "lambdalisue (lambdalisue@hashnote.net)"

class BackendBase(object):
    """Base backend class of django-inspectional-registration

    Methods:
    """

    def register(self, username, email):
        """register a new user account with given ``username`` and ``email``
        
        Returning should be a instance of new ``User``

        """
        raise NotImplementedError

    def accept(self, profile):
        """accept account registration with given ``profile`` (an instance of ``RegistrationProfile``)
        
        Returning should be a instance of accepted ``User`` for success, ``None``
        for fail.

        This method **SHOULD** work even after the account registration has rejected.

        """
        raise NotImplementedError

    def reject(self, profile):
        """reject account registration with given ``profile`` (an instance of ``RegistrationProfile``)

        Returning should be a instance of accepted ``User`` for success, ``None``
        for fail.

        This method **SHOULD NOT** work after the account registration has accepted.

        """


        raise NotImplementedError

    def activate(self, activation_key, password=None):
        """activate account with ``activation_key`` and ``password``

        This method should be called after the account registration has accepted,
        otherwise it should not be success.

        Returning is ``user``, ``password`` and ``is_generated`` for success,
        ``None`` for fail.

        If ``password`` is not given, this method will generate password and
        ``is_generated`` should be ``True`` in this case.

        """
        raise NotImplementedError

    def get_activation_form_class(self):
        """get activation form class"""
        raise NotImplementedError

    def get_registration_form_class(self):
        """get registration form class"""
        raise NotImplementedError
        
    def get_activation_complete_url(self, user):
        """get activation complete url"""
        raise NotImplementedError

    def get_registration_complete_url(self, user):
        """get registration complete url"""
        raise NotImplementedError

    def get_registration_closed_url(self):
        """get registration closed url"""
        raise NotImplementedError

    def registration_allowed(self):
        """return ``False`` if the registration has closed"""
        raise NotImplementedError