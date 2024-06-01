"""
Tests for adherence of XDG spec while preferences are loaded/saved.
"""

import os
import sys
import unittest

from pymol import plugins, testing
from pymol.Qt import QtCore


legacy_file = "~/.pymolpluginsrc.py"

# QStandardPath is XDG compliant by default I think
xdg_dir = None
xdg_file = f"{xdg_dir}/pymolpluginsrc.py"


class Test_pref_save(testing.PyMOLTestCase):
    def test_legacy_pref_save_creates_legacy_file(self):
        pass
        # delete file
        # pref_save
        # assert file is legacy

    @testing.requires_version("3.0")
    def test_pref_save_creates_xdg_file(self):
        pass
        # delete file
        # pref_save
        # assert file is xdg

    @testing.requires_version("3.0")
    def test_pref_save_respects_legacy_file(self):
        pass
        # create legacy file
        # pref_save
        # assert file is legacy
        # delete file
        # pref_save
        # assert file is xdg
