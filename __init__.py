from cs50 impor SQL

import check50
import sqlparse

@check50.check()
def exists():
  """SQL files exist"""
  for i in range(1):
    check50.exists(f"{i + 1}.sql")
  check50.include("sql_practice.db")

