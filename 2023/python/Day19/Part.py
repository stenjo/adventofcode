class Part:
    def __init__(self, input):
        self.rating = {}
        ratings = input.strip()[1:-1].split(",")
        for rating in ratings:
            key, value = rating.split("=")
            self.rating[key] = int(value)

    def validate(self, rules):
        for rule in rules:
            if ":" not in rule:
                return rule

            workflow, param, op, value = self.splitRule(rule)
            if (op == ">" and self.rating[param] > value) or (
                op == "<" and self.rating[param] < value
            ):
                return workflow

    def splitRule(self, rule):
        comp, workflow = rule.split(":")

        param = comp[0]
        op = comp[1]
        value = int(comp[2:])
        return workflow, param, op, value
