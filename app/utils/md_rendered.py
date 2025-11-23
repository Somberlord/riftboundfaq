from markdown_it.renderer import RendererHTML, MarkdownIt

class RrRenderer(RendererHTML):
    pass


def plugin(md):
    def render_em_open1(self, tokens, idx, options, env):
        return '<em class="myclass1">'
    md.add_render_rule("em_open", render_em_open1)

def init_renderer():
    md = MarkdownIt("commonmark", renderer_cls=RrRenderer).use(plugin)
