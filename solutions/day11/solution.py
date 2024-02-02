# puzzle prompt: https://adventofcode.com/2016/day/11

import sys
sys.path.insert(0, "..")
from base.utils import shortest_path
from base.advent import *
from typing import NamedTuple
import itertools as it
from parse import findall


class FloorState(NamedTuple):
    rtgs: frozenset[str] = frozenset()
    chips: frozenset[str] = frozenset()

    def is_safe(self):
        return len(self.rtgs) == 0 or self.chips.issubset(self.rtgs)


class BuildingState(NamedTuple):
    floors: tuple[FloorState, ...]
    elevator: int

    def is_safe(self):
        return all(floor.is_safe() for floor in self.floors)

    def move_with(self, dir: int, rtgs=frozenset(), chips=frozenset()):
        i_curr = self.elevator
        i_next = self.elevator + dir

        floor_curr = self.floors[i_curr]
        floor_next = self.floors[i_next]

        floor_curr_new = FloorState(
            rtgs=floor_curr.rtgs.difference(rtgs),
            chips=floor_curr.chips.difference(chips),
        )
        floor_next_new = FloorState(
            rtgs=floor_next.rtgs.union(rtgs),
            chips=floor_next.chips.union(chips),
        )

        return BuildingState(
            floors=tuple(
                floor_curr_new
                if i == i_curr
                else floor_next_new
                if i == i_next
                else floor
                for i, floor in enumerate(self.floors)
            ),
            elevator=i_next,
        )

    def normalize(self) -> "BuildingState":
        rtg_map = {}
        chip_map = {}
        elts = set()
        for i, floor in enumerate(self.floors):
            elts.update(floor.rtgs)
            for rtg in floor.rtgs:
                rtg_map[rtg] = i
            for chip in floor.chips:
                chip_map[chip] = i
        return self.rename_by(
            {
                old_name: new_name
                for old_name, new_name in zip(
                    sorted(elts, key=lambda elt: (
                        rtg_map[elt], chip_map[elt])),
                    sorted(elts),
                )
            }
        )

    def rename_by(self, names: dict[str, str]):
        return self._replace(
            floors=tuple(
                FloorState(
                    rtgs=frozenset(names[rtg] for rtg in floor.rtgs),
                    chips=frozenset(names[chip] for chip in floor.chips),
                )
                for floor in self.floors
            )
        )


def get_neighbors(state: BuildingState):
    for dir in [-1, 1]:
        elevator_next = state.elevator + dir
        if 0 <= elevator_next < len(state.floors):
            floor = state.floors[state.elevator]
            rtgs = [(rtg, "rtg") for rtg in floor.rtgs]
            chips = [(chip, "chip") for chip in floor.chips]
            for combo in it.combinations(rtgs + chips, 2):
                state_next = state.move_with(
                    dir,
                    rtgs=frozenset(
                        (name for name, kind in combo if kind == "rtg")),
                    chips=frozenset(
                        (name for name, kind in combo if kind == "chip")),
                )
                if state_next.is_safe():
                    yield state_next.normalize()
            for rtg in floor.rtgs:
                state_next = state.move_with(dir, rtgs=frozenset((rtg,)))
                if state_next.is_safe():
                    yield state_next.normalize()
            for chip in floor.chips:
                state_next = state.move_with(dir, chips=frozenset((chip,)))
                if state_next.is_safe():
                    yield state_next.normalize()


class Solution(InputAsLinesSolution):
    _year = 2016
    _day = 11

    def setup(self, lines, extra):
        floors: list[FloorState] = []
        elts = set()

        for line in lines:
            rtgs = set()
            chips = set()
            for (rtg,) in findall("{:l} generator", line):
                rtgs.add(rtg)
            for (chip,) in findall("{:l}-compatible microchip", line):
                chips.add(chip)
            elts.update(rtgs)
            floors.append(FloorState(
                rtgs=frozenset(rtgs), chips=frozenset(chips)))

        initial1 = BuildingState(tuple(floors), 0)
        final1 = BuildingState(
            floors=(FloorState(),) * (len(floors) - 1)
            + (FloorState(rtgs=frozenset(elts), chips=frozenset(elts)),),
            elevator=len(floors) - 1,
        )

        if extra:
            new_elements = {"elerium", "dilithium"}
            initial2 = initial1._replace(
                floors=(
                    FloorState(
                        rtgs=initial1.floors[0].rtgs.union(new_elements),
                        chips=initial1.floors[0].chips.union(new_elements),
                    ),
                )
                + initial1.floors[1:]
            )
            final2 = final1._replace(
                floors=final1.floors[:-1]
                + (
                    FloorState(
                        rtgs=final1.floors[-1].rtgs.union(new_elements),
                        chips=final1.floors[-1].chips.union(new_elements),
                    ),
                )
            )
            return (initial2, final2)
        else:
            return (initial1, final1)

    def find_shortest(self, lines, extra=False):
        (initial, final) = self.setup(lines, extra)

        res = shortest_path(initial, final, get_neighbors)

        return res

    def part_1(self):
        res = self.find_shortest(self.input)

        self.solve("1", res)

    def part_2(self):
        res = self.find_shortest(self.input, True)

        self.solve("2", res)


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()
