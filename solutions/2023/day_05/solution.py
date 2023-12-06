# puzzle prompt: https://adventofcode.com/2023/day/5
import re

from ...base import TextSolution, answer


def create_dict(map: list):
    mapping = {}
    for row in map:
        for idx, source in enumerate(range(row[1], row[1] + row[2])):
            mapping[source] = row[0] + idx
    return mapping


class Solution(TextSolution):
    _year = 2023
    _day = 5

    # @answer(1234)
    def part_1(self) -> int:
        seeds = [
            int(seed)
            for seed in re.search(r"seeds:.*\n", self.input)
            .group()
            .split(": ")[1]
            .split()
        ]
        text = re.sub(r"seeds:.*\n\n", "", self.input)
        text = re.sub(r".*:.*\n", "", text).split("\n\n")
        maps = [[map.split() for map in group.split("\n")] for group in text]
        maps = [[[int(val) for val in row] for row in map] for map in maps]
        print(maps)

        seed_to_soil = create_dict(maps[0])
        soil_to_fertilizer = create_dict(maps[1])
        fertilizer_to_water = create_dict(maps[2])
        water_to_light = create_dict(maps[3])
        light_to_temperature = create_dict(maps[4])
        temperature_to_humidity = create_dict(maps[5])
        humidity_to_location = create_dict(maps[6])

        locations = []
        for seed in seeds:
            print(seed)
            soil = seed_to_soil.get(seed, seed)
            fertilizer = soil_to_fertilizer.get(soil, soil)
            water = fertilizer_to_water.get(fertilizer, fertilizer)
            light = water_to_light.get(water, water)
            temperature = light_to_temperature.get(light, light)
            humidity = temperature_to_humidity.get(temperature, temperature)
            locations.append(humidity_to_location.get(humidity, humidity))

        return min(locations)

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
