"""
*What is this pattern about?
The Adapter pattern provides a different interface for a class. We can
think about it as a cable adapter that allows you to charge a phone
somewhere that has outlets in a different shape. Following this idea,
the Adapter pattern is useful to integrate classes that couldn't be
integrated due to their incompatible interfaces.



*Where is the pattern used practically?
The Grok framework uses adapters to make objects work with a
particular API without modifying the objects themselves:
http://grok.zope.org/doc/current/grok_overview.html#adapters

*References:
http://ginstrom.com/scribbles/2008/11/06/generic-adapter-class-in-python/
https://sourcemaking.com/design_patterns/adapter
http://python-3-patterns-idioms-test.readthedocs.io/en/latest/ChangeInterface.html#adapter

*TL;DR
Allows the interface of an existing class to be used as another interface.
"""

from typing import Callable, TypeVar

T = TypeVar("T")


class PPTExtractor:
    def __init__(self) -> None:
        self.name = "PPT Extractor"

    def extract_ppt(self) -> str:
        return "extracted PPT!"


class DOCExtractor:
    def __init__(self) -> None:
        self.name = "DOC Extractor"

    def extract_doc(self) -> str:
        return "extracted Doc!"



class Adapter:
    """Adapts an object by replacing methods.

    """

    def __init__(self, obj: T, **adapted_methods: Callable):
        """We set the adapted methods in the object's dict."""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object."""
        return getattr(self.obj, attr)

    def original_dict(self):
        """Print original object dict."""
        return self.obj.__dict__


def main():

    objects = []
    ppt_extractor = PPTExtractor()
    print(ppt_extractor.__dict__)
    #{'name': 'Dog'}

    objects.append(Adapter(ppt_extractor, extract=ppt_extractor.extract_ppt))


    doc_extractor = DOCExtractor()
    objects.append(Adapter(doc_extractor, extract=doc_extractor.extract_doc))


    for obj in objects:
        print("I am {0} and I will {1}".format(obj.name, obj.extract()))


main()
