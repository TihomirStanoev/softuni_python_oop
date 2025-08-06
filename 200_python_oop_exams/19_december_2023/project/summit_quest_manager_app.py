from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    __VALID_CLIMBERS = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}
    __VALID_PEAKS = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}
    def __init__(self):
        self.climbers: list[BaseClimber] = []
        self.peaks: list[BasePeak] = []

    def _find_climber_by_name(self, climber_name):
        return next((c for c in self.climbers if c.name == climber_name), None)

    def _find_peak_by_name(self, peak_name):
        return next((p for p in self.peaks if p.name == peak_name), None)

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.__VALID_CLIMBERS.keys():
            return f'{climber_type} doesn\'t exist in our register.'
        climber = self._find_climber_by_name(climber_name)

        if climber:
            return f'{climber_name} has been already registered.'

        climber = self.__VALID_CLIMBERS[climber_type](climber_name)
        self.climbers.append(climber)
        return f'{climber_name} is successfully registered as a {climber_type}.'

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.__VALID_PEAKS.keys():
            return f'{peak_type} is an unknown type of peak.'
        peak = self.__VALID_PEAKS[peak_type](peak_name,peak_elevation)
        self.peaks.append(peak)
        return f'{peak_name} is successfully added to the wish list as a {peak_type}.'

    def check_gear(self, climber_name: str, peak_name: str, gear: list[str]):
        climber = self._find_climber_by_name(climber_name)
        peak = self._find_peak_by_name(peak_name)

        peak_gear = set(peak.get_recommended_gear())
        needed_gear = set(gear)
        missing_gear = peak_gear.difference(needed_gear)

        if not missing_gear:
            return f'{climber_name} is prepared to climb {peak_name}.'
        climber.is_prepared = False
        return f'{climber_name} is not prepared to climb {peak_name}. Missing gear: {", ".join(sorted(missing_gear))}.'


    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = self._find_climber_by_name(climber_name)
        if climber is None:
            return f'Climber {climber_name} is not registered yet.'
        peak = self._find_peak_by_name(peak_name)
        if peak is None:
            return f'Peak {peak_name} is not part of the wish list.'

        if climber.can_climb() and climber.is_prepared:
            climber.climb(peak)
            return f'{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}.'

        if not climber.is_prepared:
            return f'{climber_name} will need to be better prepared next time.'

        climber.rest()
        return f'{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest.'

    def get_statistics(self):
        successfully_conquer = list(filter(lambda c: len(c.conquered_peaks) > 0, self.climbers))
        total_conquered_peaks = set()

        for climber in successfully_conquer:
            total_conquered_peaks.update(climber.conquered_peaks)

        climber_statistics = '\n'.join(str(c) for c in sorted(successfully_conquer, key=lambda p: (-len(p.conquered_peaks), p.name)))

        result = [f'Total climbed peaks: {len(total_conquered_peaks)}',
                  '**Climber\'s statistics:**']
        result.append(climber_statistics)

        return '\n'.join(result).strip()

