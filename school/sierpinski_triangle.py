class SierpTriangle:
    def __init__(self, stage: int = 0):
        self.stage = stage
        self.segments_count = 4**self.stage
        self.segments_colored = 3**self.stage
        self.segments_uncolored = self.segments_count - (3**self.stage)

    def __repr__(self):
        return f"Stage {self.stage}"

    def __str__(self):
        return f"Sierpinski Triangle\n  - Stage = {self.stage}\n  - Number of Segments = {self.segments_count}\n  - Colored Segments = {self.segments_colored}\n  - Uncolored Segments = {self.segments_uncolored}"


print(SierpTriangle(3))
