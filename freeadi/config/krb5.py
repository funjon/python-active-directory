#
# This file is part of FreeADI. FreeADI is free software and is made available
# under the terms of the GNU General Public License, version 3. Consult the
# file "LICENSE" that is distributed together with this file for the exact
# licensing terms.
#
# FreeADI is copyright (c) 2007 by the FreeADI authors. See the file "AUTHORS"
# for a complete overview.

from parse_krb5 import Krb5Parser
from write_krb5 import Krb5Writer
from config import Config


class Krb5Config(Config):
    """MIT krb5 configuration file access."""

    def __init__(self):
        super(Krb5Config, self).__init__(Krb5Parser, Krb5Writer)
