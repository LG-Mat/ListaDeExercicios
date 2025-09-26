#2) Eliminar todos os símbolos e algarismos
msg = ''
tx = input("Digite algo: ")
print(type(tx))

st = []

if tx.isalpha():
    print(tx)
else:
    for i in range(0, len(tx), 1):
        if tx[i].isalpha() or tx[i].isspace(): st.append(tx[i])

if len(st) > 0:
    for s in range(0, len(st), 1):
        msg = msg + st[s]
    print(msg)
