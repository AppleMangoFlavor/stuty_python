"""
데코레이터는 함수를 인자로 받고 새로운 함수를 반환하는 함수
함수를 감싸는 역활
"""

### 1. 일반 함수 ###
def hello(strA:str):
    print(f'hello {strA}')
    return "hello "+strA

# hello('LCB')

### 2. decorator 예시 ###
def deco(func):
    def wrapper_func(strA:str):
        print("전처리~")
        result = func(strA)
        print("후처리~")
        return result
    return wrapper_func

@deco
def say_hello(name):
    print(f'hello {name}')

# say_hello('LCB')

### 3. 중첩 ###
"""
deco(deco_2(func)) 형태로 처리됨
"""
def deco_2(func):
    def wrapper_func2(strA:str):
        print("전처리2~")
        result = func(strA)
        print("후처리2~")
        return result
    return wrapper_func2

@deco
@deco_2
def say_hello2(name):
    print(f'hello {name}')

say_hello2('LCB')