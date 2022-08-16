class AFNe():
    def __init__(self, q: set, sigma: set, delta: dict, q0: str, f: set):
        self.q = q
        self.sigma = sigma
        self.delta = delta
        self.q0 = q0
        self.f = f

        assert q0 in q, "q0 informado nao esta no conjunto de estados possiveis Q"
        assert f.issubset(q), "F nao eh subconjunto dos estados possiveis Q"

    def __str__(self) -> str:
        msg = "Q: {}\n".format(", ".join(sorted(list(self.q))))
        msg += "Sigma: " + ", ".join(sorted(list(self.sigma))) + "\n"
        msg += "Delta:\n"
        for t in self.delta:
            msg += "  delta({}, {}) = {}\n".format(*t, self.delta[t]) 
        msg += "q0: {}\n".format(self.q0)
        msg += "F: {}\n".format(", ".join(sorted(list(self.f))))

        return msg

    def _delta(self, q: set, w: str or list) -> set:
        if len(w) == 0:
            return self._epsilon(q)
        else:
            return set().union(*[self._epsilon(self.delta[(s, w[-1])]) for s in self._delta(q, w[:-1]) if (s, w[-1]) in self.delta])

    def _epsilon(self, q: set):
        return q | set().union(*[self._epsilon(self.delta[(s, "epsilon")]) for s in q if (s, "epsilon") in self.delta])

    def accepts(self, w: str or list):
        try:
            result = self._delta({self.q0}, w)
        except KeyError:
            result = set()
        print("delta({}, {}): {}".format(self.q0, w if w else '""', result))
        if result & self.f != set():
            return "Sim"
        return "Nao"

    def eClosure(self, state, delta):
        for key, value in delta:
            if key[0] == state and key[1] == 'epsilon':
                element = [e for e in value][0]
                return [key[0]] + self.eClosure(element, delta)
        return [state]

    def checkDelta(self, q, s, delta, eClosures):
        for key, value in delta:
            if q == key[0] and s == key[1]:
                return q
        
        for key1 in eClosures["e-(" + q + ")"]:
            for key2, value2 in delta:
                if key1 == key2[0] and s == key2[1]:
                    return key2[0]
        return False

    def findFinalStates(self, eClosures):
        finals = []
        for f in list(self.f):
            for e in eClosures:
                if f in eClosures[e]:
                    for eIntern in eClosures[e]:
                        if eIntern not in finals:
                            finals.append(eIntern)
        return finals
                    
    def convert(self):
        eClosures = {}
        for q in sorted(self.q):
            eClosure = self.eClosure(q, sorted(self.delta.items()))
            eClosures["e-(" + q + ")"] = eClosure

        newDelta = {}
        for q in sorted(self.q):
            for s in sorted(self.sigma):
                element = self.checkDelta(q, s, sorted(self.delta.items()), eClosures)
                if element:
                    newDelta[(q, s)] = eClosures["e-(" + element + ")"]
        
        print("Automato convertido para AFN:")
        print("\tQ: ", self.q)
        print("\tSigma: ", self.sigma)
        print("\tDelta: ")
        for delta in newDelta:
            print("\t\tdelta({}, {}) = {}".format(delta[0], delta[1], newDelta[(delta[0], delta[1])]))
        print("\tq0: ", self.q0)
        print("\tF: {}".format(self.findFinalStates(eClosures)))