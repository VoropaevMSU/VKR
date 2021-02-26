import pyeda.inter as bdd
import pyeda

# Кодировние операции "or" (4 входа и два выхода)
def boolOr(x, y):
    f = x[0] & y[0] | x[0] & ~y[1] | ~x[1] & y[0]
    g = ~x[0] & x[1] | ~y[0] & y[1]
    return(f, g)

# Кодировние операции "and" (4 входа и два выхода)
def boolAnd(x, y):
    f = x[0] & y[0] | x[0] & y[1] | x[1] & y[0]
    g = ~x[0] & x[1] & ~y[0] & y[1]
    return(f, g)

# Кодировние операции "not" (2 входа и два выхода)
def boolNot(x):
    f = x[0]
    g = ~x[0] & ~x[1]
    return(f, g)

# Кодировние операции "nand" (4 входа и два выхода)
def boolNand(x, y):
    return boolNot(boolAnd(x, y))
 
# Кодировние операции "nor" (4 входа и два выхода)
def boolNor(x, y):
    return boolNot(boolOr(x, y))

# Кодировние операции "xor" (4 входа и два выхода)
def boolXor(x, y):
    f = x[0] | y[0]
    g = ~x[0] & x[1] & ~y[0] & ~y[1] | ~x[0] & ~x[1] & ~y[0] & y[1]
    return(f, g)

# Кодировние операции "xnor" (4 входа и два выхода)
def boolXnor(x, y):
    return boolNot(boolXor(x, y))

# Кодировние операции "_DC" (4 входа и два выхода)
def boolDC(x, y):
    f = x[0] | y[0] | y[1]
    g = ~x[0] & x[1] & ~y[0] & ~y[1]
    return(f, g)

# Кодировние операции "buf" (2 входа и два выхода)
def boolBuf(x):
    f = x[0]
    g = x[1]
    return(f, g)

# Кодирование операции "boolMux" (6 входов и два выхода)
def boolMux(x, y, z):
    f = boolAnd(~z, x)[0] | boolAnd((~z[0],z[1]),y)[0] | z[0]
    g = boolAnd(~z, x)[1] | boolAnd((~z[0],z[1]),y)[1] | ~z[0]
    return(f, g)

# Кодирование константы 1
def boolOne():
    f = bdd.expr("0")
    f = bdd.expr2bdd(f)
    g = bdd.expr("1")
    g = bdd.expr2bdd(g)
    return (f, g)

# Кодирование константы 0
def boolZero():
    f = bdd.expr("0")
    f = bdd.expr2bdd(f)
    g = bdd.expr("0")
    g = bdd.expr2bdd(g)
    return (f, g)

# Кодирование константы x
def boolX():
    f = bdd.expr("1")
    f = bdd.expr2bdd(f)
    g = bdd.expr("0")
    g = bdd.expr2bdd(g)
    return (f, g)

