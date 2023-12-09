class NumberSequence:
    def __init__(self, sequencesStrings):
        self.sequences = [
            [int(n) for n in nList]
            for nList in [seqStr.split() for seqStr in sequencesStrings]
        ]

    def newSequence(self, sequence):
        if len(sequence) < 2:
            return []
        t = [
            (a, sequence[i + 1])
            for i, a in enumerate(sequence)
            if i < len(sequence) - 1
        ]
        return [a[1] - a[0] for a in t]

    def allZeros(self, sequence):
        zeros = list(set(list(sequence)))
        return len(zeros) == 1 and zeros[0] == 0

    def nextNumber(self, sequence):
        if self.allZeros(self.newSequence(sequence)) == False:
            return sequence[-1] + self.nextNumber(self.newSequence(sequence))

        return sequence[-1]

    def previousNumber(self, sequence):
        if self.allZeros(self.newSequence(sequence)) == False:
            return sequence[0] - self.previousNumber(self.newSequence(sequence))

        return sequence[0]

    def sumOfNextNumbers(self):
        return sum([self.nextNumber(numbers) for numbers in self.sequences])

    def sumOfPreviousNumbers(self):
        return sum([self.previousNumber(numbers) for numbers in self.sequences])
