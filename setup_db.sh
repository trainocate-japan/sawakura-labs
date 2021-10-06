#!/bin/sh

mysql -p -h db -u admin -D labdb < ./sql/setup.sql
