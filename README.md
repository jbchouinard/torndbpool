# torndbpool

## Info

This package provides a drop-in replacement for torndb.Connection that uses a sqlalchemy QueuePool behind the scenes to manage connection.

## Requirements

 - MySQL-python >= 1.2.5
 - SQLAlchemy >= 1.0.9
 - torndb >= 0.3

## Usage

    \# from torndb import Connection
    from torndbpool import PoolConnection as Connection
