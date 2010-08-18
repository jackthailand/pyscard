"""RemoteCardConnection class manages connections to a remote reader
thru pyro (http://www.xs4all.nl/~irmen/pyro3/).

__author__ = "http://www.gemalto.com"

Copyright 2001-2010 gemalto
Author: Jean-Daniel Aussel, mailto:jean-daniel.aussel@gemalto.com

This file is part of pyscard.

pyscard is free software; you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation; either version 2.1 of the License, or
(at your option) any later version.

pyscard is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with pyscard; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""

import Pyro.core
import Pyro.naming

from smartcard.CardConnection import CardConnection
from smartcard.CardConnectionDecorator import CardConnectionDecorator
from smartcard.Exceptions import CardConnectionException, NoCardException
from smartcard.Observer import Observable

class RemoteCardConnection(CardConnectionDecorator,Pyro.core.ObjBase):
    """Remote connection class. Handles connection with a card inserted inside a remote PC."""

    def __init__(self, cardConnectionComponent):
        """Construct a new remote card connection.

        connection: the reader connection
        """
        Pyro.core.ObjBase.__init__(self)
        CardConnectionDecorator.__init__( self, cardConnectionComponent )

