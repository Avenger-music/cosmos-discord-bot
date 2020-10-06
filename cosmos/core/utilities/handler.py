"""
Cosmos: A General purpose Discord bot.
Copyright (C) 2020 thec0sm0s

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from . import handlers

from .utils import Utils
from .api import TMDBClient
from .api import ImgurClient


class Utility(Utils):

    def __init__(self, bot):
        self.bot = bot
        self.file_handler = handlers.FileHandler()
        self.tmdb = TMDBClient(self.bot.configs.tmdb.access_token)
        self.imgur = ImgurClient(self.bot.configs.imgur.client_id)
