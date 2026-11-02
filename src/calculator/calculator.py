
class Calculator(object):
    _instance = None

    def add(_self, a, b):
        return _self._to_number(a) + _self._to_number(b)
    
    def _to_number(_self, value):
        numbers = {
        # English
        "zero": 0, "one": 1, "two": 2, "three": 3,
        "four": 4, "five": 5, "six": 6, "seven": 7,
        "eight": 8, "nine": 9,

        # German
        "null": 0, "eins": 1, "zwei": 2, "drei": 3,
        "vier": 4, "fünf": 5, "sechs": 6, "sieben": 7,
        "acht": 8, "neun": 9,

        # Spanish
        "cero": 0, "uno": 1, "dos": 2, "tres": 3,
        "cuatro": 4, "cinco": 5, "seis": 6,
        "siete": 7, "ocho": 8, "nueve": 9,

        # Russian
        "ноль": 0, "один": 1, "два": 2, "три": 3,
        "четыре": 4, "пять": 5, "шесть": 6,
        "семь": 7, "восемь": 8, "девять": 9,

        # Chinese
        "零": 0, "一": 1, "二": 2, "三": 3,
        "四": 4, "五": 5, "六": 6, "七": 7,
        "八": 8, "九": 9,
        }

        if isinstance(value, (int, float)):
            return value

        value = value.strip()

        if value.lower() in numbers:
            return numbers[value.lower()]
    # Convert numeric strings first
        try:
            return float(value)
        except ValueError:
            pass

        # Roman numerals
        roman = {
        "I": 1, "V": 5, "X": 10,
        "L": 50, "C": 100, "D": 500, "M": 1000
        }

        if value.upper() and all(char in roman for char in value.upper()):
            total = 0
            previous = 0

        for char in reversed(value.upper()):
            current = roman[char]

            if current < previous:
                total -= current
            else:
                total += current

            previous = current

        return total

        try:
         return float(value)
        except ValueError:
            pass

        raise ValueError(f"Cannot convert {value!r} to a number")

    def sub(_self, a, b):
        return _self._to_number(a) - _self._to_number(b)
    
    def mul(_self, a, b):
        return _self._to_number(a) * _self._to_number(b)
    
    def div(_self, a, b):
        return _self._to_number(a) /_self._to_number(b)
    
    def factorize(_self, n):
        n=int(_self._to_number(n))
        factors = []
        divisor = 2

        while divisor * divisor <= n:
            while n % divisor == 0:
                factors.append(divisor)
                n = n // divisor
            divisor += 1

        if n > 1:
            factors.append(n)

        return factors
    def __init__(self):
        pass

    # Singleton pattern by overloading the new operator, see
    # https://stackoverflow.com/questions/31875/is-there-a-simple-elegant-way-to-define-singletons

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance