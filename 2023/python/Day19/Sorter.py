from functools import reduce
from Day19.Part import Part


class Sorter:
    def __init__(self, input):
        workflows, parts = input.strip().split("\n\n")
        self.workflows = {}
        self.A = []
        self.R = []
        self.parts = [Part(p) for p in parts.strip().split()]
        for name, instructions, _ in [
            (w.replace("{", "}").split("}")) for w in workflows.split("\n")
        ]:
            self.workflows[name] = instructions.split(",")

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

    def getDistinctCombinations(self):
        return 0
