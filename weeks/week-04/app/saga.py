# Реализуйте здесь простую машину состояний (State Machine).
# Функция должна принимать текущее состояние и событие,
# и возвращать следующее состояние.

import random
import time

def next_state(state: str, event: str) -> str:
    transitions = {
        ('NEW', 'PAY_OK'): 'PAID',
        ('NEW', 'PAY_FAIL'): 'CANCELLED',
        ('NEW', 'CANCEL'): 'CANCELLED',
        
        ('PAID', 'COMPLETE'): 'DONE',
        ('PAID', 'CANCEL'): 'CANCELLED',
        ('PAID', 'PAY_FAIL'): 'CANCELLED',
        
        ('DONE', 'CANCEL'): 'CANCELLED',
        
        ('CANCELLED', 'RETRY'): 'NEW',
    }
    return transitions.get((state, event), state)

def process_step(state: str, retries: int = 2) -> str:
    success = random.choice([True, False])
    
    if success:
        return next_state(state, 'PAY_OK')
    
    print(f"Ошибка оплаты")
    state = next_state(state, 'CANCEL')
    
    for i in range(retries):
        print(f"Попытка компенсации {i+1}")
        if random.choice([True, False]):
            print("Компенсация, билет отменен")
            return state  
    print("Не удалось выполнить компенсацию")
    return state

def run_saga():
    state = 'NEW'
    print(f"Билет создан: {state}")
    
    state = process_step(state)
    
    if state == 'PAID':
        state = next_state(state, 'COMPLETE')
        print(f"Билет куплен: {state}")
    elif state == 'CANCELLED':
        print(f"Билет отменен: {state}")

if __name__ == "__main__":
    run_saga()