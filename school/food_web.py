from enum import Enum, auto


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class RANKS(AutoName):
    PRODUCER = auto()
    PRIMARY = auto()
    SECONDARY = auto()
    TERTIARY = auto()
    DECOMPOSER = auto()


class Entity:
    def __init__(
        self,
        name: str,
        prey: list | None = None,
        decomposer: bool = False,
    ):
        self.name = name
        self.predator = []
        self.prey = prey
        self.apex = False

        pri_prey = False
        sec_prey = False
        if self.prey:
            for thing in self.prey:
                if thing.rank == RANKS.PRIMARY:
                    pri_prey = True
                if thing.rank == RANKS.SECONDARY:
                    sec_prey = True

        if decomposer:
            self.rank = RANKS.DECOMPOSER
        elif not prey and not decomposer:
            self.rank = RANKS.PRODUCER
        elif prey:
            if sec_prey:
                self.rank = RANKS.TERTIARY
            elif pri_prey and not sec_prey:
                self.rank = RANKS.SECONDARY
            elif not pri_prey and not sec_prey:
                self.rank = RANKS.PRIMARY

        if prey:
            for thing in prey:
                thing.predator.append(self)

    def __str__(self):
        return f"I am {self.name}, of rank {self.rank.value}{', and an apex predator' if self.apex else ''}.\nI{f' eat {', '.join(f'{thing.name}' for thing in self.prey)}, and' if self.prey else ''} am eaten by {'nothing' if not self.predator else ', '.join(f'{thing.name}' for thing in self.predator)}."

    def __repr__(self):
        return self.name


class FoodWeb:
    def __init__(self, *entities: Entity):
        self.entities: dict[Entity, dict] = {}
        self.catagorised = {
            "Decomposer": [],
            "Producer": [],
            "Primary": [],
            "Secondary": [],
            "Tertiary": [],
            "Apex": [],
        }

        for entity in entities:
            self.entities[entity] = {
                "Name": entity.name,
                "Rank": entity.rank,
                "Apex": entity.apex,
                "Object": entity,
            }

        for entity in self.entities:
            if not entity.predator and entity.prey:
                entity.apex = True
                self.entities[entity]["Apex"] = entity.apex
                self.catagorised["Apex"].append(entity)
            if entity.rank == RANKS.DECOMPOSER:
                self.catagorised["Decomposer"].append(entity)
            elif entity.rank == RANKS.PRODUCER:
                self.catagorised["Producer"].append(entity)
            elif entity.rank == RANKS.PRIMARY:
                self.catagorised["Primary"].append(entity)
            elif entity.rank == RANKS.SECONDARY:
                self.catagorised["Secondary"].append(entity)
            elif entity.rank == RANKS.TERTIARY and entity.predator:
                self.catagorised["Tertiary"].append(entity)


# plant = Entity("Plant")
# prim = Entity("prim", prey=[plant])
# sec = Entity("sec", prey=[prim])

# web = FoodWeb(plant, prim, sec)

# print("\n")
# print(plant)
# print("\n")
# print(prim)
# print("\n")
# print(sec)
# print("\n")
# print("\n")

# print(web.entities)
# print("\n")
# print(web.catagorised)

kpp = Entity("King Protea Plant")
at = Entity("Acacia Tree")
fs = Entity("Forage Shrub")

gh = Entity("Grasshopper", prey=[fs, kpp])
wb = Entity("Wombat", prey=[fs])
kl = Entity("Koala", prey=[kpp, at, fs])
kr = Entity("Kangaroo", prey=[kpp, fs])

bd = Entity("Budgie", prey=[gh])
bb = Entity("Bilbies", prey=[gh])

qu = Entity("Quoll", prey=[bd])
em = Entity("Emu", prey=[kpp, fs, gh])
py = Entity("Python", prey=[bb, kr])
dg = Entity("Dingo", prey=[qu, kr, py, kl, wb, bb, em])
py.prey.append(dg)
dg.predator.append(py)
wte = Entity("Wedge Tailed Eagle", prey=[bb, wb, em, kl, kr, qu, py])

db = Entity("Dung Beetle", decomposer=True)

web = FoodWeb(kpp, at, fs, gh, wb, kl, kr, bd, bb, qu, em, py, dg, wte, db)

print(web.entities, "\n\n", web.catagorised)

for e in web.entities:
    print("\n")
    print(e)
