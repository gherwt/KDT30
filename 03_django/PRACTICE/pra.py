

# 1등 num 6개 다 맞을때
# 2등 num 5개 + 보너스
# 3등 num 5개
# 4등 num 4개
# 5등 num 3개
def lotto_out(num):
    bonus_nu = [7]
    num = [1, 2, 3, 4, 5, 6]
    collect_number = [2, 4, 5, 6, 7, 8]

    for i in range(len(num)):   
        count = 0
        if i in collect_number:
            count += 1

    if count == 6:
        result = '1등입니다.'

    elif count == 5:
        if bonus_nu in num:
            result = '2등입니다.'
        else:
            result = '3등입니다.'

    elif count == 4:
        result = '4등입니다.'

    elif count == 3:
        result = '5등입니다.'

    else:
        result = '당첨되지 않으셨습니다.'

    return result