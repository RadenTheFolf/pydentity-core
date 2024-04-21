# Copyright (C) 2024 RadenTheFolf (GitHub Account Holder)
#
# This file is part of Pydentity.
#
# pydentity-core is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pydentity-core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pydentity-core.  If not, see <https://www.gnu.org/licenses/>.
from datetime import datetime


class Session:
    session_id: str = None
    session_token: str = None
    ip_address: str = None
    user_agent: str = None
    user_id: int = None
    created_at: datetime = None
    last_activity: datetime = None
    expires_at: datetime = None
