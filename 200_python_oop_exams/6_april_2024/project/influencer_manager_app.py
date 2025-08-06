from collections import defaultdict

from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    _VALID_INFLUENCERS = {
        "PremiumInfluencer": PremiumInfluencer,
        "StandardInfluencer": StandardInfluencer
    }
    _VALID_CAMPAIGN = {
        "HighBudgetCampaign": HighBudgetCampaign,
        "LowBudgetCampaign": LowBudgetCampaign
    }
    def __init__(self):
        self.influencers: list[BaseInfluencer] = []
        self.campaigns: list[BaseCampaign] = []

    def _find_influencer_by_username(self, username):
        return next((f for f in self.influencers if f.username == username), None)

    def _find_campaign_by_id(self, campaign_id):
        return next((c for c in self.campaigns if c.campaign_id == campaign_id), None)


    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self._VALID_INFLUENCERS.keys():
            return f'{influencer_type} is not an allowed influencer type.'

        influencer = self._find_influencer_by_username(username)
        if influencer:
            return f'{username} is already registered.'

        influencer = self._VALID_INFLUENCERS[influencer_type](username,followers,engagement_rate)
        self.influencers.append(influencer)
        return f'{username} is successfully registered as a {influencer_type}.'

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self._VALID_CAMPAIGN.keys():
            return f'{campaign_type} is not a valid campaign type.'
        campaign = self._find_campaign_by_id(campaign_id)

        if campaign:
            return f'Campaign ID {campaign_id} has already been created.'

        campaign = self._VALID_CAMPAIGN[campaign_type](campaign_id,brand,required_engagement)
        self.campaigns.append(campaign)
        return f'Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}.'

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer = self._find_influencer_by_username(influencer_username)
        if influencer is None:
            return f'Influencer \'{influencer_username}\' not found.'

        campaign = self._find_campaign_by_id(campaign_id)
        if campaign is None:
            return f'Campaign with ID {campaign_id} not found.'

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f'Influencer \'{influencer_username}\' does not meet the eligibility criteria for the campaign with ID {campaign_id}.'

        influencer_payment = influencer.calculate_payment(campaign)

        if influencer_payment <= 0:
            return None

        campaign.budget -= influencer_payment
        campaign.approved_influencers.append(influencer)
        influencer.campaigns_participated.append(campaign)

        return f'Influencer \'{influencer_username}\' has successfully participated in the campaign with ID {campaign_id}.'

    def calculate_total_reached_followers(self) -> dict[BaseCampaign: int]:
        total_followers = defaultdict(int)

        for campaign in self.campaigns:
            for influencer in campaign.approved_influencers:
                followers = influencer.reached_followers(campaign.campaign_type)
                if followers > 0:
                    total_followers[campaign] += followers

        return total_followers

    def influencer_campaign_report(self, username: str):
        influencer = self._find_influencer_by_username(username)

        if influencer is None:
            return f'{username} has not participated in any campaigns.'
        return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        total_followers = self.calculate_total_reached_followers()

        result = ['$$ Campaign Statistics $$']
        for campaign in sorted(self.campaigns, key=lambda c: (len(c.approved_influencers), -c.budget)):
            total_reached_followers = total_followers.get(campaign, 0)
            result.append(f'  * Brand: {campaign.brand}, Total influencers: {len(campaign.approved_influencers)}, Total budget: ${campaign.budget:.2f}, Total reached followers: {total_reached_followers}')

        return '\n'.join(result).strip()