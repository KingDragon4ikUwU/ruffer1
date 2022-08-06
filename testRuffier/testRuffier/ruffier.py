txt_index = "Ваш індекс Руф’є:"
txt_workheart = "Працездатність серця:"
txt_nodata = ''' Немає даних для такого віку '''
txt_res = []
txt_res.append(''' Низька. Терміново зверніться до лікаря! ''')
txt_res.append(''' Задовільна. Зверніться до лікаря! ''')
txt_res.append(''' Середня. Можливо, варто додатково обстежитись у лікаря. ''')
txt_res.append(''' Вище середнього ''')
txt_res.append(''' Висока ''')


def ruffier_index(P1, P2, P3):
    ''' повертає значення індексу за трьома показниками пульсу для звірки з таблицею'''
    return (4*(P1+P2+P3)-200)/10


def neud_level(age):
    ''' варіанти з віком менше 7 і дорослим треба обробляти окремо,
     тут підбираємо рівень "незадовільно" тільки всередині таблиці:
     у віці 7 років "незад" - це індекс 21, далі кожні 2 роки він знижується на 1.5 до значення 15 в 15-16 років '''
    norm_age = (min(age, 15) - 7)//2
    result = 21 -norm_age*1.5
    return result


def ruffier_result(r_index, level):
    if r_index >= level:
        return 0
    level = level - 4
    if r_index >= level:
        return 1
    level = level - 5
    if r_index >= level:
        return 2
    level = level - 5.5
    if r_index >= level:
        return 3
    return 4

def test(P1, P2, P3, age):
    if age < 7:
        return(txt_index + "0", txt_nodata)
    else:
        ruff_index = ruffier_index(P1, P2, P3)
        result = txt_res[ruffier_result(ruff_index,neud_level(age))]
        res = txt_index + str(ruff_index) + "\n" + txt_workheart + result
        return res