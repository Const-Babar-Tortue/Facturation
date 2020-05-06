

from SHI.web import webPage, readForm, htmlObject, htmlTable
import mod_menu
import parametres
from SHI.tools import sizingImage
import SHI.local_db as db
from yattag import Doc
if __name__ == '__main__':
    from SHI.session import loginRequired

programme = {'Finances': ['inge', 'sciences éco', 'plombier'],
             'Sciences': ['math', 'physique', 'trigo']
             }


@loginRequired
def page(S=None):
    doc, tag, text = Doc().tagtext()
    Data = readForm()
    if S:

        with tag('div', klass='wrapper'):
            doc, tag, text = mod_menu.sidebar(doc, tag, text)
            with tag('div', id='content'):
                pass


        
        with tag('script', src="dist/js/myjs.js"):
            pass
        with tag('stylesheet', src='./dist/css/mycss.css'):
            pass

        webPage(Page=doc, Session=S)
    else:
        webPage(doc)


if __name__ == '__main__':
    page()
