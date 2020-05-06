
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

            with tag('a', href="prof_sujets.py"):
                text('Sujets')

            with tag('a', href="prof_ajouter_sujet.py"):
                text('Ajouter sujet')

    return doc, tag, text


if __name__ == '__main__':
    sidebar()
