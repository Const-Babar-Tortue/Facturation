

from SHI.web import webPage
from yattag import Doc


def sidebar(doc, tag, text):

    with tag('div', klass="dropdown"):
        """Bouton menu"""
        with tag('button', klass="dropbtn"):
            text('Menu')
        """Menu descendant"""
        with tag('div', klass="dropdown-content"):
            with tag('a', href="index.py"):
                text('Tableau de bord')

            with tag('a', href="mod_prendre_place.py"):
                text('Prendre la place de')

            with tag('a', href="mod_association.py"):
                text('Association')

    return doc, tag, text


if __name__ == '__main__':
    sidebar()
