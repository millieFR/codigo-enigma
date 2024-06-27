mapa = {
    '6': 'F',
    '5': 'E',
    '50': 'L',
    '1': 'I',
    '26': 'Z',
    'MM': '2000',
    'R': '18'
}
mensagem = "6550126MMR"

enigma = ''
i = 0
while i < len(mensagem):
        if mensagem[i:i+2] in mapa:
            enigma += mapa[mensagem[i:i+2]]
            i += 2
        elif mensagem[i] in mapa:
            enigma += mapa[mensagem[i]]
            i += 1


print("mensagem codificada:", mensagem)
print("mensagem decodificada:", enigma [0:5] + ' ' + enigma [5:7] + enigma [7 + 2:])


