### 1. 일반 함수 ###
def hello(strA:str):
    print(f'hello {strA}')
    return "hello "+strA

hello('LCB')

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

say_hello('LCB')

