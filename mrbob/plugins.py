# -*- coding: utf-8 -*-

"""Plugins loader.

"""

__docformat__ = 'restructuredtext en'

import pkg_resources


entries = [entry for entry in
           pkg_resources.iter_entry_points(group='mr.bob.plugins')]


def load_plugin(plugin, entries=entries):
    """Load and sort possibles plugins from pkg."""
    if entries:
        plugins = [ep for ep in entries if ep.name == plugin]
        ordered_plugins = sorted(plugins, key=lambda plugin: '%d-%s' %
                (getattr(plugin.load(False), 'order', 0), plugin.module_name))
        return ordered_plugins[-1].load(False)

# vim:set et sts=4 ts=4 tw=80:
