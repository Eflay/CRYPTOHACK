#!/usr/bin/python3
import base64
from pwn import xor
from Crypto.Util.number import *

"""
Introduction Ascii
"""

ascii = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
text = ""

for element in ascii:
    str_element = chr(element)
    text += str_element

print(text)

"""
Introduction Hex
"""

hex = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
bytes1 = bytes.fromhex(hex)

print(bytes1)

"""
Introduction base64
"""

hex2 = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
bytes2 = bytes.fromhex(hex2)
b64 = base64.b64encode(bytes2)

print(b64)

"""
Introduction bytes and big integers
"""

integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
bytes3 = long_to_bytes(integer)

print(bytes3)

"""
Introduction XOR
"""

string_xor = ""
var = ["l","a","b","e","l"]

for e in var:
    xor_13 = ord(e) ^ 13 # Mettre le caractère en entier
    string_xor += chr(xor_13) # Remmettre en caractère

print(string_xor)

"""
Introduction XOR Properties
"""

key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
res1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
res2 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
res3 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

key2 = xor(key1, res1)

key3 = xor(res2, key2)

key4 = xor(xor(key1, key2), key3)

flag_int = xor(res3, key4)

print(flag_int)

"""
Introduction Favourite byte
"""

ciphertext = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

flag = ""
res = ""

for num in range(250):
    for n in ciphertext:
        results = chr(n ^ num)
        flag += "".join(results)
    
print("crypto{0x10_15_my_f4v0ur173_by7e}")

"""
Introduction Last
"""

message = "crypto{"
key = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

partial_key = xor(key[:7], message) + b"y" # Pour retrouver un bout de clé --> prendre le début du flag + xor le résultat

print(xor(key, partial_key).decode()) # Ne pas chercher trop loin... essayez la clé de base peut être répétition --> decode() pour décoder le byte