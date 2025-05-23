import logging
import os
import platform
import configparser

import idaapi

import yaml
from attrdict import AttrMap

class DIEConfig(object):
    DEFAULT = os.path.join(os.path.dirname(__file__), "config.yml")
    CUSTOM = os.path.join(os.path.dirname(__file__), "DIE.yml")

    def __init__(self):
        path = self.DEFAULT
        if os.path.exists(self.CUSTOM):
            path = self.CUSTOM

        with open(path, "rt") as f:
            default = yaml.safe_load(f)

        self._config = AttrMap(default)

    @property
    def install_path(self):
        return os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))

    @property
    def icons_path(self):
        return self.install_path + "/icons" if platform.system() == "Linux" else self.install_path + "\\Icons"

    @property
    def parser_path(self):
        return self.install_path + "/Plugins/DataParsers" if platform.system() == "Linux" else self.install_path + "\\Plugins\\DataParsers"

    def load(self):
        path = self.DEFAULT
        if os.path.exists(self.CUSTOM):
            path = self.CUSTOM

        with open(path, "rt") as f:
            custom = yaml.safe_load(f)

        custom = AttrMap(custom)

        for attr in self._config:
            if attr in custom:
                self._config[attr].update(custom[attr])

    def save(self):
        with open(self.CUSTOM, "wt") as f:
            yaml.safe_dump(dict(self._config), f, default_flow_style=False)

    def __getattr__(self, name):
        return getattr(self._config, name)

    def __setattr__(self, name, value):
        if name.startswith("_"):
            return super(DIEConfig, self).__setattr__(name, value)

        return setattr(self._config, name, value)

#############################################################################
#                              Singleton
#############################################################################

_config_parser = None

def get_config():
    """
    Return a singleton instance of the global configuration object
    """
    return _config_parser

def initialize():
    global _config_parser
    _config_parser = DIEConfig()
