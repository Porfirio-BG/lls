#!/usr/bin/python
# -*- coding: utf8 -*-
import hashlib
import decimal
import logging
import os
from Crypto.Cipher import AES
import base64
import keyring
key = keyring.get_password('lls','clv')
bs = 32
key = hashlib.sha256(key.encode()).digest()

def encript(raw):
    raw = _pad(raw)
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))

def decript(enc):
    enc = base64.b64decode(enc)
    iv = enc[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return _unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

def _pad(s):
    return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)


def _unpad(s):
    return s[:-ord(s[len(s)-1:])]