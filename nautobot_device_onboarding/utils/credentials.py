"""User credentials helper module for device onboarding.

(c) 2020-2021 Network To Code
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
  http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


class Credentials:
    """Class used to hide user's credentials in RQ worker and Django."""

    def __init__(self, username=None, password=None, secret=None):
        """Create a Credentials instance."""
        self.username = username
        self.password = password
        self.secret = secret

    def __repr__(self):
        """Return string representation of a Credentials object."""
        return "*Credentials argument hidden*"

    def nautobot_serialize(self):
        """Serialize object for Celery."""
        return {
            "username": self.username,
            "password": self.password,
            "secret": self.secret,
        }

    @classmethod
    def nautobot_deserialize(cls, data):
        """Deserialize object for Celery."""
        return cls(
            username=data["username"],
            password=data["password"],
            secret=data["secret"],
        )
