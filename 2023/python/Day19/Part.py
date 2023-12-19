class Part:
    def __init__(self, input):
        self.rating = {}
        ratings = input.strip()[1:-1].split(",")
        for rating in ratings:
            key, value = rating.split("=")
            self.rating[key] = int(value)

    def validate(self, rule):
        if "," not in rule:
            return rule
        param = rule[0]
        op = rule[1]
        value = int(rule.split(":")[0][2:])
        workflow = rule.split(":")[1]
        first, second = workflow.split(",")
        if op == ">":
            return first if self.rating[param] > value else second
        if op == "<":
            return first if self.rating[param] < value else second
        else:
            return None
