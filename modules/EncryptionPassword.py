class Encryption:

    """
    Realisation of the caesar cipher, use static key.
    """

    ENCRYPTION_KEY = 5
    PATTERN_FOR_ENCRYPTION = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijklmnpqrstuvwxyz1234567890#!?{}$%&@"

    def get_encrypted_word(self, str_encrypt):
        return self.__encrypt_with_caesar(str_encrypt)

    def get_decrypted_word(self, str_decrypt):
        return self.__decrypt_caesar(str_decrypt)

    def __encrypt_with_caesar(self, string_for_encryption):
        encrypted_word = ""
        for char in string_for_encryption:
            encrypted_word += self.PATTERN_FOR_ENCRYPTION[
                (self.PATTERN_FOR_ENCRYPTION.index(char) + self.ENCRYPTION_KEY) %
                len(self.PATTERN_FOR_ENCRYPTION)]

        return encrypted_word

    def __decrypt_caesar(self, string_for_encryption):
        encrypted_word = ""
        for char in string_for_encryption:
            encrypted_word += self.PATTERN_FOR_ENCRYPTION[
                (self.PATTERN_FOR_ENCRYPTION.index(char) - self.ENCRYPTION_KEY) %
                len(self.PATTERN_FOR_ENCRYPTION)]

        return encrypted_word




