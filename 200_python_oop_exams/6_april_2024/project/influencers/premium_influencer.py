from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    _PAYMENT_PERCENTAGE = 0.85
    _CALCULATE_REACHED = {
        'HighBudgetCampaign': 1.5,
        'LowBudgetCampaign': 0.8,
    }
    def calculate_payment(self, campaign: BaseCampaign):
        return campaign.budget * self._PAYMENT_PERCENTAGE

    def reached_followers(self, campaign_type: str):
        return int(self._CALCULATE_REACHED[campaign_type] * self.engagement_rate *  self.followers)

