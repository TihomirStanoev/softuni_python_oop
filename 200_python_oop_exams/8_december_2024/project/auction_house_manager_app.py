from project.artifacts.base_artifact import BaseArtifact
from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.base_collector import BaseCollector
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:
    _VALID_ARTIFACT = {
        'RenaissanceArtifact': RenaissanceArtifact,
        'ContemporaryArtifact': ContemporaryArtifact
    }
    _VALID_COLLECTORS = {
        'Museum': Museum,
        'PrivateCollector': PrivateCollector
    }
    def __init__(self):
        self.artifacts: list[BaseArtifact] = []
        self.collectors: list[BaseCollector] = []

    def _find_name(self, collection, name) -> BaseArtifact | BaseCollector | None:
        return next((item for item in collection if item.name == name), None)

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        if artifact_type not in self._VALID_ARTIFACT.keys():
            raise ValueError('Unknown artifact type!')

        artifact = self._find_name(self.artifacts, artifact_name)

        if artifact:
            raise  ValueError(f'{artifact_name} has been already registered!')

        artifact = self._VALID_ARTIFACT[artifact_type](artifact_name, artifact_price, artifact_space)
        self.artifacts.append(artifact)

        return f'{artifact_name} is successfully added to the auction as {artifact_type}.'

    def register_collector(self, collector_type: str, collector_name: str):
        if collector_type not in self._VALID_COLLECTORS.keys():
            raise ValueError('Unknown collector type!')
        collector = self._find_name(self.collectors, collector_name)

        if collector:
            raise ValueError(f'{collector_name} has been already registered!')

        collector = self._VALID_COLLECTORS[collector_type](collector_name)
        self.collectors.append(collector)

        return f'{collector_name} is successfully registered as a {collector_type}.'

    def perform_purchase(self, collector_name: str, artifact_name: str):
        collector = self._find_name(self.collectors, collector_name)
        if collector is None:
            raise ValueError(f'Collector {collector_name} is not registered to the auction!')

        artifact = self._find_name(self.artifacts, artifact_name)
        if artifact is None:
            raise ValueError(f'Artifact {artifact_name} is not registered to the auction!')

        if not collector.can_purchase(artifact.price, artifact.space_required):
            return 'Purchase is impossible.'

        self.artifacts.remove(artifact)
        collector.purchased_artifacts.append(artifact)
        collector.available_money -= artifact.price
        collector.available_space -= artifact.space_required

        return f'{collector_name} purchased {artifact_name} for a price of {artifact.price:.2f}.'

    def remove_artifact(self, artifact_name: str):
        artifact = self._find_name(self.artifacts, artifact_name)

        if artifact is None:
            return "No such artifact."

        self.artifacts.remove(artifact)
        return f'Removed {artifact.artifact_information()}'

    def fundraising_campaigns(self, max_money: float):
        increased_collectors = 0

        for collector in self.collectors:
            if collector.available_money <= max_money:
                collector.increase_money()
                increased_collectors += 1

        return f'{increased_collectors} collector/s increased their available money.'

    def get_auction_report(self):
        total_sold_artifacts = 0
        available_artifact = len(self.artifacts)
        result = ['**Auction statistics**']
        sorted_collectors = sorted(self.collectors, key=lambda c: (-len(c.purchased_artifacts), c.name))

        result.extend([f'Available artifacts for sale: {available_artifact}','***'])
        for collector in sorted_collectors:
            total_sold_artifacts += len(collector.purchased_artifacts)
            result.append(str(collector))
        result.insert(1, f'Total number of sold artifacts: {total_sold_artifacts}')

        return '\n'.join(result).strip()





