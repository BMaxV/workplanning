#import cybernetics

class Problem:
    def __init__(self,desc):
        self.descriptiontext=desc
        assert type(desc)==str

class Actor:
    def __init__(self):
        self.someid=None
        self.descriptiontext=None

class Approach:
    def __init__(self):
        self.abstract=""
        seld.detailed_text=""


class DummyNode:
    def __init__(self):
        self.elements=[None,None,None]

def format_check(node):
    try:
        assert type(node.elements[0]) == Problem
        assert type(node.elements[1]) in [type(None),Actor]
        assert type(node.elements[2]) in [type(None),Approach]
    except:
        raise TypeError("node does not conform to the defined format")

D=DummyNode()
P=Problem("i want cake")
D.elements[0]=P

format_check(D)
print("this is fine")
