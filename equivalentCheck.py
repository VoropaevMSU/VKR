import parser
import pyeda.inter as bdd
import execution as exe

# Поиск всех путей в бдд от терминальной вершины 1 
# Если необходим поиск всех путей в бдд от терминальной вершины 0, 
# то на вход необходимо подать ~f
def findAllWays(f):
    v = bdd.expr("0")
    v = bdd.expr2bdd(v)
    for i in f.satisfy_all():
        s = bdd.expr("1")
        s = bdd.expr2bdd(s)
        for a in i.items():
            if (a[1] == 1):
                s = s & a[0]
            else:
                s = s & ~a[0]
        v = v | s
    return v


# Осуществляет проверку эквивалентности двух схем из файлов
def EquivalentCheckFromFile(path1, path2):
    answ1 = exe.Execution(path1)
    answ2 = exe.Execution(path2)
    prs = parser.Parser(path1)
    for name in prs.varNames("output"):
        r1 = bdd.expr2bdd(answ1[name][0])
        r3 = bdd.expr2bdd(answ2[name][0])
        f1 = findAllWays(~r1) & findAllWays(r3)
        if (~f1.is_zero()):
            return f1
        r2 = bdd.expr2bdd(answ1[name][1])
        r4 = bdd.expr2bdd(answ2[name][1])
        f2 = findAllWays(~r1) & findAllWays(r2) & findAllWays(~r3) & findAllWays(~r4)
        if (~f2.is_zero()):
            return f2
        f3 = findAllWays(~r1) & findAllWays(~r2) & findAllWays(~r3) & findAllWays(r4)
        if (~f3.is_zero()):
            return f3
        f = bdd.expr("0")
        return f

# Осуществляет проверку эквивалентности двух схем
def EquivalentCheck(out1, out2, inV):
    r1 = out1[0]
    r2 = out1[1]
    r3 = out2[0]
    r4 = out2[1]
    f1 = findAllWays(~r1) & findAllWays(r3)
    f2 = findAllWays(~r1) & findAllWays(r2) & findAllWays(~r3) & findAllWays(~r4)
    f3 = findAllWays(~r1) & findAllWays(~r2) & findAllWays(~r3) & findAllWays(r4)
    f = f1 | f2 | f3
    f = bdd.expr2bdd(f)
    return f
