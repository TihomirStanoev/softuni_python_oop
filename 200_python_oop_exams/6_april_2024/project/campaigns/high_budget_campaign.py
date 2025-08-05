from project.campaigns.base_campaign import BaseCampaign


class HighBudgetCampaign(BaseCampaign):
    _REQUIRED_ENGAGEMENT = 1.2
    def __init__(self,campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id=campaign_id, brand=brand, required_engagement=required_engagement, budget=5000.0)

    def check_eligibility(self, engagement_rate: float):
        return engagement_rate >= (self._REQUIRED_ENGAGEMENT * self.required_engagement)

