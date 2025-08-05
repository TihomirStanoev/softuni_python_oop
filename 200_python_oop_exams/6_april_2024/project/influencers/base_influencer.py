from abc import ABC, abstractmethod

from project.campaigns.base_campaign import BaseCampaign


class BaseInfluencer(ABC):
    def __init__(self, username: str, followers: int, engagement_rate: float):
        self.username = username
        self.followers = followers
        self.engagement_rate = engagement_rate
        self.campaigns_participated: list[BaseCampaign] = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value:str):
        if value.strip() == '':
            raise ValueError('Username cannot be empty or consist only of whitespace!')
        self.__username = value
        
    @property
    def followers(self):
        return self.__followers
    
    @followers.setter
    def followers(self, value):
        if value < 0:
            raise ValueError('Followers must be a non-negative integer!')
        self.__followers = value

    @property
    def engagement_rate(self):
        return self.__engagement_rate
    
    @engagement_rate.setter
    def engagement_rate(self, value):
        if value < 0 or value > 5:
            raise ValueError('Engagement rate should be between 0 and 5.')
        self.__engagement_rate = value

    @abstractmethod
    def calculate_payment(self, campaign: BaseCampaign):
        pass

    @abstractmethod
    def reached_followers(self, campaign_type: str):
        pass

    @property
    def type_of_influencer(self):
        return type(self).__name__

    def display_campaigns_participated(self):
        if not self.campaigns_participated:
            return f'{self.username} has not participated in any campaigns.'

        result = [f'{self.type_of_influencer} :) {self.username} :) participated in the following campaigns:']
        for campaign in self.campaigns_participated:
            result.append(f'  - Campaign ID: {campaign.campaign_id}, Brand: {campaign.brand}, Reached followers: {self.reached_followers(campaign.campaign_type)}')

        return '\n'.join(result).strip()
