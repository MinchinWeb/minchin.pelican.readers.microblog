from pelican import signals

from .constants import __version__  # NOQA
from .generator import addMicroArticle, pelican_finalized
from .initialize import check_settings, microblog_version


def register():
    """Register the plugin pieces with Pelican."""
    signals.initialized.connect(check_settings)
    signals.initialized.connect(microblog_version)
    signals.article_generator_pretaxonomy.connect(addMicroArticle)
    signals.finalized.connect(pelican_finalized)
