import argparse

parser = argparse.ArgumentParser(description = 'Um programa de exemplo.')
parser.add_argument('--frase', action = 'store', dest = 'frase',
                           default = 'Hello, world!', required = False,
                           help = 'A frase que deseja imprimir n vezes.')

arguments = parser.parse_args()

for i in range(0, int(arguments.n)):
    print arguments.frase