from functions.deposit import deposit
from functions.withdraw import withdraw
from functions.interest import calculate_interest
from functions.exchange import exchange_money
from functions.saving import monthly_saving
from functions.fee import calculate_fee
from functions.withdraw_check import can_withdraw
from functions.balance_status import balance_status

balance = 100000

print("===== 금융 도구 실행 결과 =====")

balance = deposit(balance, 50000)
print(f"입금 후 잔액: {balance}원")

balance = withdraw(balance, 30000)
print(f"출금 후 잔액: {balance}원")

interest = calculate_interest(balance, 0.03)
print(f"예상 이자: {interest}원")

exchanged = exchange_money(10000, 0.00072)
print(f"환율 변환 결과: {exchanged}")

saving = monthly_saving(1200000, 12)
print(f"월 저축액: {saving}원")

fee = calculate_fee(balance, 0.01)
print(f"수수료: {fee}원")

print(f"출금 가능 여부 (50000원): {can_withdraw(balance, 50000)}")
print(f"출금 가능 여부 (999999원): {can_withdraw(balance, 999999)}")

status = balance_status(balance)
print(f"잔액 상태: {status}")
