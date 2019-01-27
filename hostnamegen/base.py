# -*- coding: utf-8 -*-
#######################################################################
# License: BSD-3-Clause (http://opensource.org/licenses/BSD-3-Clause) #
# Homepage: https://github.com/tasooshi/hostnamegen/                  #
# Version: 0.9.0                                                      #
#######################################################################

from __future__ import absolute_import


class Pattern:

    pattern = None
    method_prefix = 'var_'

    def __init__(self, factory):
        self.factory = factory

    def output(self):
        format_args = {}
        methods = [m for m in dir(self) if m.startswith(self.method_prefix)]
        for method in methods:
            format_args[method] = getattr(self, method)()
        return self.pattern.format(**format_args)
