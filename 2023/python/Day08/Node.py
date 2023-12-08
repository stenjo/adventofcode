
from math import gcd
import re

        
class NodeTree:
    def __init__(self, nodeStrings):
        self.nodes = {}
        
        for nodeString in nodeStrings[2:]:
            if len(nodeString) < 5:  continue
            top, left, right, _ = re.split(' = \(|, |\)', nodeString.strip())
            print(top, left, right)
            self.nodes[top] = (left, right)
            
        self.navigation = list(nodeStrings[0].strip())
    
    def navigateSteps(self):
        
        node = "AAA"
        return self.getStepsLambda(node, self.isZZZ)

    def getStepsLambda(self, node, isLastNode):
        steps = 0
        while isLastNode(node) and steps < 100000:
            dir = self.navigation[steps%len(self.navigation)]
            if dir == "L":
                node = self.nodes[node][0]
            elif dir == "R":
                node = self.nodes[node][1]
            else:
                raise ValueError("Invalid direction: ", dir)
            steps +=1
        
        return steps

    def isZZZ(self, node):
        return node != "ZZZ"

    def isAnyLastZ(self, node):
        return list(node)[-1] != "Z"
    
    def getStartingNodes(self):
        return [n for n in self.nodes if n[-1] == 'A']
    
    def isEndNodes(self, nodes):
        return len(nodes) == len(list(filter(lambda x: list(x)[-1] == 'Z', nodes)))
    
    def navigateSeveralSteps(self):
        lcm = 1
        nodes = self.getStartingNodes()
        steps = [self.getStepsLambda(node, self.isAnyLastZ) for node in nodes]
        for i in steps:
            lcm = lcm*i//gcd(lcm, i)
        
        return lcm
    
    