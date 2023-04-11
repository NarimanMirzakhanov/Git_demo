print(dir(__builtins__))
print(globals())

var = 'global'  # функция обращается к этой переменной, если нет переназначенной переменной внутри функции


def func():
    var = 'enclosed'  # функция обращается к этой переменной, если нет переназначенной переменной внутри функции

    def local():
        var = 'local'  # происходит поиск переменной из внутри наружу
        print(var)

    local()


func()
print(f"outside: {var}")
