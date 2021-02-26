import pyeda.inter as bdd
import pyeda
import parser
import variableEncoding as encode

# Возвращает словарь вида <название переменной из файла, две фактические переменные>
def initializationVariables(prs):
    dictOfVar = {}
    # Инициализируем входные переменные
    inputVar = prs.varNames("input")
    inV = bdd.exprvars("inV", len(inputVar) * 2)
    i = 0
    for varName in inputVar:
        if varName not in dictOfVar:
            dictOfVar[varName] = (inV[i], inV[i+1])
            i += 2
    # Инициализируем выходные переменные
    outputVar = prs.varNames("output")
    outV = bdd.exprvars("outV", len(outputVar) * 2)
    i = 0
    for varName in outputVar:
        if varName not in dictOfVar:
            dictOfVar[varName] = (outV[i], outV[i+1])
            i += 2
    # Инициализируем промежуточные переменные
    wireVar = prs.varNames("wire")    
    wireV = bdd.exprvars("wire", len(wireVar) * 2)
    i = 0
    for varName in wireVar:
        if varName not in dictOfVar:
            dictOfVar[varName] = (wireV[i], wireV[i+1])
            i += 2
    return dictOfVar
        
def Execution(path):
    prs = parser.Parser(path)
    dictOfVar = initializationVariables(prs)
    for expr in prs.parse():
        operation = expr.op
        if expr.left == "1b'1":
            left = boolOne()
        elif expr.left == "1b'0":
            left = boolZero()
        elif expr.left == "1b'x":
            left = boolX()
        else:
            left = dictOfVar[expr.left]
        if (operation == "_HMUX"):
            dictOfVar[expr.res] = encode.boolMux(left, dictOfVar[expr.right], dictOfVar[expr.last])
        if (type(expr.right) == str):
            if expr.right == "1b'1":
                right = boolOne()
            elif expr.right == "1b'0":
                right = boolZero()
            elif expr.right == "1b'x":
                right = boolX()
            else:
                right = dictOfVar[expr.right]
            if operation == "and":
                dictOfVar[expr.res] = encode.boolAnd(left, right)
            elif operation == "or":
                dictOfVar[expr.res] = encode.boolOr(left, right)
            elif operation == "nor":
                dictOfVar[expr.res] = encode.boolNor(left, right)
            elif operation == "nand":
                dictOfVar[expr.res] = encode.boolNand(left, right)
            elif operation == "_DC":
                dictOfVar[expr.res] = encode.boolDC(left, right)
            elif operation == "xor":
                dictOfVar[expr.res] = encode.boolXor(left, right)
            elif operation == "xnor":
                dictOfVar[expr.res] = encode.boolXnor(left, right)
        else:
            if operation == "buf":
                dictOfVar[expr.res] = encode.boolBuf(left)
            elif operation == "not":
                dictOfVar[expr.res] = encode.boolNot(left)
    return dictOfVar
    
