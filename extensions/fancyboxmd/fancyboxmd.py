from markdown.extensions import Extension
from markdown.inlinepatterns import LinkInlineProcessor
import xml.etree.ElementTree as etree


class FancyBoxInlineProcessor(LinkInlineProcessor):
    """ Return a img element with fancybox attributes from the given match. """

    def handleMatch(self, m, data):
        text, index, handled = self.getText(data, m.end(0))
        if not handled:
            return None, None, None

        src, title, index, handled = self.getLink(data, index)
        if not handled:
            return None, None, None

        el_a = etree.Element("a")
        el_a.set("href", src)
        el_a.set("data-fancybox", "gallery")
        if title is not None:
            el_a.set("data-caption", title)

        el_img = etree.Element("img")
        el_img.set("src", src)

        if title is not None:
            el_img.set("title", title)

        el_img.set('alt', self.unescape(text))
        el_a.append(el_img)
        return el_a, m.start(0), index


FB_BRACKETS_RE = r"!!\["

class FancyBoxExtension(Extension):
    """
    The FancyBoxExtension creates fancybox attributes on images using exclamation marks.
    !![Description Here](image_url_here.jpg)
    """

    def __init__(self, **kwargs):
        # Call the parent class's __init__ method to configure options
        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        pattern = FancyBoxInlineProcessor(FB_BRACKETS_RE, md)
        md.inlinePatterns.register(pattern, "fancybox-brackets", 200)


def makeExtension(**kwargs):
    """
    Return an instance of the FancyBox Python-Markdown extension.
    This method enables the extension for use in MkDocs.
    """
    return FancyBoxExtension(**kwargs)
