# -*- coding: utf-8 -*-

"""Plugins loader.

    You could register your ownn plug_in with an entry_points.

    Code a class in your egg and register it within your setup.py file

    code_block ::

        entry_points='''
        # -*- Entry points: -*-
        [mr.bob.plugins]
        render_filename=your_naemspace.pkg.module:FooRenderFilename
        ''',

   If there are multiples plugins with same name, you coul push yours with an order attribute.
   Max is prefered, otherwise alphabetic sorting on namesapce returns the last entry.

    ..note:: Please notice that just mrbob.rendering.render_filename is iactually plugguable, but infra is here.

"""

__docformat__ = 'restructuredtext en'

import operator
import pkg_resources


entries = [entry for entry in
           pkg_resources.iter_entry_points(group='mr.bob.plugins')]


def load_plugin(plugin, entries=entries, target=None):
    """Load and sort possibles plugins from pkg."""
    if entries:
        plugins = [(ep, '%d-%s-%s' % (getattr(ep.load(False), 'order', 10),
                                      ep.module_name, ep.name))
                    for ep in entries if ep.name == plugin]
        ordered_plugins = sorted(plugins, key=operator.itemgetter(1))
        if target is not None:
            targets = [ep for ep in ordered_plugins
                                if ep[1].split('-')[0] == str(target)]
            if targets:
                return targets[-1][0].load(False)
            else:
                raise AttributeError('No matching target : %d' % target)

        return ordered_plugins[-1][0].load(False)

# vim:set et sts=4 ts=4 tw=80:
