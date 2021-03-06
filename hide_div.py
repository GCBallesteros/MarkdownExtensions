import re
from markdown.extensions import Extension
import xml.etree.ElementTree as etree
from markdown.blockprocessors import BlockProcessor

def makeExtension(configs=None):
    if configs is None:
        return CollapseBlockExtension()
    else:
        return CollapseBlockExtension(configs=configs)

class CollapseBlockProcessor(BlockProcessor):
    RE_FENCE_START = r'^ *\?{3,}([ -~]+)\n' # start line, e.g., `   ????? `
    RE_FENCE_END = r'\n *\?{3,}\s*$'  # last non-blank line, e.g, '?????\n  \n\n'

    # <div id='proof-1-div' class="collapsable-proof-div">
    #   <div class='measuringWrapper'>
    #     <div class="proof-div">
    def test(self, parent, block):
        return re.match(self.RE_FENCE_START, block)

    def run(self, parent, blocks):
        original_block = blocks[0]
        # Extract
        div_id = re.search(self.RE_FENCE_START, original_block).group(1)
        # Remove start fence
        blocks[0] = re.sub(self.RE_FENCE_START, '', blocks[0])


        # Find block with ending fence
        for block_num, block in enumerate(blocks):
            if re.search(self.RE_FENCE_END, block):
                # remove fence
                blocks[block_num] = re.sub(self.RE_FENCE_END, '', block)
                # render fenced area inside a new div
                e = etree.SubElement(parent, 'div')
                e.set('class', 'collapsable-proof-div')
                e.set('id', div_id)
                f = etree.SubElement(e, 'div')
                f.set('class', 'measuringWrapper')
                g = etree.SubElement(f, 'div')
                g.set('class', 'proof-div')
                self.parser.parseBlocks(g, blocks[0:block_num + 1])
                # remove used blocks
                for i in range(0, block_num + 1):
                    blocks.pop(0)
                return True  # or could have had no return statement
        # No closing marker!  Restore and do nothing
        blocks[0] = original_block
        return False  # equivalent to our test() routine returning False

class CollapseBlockExtension(Extension):
    def extendMarkdown(self, md):
        md.parser.blockprocessors.register(CollapseBlockProcessor(md.parser), 'collapse', 175)
