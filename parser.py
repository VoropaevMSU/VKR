from collections import namedtuple

class Parser:
    # Класс работает с файлами вида: 
    # входные переменные input <название переменных через запятую> ;
    # выходные переменные output <название переменных через запятую> ;
    # промежуточные переменные (провода) wire <название переменных через запятую> ;
    # операция (результат, {операнды}) ;
    def __init__(self, path):
        with open(path, 'r') as rf:
            self.text = rf.read().replace("\n","")
            
    # Поиск названия перменных по файлу
    # На вход подается строка начиная с которой 
    # и до точки с запятой будут искаться названия переменных в файле
    def varNames(self, substr):
        #print(self.text)
        split = self.text[self.text.find(substr) + len(substr) + 1:self.text.find(";",self.text.find(substr))]
        split = split.replace("\\","").replace(" ","").split(",")
        return split
    
    # Возвращает объект с четырьмя полями:
    # res — куда кладется результат операции
    # left — левый операнд
    # right — правый операнд
    # op — операция
    def parse(self):
        split = self.text[self.text.find(";",self.text.find("wire")) + 1: len(self.text)].replace("\\","").split(";")
        for substr in split:
            expr = namedtuple("expr", ['res', 'left', 'right', 'op', 'last'])
            expr.op = substr.split(" ")[0]
            l = substr[substr.find("(") + 1: substr.find(")")].replace(" ","").split(",")
            expr.res = l[0]
            l.remove(expr.res)
            if len(l) == 0:
                continue
            expr.left = l[0]
            if len(l) <= 1:
                yield expr
            for i in range(len(l) - 1):
                if (len(l) > 1):
                    if (expr.op == "_HMUX"):
                        if (len(l) > 2):
                            expr.right = l[i+1]
                            expr.last = l[i+2]
                            yield expr
                            break
                    if (i >= 1):
                        expr.left = expr.res
                    expr.right = l[i+1]
                yield expr
