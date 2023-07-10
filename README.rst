====================
Pelian Microblogging
====================

*A Pelican plugin providing "microblogging" capabilities.*

Quickstart
----------

1. If needed, add the plugin to your configuration. Generally, the plugin should be loaded auyomatically without effort on your part.
2. Create a `micro` folder in your content folder.
3. Create a new post in your `micro` folder. This can be generally be just the text (body) of your post. In terms of metadata, `title` is unneeded (and ignored), `slug` will be auto-generated based on the post date, and `date` will determined from the file creation datetime of the post file (although you may want to provide it in the post metadata). Depending on your settings, you may need to provide an `author`. Your post can be in any format Pelican can read (by default, Markdown, ReStructured Text, or HTML).
4. Regenerate your Pelican site!

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

Microblogging is generally considered to be blog posts, but very short in length.

The most common example is Twitter, with an original limit of 140 characters (to be less than the SMS max of 160 characters). Twitter has since doubled their limit to 280 characters. The default on Mastedon is 500 characters, the same as (newly released) Threads.

(Note that on Twitter, all links are run through a shortener and so are 23 characters long.)

Installation
------------

The easist way to installed *Microblogging* is through ``pip``:

.. code-block:: sh
   pip install minchin.pelican.reader.microblog

Requirements
------------

*Microblogging* relies on Pelican, and the ``autoloader`` plugin (for autoloading). If this plugin is installed from PyPI, these should automatically be installed.

if you needbto insatll them manually:

.. code-block:: sh

   pip install pelican
   pip install minchin.pelican.plugins.autoloader


Additional Images
-----------------

Micro blog post, using the Seafoam theme:

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
 on `GitHub <https://github.com/MinchinWeb/minchin.pelican.readers.microblog/issues>`_. 
  
 .. use the ".. data::" directive here for Sphinx output, but on GitHub, that just causes everything to disappear


MICROBLOG_MAX_LENGTH = 140
    How long should your micro blog posts ve limited to. Pelican will emmot a warning if you exceed this.

