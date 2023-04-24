from Converter8Bit import Converter8Bit
from ConverterInt import ConverterInt

# create an instance of the Converter8Bit class
converter = Converter8Bit()

# test with some binary sequences
binary_sequences = ['00000000', '00000001', '00000010', '00000100', '00001000', '00010000', '00100000', '01000000', '10000000']
for binary_seq in binary_sequences:
    # convert the binary sequence to a decimal number using the Converter8Bit class
    decimal_val = converter.to_spring_system(binary_seq)
    print(f"The decimal value of binary sequence {binary_seq} is {decimal_val}")


# create an instance of ConverterInt
conv = ConverterInt()

# test converting binary to decimal for different input values
print(conv.evaluate('1010')) # expected output: 10
print(conv.evaluate('11110000')) # expected output: 240
print(conv.evaluate('110110110')) # expected output: 438
