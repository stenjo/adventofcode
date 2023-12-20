from functools import reduce
from Day19.Part import Part


class Sorter:
    def __init__(self, input):
        workflows, parts = input.strip().split("\n\n")
        self.workflows = {}
        self.A = []
        self.R = []
        self.parts = [Part(p) for p in parts.strip().split()]
        for w in workflows.split("\n"):
            name, rules = self.splitWorkflow(w)
            self.workflows[name] = rules

    def splitWorkflow(self, workflow):
        name, instructions, _ = workflow.replace("{", "}").split("}")
        return (name, instructions.split(","))

    def run(self):
        for part in self.parts:
            workflow = "in"
            rules = self.workflows[workflow]
            workflow = part.validate(rules)
            while workflow in self.workflows.keys():
                workflow = part.validate(self.workflows[workflow])

            if workflow == "A":
                self.A.append(part)
            elif workflow == "R":
                self.R.append(part)

        return self.A

    def ratingsOfAccepted(self):
        partRatings = [sum(p.rating.values()) for p in self.run()]
        return sum(partRatings)

    def getCombination(self, workflow):
        ratings = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
        path = [workflow]

    def reverse(self):
        # rfg{s<537:gd,x>2440:R,A}
        # wfl: [(rating:(min,max), source)]
        for w, rules in self.workflows.items():
            for rule in rules[::-1]:
                wfl = None
                if ":" not in rule:
                    wfl = rule
                else:
                    workflow, param, op, value = Part().splitRule(rule)
                    if op == ">":
                        lim = {param: (0, value)}
                        self.rev[wfl].append(lim)

    def getDistinctCombinations(self):
        return 0
