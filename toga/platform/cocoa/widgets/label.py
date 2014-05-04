from __future__ import print_function, unicode_literals, absolute_import, division

from ..libs import *
from .base import Widget


class Label(Widget):
    def __init__(self, value=None, placeholder=None, command=None):
        super(Label, self).__init__()

        self.command = command

        self._impl = NSTextField.new()

        self._impl.setEditable_(False)
        self._impl.setBezeled_(False)
