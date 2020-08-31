#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Hash+salt de contraseña usando blowfish
import bcrypt
import getpass
import time
import sys

def get_hashed_password(plain_text_password):
	# Hash a password for the first time
	# (Using bcrypt, the salt is saved into the hash itself)
	salt = bcrypt.gensalt()
	pass_salted = bcrypt.hashpw(plain_text_password, salt)
	return pass_salted

def check_password(plain_text_password, salted_password):
	if bcrypt.checkpw(plain_text_password, salted_password):
		print(chr(27)+"[1;32m"+"\nOk, las contraseñas coinciden."+chr(27)+"[0m")
	else:
		print(chr(27)+"[1;31m"+"\nContraseña incorrecta."+chr(27)+"[0m")

user = str(input("Introduce tu usuario: "))
passwd = str(getpass.getpass("Introduce una contraseña: ")).encode()
passwd2 = str(getpass.getpass("Introduce nuevamente la contraseña:")).encode()
hashed = get_hashed_password(passwd)

print("┬───────────────────────────────────────────────────────────────┬")
print("│               C o n t r a s e ñ a   S e g u r a               │")
print("┼───────────────────────────────────────────────────────────────┼")
print("│"+str(hashed)+"│")
print("┴───────────────────────────────────────────────────────────────┴")

print("Revisando la coherencia de las contraseñas")
#Fake progress bar.
for i in range(30):
	if i < 29:
		print("█", end = '')
		sys.stdout.flush()
		time.sleep(0.05)
	else:
		print(" 100%!", end='')
		sys.stdout.flush()

check_password(passwd2, hashed)
print("                     ┌─────────────────┐")
print("                     │Fin del programa.│")
print("                     └─────────────────┘")
print("")
