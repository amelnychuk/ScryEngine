from collections import OrderedDict


class MetaProcess(type):
    """
    This meta class allows classes functions to be ordered in the class dict.

    New instances of classes with functions containing _filter attributes
    are appeneded to an array.



    """

    @classmethod
    def __prepare__(metacls, name, bases):
        return OrderedDict()

    def __new__(metacls, name, bases, namespace, **kwds):
        newclass = type.__new__(metacls, name, bases, dict(namespace))
        newclass._processes = []
        if isinstance(bases, tuple):
            if len(bases) > 0:
                if hasattr(bases[0],"_micro"):
                    for value in namespace.values():
                        if hasattr(value, '_filter'):
                            newclass._processes.append(value)

                elif hasattr(bases[0],"_macro"):
                    for value in namespace.values():
                        if callable(value):
                            newclass._processes.append(value)

        """
        elif MacroProcess in bases:
            for value in namespace.values():
                newclass._processes.append(value)
        """
        return newclass


class Process(metaclass=MetaProcess):
    """
    All MicroProcess should inherit from.
    """

    def __call__(self, *args, **kwargs):
        """

        Sequential execution of all classes appended to the metaclass's
        _processes array.

        :param args:
        :param kwargs:
        :return:
        """

        processes = []
        for _process in self._processes:
            result = _process(self, *args, **kwargs)
            if result:
                #assert isinstance(result, MicroProcess), "{0} is not a MicroProcess".format(result)
                processes.append(result)

        return processes

class MicroProcess(Process):

    _micro = True

    def process(func):
        """
        Wraper fuction for MicoProcesses

        :return: wrapped function with _filter attribute set to true
        """
        func._filter = True
        return func

class MacroProcess(Process):
    _macro = True

class Processor(object):

    """
    This class collects Process up and then runs them.

    """



    def __init__(self):
        self._microprocesses = []

    def add(self, micro_process):
        assert isinstance(micro_process, Process), "{0} is not a Process".format(micro_process)
        self._microprocesses.append(micro_process)

    def run(self, *args, **kwargs):
        for process in self._microprocesses:
            result = process(*args, **kwargs)
            self._microprocesses += result




