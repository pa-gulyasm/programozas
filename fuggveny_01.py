# ord()
# A megadott karakter Unicode-ját képviselő egész szám konvertálása
x = ord("h")
print(x)
#-------------------------------------------------------------------------
# chr()
# Egy karaktert ad vissza a megadott Unicode kódból.
x = chr(97)
print(x)
#-------------------------------------------------------------------------
# min()
# Az iterálható legkisebb elemet adja vissza
x = min(5, 10)
print(x)
#-------------------------------------------------------------------------
# max()
# Az iterálható legnagyobb elemet adja vissza
x = max(5, 10)
print(x)
#-------------------------------------------------------------------------
# index()
# Megkeresi a karakterláncot egy megadott érték után, és visszaadja a keresés helyét
txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)
#-------------------------------------------------------------------------
# list() 
# Listát ad vissza
x = list(('apple', 'banana', 'cherry'))
print(x)
