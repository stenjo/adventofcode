from math import gcd, lcm
from Day20.Module import Module


class Machine:
    def __init__(self, input):
        self.modules = {}
        for line in input.strip().split("\n"):
            m, subs = line.split(" -> ")
            type, name = m[0], m[1:].strip()
            if type not in "%&":
                name = m.strip()
            subscribers = [s.strip() for s in subs.split(",")]
            self.modules[name] = Module(type, subscribers)

        for name, module in [
            (name, module)
            for name, module in self.modules.items()
            if module.type == "&"
        ]:
            module.setSenders(self.getSenders(name))

    def getSenders(self, module: str):
        senders = [k for k, v in self.modules.items() if module in v.subscribers]
        return senders

    def signal(self, signal):
        receivers = [("button", "broadcaster", signal)]
        highs = 0
        lows = 0
        while len(receivers) > 0:
            origin, receiver, signal = receivers[0]

            if signal:
                highs += 1
            else:
                lows += 1

            # print( origin, "-", signal, "->", receiver)
            if receiver in self.modules.keys():
                signal, destinations = self.modules[receiver].signal(origin, signal)
                for d in destinations:
                    receivers.append((receiver, d, signal))

            receivers = receivers[1:]

        return highs, lows

    def sumHighsAndLows(self, pushes):
        highs = []
        lows = []
        for n in range(pushes):
            h, l = self.signal(False)
            highs.append(h)
            lows.append(l)

        return sum(highs) * sum(lows)

    def minButtonPresses(self, module):
        [senderId] = self.getSenders(module)
        sender = self.modules[senderId]
        cycles = {m: None for m in sender.senderStates.keys()}

        presses = 0
        while None in cycles.values() and presses < 4000:
            presses += 1
            self.signal(False)
            for m in cycles.keys():
                if self.modules[m].stateChanged == True:
                    if cycles[m] == None:
                        cycles[m] = presses
                        print(cycles)

        return lcm(*cycles.values())
