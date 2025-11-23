from markdown_it.renderer import RendererHTML
from markdown_it import MarkdownIt
import pprint

class RrRenderer(RendererHTML):
    def render_em_open1(self, tokens, idx, options, env):
        return '<em class="myclass1">'

    def heading_open(self, tokens, idx, options, env):
        token = tokens[idx]
        if token.tag == 'h2':
            token.attrs.update({'class': 'mb-3'})
        if token.tag == 'h3':
            token.attrs.update({'class': 'mt-4 mb-2'})
        tokens[idx] = token
        return RendererHTML.renderToken(self, tokens, idx, options, env)
    
    def list_item_open(self, tokens, idx, options, env):
        token = tokens[idx]
        token.attrs.update({'class': 'list-group-item'})
        return RendererHTML.renderToken(self, tokens, idx, options, env)
    
    def bullet_list_open(self, tokens, idx, options, env):
        token = tokens[idx]
        token.attrs.update({'class': 'list-group themed-list mb-3'})
        return RendererHTML.renderToken(self, tokens, idx, options, env)
    
    def icon(self, tokens, idx, options, env):
        token = tokens[idx]
        content = token.content.lower()
        alt_text = token.content
        img_str = f'<img class="might-icon" src="/static/images/{content}_darkmode.webp" data-light="/static/images/{content}.webp" \
            data-dark="/static/images/{content}_darkmode.webp" alt="{alt_text}" style="height:1em; vertical-align:middle;">'
        return img_str

def parse_icon(state, silent):
    max = state.posMax
    if state.src[state.pos] != ":":
        return False

    if state.pos + 1 < state.posMax and state.src[state.pos + 1] != "[":
        return False

    labelStart = state.pos + 2
    labelEnd = state.md.helpers.parseLinkLabel(state, state.pos + 1, False)
    pos = labelEnd + 1

    if labelEnd < 0:
        return False
    
    if not silent:
        content = state.src[labelStart:labelEnd]
    
    tokens = list()
    state.md.inline.parse(content, state.md, state.env, tokens)

    token = state.push("icon", "img", 0)
    token.attrs = dict()
    token.children = tokens or None
    token.content = content

    state.pos = pos
    state.posMax = max
    return True


def init_renderer():
    md = MarkdownIt("gfm-like", renderer_cls=RrRenderer)
#    pprint.pprint(md.get_all_rules())
    pprint.pprint(md.inline.ruler.push("icon", parse_icon))
    return md
