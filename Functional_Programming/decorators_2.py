
def capitalize(function):
    def inner(name):
        return function(name.capitalize())

    return inner

def reverse(fn):
    def inner(name):
        return fn(name[::-1])

    return inner

def inner_wrapper(fn, tag, tag_2):
    def inner(name):
        result = fn(f'<{tag_2}>{name}<{tag_2}/>')
        return f'<{tag}>{result}</{tag}>'
    return inner



def gen_html(cb=None, *, tag='h1',tag_2='b'):

    if callable(cb):
        return inner_wrapper(cb, tag, tag_2)


    def wrapper(cb_):
        return inner_wrapper(cb_, tag, tag_2)

    return wrapper






# def gen_html(fn):
#     def inner(name):
#         result = fn(f'<b>{name}<b/>')
#         return f'<h1>{result}</h1>'
#
#     return inner


@capitalize
@gen_html(tag_2='H')
# @reverse
# @capitalize
def bye(name):
    return f"Bye {name}"
# def hello(name):
#     return f'<h1>Hello <b>{name}<b/></h1>'

@capitalize
@gen_html(tag='h3',tag_2='i')
# @capitalize
# @reverse
def hello(name):
    return f"Hello {name}"
# def bye(name):
#     return f'<h1>Bye <b>{name}<b/></h1>'

print(hello("ola")) # <h1>Hello <b>Ola<b/></h1>
print(bye("lech"))  # <h1>Bye <b>Lech<b/></h1>

