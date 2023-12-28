from collections import defaultdict


class Mirror:
    def __init__(self, input):
        self.mirror = [line.strip() for line in input if line]

    def findMirrorLine(self, mirror):
        mirrorLines = self.findMirrorLines(mirror)
        return list(set.intersection(*map(set, mirrorLines)))

    def findMirrorLines(self, mirror=None):
        if mirror is None:
            mirror = self.mirror
        mirrorLines = [
            [i for i in range(len(line)) if self.isMirror(line, i) and i > 0]
            for line in mirror
        ]
        return mirrorLines

    def findMirrorCol(self, mirror=None):
        if not mirror:
            mirror = self.mirror
        lines = self.findMirrorLine(mirror)
        return lines[-1] if len(lines) > 0 else None

    def findMirrorRow(self):
        t = list(map(list, zip(*self.mirror)))
        return self.findMirrorCol(t)

    def isMirror(self, line, p):
        mRange = min([len(line) - p, p])
        return line[p - mRange : p] == line[p : p + mRange][::-1]

    def findCandidateSmudgedMirror(self, mirror=None):
        if mirror is None:
            mirror = self.mirror
        mirrorLines = self.findMirrorLines(mirror)
        candidates = defaultdict(int)
        for mList in mirrorLines:
            for r in mList:
                candidates[r] += 1

        lineFreqList = [
            (line, candidates[line])
            for line in sorted(candidates, key=candidates.get, reverse=True)
        ]
        return lineFreqList

    def findCandidateCol(self, mirror=None):
        if not mirror:
            mirror = self.mirror
        lines = self.findCandidateSmudgedMirror(mirror)
        d = {c: r for (r, c) in lines}
        return d[len(mirror) - 1] if (len(mirror) - 1) in d.keys() else None

    def findCandidateRow(self):
        t = ["".join(l) for l in map(list, zip(*self.mirror))]
        return self.findCandidateCol(t)
