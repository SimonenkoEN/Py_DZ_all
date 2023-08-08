# ДЗ к семинару 4, задание 3
# Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.

MULTIPLICITY = 50
WITHDRAW_PERC = 0.015
WITHDRAW_MIN = 30
WITHDRAW_MAX = 600
OPERATIONS = 3
OPs_PERC = 0.03
RICH_SCORE = 5_000_000
RICH_PERC = 0.1


def get_cash_value():
    cash_value = float(input('Введите сумму кратную 50: '))
    return cash_value


def check_multiplicity(cash_):
    if cash_ % MULTIPLICITY == 0:
        return True
    else:
        return False


def get_ops_perc(ts_, cash_):
    op = 0
    if ts_[1] != 0 and ts_[1] % OPERATIONS == 0:
        op = cash_ * OPs_PERC
    return op


def get_rich_perc(ts_, cash_):
    rp = 0
    if ts_[0] >= RICH_SCORE:
        rp = cash_ * RICH_PERC
    return rp


def withdraw_perc_value(cash_):
    w_perc = cash_ * WITHDRAW_PERC
    if w_perc < WITHDRAW_MIN:
        w_perc = WITHDRAW_MIN
    elif w_perc > WITHDRAW_MAX:
        w_perc = WITHDRAW_MAX
    return w_perc


def ops_info_print(ts_, cash_, wp_, op_, rp_):
    print('Сумма операции:', cash_)
    print('Комиссия за операцию:', wp_ + op_)
    if rp_ != 0:
        print ('Налог на богатство:', rp_)
    print('-------------')
    print('БАЛАНС СЧЕТА:', ts_[0])
    tmp = input('Для продолжения нажмите "Enter"')


def withdraw_operation(ts_):
    print('ОПЕРАЦИЯ СНЯТИЯ СО СЧЕТА:')
    cash = get_cash_value()
    while check_multiplicity(cash) == False or cash <= 0:
        cash = get_cash_value()
    wp = withdraw_perc_value(cash)
    w_sum = cash + wp
    op = get_ops_perc(ts_, cash)
    rp = get_rich_perc(ts_, cash)
    if (w_sum + op + rp) <= ts_[0]:
        ts_[0] -= w_sum + op + rp
        ts_[1] += 1
        ops_info_print(ts_, cash, wp, op, rp)
    else:
        ts_[0] -= rp
        print('У Вас недостаточно средств для проведения операции!')
        ops_info_print(ts_, cash, wp, op, rp)
    global ops_list
    ops_list.append(-1 * (w_sum + op + rp))
    return ts_


def deposit_operation(ts_):
    print('ОПЕРАЦИЯ ПОПОЛНЕНИЯ СЧЕТА:')
    cash = get_cash_value()
    while check_multiplicity(cash) == False or cash <= 0:
        cash = get_cash_value()
    op = get_ops_perc(ts_, cash)
    wp = 0
    rp = get_rich_perc(ts_, cash)
    ts_[0] -= op + rp
    ts_[0] += cash
    ts_[1] += 1
    ops_info_print(ts_, cash, wp, op, rp)
    global ops_list
    ops_list.append(cash - op - rp)
    return ts_


if __name__ == '__main__':
    total_score = [0, 0]
    ops_list = []

    with open('total_score.txt', 'r') as data:
        tmp_ts = data.readline()
        ts = tmp_ts.split(',')
        total_score[0] = float(ts[0])
        total_score[1] = int(ts[1])

    while True:
        print('Python Банк')
        print('1 -> Пополнение счета')
        print('2 -> Снятие со счета')
        print('0 -> Выход')
        print('----------')
        print('Баланс счета:', total_score[0], '\n')
        mode = int(input('Выберите опрерацию: '))
    
        match mode:
            case 1:
                total_score = deposit_operation(total_score)
            case 2:
                total_score = withdraw_operation(total_score)
            case 0:
                with open('total_score.txt', 'w') as data:
                    data.write(str(total_score[0]) + ',' + str(total_score[1]))
                if not ops_list == []:
                    with open('ops_list.txt', 'a') as ol:
                        for i in ops_list:
                            ol.write(str(f'{i}\n'))
                break
            case _:
                continue