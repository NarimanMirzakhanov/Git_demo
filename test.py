import my_calc
import datetime

def tests():
    assert my_calc.addition(5, 8) == 13, f'Wrong number, actual result is {my_calc.addition(5, 8)}'
    # assert my_calc.addition(5, 8) == 15, f'Wrong number, actual result is {my_calc.addition(5, 8)}'


tests()


birth_year = 1983
current_date = datetime.date.today()
print(current_date)
current_age= current_date.year - birth_year
print(current_age)
