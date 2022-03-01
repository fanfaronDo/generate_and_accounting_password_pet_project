from random import sample


class GenerationPass:
    """class generation password"""

    __slots__ = ("__symbols", "__length", "__alphabet", "__numbers", "__is_spec_symbol",
                 "__is_numbers", "char_for_generate")

    def __init__(self, spec_symbol, numbers, length):
        self.__is_spec_symbol = spec_symbol
        self.__is_numbers = numbers
        self.__length = length
        self.__symbols = "#!?{}$%&@"
        self.__numbers = "1234567890"
        self.__alphabet = "ABCDEFGHJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        self.char_for_generate = self.__define_range_char()

    def __define_range_char(self):
        result_range_char = self.__alphabet
        if self.__is_spec_symbol:
            result_range_char += self.__symbols
        if self.__is_numbers:
            result_range_char += self.__numbers
        return result_range_char

    def __generation(self):
        return sample(self.char_for_generate, int(self.__length))

    @property
    def gen_pass(self):
        return ''.join(self.__generation())





