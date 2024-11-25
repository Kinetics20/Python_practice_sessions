
def capitalize(function):
    def inner(name):
        return function(name.capitalize())

    return inner

def reverse(fn):
    def inner(name):
        return fn(name[::-1])

    return inner


def gen_html(fn):
    def inner(name):
        result = fn(f'<b>{name}<b/>')
        return f'<h1>{result}</h1>'
        

    return inner
@capitalize
@gen_html
# @capitalize
# @reverse
def hello(name):
    return f"Hello {name}"
# def hello(name):
#     return f'<h1>Hello <b>{name}<b/></h1>'

@capitalize
@gen_html
# @reverse
# @capitalize
def bye(name):
    return f"Bye {name}"
# def bye(name):
#     return f'<h1>Bye <b>{name}<b/></h1>'

print(hello("ola")) # <h1>Hello <b>Ola<b/></h1>
print(bye("lech"))  # <h1>Bye <b>Lech<b/></h1>

