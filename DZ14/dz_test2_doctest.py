# Задание
#  Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
#  Напишите к ним тесты.
#  2-5 тестов на задачу в трёх вариантах:
# - doctest,
# - unittest,
# - pytest.


from math import gcd


class My_Fractions:

    def get_fraction(self, fract: str) -> tuple:
        """
        >>> My_Fractions().get_fraction('3/4')
        (3, 4)
        """
        return tuple(map(int, fract.split('/')))

    def sum_fractions(self, fract_1: tuple, fract_2: tuple) -> str:
        """
        >>> My_Fractions().sum_fractions(My_Fractions().get_fraction('1/4'), My_Fractions().get_fraction('1/2'))
        '3/4'
        """
        num_res = fract_1[0] * fract_2[1] + fract_2[0] * fract_1[1]
        denom_res = fract_1[1] * fract_2[1]
        nod = gcd(num_res, denom_res)
        res = ''.join([str(num_res//nod), '/', str(denom_res//nod)])
        return res

    def mult_fractions(self, fract_1: tuple, fract_2: tuple) -> str:
        """
        >>> My_Fractions().mult_fractions(My_Fractions().get_fraction('1/4'), My_Fractions().get_fraction('1/2'))
        '1/8'
        """
        num_res = fract_1[0] * fract_2[0]
        denom_res = fract_1[1] * fract_2[1]
        nod = gcd(num_res, denom_res)
        res = ''.join([str(num_res//nod), '/', str(denom_res//nod)])
        return res

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)