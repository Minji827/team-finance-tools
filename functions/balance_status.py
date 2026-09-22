def balance_status(balance):
    if balance < 0:
        return "마이너스 잔액"
    elif balance == 0:
        return "잔액 없음"
    else:
        return "정상 잔액"