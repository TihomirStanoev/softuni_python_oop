from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    VALID_DIVER = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    VALID_FISH = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}
    def __init__(self):
        self.divers: list[BaseDiver] = []
        self.fish_list: list[BaseFish] = []

    def _find_diver_by_name(self, diver_name) -> BaseDiver | None:
        return next((d for d in self.divers if d.name == diver_name) , None)

    def _find_fish_by_name(self, fish_name) -> BaseFish | None:
        return next((f for f in self.fish_list if f.name == fish_name), None)

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_DIVER.keys():
            return f'{diver_type} is not allowed in our competition.'
        diver = self._find_diver_by_name(diver_name)

        if diver:
            return f'{diver_name} is already a participant.'

        diver = self.VALID_DIVER[diver_type](diver_name)
        self.divers.append(diver)
        return f'{diver_name} is successfully registered for the competition as a {diver_type}.'

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISH.keys():
            return f'{fish_type} is forbidden for chasing in our competition.'

        fish = self._find_fish_by_name(fish_name)
        if fish:
            return f'{fish_name} is already permitted.'

        fish = self.VALID_FISH[fish_type](fish_name, points)
        self.fish_list.append(fish)
        return f'{fish_name} is allowed for chasing as a {fish_type}.'


    def health_recovery(self):
        count = 0
        for diver in self.divers:
            if diver.has_health_issue:
                count += 1
                diver.update_health_status()
                diver.renew_oxy()
        return f'Divers recovered: {count}'

    def diver_catch_report(self,diver_name: str):
        diver = self._find_diver_by_name(diver_name)
        result = [f'**{diver_name} Catch Report**']

        for fish in diver.catch:
            result.append(fish.fish_details())

        return '\n'.join(result)

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = self._find_diver_by_name(diver_name)
        if diver is None:
            return f'{diver_name} is not registered for the competition.'

        fish = self._find_fish_by_name(fish_name)
        if fish is None:
            return f'The {fish_name} is not allowed to be caught in this competition.'

        if diver.has_health_issue:
            return f'{diver_name} will not be allowed to dive, due to health issues.'

        equal_zero = diver.oxygen_level == fish.time_to_catch

        if diver.oxygen_level < fish.time_to_catch or (equal_zero and not is_lucky):
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f'{diver.name} missed a good {fish.name}.'

        elif diver.oxygen_level > fish.time_to_catch or (equal_zero and is_lucky):
            diver.hit(fish)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f'{diver.name} hits a {fish.points}pt. {fish.name}.'
        return None


    def competition_statistics(self):
        sorted_diver = [diver for diver in sorted(self.divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name)) if not diver.has_health_issue]
        result = ['**Nautical Catch Challenge Statistics**']
        for diver in sorted_diver:
            result.append(str(diver))

        return '\n'.join(result)


