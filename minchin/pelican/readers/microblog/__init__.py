from pelican import signals

from .initialize import check_settings, microblog_version
from .constants import __version__  # NOQA
from .generator import addMicroArticle

def register():
    """Register the plugin pieces with Pelican."""
    signals.initialized.connect(check_settings)
    signals.initialized.connect(microblog_version)
    signals.article_generator_pretaxonomy.connect(addMicroArticle)
