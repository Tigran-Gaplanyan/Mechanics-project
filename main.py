from Converter8Bit import Converter8Bit
from ConverterInt import ConverterInt
from ConverterFloat import ConverterFloat

# create an instance of the Converter8Bit class
print("Converter8Bit")
converter = Converter8Bit()

# test with some binary sequences
binary_sequences = ['00000000', '00000001', '00000010', '00000100', '00001000', '00010000', '00100000', '01000000', '10000000']
for binary_seq in binary_sequences:
    # convert the binary sequence to a decimal number using the Converter8Bit class
    decimal_val = converter.binary_to_decimal(binary_seq)
    springs_8bit = converter.bits_to_springs(binary_seq)
    print(f"The length of the spring {len(springs_8bit)}")
    print(f"The decimal value of binary sequence {binary_seq} is {decimal_val}")

print()
print("ConverterInt")
print()
# create an instance of ConverterInt
conv = ConverterInt()

# test converting binary to decimal for different input values
binary_sequences1 = ['1010', '11110000', '110110110']
for binary_seq in binary_sequences1:
    # convert the binary sequence to a decimal number using the ConverterInt class
    decimal_val = conv.binary_to_decimal(binary_seq)
    springs_int = conv.bits_to_springs(binary_seq)
    print(f"The length of the spring {len(springs_int)}")
    print(f"The decimal value of binary sequence {binary_seq} is {decimal_val}")

print()
print("ConverterFloat")
print()

# create an instance of ConverterInt
conv_float = ConverterFloat(4,4)

# Test case 1: binary representation of 12.75
binary = "1100.11"
decimal = conv_float.binary_to_decimal(binary)
springs1 = conv_float.bits_to_springs(binary)
print("Test case 1:")
print(f"Binary representation: {binary}")
print(f"Decimal value: {decimal}")
print(f"Used unit springs: {len(springs1)}")
print()

# Test case 2: binary representation of 0.125
binary = "0.001"
decimal = conv_float.binary_to_decimal(binary)
springs = conv_float.bits_to_springs(binary)
print("Test case 2:")
print(f"Binary representation: {binary}")
print(f"Decimal value: {decimal}")
print(f"Used unit springs: {springs}")
print()

# Test case 3: binary representation of 6.625
binary = "110.101"
decimal = conv_float.binary_to_decimal(binary)
springs5 = conv_float.bits_to_springs(binary)
print("Test case 3:")
print(f"Binary representation: {binary}")
print(f"Decimal value: {decimal}")
print(f"Used unit springs: {len(springs5)}")
print()