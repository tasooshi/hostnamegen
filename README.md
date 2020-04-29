# hostnamegen

## About

This little tool generates random host names that make sense. It is a complementary library for [namechanger](https://github.com/tasooshi/namechanger).

## Installation

Easiest way is by pulling from PyPI:

    pip3 install hostnamegen

## Usage

### Random host name with defaults

    $ hostnamegen
    HOLZAPFEL-W3WS1Q

### Ten random names using Japanese locale and selected classes

    $ hostnamegen -lja_JP -n10 -d";" -cFirstNameDesktop,CompanyDesktop
    GONG-ZE-DIAN-QI-YOU-XIAN-HUI-SHE-Y88FW4;HE-TONG-HUI-SHE-JIN-TENG-YIN-XING-1SW7YY;Liang-jie;Zhi-shu;Ying-shu;Yi;ZHONG-DAO-YIN-SHUA-ZHU-SHI-HUI-SHE-641IAN;YOU-XIAN-HUI-SHE-TIAN-BIAN-KUANG-YE-3AAQ5Q;QI-TENG-GASUZHU-SHI-HUI-SHE-1SH0DN;Yang-yi

### List available classes

    $ hostnamegen -cl
    CompanyDesktop, FirstNameDesktop, WindowsDefault

### List available locale

    $ hostnamegen -ll
    ar_EG, bg_BG, bs_BA, cs_CZ, de_DE, el_GR, en_US, es_ES, et_EE, fa_IR, fi_FI, fr_FR, hi_IN, hr_HR, hu_HU, it_IT, ja_JP, ko_KR, lt_LT, lv_LV, nl_NL, pl_PL, pt_BR, ro_RO, ru_RU, sl_SI, sv_SE, tr_TR, uk_UA, zh_CN

## Legal

* License: BSD-3-Clause (http://opensource.org/licenses/BSD-3-Clause)

## Contact

In case you feel the need to get in touch:

* tasooshi@pm.me
* [GPG](https://tasooshi.github.io/6C3E62B2.asc)
