import datetime
import re
import logging
import os

from pelican import signals
from pelican.contents import Article
from pelican.readers import BaseReader
from pelican.utils import get_date, pelican_open
from pelican.readers import MarkdownReader

from markupsafe import Markup

from .constants import (
    LOG_PREFIX,
)

logger = logging.getLogger(__name__)

_micropost_count = 0


def addMicroArticle(articleGenerator):
    global _micropost_count

    settings = articleGenerator.settings

    # Author, category, and tags are objects, not strings, so they need to
    # be handled using myBaseReader's process_metadata() function.
    # myBaseReader = BaseReader(settings)
    myMarkdownReader = MarkdownReader(settings)
    myBaseReader = myMarkdownReader

    file_extensions = [
        "txt",
    ] + MarkdownReader.file_extensions

    for post in articleGenerator.get_files(
        paths=settings["MICROBLOG_FOLDER"], extensions=file_extensions
    ):
        # raw_content = pelican_open(post)
        # print(post, type(post))
        # print(settings)
        post = settings["PATH"] + os.sep + post

        content, metadata = myMarkdownReader.read(source_path=post)

        # print(settings["MICROBLOG_SLUG"])
        print(metadata)

        post_date = metadata["date"]
        post_slug = settings["MICROBLOG_SLUG"].format(**metadata)
        metadata["slug"] = post_slug
        post_save_as = settings["MICROBLOG_SAVE_AS"].format(**metadata)
        post_url = settings["MICROBLOG_URL"].format(**metadata)

        # warn if too long
        safe_content = Markup(content).striptags()
        post_len = len(safe_content)
        if post_len > settings["MICROBLOG_MAX_LENGTH"] + 6:
            relative_filename = post.removeprefix(settings["PATH"])
            logger.warning(
                '%s micropost "%s" longer than expected (%s > %s).'
                % (
                    LOG_PREFIX,
                    relative_filename,
                    post_len,
                    settings["MICROBLOG_MAX_LENGTH"],
                )
            )

        newArticle = Article(
            content,
            {
                # "title": None,
                "title": myBaseReader.process_metadata("title", post_slug),
                "date": post_date,
                "category": myBaseReader.process_metadata("category", "µ"),
                # "tags": myBaseReader.process_metadata("tags", "tagA, tagB"),
                "micro": myBaseReader.process_metadata("micro", True),
                "slug": myBaseReader.process_metadata("slug", post_slug),
                "save_as": myBaseReader.process_metadata("save_as", post_save_as),
                "url": myBaseReader.process_metadata("url", post_url),
                # "summary": myBaseReader.process_metadata("summary", False),
            },
        )

        articleGenerator.articles.insert(0, newArticle)
        _micropost_count += 1

        # logging.debug(
        #     '%s MICROBLOG_FOLDER set to "%s"'
        #     % (LOG_PREFIX, pelican.settings["MICROBLOG_FOLDER"])
        # )


def pelican_finalized(pelican):
    global _micropost_count
    print(
        "%s Processed %s micropost%s."
        % (LOG_PREFIX, _micropost_count, "s" if _micropost_count != 1 else ""),
    )
