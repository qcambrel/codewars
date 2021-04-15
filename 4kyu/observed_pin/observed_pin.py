"""
Title: The Observed PIN
URL: https://www.codewars.com/kata/the-observed-pin
"""

from itertools import product

def get_pins(observed):
  print(observed)
  keypad = {'1':['1', '2', '4'],
            '2':['1', '2', '3', '5'],
            '3':['2', '3', '6'],
            '4':['1', '4', '5', '7'],
            '5':['2', '4', '5', '6', '8'],
            '6':['3', '5', '6', '9'],
            '7':['4', '7', '8'],
            '8':['5', '7', '8', '9', '0'],
            '9':['6', '8', '9'],
            '0':['8', '0']}
  possible_keys = [keypad[key] for key in observed]
  return [''.join(pin) for pin in product(*possible_keys)]

# Sample tests
assert get_pins('8') == sorted(['5','7','8','9','0'])
assert get_pins('11') == sorted(['11', '22', '44', '12', '21', '14', '41', '24', '42'])
assert get_pins('369') == sorted(['339','366','399','658','636','258','268','669','668','266','369','398','256','296','259','368','638','396','238','356','659','639','666','359','336','299','338','696','269','358','656','698','699','298','236','239'])