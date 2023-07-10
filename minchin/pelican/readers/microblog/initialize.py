import logging

from .constants import (
    LOG_PREFIX,
    __url__,
    __version__,
)

logger = logging.getLogger(__name__)

def check_settings(pelican):
    """
    Insert defaults in Pelican settings, as needed.
    """
    logger.debug("%s massaging settings, setting defaults." % LOG_PREFIX)

    if not "MICROBLOG_FOLDER" in pelican.settings.keys():
        pelican.settings["MICROBLOG_FOLDER"] = "micro"
        logging.debug(
            '%s MICROBLOG_FOLDER set to "%s"'
            % (LOG_PREFIX, pelican.settings["MICROBLOG_FOLDER"])
        )
    else:
        logging.debug(
            '%s MICROBLOG_FOLDER previously set manually. Is "%s"'
            % (LOG_PREFIX, pelican.settings["MICROBLOG_FOLDER"])
        )

    if not "MICROBLOG_MAX_LENGTH" in pelican.settings.keys():
        pelican.settings["MICROBLOG_MAX_LENGTH"] = 140
        logging.debug(
            '%s MICROBLOG_MAX_LENGTH set to "%s"'
            % (LOG_PREFIX, pelican.settings["MICROBLOG_MAX_LENGTH"])
        )
    else:
        logging.debug(
            '%s MICROBLOG_MAX_LENGTH previously set manually. Is "%s"'
            % (LOG_PREFIX, pelican.settings["MICROBLOG_MAX_LENGTH"])
        )

    if not "MICROBLOG_SAVE_AS" in pelican.settings.keys():
        pelican.settings["MICROBLOG_SAVE_AS"] = pelican.settings["ARTICLE_SAVE_AS"]
        logging.debug(
            '%s MICROBLOG_SAVE_AS set to "%s"'
            % (LOG_PREFIX, pelican.settings["MICROBLOG_SAVE_AS"])
        )
    else:
        logging.debug(
            '%s MICROBLOG_SAVE_AS previously set manually. Is "%s"'
            % (LOG_PREFIX, pelican.settings["MICROBLOG_SAVE_AS"])
        )

    if not "MICROBLOG_SLUG" in pelican.settings.keys():
        pelican.settings["MICROBLOG_SLUG"] = "u{date:%Y%m%d%H%M}"
        logging.debug(
            '%s MICROBLOG_SLUG set to "%s"'
            % (LOG_PREFIX, pelican.settings["MICROBLOG_SLUG"])
        )
    else:
        logging.debug(
            '%s MICROBLOG_SLUG previously set manually. Is "%s"'
            % (LOG_PREFIX, pelican.settings["MICROBLOG_SLUG"])
        )

    if not "MICROBLOG_URL" in pelican.settings.keys():
        pelican.settings["MICROBLOG_URL"] = pelican.settings["ARTICLE_URL"]
        logging.debug(
            '%s MICROBLOG_URL set to "%s"'
            % (LOG_PREFIX, pelican.settings["MICROBLOG_URL"])
        )
    else:
        logging.debug(
            '%s MICROBLOG_URL previously set manually. Is "%s"'
            % (LOG_PREFIX, pelican.settings["MICROBLOG_URL"])
        )




def microblog_version(pelican):
    """
    Insert seafoam version into Pelican context.
    """

    if "MICROBLOG_VERSION" not in pelican.settings.keys():
        pelican.settings["MICROBLOG_VERSION"] = __version__
        logger.debug(
            '%s Adding Microblog version "%s" to context.' % (LOG_PREFIX, __version__)
        )
    else:
        logger.debug(
            '%s MICROBLOG_VERSION already defined. Is "%s".'
            % (LOG_PREFIX, pelican.settings["MICROBLOG_VERSION"])
        )

    if "MICROBLOG_URL" not in pelican.settings.keys():
        pelican.settings["MICROBLOG_URL"] = __url__
        logger.debug('%s Adding Microblog URL "%s" to context.' % (LOG_PREFIX, __url__))
    else:
        logger.debug(
            '%s MICROBLOG_URL already defined. Is "%s".'
            % (LOG_PREFIX, pelican.settings["MICROBLOG_URL"])
        )