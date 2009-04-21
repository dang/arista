#!/usr/bin/env python

import os
from glob import glob

from distutils.core import setup

# Patch distutils if it can't cope with the "classifiers" or
# "download_url" keywords
from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None

setup(
    name = "arista",
    version = "0.8",
    description = "An easy multimedia transcoder for GNOME",
    long_description = """Overview
========
An easy to use multimedia transcoder for the GNOME Desktop. Arista focuses on
being easy to
use by making the complex task of encoding for various devices simple. Pick your
input, pick your target device, choose a file to save to and go.

Arista has been in development since early 2008 as a side project and was just
recently polished to make it release-worthy. The 0.8 release is the first public
release and includes a to-do of items that will be completed for the 1.0 final
release.

Features
---------

* Presets for iPod, computer, DVD player, PSP, and more
* Live preview to see encoded quality
* Automatically discover available DVD drives and media
* Rip straight from DVD media easily (requires libdvdcss)
* Simple terminal client for scripting

Requirements
---------------
Arista is written in Python and requires the bindings for GTK+ 2.16 or newer,
GStreamer, GConf, GObject, Cairo, and DBus. If you are an Ubuntu user this means
you need to be using at least Ubuntu 9.04 (Jaunty). The GStreamer plugins
required depend on the presets available, but at this time you should have
gst-plugins-good, gst-plugins-bad, gst-plugins-ugly, and gst-ffmpeg. If you are
on Ubuntu don't forget to install the multiverse packages.
""",
    author = "Daniel G. Taylor",
    author_email = "dan@programmer-art.org",
    url = "http://programmer-art.org/projects/arista-transcoder",
    download_url = "http://programmer-art.org/media/releases/arista-transcoder/arista-0.8.tar.gz",
    packages = [
        "arista",
    ],
    scripts = [
        "arista-gtk",
        "arista-transcode",
    ],
    data_files = [
        (os.path.join("share", "arista", "presets"),
         glob(os.path.join("presets", "*"))),
        (os.path.join("share", "arista", "ui"),
         glob(os.path.join("ui", "*"))),
    ],
    requires = [
        "gtk(>=2.16)", 
        "gst(>=10.22)",
        "gconf",
        "cairo",
        "dbus",
    ],
    provides = [
        "arista",
    ],
    keywords = "gnome gtk gstreamer transcode multimedia",
    platforms = [
        "Platform Independent",
    ],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: X11 Applications :: GTK",
        "Environment :: X11 Applications :: Gnome",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Multimedia :: Sound/Audio :: Conversion",
        "Topic :: Multimedia :: Video :: Conversion",
        "Topic :: Utilities",
    ],
)
