#!/usr/bin/python3


class Text(str):
    def __str__(self):
        return super().__str__().replace('<','&lt;').replace('>','&gt;').replace('"','&quot;').replace('\n', '\n<br />\n')


class Elem:
    class ValidationError(Exception):
        def __init__(self) -> None:
            super().__init__("incorrect behaviour.")

        def __str__(self):
            return self.message

    def __init__(self,content=None, tag: str = 'div', attr: dict = {},  tag_type: str = 'double'):
        self.tag = tag
        self.attr = attr
        self.content = []
        if not (self.check_type(content) or content is None):
            raise self.ValidationError
        if type(content) == list:
            self.content = content
        elif content is not None:
            self.content.append(content)
        if (tag_type != 'double' and tag_type != 'simple'):
            raise self.ValidationError
        self.tag_type = tag_type


    def __str__(self):
        attr = self.__make_attr()
        result = f"<{self.tag}{attr}"
        content=self.__make_content()
        if self.tag_type == 'double':
            result += f">{content}</{self.tag}>"
        elif self.tag_type == 'simple':
            result += " >"
        return result

    def __make_attr(self):
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        if len(self.content) == 0:
            return ""
        result = "\n"
        for elem in self.content:
            if (len(str(elem)) != 0):
                result += f"{elem}\n"
        result = "  ".join(line for line in result.splitlines(True))
        if len(result.strip()) == 0:
            return ''
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


if __name__ == '__main__':
    #print(str(Elem(tag='body', attr={}, content=Elem(), tag_type='double')))

    print(str(Elem(content=Elem(content=Elem(content=Elem())))))