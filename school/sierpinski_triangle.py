class SierpTriangle:
    def __init__(self, stage: int = 0):
        # Total number of segments and the number of colored and uncolored segments.
        self.stage = stage
        self.segments_count = 4**self.stage
        self.segments_colored = 3**self.stage
        self.segments_uncolored = self.segments_count - (3**self.stage)
        # The colored and uncolored segment areas.
        self.colored_area = 1 * ((3 / 4) ** self.stage)  # Stage 0 = 1
        self.uncolored_area = 1 - self.colored_area  # Whatever area isn't colored.
        # The colored and uncolored segment areas shown as fractions.
        self.colored_area_frac = f"{self.segments_colored}/{self.segments_count}"
        self.uncolored_area_frac = f"{self.segments_uncolored}/{self.segments_count}"

    def __repr__(self):
        return f"Stage {self.stage}"

    def __str__(self):
        return f"Sierpinski Triangle\n  - Stage = {self.stage}\n\nSegment Counts\n  - Number of Segments = {self.segments_count}\n  - Colored Segments = {self.segments_colored}\n  - Uncolored Segments = {self.segments_uncolored}\n\nSegment Areas (Where the area of colored segments is 1 unit at stage 0.)\n  - Colored Area = {self.colored_area} Units\n  - Uncolored Area = {self.uncolored_area} Units\n  - Fraction Representation\n    - Colored Area (fraction representation) = {self.colored_area_frac} Units\n    - Uncolored Area (fraction representation) = {self.uncolored_area_frac} Units"


stagen = input()
# print("\n" * 100)
print(SierpTriangle(int(stagen)))
