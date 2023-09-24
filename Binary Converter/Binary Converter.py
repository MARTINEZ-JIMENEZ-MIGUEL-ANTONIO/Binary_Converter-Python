
def textbinary(text):
    binary = ' '.join(format(ord(char), '08b') for char in text)
    return binary

textoriginal = "123"

textconvertbinary = textbinary(textoriginal)

# Imprime el resultado
print("Texto original:", textoriginal)
print("Texto en binario:", textconvertbinary)