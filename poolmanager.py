#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
Manage pools of connections to mysql databases.
"""
from sqlalchemy import pool
from MySQLdb import connect

_POOLS = {}
POOL_SIZE = 10
MAX_OVERFLOW = 25
AUTOCOMMIT = True


def get_pool(db_args):
    poolkey = frozenset(db_args.items())
    if poolkey not in _POOLS:
        conn_func = _get_connector_func(db_args)
        _POOLS[poolkey] = pool.QueuePool(
            conn_func, pool_size=POOL_SIZE,
            max_overflow=MAX_OVERFLOW
        )
    return _POOLS[poolkey]


def _get_connector_func(db_args):
    def connector_func():
        conn = connect(**db_args)
        if AUTOCOMMIT:
            conn.autocommit(True)
        return conn
    return connector_func


def dispose_all():
    for p in _POOLS.keys():
        p.dispose()
