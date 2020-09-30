massiv = [[10, 11],
          [20, 21, 22],
          [30, 31, 32, 33],
          [40, 41, 42, 43, 44]]

output = []
from pprint import pprint as pp
pp(massiv)
print(massiv)

m_sum = sum(sum(1 for sel in row if sel%2 == 1)
            for row in massiv
            if len(row)%2 == 1)
print('Summa: {}'.format(m_sum))