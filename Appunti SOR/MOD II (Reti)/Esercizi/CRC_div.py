import argparse


# Funzione aggiornata per restituire anche il quoziente e il resto della divisione
def crc_division(data_bits, generator_bits):
    # Convertiamo il data_bits e generator_bits in lista di interi
    data = [int(bit) for bit in data_bits]
    generator = [int(bit) for bit in generator_bits]

    # Appendiamo zeri alla fine del pacchetto in base alla lunghezza del generatore - 1
    data_extended = data + [0] * (len(generator) - 1)
    quotient = [0] * len(data)  # Inizializziamo il quoziente

    # Effettuiamo la divisione binaria XOR
    for i in range(len(data_bits)):
        if data_extended[i] == 1:  # XOR solo quando il bit corrente è 1
            quotient[i] = 1  # Aggiorniamo il quoziente
            for j in range(len(generator)):
                data_extended[i + j] ^= generator[j]

    # Il resto è rappresentato dagli ultimi bit della lista data_extended
    remainder = data_extended[-(len(generator) - 1) :]

    return "".join(map(str, quotient)), "".join(map(str, remainder))


# Instantiate the parser
parser = argparse.ArgumentParser(description="CRC calculator with rest and quotient")

parser.add_argument("-d", type=int, nargs="?", help="Dividendo")
parser.add_argument("-da", type=int, nargs="?", help="Divisore")
args = parser.parse_args()

# Eseguiamo il calcolo per trovare quoziente e resto
data_bits = str(args.d)
generator_bits = str(args.da)
quotient, remainder = crc_division(data_bits, generator_bits)

print(
    "Dividendo:{}, Divisore:{}, Quoziente:{}, Resto:{}".format(
        data_bits, generator_bits, quotient, remainder
    )
)
