roman = [
    ['','I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
    ['','X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
    ['','C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
    ['', 'M', 'MM', 'MMM']
]

class Solution:
    def intToRoman(self, num: int) -> str:
        my_roman = []
        for i, d in enumerate(str(num)[::-1]):
            my_roman.append(roman[i][int(d)])
        return ''.join(my_roman[::-1])
        