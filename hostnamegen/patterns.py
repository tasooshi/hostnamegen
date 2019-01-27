# -*- coding: utf-8 -*-
#######################################################################
# License: BSD-3-Clause (http://opensource.org/licenses/BSD-3-Clause) #
# Homepage: https://github.com/tasooshi/hostnamegen/                  #
# Version: 0.9.0                                                      #
#######################################################################

from __future__ import absolute_import

import inspect

import slugify

from hostnamegen import base


UNIQUE_ID = {'length': 6, 'special_chars': False, 'digits': True, 'upper_case': True, 'lower_case': False}


class WindowsDefault(base.Pattern):

    pattern = u'DESKTOP-{var_1}'

    def var_1(self):
        return self.factory.password(**UNIQUE_ID)


class FirstNameDesktop(base.Pattern):

    pattern = u'{var_1}'

    def var_1(self):
        return slugify.slugify(self.factory.first_name()).capitalize()


class CompanyDesktop(base.Pattern):

    pattern = u'{var_1}-{var_2}'

    def var_1(self):
        return slugify.slugify(self.factory.company().split(',')[0]).upper()

    def var_2(self):
        return self.factory.password(**UNIQUE_ID)


__all__ = [
    cls for (cls, obj) in iter(globals().copy().items())
    if inspect.isclass(obj) and issubclass(obj, base.Pattern)
]
