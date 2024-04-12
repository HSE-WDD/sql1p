from cs50 import SQL

import check50
import sqlparse

@check50.check()
def exists():
  """SQL files exist"""
  for i in range(1):
    check50.exists(f"part{i + 1}.sql")
  check50.include("sql_practice.db")

