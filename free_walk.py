import re
def solve_2(S): #working
    su_1 = 0
    val_1 = 0
    K1= S.replace('?','A')
    for i in K1:
        if i == 'A':
            su_1 = su_1 + 1
            if val_1 < su_1:
                val_1 = su_1
        else:
            su_1 =  su_1 - 1
    
    su_2 = 0
    val_2 = 0
    K2= S.replace('?','C')
    for i in K2:
        if i == 'C':
            su_2 = su_2 + 1
            if val_2 < su_2:
                val_2 = su_2
        else:
            su_2 =  su_2 - 1
    return max(val_1,val_2)


print(solve_2('C?'))

    
