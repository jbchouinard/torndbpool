#!/usr/bin/env python
# -*- coding=utf8 -*-
from torndb import Connection

from torndbpool.poolmanager import get_pool


class PoolConnection(Connection):
    """
    This is meant as a drop-in replacement for torndb.Connection that uses a pool
    behind the scenes to manage connections.

    Usage
      # from torndb import Connection
      from torndbpool import PoolConnection as Connection

      # Use Connection as usual...
    """
    def reconnect(self):
        self.close()
        pool = get_pool(self._db_args)
        self._db = pool.connect()
