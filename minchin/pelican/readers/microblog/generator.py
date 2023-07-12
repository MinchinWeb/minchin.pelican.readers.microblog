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
from jinja2.utils import url_quote

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

        new_article_metadata = {
            "category": myBaseReader.process_metadata("category", "µ"),
            # "tags": myBaseReader.process_metadata("tags", "tagA, tagB"),
            "micro": myBaseReader.process_metadata("micro", True),
        }

        post_slug = settings["MICROBLOG_SLUG"].format(**metadata)
        metadata["slug"] = post_slug
        
        new_article_metadata["title"] = myBaseReader.process_metadata("title", post_slug)
        new_article_metadata["date"] = metadata["date"]
        new_article_metadata["slug"] = post_slug
        new_article_metadata["save_as"] = myBaseReader.process_metadata("save_as", settings["MICROBLOG_SAVE_AS"].format(**metadata))
        new_article_metadata["url"] = myBaseReader.process_metadata("url", settings["MICROBLOG_URL"].format(**metadata))

        if "image" in metadata.keys():
            new_article_metadata["image"] = myBaseReader.process_metadata("image", metadata["image"])

            # add image link to end of content
            image_url = f'{settings["SITEURL"]}/{metadata["image"]}'
            image_url = url_quote(image_url)  # Jinja filter "urlencode"

            image_link = f'<a href={image_url}">{image_url}</a>'

            content = content.removesuffix("</p>") + " " + image_link + "</p>"

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
        new_article_metadata["char_len"] = post_len
        
        print(post_len)

        new_article = Article(
            content,
            new_article_metadata,
        )

        articleGenerator.articles.insert(0, new_article)
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
