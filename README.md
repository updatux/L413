# L413
Cryptage en Python 

# Comment sa marche?

Le programme vous demande un mot de passe et le crypt en SHA512 puis le convertis en base décimal (car il est par défault en hexadecimal) puis convertis le text en hexadecimal et génère une clé secrette en hexadécimal et les connvertis en décimal puis il additionne le mot de passe, le text et la clé et retourne le text crypter en hexadecimal avec la clé (qui n'est pas votre mot de passe)

# Syntaxe

python l413.py -e TEXT // Pour le crypter
python l413.py -d TEXTCRYPTER CLESECRETTE // Pour le décrypter
