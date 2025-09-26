import xml.sax

class GroupHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        self.current = name
        if self.current == 'person':
            print("--------Person----------")
            print(f"id:{attrs['id']}")
        return super().startElement(name, attrs)
    def characters(self, content):
        if self.current=='name':
            self.name = content
        elif self.current == 'sex':
            self.sex = content
        return super().characters(content)
    def endElement(self, name):
        if self.current=='name':
            print(f'name:{self.name}')
        elif self.current == 'sex':
            print(f'sex:{self.sex}')
        self.current = ''
        return super().endElement(name)


handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('data.xml')