# -*- coding: utf-8 -*-
# usr/bin/python
from __future__ import nested_scopes
from __future__ import generators
from __future__ import division
from __future__ import absolute_import
from __future__ import with_statement
from __future__ import print_function
from __future__ import unicode_literals
from datetime import datetime
from hashlib import sha256


def dec(has):
    return has.decode('hex')[::-1]


def double256(has):
    return sha256(sha256(has).digest()).digest()[::-1].encode('hex')


def main():
    version = 4
    prev_block = "0000000000000000005629ef6b683f8f6301c7e6f8e796e7c58702a079db14e8"
    markle_root = "efb8011cb97b5f1599b2e18f200188f1b8207da2884392672f92ac7985534eeb"
    timestamp = "2016-01-30 13:23:09"
    bits = 403253488
    nonce = 1448681410  # 承認済みのブロックなので、nonceの値もわかっている
    start = datetime(1970, 1, 1)
    date = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S") - start
    timestamp = int(date.total_seconds())
    # 新規
    version_h = dec('{0:08x}'.format(version))
    prev_block_h = dec(prev_block)
    markle_root_h = dec(markle_root)
    timestamp_h = dec("{0:x}".format(timestamp))
    bits_h = dec("{0:x}".format(bits))
    nonce_h = dec("{0:x}".format(nonce))
    total = version_h + prev_block_h + markle_root_h + timestamp_h
    bitno = total + bits_h + nonce_h
    print(double256(bitno))


if __name__ == '__main__':
    main()
