import Type as ty
import Rational as option
import Complex as optionCom
from cmath import *

type = ty.type()

if type == 'rat':
    option.mainterminal()

if type == 'comp':
    repeat = True
    while repeat == True:
        optionCom.mainterminal()