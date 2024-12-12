# vim: set fileencoding=utf-8
"""
pythoneda/runtime/secrets/events/credential_issued.py

This file defines the CredentialIssued class.

Copyright (C) 2024-today boot's pythoneda-runtime/secrets-events

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import asyncio
from pythoneda.shared import Event
from typing import Dict, List


class CredentialIssued(Event):
    """
    Represents the event in which a credential is issued.

    Class name: CredentialIssued

    Responsibilities:
        - Represent the information associated to the event.

    Collaborators:
        - None
    """

    def __init__(
        self,
        name: str,
        value: str,
        metadata: Dict[str, str] = {},
        previousEventIds: List[str] = None,
        reconstructedId: str = None,
        reconstructedPreviousEventIds: List[str] = None,
    ):
        """
        Creates a new CredentialIssued instance.
        :param name: The name of the credential.
        :type name: str
        :param value: The name of the credential.
        :type value: str
        :param metadata: The additional metadata.
        :type metadata: str
        :param previousEventIds: The id of previous events, if any.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        :param reconstructedPreviousEventIds: The id of the previous events, if an external event
        is being reconstructed.
        :type reconstructedPreviousEventIds: List[str]
        """
        super().__init__(
            previousEventIds,
            reconstructedId,
            reconstructedPreviousEventIds,
        )

        self._name = name
        self._value = value
        self._metadata = metadata

    @property
    def name(self) -> str:
        """
        Retrieves the name of the credential.
        """
        return self._name

    @property
    def value(self) -> str:
        """
        Retrieves the value of the credential.
        """
        return self._value

    @property
    def metadata(self) -> Dict[str, str]:
        """
        Retrieves the metadata of the event.
        """
        return self._metadata


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
