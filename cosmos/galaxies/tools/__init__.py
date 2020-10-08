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

from .tags import Tags
from .imgur import Imgur
from .reminder import Reminder
from .hastebin import HasteBin
from .utilitiies import Utilities
from .urban import UrbanDictionary


__all__ = [
    Tags,
    Imgur,
    Reminder,
    HasteBin,
    Utilities,
    UrbanDictionary,
]


def setup(bot):
    bot.plugins.setup(__file__)
