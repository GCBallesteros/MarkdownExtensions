import re
from markdown.extensions import Extension
from markdown.postprocessors import Postprocessor

def makeExtension(configs=None):
    if configs is None:
        return AbbreviationExtension()
    else:
        return AbbreviationExtension(configs=configs)

class AbbreviationExtension(Extension):
    def __init__(self, **kwargs):
        self.config = {}
        super(AbbreviationExtension, self).__init__(**kwargs)
    def extendMarkdown(self, md, md_globals):
        postprocessors = AbbreviationPostprocessor(md)
        md.postprocessors.add("abbreviation", postprocessors, ">raw_html")

class AbbreviationPostprocessor(Postprocessor):
    abbreviation_pattern = re.compile(r"\?\[([^\[]*)\]\[([^\[]*)\]")
    def __init__(self, *args, **kwargs):
        super(AbbreviationPostprocessor, self).__init__(*args, **kwargs)
    def run(self, html):
        return re.sub(self.abbreviation_pattern, self._code, html)
    def _code(self, match):
        title, name = match.groups()
        return "<abbr title=\"" + title + "\">" + name + "</abbr>"

