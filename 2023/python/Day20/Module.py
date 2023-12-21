class Module:
    def __init__(self, type, subscribers=[]):
        self.subscribers = subscribers
        self.type = type
        self.stateChanged = None
        self.state = False
        self.senderStates = {}

    def setSenders(self, senders):
        for sender in senders:
            self.senderStates[sender] = False

    def signal(self, sender, signal: bool):
        self.stateChanged = signal if self.stateChanged != None else None
        match self.type:
            case "&":
                self.senderStates[sender] = signal
                signal = not all(self.senderStates.values())
                return signal, self.subscribers

            case "%":
                if signal == False:
                    self.state = not self.state
                    return self.state, self.subscribers
                else:
                    return signal, []
            case _:
                return signal, self.subscribers
