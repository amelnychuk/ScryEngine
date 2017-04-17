from ProcessFactory import Executor, Executor, MacroProcess

class ExampleProcessor(Executor):
    pass



#When Inheriting from MicroProcess a wrapper is used to tag which functions will exectute when class is called.
class ExampleExecutor(Executor):
    @Executor.task
    def B_print(self, arg):
        print("Test1", arg)

    @Executor.task
    def A_print(self, arg):
        print("Test2", arg)


    def C_print(self, arg):
        print("Test3", arg)


#When inheriting from a macro process all functions execute in the order of their definitions when class is called.
class SubMicroProcess(MacroProcess):

    def subProcessB(self, arg):
        print("subprocess B", arg)

    def subProcessA(self, arg):
        print("subprocess A", arg)

    def randomFunc(self, arg):
        print("random function", arg)


class PracticalProcess(MacroProcess):

    def caps(self, arg):
        return arg.lower()
    def removeDoubleSpaces(self,arg):
        return arg.replace("  ", " ")



s = SubMicroProcess()

s("my sub argument")

d = ExampleExecutor()
d("my arg")

""
p = ExampleProcessor()

p.add(s)
p.add(d)

p.run("All functions of s and d process this argument")
