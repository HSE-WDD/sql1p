from cs50 import SQL

import check50
import sqlparse

@check50.check()
def exists():
  """SQL files exist"""
  for i in range(2):
    check50.exists(f"part{i + 1}.sql")
  check50.include("sql_practice.db")


@check50.check(exists)
def test1():
  """p1.sql produces correct result"""
  check_multi_col(
    run_query("p1.sql"), 
    [{'Advanced Squad Leader', '1985'},
     {'BattleTech', '1985'},
     {'World in Flames', '1985'},
     {"You're Bluffing!", '1985'},
     {'DungeonQuest', '1985'},
     {'Code 777', '1985'},
     {'Tables of the Arabian Nights', '1985'}],
    ordered=False,
  )
