def withdraw(balance, amount):
    if amount > balance:
        print("잔액 부족으로 출금할 수 없습니다.")
        return balance
    return balance - amount
