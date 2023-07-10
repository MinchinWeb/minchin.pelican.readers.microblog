=====================
Pelican Microblogging
=====================

*A Pelican plugin providing "microblogging" capabilities.*

.. image:: https://img.shields.io/pypi/v/minchin.pelican.readers.microblog.svg?style=flat
   :target: https://pypi.python.org/pypi/minchin.pelican.readers.microblog/
   :alt: PyPI version number

.. image:: https://img.shields.io/badge/-Changelog-success
   :target: https://github.com/MinchinWeb/minchin.pelican.readers.microblog/blob/master/CHANGELOG.rst
   :alt: Changelog

.. image:: https://img.shields.io/pypi/pyversions/minchin.pelican.readers.microblog?style=flat
   :target: https://pypi.python.org/pypi/minchin.pelican.readers.microblog/
   :alt: Supported Python version

.. image:: https://img.shields.io/pypi/l/minchin.pelican.readers.microblog.svg?style=flat&color=green
   :target: https://github.com/MinchinWeb/minchin.pelican.readers.microblog/blob/master/LICENSE.txt
   :alt: License

.. image:: https://img.shields.io/pypi/dm/minchin.pelican.readers.microblog.svg?style=flat
   :target: https://pypi.python.org/pypi/minchin.pelican.readers.microblog/
   :alt: Download Count

Quickstart
----------

1. Install the plugin via pip: ``pip install
   minchin.pelican.readers.microblogging``
2. If needed, add the plugin to your configuration. Generally, the plugin
   should be loaded automatically without effort on your part.
3. Create a ``micro`` folder in your content folder (to hold your micro blog
   posts!).
4. Create a new post in your ``micro`` folder. This can be generally be just
   the text (body) of your post. In terms of metadata, ``title`` is unneeded
   (and ignored), ``slug`` will be auto-generated (based on the post date), and
   ``date`` will determined from the file creation datetime of the post file
   (although you may want to provide it in the post metadata). Depending on
   your settings, you may need to provide an ``author``. Your post can be in
   any format Pelican can read (by default, Markdown, ReStructured Text, or
   HTML).
5. Regenerate your Pelican site!

Sample (Micro) Post File
------------------------

.. code-block:: md

   <!-- ./content/micro/202307091701.md -->

   created: 2023-07-09 17:01+0600
   ---

   I'm microblogging with Pelican!
   <https://blog.minchin.ca/label/microblogging-pelican>

Background Notes (on Micro Blogging)
------------------------------------

Microblogging is generally considered to be blog posts, but very short in
length.

The most common example is Twitter, with an original limit of 140 characters
(to be less than the SMS max of 160 characters). Twitter has since doubled
their limit to 280 characters. The default on Mastodon is 500 characters, the
same as (newly released) Threads.

(Note that on Twitter, all links are run through a shortener and so are
considered 23 characters long.)

Installation
------------

The easiest way to installed *Microblogging* is through ``pip``:

.. code-block:: sh

   pip install minchin.pelican.reader.microblog

Requirements
------------

*Microblogging* relies on Pelican, and the ``autoloader`` plugin (for
autoloading). If this plugin is installed from PyPI, these should automatically
be installed.

if you need to insrall them manually:

.. code-block:: sh

   pip install pelican
   pip install minchin.pelican.plugins.autoloader


Additional Images
-----------------

Micro blog post, using the Seafoam theme:

(Placeholder image for the moment...)

.. image:: https://github.com/MinchinWeb/seafoam/raw/master/docs/screenshots/2.6.0/article_with_header.png
   :align: center
   :alt: Replace Image...


Pelican Settings
----------------

These settings can be set in your ``pelicanconf.py`` file (your Pelican settings
file) to alter the behavior of the plugin.

If a value is given below, this represents the effective default value. If no
value is given, the effective default value is ``None``.

*Microblogging* also auto-configures itself when possible.  If you need to manually 
create the default configuration, you would need the following: 

.. code-block:: python 

   # pelicanconf.py 

   # if PLUGINS is not defined on Pelican 4.5+, these plugins will autoload 
   PLUGINS = [ 
       "minchin.pelican.readers.microblog", 
       # others, as desired... 
   ] 

   # the rest of the your configuration file... 

This documentation has to be manually updated. If the settings no longer match
the plugin's behavior, or a setting is missing from here, please open a ticket
on `GitHub
<https://github.com/MinchinWeb/minchin.pelican.readers.microblog/issues>`_. 

.. use the ".. data::" directive here for Sphinx output, but on GitHub, that just causes everything to disappear

MICROBLOG_FOLDER = "micro"
   Folder containing your micro blog posts.
MICROBLOG_MAX_LENGTH = 140
   How long should your micro blog posts ve limited to. Pelican will emit a
   warning if you exceed this.
MICROBLOG_SAVE_AS = ARTICLE_SAVE_AS
   What to save the micro blog posts output file as. Defaults to using the same
   file structure as you are using for articles. c.f. ``MICROBLOG_URL``.
MICROBLOG_SLUG = "u{date:%Y%m%d%H%M}"
   The slug that will be used for micro blog posts. Eg. ``u202307091701``.

   Note that Pelican expects slugs to be universally unique.
MICROBLOG_URL = ARTICLE_URL
   What URL to post the micro blog posts to. Defaults to using the same URL
   structure as you are using for articles. c.f. ``MICROBLOG_SAVE_AS``.

.. Changelog
.. Known Issues
.. Credits
