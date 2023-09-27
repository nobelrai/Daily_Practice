"""Given a non-negative number "num",
return True if num is within 2 of a multiple of 10. Note:
 (a % b) is the remainder of dividing a by b, so (7 % 5) is 2.
 See also: Introduction to Mod"""


# near_ten(12) → True
# near_ten(17) → False
# near_ten(19) → True


def near_ten(num):
    if abs(num) % 10 == 2 or abs(num) % 10 == 1 or abs(num) % 10 == 0 or abs(num) % 10 == 9 or abs(num) % 10 == 8:
        return True
    else:
        return False
