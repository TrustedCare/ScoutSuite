from ScoutSuite.providers.aws.facade.base import AWSFacade
from ScoutSuite.providers.aws.resources.config.recorders import Recorders
from ScoutSuite.providers.aws.resources.config.rules import Rules
from ScoutSuite.providers.aws.resources.regions import Regions


class Config(Regions):
    _children = [
        (Recorders, 'recorders'),
        (Rules, 'rules')
    ]

    def __init__(self, facade: AWSFacade):
        super(Config, self).__init__('config', facade)

    async def fetch_all(self, regions=None, partition_name='aws'):
        await super(Config, self).fetch_all(regions, partition_name)

