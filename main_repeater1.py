# import repeater
from repeater import *

s = input("반복할 문자를 입력하세요: ")
n = input("반복 횟수를 입력하세요: ")
# repeater.repeat(s, int(n))
# repeater.repeat(s)
# repeater.once(s)
repeat(s, int(n))
repeat(s)
once(s)