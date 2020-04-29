# -*- coding: utf-8 -*-
#######################################################################
# License: BSD-3-Clause (http://opensource.org/licenses/BSD-3-Clause) #
# Homepage: https://github.com/tasooshi/hostnamegen/                  #
# Version: 1.0.0                                                      #
#######################################################################

import random
import sys

import click
import faker

from hostnamegen import (
    patterns,
    exceptions,
)


__version__ = (1, 0, 0)

VERSION = '{}.{}.{}'.format(*__version__)

LOCALE = (
    'ar_EG',
    'bg_BG',
    'bs_BA',
    'cs_CZ',
    'de_DE',
    'el_GR',
    'en_US',
    'es_ES',
    'et_EE',
    'fa_IR',
    'fi_FI',
    'fr_FR',
    'hi_IN',
    'hr_HR',
    'hu_HU',
    'it_IT',
    'ja_JP',
    'ko_KR',
    'lt_LT',
    'lv_LV',
    'nl_NL',
    'pl_PL',
    'pt_BR',
    'ro_RO',
    'ru_RU',
    'sl_SI',
    'sv_SE',
    'tr_TR',
    'uk_UA',
    'zh_CN',
)


def print_locale_list(ctx, param, value):

    if not value or ctx.resilient_parsing:
        return
    click.echo(', '.join(LOCALE))
    ctx.exit()


def print_classes_list(ctx, param, value):

    if not value or ctx.resilient_parsing:
        return
    click.echo(', '.join(patterns.__all__))
    ctx.exit()


def print_version(ctx, param, value):

    if not value or ctx.resilient_parsing:
        return
    click.echo(VERSION)
    ctx.exit()


def generate(locale=None, classes=None, number=1, delimiter=','):

    if locale is None:
        locale = random.choice(LOCALE)
    else:
        if locale not in LOCALE:
            raise exceptions.ConfigurationError(
                'Provided locale is not available: {}'.format(locale)
            )

    if classes:
        classes = [c.strip() for c in classes.split(',')]
        classes_missing = set(classes) - set(patterns.__all__)
        if classes_missing:
            raise exceptions.ConfigurationError(
                'Some classes were not found: {}'.format(', '.join(classes_missing))
            )
    else:
        classes = patterns.__all__

    factory = faker.Factory.create(locale)
    hostname_insts = {}
    hostnames = []
    for _ in range(number):
        class_name = random.choice(classes)
        if class_name not in hostname_insts:
            hostname_insts[class_name] = getattr(patterns, class_name)(factory)
        hostnames.append(hostname_insts[class_name].output())

    return delimiter.join(hostnames)


@click.command()
@click.option('-l', '--locale', type=click.STRING, help='Locale, e.g. en_US. [Default: random]')
@click.option('-c', '--classes', type=click.STRING, help='Name generation classes, comma separated. [Default: random]')
@click.option('-n', '--number', type=click.INT, default=1, help='Number of names to be generated. [Default: 1]')
@click.option('-d', '--delimiter', type=click.STRING, default=',', help='Delimiter. [Default: ,]')
@click.option('-cl', '--classes-list', is_flag=True, callback=print_classes_list, expose_value=False, is_eager=True, help='List name generation classes')
@click.option('-ll', '--locale-list', is_flag=True, callback=print_locale_list, expose_value=False, is_eager=True, help='List available locale')
@click.option('-v', '--version', is_flag=True, callback=print_version, expose_value=False, is_eager=True, help='Print version')
def main(locale, classes, number, delimiter):
    try:
        print(generate(locale, classes, number, delimiter))
    except (Exception, KeyboardInterrupt) as exc:
        sys.exit('Error: {}'.format(exc))


if __name__ == '__main__':
    main()
