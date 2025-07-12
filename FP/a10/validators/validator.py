from string import ascii_letters


class Validator:

    def validate_coordinate(self, x:int, lower_limit:int, upper_limit:int)->bool:
        if x < lower_limit or x > upper_limit:
            return False
        return True

    def validate_input(self, input:str):
        if input in ascii_letters:
            return False
        return True