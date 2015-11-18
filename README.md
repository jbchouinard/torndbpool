# torndbpool

## Info

This package provides a drop-in replacement for torndb.Connection that uses a sqlalchemy QueuePool behind the scenes to manage connection.

## Requirements

 - MySQLdb
 - sqlalchemy
 - torndb

## Usage

\# from torndb import Connection
from torndbpool import PoolConnection as Connection
