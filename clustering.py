
from BSAS import *
from MBSAS import *
from TTSAS import *


if __name__ == '__main__':
    x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14 = [1, 1], [1, 2], [2, 2], [2, 3], [3, 3], [3, 4], \
                                                                  [4, 4], [4, 5], [5, 5], [5, 6], [-4, 5], [-3, 5], \
                                                                  [-4, 4], [-3, 4]

    # Different order may cause different results
    # questionA
    x_list = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14]

    # questionB
    # x_list = [x1, x10, x2, x3, x4, x11, x12, x5, x6, x7, x13, x8, x14, x9]

    # questionC
    # x_list = [x1, x10, x5, x2, x3, x11, x12, x4, x6, x7, x13, x14, x8, x9]

    # Args
    maxNumClass = 14
    t_hold = 2 ** (1 / 2)
    t_hold1 = 2 ** (1 / 2)
    t_hold2 = 2

    # 3 methods
    res1 = BSAS(x_list, t_hold, maxNumClass)
    res2 = MBSAS(x_list, t_hold, maxNumClass)
    res3 = TTSAS(x_list, t_hold1, t_hold2, maxNumClass)

    for i in res3:
        print(i)
