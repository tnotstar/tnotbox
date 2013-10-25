#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import Quandl

authtoken = os.environ.get("QUANDL_AUTHTOKEN", None)

data = Quandl.get("GOOG/NYSE_IBM", collapse="weekly", authtoken=authtoken)
print(data.to_string())

# EOF