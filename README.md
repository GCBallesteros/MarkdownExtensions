# Extensions
This repo currently contains the following extensions:
- AbbreviationExtension: Abbreviations of the form ?[EM][Electromagnetism]. Courtesy of [Daniel Bauer](https://www.dj-bauer.de/python-markdown-extensions-en.html).
- CollapseBlockExtension: Code between ????\<some-id\> fences gets wrapped in special divs that are used to make collapsible text areas.
- WarningBlockExtension: Fences made out of !!!! are used to create a custom div that gets rendered in a box.
- PrismCodeExtension: Code fences are reinterpreted to use the format expected by Prism. Courtesy of [smartchaos/prism_markdown](https://github.com/smartchaos/prism_markdown).


# Installation
Add the contents of this repo into a folder named `markdown` in the root of your pelican project, i.e.
where your `pelicanconf.py` lives.

Then add the following to your `pelicanconf.py`:

```
import sys
sys.path.append("markdown")

# Extensions
from markdown_abbreviation import AbbreviationExtension
from warning_msg import WarningBlockExtension
from hide_div import CollapseBlockExtension
from prism_markdown import PrismCodeExtension

MARKDOWN = {
    "extensions": [
        AbbreviationExtension(),
        CollapseBlockExtension(),
        WarningBlockExtension(),
        PrismCodeExtension(),
    ]
}
```
