#继承的深度优先&继承的广度优先
#mro列表去记录类的继承顺序  根据C3线性算法实现
#python 2 深度优先  python 3 广度优先

class trafic_tools:
    country = "china"
    def __init__(self,name,speed,load):
        self.name = name
        self.speed = speed
        self.load = load
    def run(self):
        print("start run")

class sub_way(trafic_tools):
    def __init__(self,name,speed,load,line):
        super().__init__(name,speed,load)
        self.line = line

    def show_line(self):
        print(self.line)

    def run(self):
        super().run()
        print("%s start run" %(self.line))
line  = sub_way("shenzhenditie","60km/h","50000","3号线");
line.run()
line.show_line()