import pyeda.inter as bdd
import pyeda
import variableEncoding as encode
import equivalentCheck as eqch
import parser
import variableEncoding as encode
import execution
import sys
            
# Печать ответа 
def printAnswerIntoFile(f, inV):
    print(bdd.bdd2expr(f))
    file = open("output.txt", 'w')
    if (f.is_zero()):
        file.write("Equivalent")
    else:
        file.write("Not equivalent")
        for way in f.satisfy_all():
            f.write(way)
            for var in way.keys():           
                for key, value in inV.items():
                    if value[0] == var:
                        if way[var] == 1 or way[var] == 1 and value[1] in way and way[value[1]] == 0:
                            f.write(key, "= x")
                        elif value[1] in way and way[value[1]] == 0:
                            f.write(key, "= 0")
                        else:
                            f.write(key, "= 1")
                        break
            break
    file.close()
    
def execute(path1, path2):
    g = eqch.EquivalentCheckFromFile(path1, path2)
    prs = parser.Parser(path1)
    inv = execution.initializationVariables(prs, "input")
    printAnswerIntoFile(g, inv)

if len(sys.argv) > 2:
    execute(sys.argv[1], sys.argv[2])
else:
    print("Введите относительный путь к двум файлам со схемами")