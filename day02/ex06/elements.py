from elem import Elem, Text

class html(Elem):
    def __init__(self,content=None, tag: str = 'html', attr: dict = {}, tag_type: str = 'double'):
        super().__init__(content, tag, attr, tag_type)

class head(Elem):
    def __init__(self,content=None, tag: str = 'head', attr: dict = {}, tag_type: str = 'double'):
        super().__init__(content, tag, attr, tag_type)

class body(Elem):
    def __init__(self,content=None, tag: str = 'body', attr: dict = {}, tag_type: str = 'double'):
        super().__init__(content, tag, attr, tag_type)

class title(Elem):
    def __init__(self,content=None, tag: str = 'title', attr: dict = {}, tag_type: str = 'double'):
        super().__init__(content, tag, attr, tag_type)

class meta(Elem):
    def __init__(self, content=None, tag: str = 'meta', attr: dict = {}, tag_type: str = 'simple'):
        super().__init__(content, tag, attr, tag_type)

class img(Elem):
    def __init__(self, content=None, tag: str = 'img', attr: dict = {}, tag_type: str = 'simple'):
        super().__init__(content, tag, attr, tag_type)

class table(Elem):
    def __init__(self, content=None, tag: str = 'table', attr: dict = {}, tag_type: str = 'double'):
        super().__init__(content, tag, attr, tag_type)
class th(Elem):
    def __init__(self, content=None, tag: str = 'th', attr: dict = {}, tag_type: str = 'double'):
        super().__init__(content, tag, attr, tag_type)       
class tr(Elem):
    def __init__(self, content=None, tag: str = 'tr', attr: dict = {}, tag_type: str = 'double'):
        super().__init__(content, tag, attr, tag_type)
class td(Elem):
    def __init__(self, content=None, tag: str = 'td', attr: dict = {}, tag_type: str = 'double'):
        super().__init__(content, tag, attr, tag_type)
class ul(Elem):
    def __init__(self, content=None, tag: str = 'ul', attr: dict = {}, tag_type: str = 'double'):
        super().__init__(content, tag, attr, tag_type)
class ol(Elem):
    def __init__(self, content=None, tag: str = 'ol', attr: dict = {}, tag_type: str = 'double'):
        super().__init__(content, tag, attr, tag_type)
class li(Elem):
    def __init__(self, content=None, tag: str = 'li', attr: dict = {}, tag_type: str = 'double'):
        super().__init__(content, tag, attr, tag_type)
class h1(Elem):
    def __init__(self, content=None, tag: str = 'h1', attr: dict = {}, tag_type: str = 'double'):
        super().__init__(content, tag, attr, tag_type)
class h2(Elem):
    def __init__(self, content=None, tag: str = 'h2', attr: dict = {}, tag_type: str = 'double'):
        super().__init__(content, tag, attr, tag_type)
class p(Elem):
    def __init__(self, content=None, tag: str = 'p', attr: dict = {}, tag_type: str = 'double'):
        super().__init__(content, tag, attr, tag_type)
class div(Elem):
    def __init__(self, content=None, tag: str = 'div', attr: dict = {}, tag_type: str = 'double'):
        super().__init__(content, tag, attr, tag_type)
class span(Elem):
    def __init__(self, content=None, tag: str = 'span', attr: dict = {}, tag_type: str = 'double'):
        super().__init__(content, tag, attr, tag_type)
class hr(Elem):
    def __init__(self, content=None, tag: str = 'hr', attr: dict = {}, tag_type: str = 'simple'):
        super().__init__(content, tag, attr, tag_type)
class br(Elem):
    def __init__(self, content=None, tag: str = 'br', attr: dict = {}, tag_type: str = 'simple'):
        super().__init__(content, tag, attr, tag_type)
def TestClass():
    print(html([head(),body()]))
    print(html([head(title(Text("Hello ground!"))),body([h1(Text("Oh no, not again!")), img(attr={'src':'http://i.imgur.com/pfp3T.jpg'})])]))

if __name__ == '__main__':
    TestClass()
   