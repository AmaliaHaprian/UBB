from string import ascii_letters


class Validator:
    @staticmethod
    def validate_string(string_input):
        for char in string_input:
            if char not in list(ascii_letters):
                return False

        return True