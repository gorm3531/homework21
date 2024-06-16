def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
test_function() # я не могу вызвать функцию inner_function() вне функции test_function(), тк они в разных пространствах

