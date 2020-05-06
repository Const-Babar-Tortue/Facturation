from datetime import datetime, date
from SHIDev.web import webPage
import admin_tableaub
import mod_tableaub
import etu_tableaub
import prof_tableaub
from yattag import Doc
if __name__ == '__main__':
    from SHI.session import loginRequired


@loginRequired
def page(S=None):
    doc, tag, text = Doc().tagtext()
    if S:
        with tag('div', klass='wrapper'):

            # """TABLEAU DE BORD PROFS"""
            # doc, tag, text = prof_tableaub.tableau_de_bord_page(doc, tag, text)
            # doc, tag, text = mod_tableaub.tableau_de_bord_page(
            #     S, doc, tag, text)
            # doc, tag, text = admin_tableaub.tableau_de_bord_page(
            #     doc, tag, text)
            doc, tag, text = etu_tableaub.tableau_de_bord_page(doc, tag, text)

        webPage(Page=doc, Session=S)

    else:
        webPage(doc)


if __name__ == '__main__':
    page()
