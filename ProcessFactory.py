from collections import OrderedDict

class MetaProcess(type):

    @classmethod
    def __prepare__(metacls, name, bases):
        return OrderedDict()

    def __new__(metacls, name, bases, namespace, **kwds):
        newclass = type.__new__(metacls, name, bases, dict(namespace))

        newclass._processes = []
        for value in namespace.values():
            if hasattr(value, '_filter'):
                newclass._processes.append(value)
        return newclass

class MicroProcess(metaclass=MetaProcess):
    """
    The base class for scraping objects.
    """

    def __call__(self, *args, **kwargs):

        processes = []
        for _process in self._processes:
            processes.append(_process(self, *args, **kwargs))

        return processes

    def process(func):
        func._filter = True
        return func


class Processor(object):

    def __init__(self):
        self._processes = []

    def add(self, microProcess):
        assert isinstance(microProcess, MicroProcess), "{0} is not a MicroProcess".format(microProcess)
        self._process.append(microProcess)

    def run(self, *args, **kwargs):
        for process in self._processes:
            result = process(*args, **kwargs)
            assert isinstance(result, MicroProcess), "{0} is not a MicroProcess".format(result)
            self._process.append(result)