# https://www.codewars.com/kata/520446778469526ec0000001

import re
def same_structure_as(original, other):
    new_original = str(original).replace("'['", "x")
    new_original = new_original.replace("']'", "x")

    new_other = str(other).replace("'['", "x")
    new_other = new_other.replace("']'", "x")

    new_original = re.sub(r'-?\d+', 'x', new_original)
    new_other = re.sub(r'-?\d+', 'x', new_other)

    if new_original != new_other:
        return False
    return True


