


from SHI.web import webPage, readForm, htmlObject, htmlTable
import parametres
from SHI.tools import sizingImage
import SHI.local_db as db
from yattag import Doc
import admin_menu
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
            doc, tag, text = admin_menu.sidebar(doc, tag, text)
            with tag('div', id='content'):
                pass
        

        with tag('div', klass="dropdown"):
            """Bouton menu"""
            with tag('button', klass="dropbtn"):
                text('Faculté ')
            """Menu descendant"""
            with tag('div', klass="dropdown-content"):

                with tag('a', href=''):
                    text('Droit')

                with tag('a', href=''):
                    text('Economie')

                with tag('a', href=''):
                    text('Informatique')

        
        with tag('script', src="dist/js/myjs.js"):
            pass
        with tag('stylesheet', src='./dist/css/mycss.css'):
            pass

        webPage(Page=doc, Session=S)
    else:
        webPage(doc)


if __name__ == '__main__':
    page()


