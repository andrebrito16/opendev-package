#!/usr/bin/env python3
from dev_aberto import hello
import gettext
from babel.dates import format_date
from datetime import datetime
import locale
import os

system_locale, _ = locale.getdefaultlocale()

system_locale = os.environ.get("LANGUAGE", system_locale)

if system_locale is None:
    system_locale = "en_US"

gettext.bindtextdomain('cli', 'locale')
gettext.textdomain('cli')
_ = gettext.gettext

if __name__ == '__main__':
    date, name = hello()

    date_obj = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')

    localized_date = format_date(date_obj, locale=system_locale)

    print(_('Último commit feito em:'), localized_date, _(' por'), name)
