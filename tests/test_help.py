#!/usr/bin/python
# -*- coding:utf-8 -*-
"""unit test for help system"""
import sys
sys.path.append("src")
from help import Help, KEY_HELP, KEY_SPLIT

HELP = Help()

def test_help_all():
    """test doc of navigation"""
    assert HELP.handle_msg(f'{KEY_HELP}', True)
    assert HELP.get_reply() == HELP.all()

def test_help_individual():
    """test doc of individual function"""
    for key in HELP.dict_help:
        assert HELP.handle_msg(f'{KEY_HELP} {KEY_SPLIT}{key}', True)
        assert HELP.get_reply() == HELP.dict_help(key)

    false_keyword = 'no such key word'
    assert HELP.handle_msg(f'{KEY_HELP}{KEY_SPLIT}{false_keyword}', True)
    assert HELP.get_reply() == HELP.no_such_method()
