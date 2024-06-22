# scopes3.py
# Local, Enclosing and Global
def enclosing_func():
    m = 13
    def local():
        # m doesn't belong to the scope defined by the local
        # function so Python will keep looking into the next
        # enclosing scope. This time m is found in the enclosing
        # scope
        print(m, 'printing from the local scope')

    # calling the function local
    local()

m = 5
print(m, 'printing from the global scope')

enclosing_func()

# output:
# Running scopes3.py will print on the console:
# $ python scopes3.py
# 5 printing from the global scope
# 13 printing from the local scope
