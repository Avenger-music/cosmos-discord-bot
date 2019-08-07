import discord

from io import BytesIO

from .levels import Levels
from .settings import GuildSettings
from .roleshop import GuildRoleShop


class CosmosGuild(GuildSettings, GuildRoleShop):

    @property
    def plugin(self):
        return self.__plugin

    @property
    def id(self):
        return self.__id

    @classmethod
    def from_document(cls, plugin, document: dict):
        return cls(plugin, **document)

    async def fetch_member_profile(self, _id):
        return await self.plugin.bot.profile_cache.get_guild_profile(_id, self.id)

    def __init__(self, plugin, **kwargs):
        self.__plugin = plugin
        self.__id = kwargs["guild_id"]
        self.is_prime = kwargs.get("is_prime", False)
        GuildSettings.__init__(self, **kwargs)
        GuildRoleShop.__init__(self, **kwargs)
        self.levels = Levels(self, **kwargs)

    async def send_welcome_banner(self, name, avatar_url, channel: discord.TextChannel = None):
        channel = channel or self.welcome_banner_channel
        banner_bytes = await self.plugin.bot.image_processor.discord.get_welcome_banner(
            self.welcome_banner_url, avatar_url, name, self.welcome_banner_text
        )
        banner_format = self.welcome_banner_url.split(".")[-1]
        file = discord.File(BytesIO(banner_bytes), filename=f"{self.plugin.data.settings.banner_name}.{banner_format}")
        await channel.send(file=file)
