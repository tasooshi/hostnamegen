# -*- coding: utf-8 -*-
#######################################################################
# License: BSD-3-Clause (http://opensource.org/licenses/BSD-3-Clause) #
# Homepage: https://github.com/tasooshi/hostnamegen/                  #
# Version: 0.9.0                                                      #
#######################################################################

from __future__ import absolute_import

import re

import faker

from hostnamegen import patterns


def test_windows_default():
    factory = faker.Factory.create()
    assert re.match(r'DESKTOP-[A-Z0-9]{6}', patterns.WindowsDefault(factory).output())


def test_first_name_desktop():
    factory = faker.Factory.create()
    assert re.match(r'[A-Z]{1}[a-z]+', patterns.FirstNameDesktop(factory).output())


def test_company_desktop():
    factory = faker.Factory.create()
    assert re.match(r'[A-Z-]+-[A-Z0-9]{6}', patterns.CompanyDesktop(factory).output())
