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


def check_multi_col(actual, expected, ordered=False):
    """
    Checks that the columns in 'actual' matches 'expected'.

    positional arguments:
        actual (list[dict])       result returned by run_query
        expected (list[set])      expected result to match against

    options:
        ordered (bool)            whether to check whether actual's order matches expected's

    returns:
        None

    raises:
        check50.Mismatch if actual does not match expected
        check50.Failure if error occurs
    """

    # convert list of sets to list of frozen sets or set of frozen sets
    try:
        if ordered:
            expected = [frozenset(unfrozen_set) for unfrozen_set in expected]
        else:
            expected = {frozenset(unfrozen_set) for unfrozen_set in expected}
    except Exception as e:
        raise check50.Failure(f"Error when reading expected result: {str(e)}")
    return _check(actual, expected, ordered)
