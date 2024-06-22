# scopes2.py
# Local versus Global
def local():
    # m doesn't belong to the scope defined by the local function
    # so Python will keep looking into the next enclosing scope.
    # m is finally found in the global scope
    print(m, 'printing from the local scope')
m = 5
print(m, 'printing from the global scope')
local()

# output:
# Running scopes2.py will print this:
# $ python scopes2.py
# 5 printing from the global scope
# 5 printing from the local scope
