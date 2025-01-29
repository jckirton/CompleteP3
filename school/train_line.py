class Station:
    def __init__(self, name: str, *connected):
        self.name = name
        self.line = None
        self.connected = list(connected)

        for statn in self.connected:
            if self not in statn.connected:
                statn.connected.append(self)

    def __str__(self):
        return f"Station Name: {self.name}\nLine: {self.line.name}\nConnected Stations: {', '.join(f'{s.name}' for s in self.connected)}"

    def __repr__(self):
        return self.name


class Line:
    def __init__(self, name: str, *stations: Station):
        self.name = name
        self.stations = list(stations)

        for statn in self.stations:
            statn.line = self

    def __str__(self):
        return f"Line Name: {self.name}\nStations:\n  {'\n  '.join(f'{s.name}' for s in self.stations)}"

    def __repr__(self):
        return self.name


a = Station("A")
b = Station("B", a)
c = Station("C", b)
d = Station("D", c)
e = Station("E", d)
f = Station("F", e)

line1 = Line("Line 1", a, b, c, d)
line2 = Line("Line 2", e, f)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(line1)
print(line2)
