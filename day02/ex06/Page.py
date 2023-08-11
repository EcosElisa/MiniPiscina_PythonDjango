from elem import Elem, Text
from elements import html, h1, img, div, span, body , head, title, meta,table,th, tr, td, ul, ol, li, h2, p, hr, br

class Page:
    def __init__(self, elem):
        self.elem = elem
    
    def is_valid(self):
        valid_types = [
            'html', 'head', 'title', 'meta','body',  'img', 'table', 'th', 'tr', 'td',
            'ul', 'ol', 'li', 'h1', 'h2', 'p', 'div', 'span', 'hr', 'br', 'Text'
        ]        
        return self.validate_structure(self.elem, valid_types)
    
    def validate_structure(self, element, valid_types):

        if not isinstance(element, Elem):
            return element in valid_types
        
        if element.tag not in valid_types:
            return False
        
        valid_content_types = [
            'h1', 'h2', 'div','p','div','hr', 'br',   'table', 'ul', 'ol', 'span', 'text','th', 'tr', 'td',
        ]

        if element.tag == 'html':
            return all(isinstance(content, Elem) for content in element.content) and \
                   all(self.validate_structure(content, valid_types) for content in element.content)
        
        if element.tag == 'head':
            title_count = 0
            for content in element.content:
                if content.tag == 'title':
                    title_count += 1
                elif content.tag == 'meta':
                    return True
                elif not self.validate_structure(content, valid_types):
                    return False
            return title_count == 1
        
        if element.tag == 'body' or element.tag == 'div':

            return all(content.tag in valid_content_types or isinstance(content, Text) for content in element.content) and \
                   all(self.validate_structure(content, valid_types) for content in element.content)
        
        if element.tag in valid_content_types:
            return len(element.content) == 1 and isinstance(element.content[0], Text)
        
        if element.tag == 'span':
            return all(isinstance(content, Text) or content.tag == 'p' for content in element.content) and \
                   all(self.validate_structure(content, valid_types) for content in element.content)
        
        if element.tag == 'ul' or element.tag == 'ol':
            return all(content.tag == 'li' for content in element.content) and \
                   all(self.validate_structure(content, valid_types) for content in element.content)
        
        if element.tag == 'tr':
            return any(content.tag in ['th', 'td'] for content in element.content) and \
                   all(content.tag in ['th', 'td'] for content in element.content) and \
                   all(self.validate_structure(content, valid_types) for content in element.content)
        
        if element.tag == 'table':
            return all(content.tag == 'tr' for content in element.content) and \
                   all(self.validate_structure(content, valid_types) for content in element.content)
        
        return False
    #validar se tem um head e body em seguida
    #Cabeçalho deve conter apenas um Título e apenas um Título.
    def __str__(self):
        return str(self.elem)
    
    def write_to_file(self, filename):
        with open(filename, 'w') as file:
            if isinstance(self.elem, html):
                file.write("<!DOCTYPE html>\n")
            file.write(str(self.elem))
             
            file.close()
        print("arquivo gerado com sucessso")

    def TesteAll():
          # Test elements
        content = [
            h1(Text("This is a test page")),
            p(Text("Welcome to our website!")),
            img(attr={'src': 'https://cbissn.ibict.br/images/phocagallery/galeria2/thumbs/phoca_thumb_l_image03_grd.png', 'alt':'imagem'}),
            ul([li(Text("Item 1")), li(Text("Item 2")), li(Text("Item 3"))]),
            ol([li(Text("Item 1")), li(Text("Item 2")), li(Text("Item 3"))]),
            table([tr([th(Text("Header 1")), th(Text("Header 2"))]),
                tr([td(Text("Data 1")), td(Text("Data 2"))])]),
            div([h2(Text("Subheading")), p(Text("This is a subheading text."))]),
            span(Text("Hello, This is a span with a paragraph.")),
            hr(),
            br(),
            Text("This is a plain text.")
        ]
    

        page_body = body(content=content)
        page_head = head([meta(attr={'charset':'UTF-8'}),title(Text("Hello ground!"))])
        page_html = html([page_head, page_body],attr={'lang': 'en'})
        
        # Test Page
        #test_page =Page(html([ead(Title(Text('title'))), Body(Li())])).is_valid()
        #test_page.is_valid()  # Should print True
        
        # Display HTML code of the page
        #print(test_page)
        
        # Write the page HTML to a file
       # test_page.write_to_file("test_page.html")
        Page(html([head(title(Text('title'))), body()])).write_to_file("test.html")

    def Test():
         # Demonstrate how Page class works with tests
        body_content = [
            h1(Text("Oh no, not again!"),
            img(attr={'src':'http://i.imgur.com/pfp3T.jpg'}))
        ]
        page_body = body(content=body_content)
        page_head = head(title(Text("Hello ground!")))
        page_html = html([page_head, page_body])
        
        page = Page(page_html)
        print(page.is_valid())  # Should print True
        print(page)  # Print the HTML code
        page.write_to_file("output.html")  # Write HTML to a file

if __name__ == '__main__':
    #Page.Test()
    Page.TesteAll()