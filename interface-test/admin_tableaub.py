from datetime import datetime, date
from SHI.web import webPage
from vues.personne import PersonPageView
import parametres
import SHI.local_db as db
from yattag import Doc
import admin_menu
if __name__ == '__main__':
    from SHIDev.session import loginRequired


def tableau_de_bord_page(doc, tag, text):

    with tag('div', klass='wrapper'):
        doc, tag, text = admin_menu.sidebar(doc, tag, text)
        with tag('div', id='content', klass='text-center'):

            with tag('h5', onclick="switch_table_etus_sujets()", klass='mouse-hand text-center '):
                with tag('div', klass='mouse-hand'):
                    text('Liste des étudiants qui ont choisi un de vos sujets')
            with tag('div', id='div_chercher_nom_etu'):
                # """Recherche tab étuaints-sujet"""
                # with tag('input', type='text', id='chercher_nom_etu', onkeyup='recherche_etudiant()', placeholder='Chercher par nom', title='introduire un nom'):pass

                with tag('table', id='admin_table_sujets_profs', klass="table table-striped table-bordered table-sm top-buffer", cellspacing="0", width="100%"):
                    with tag('thead'):
                        with tag('tr'):

                            with tag('th',      klass="th-sm",      scope="col"):
                                text('Nom')
                            with tag('th',      klass="th-sm",      scope="col"):
                                text('Prénom')
                            with tag('th',      klass="th-sm",      scope="col"):
                                text('Programme')
                            with tag('th',      klass="th-sm",      scope="col"):
                                text('Sujets choisis')
                            with tag('th',      klass="th-sm",      scope="col"):
                                text('Etudiants l\'ayant choisi le même sujet')
                    with tag('tbody'):
                        """A FAIRE UNE BOUCLE POUR LES ETUDIANTS"""

                        with tag('tr'):

                            with tag('td', scope="col"):
                                text('Johniiii')
                            with tag('td', scope="col"):
                                text('Antoineyyyy')
                            with tag('td', scope="col"):
                                text('Programme2')
                            with tag('td', scope="col"):
                                text('wwww wwwww')
                            with tag('td', scope="col"):
                                text('2')

                        with tag('tr'):

                            with tag('td', scope="col"):
                                text('qaaaaa')
                            with tag('td', scope="col"):
                                text('Antoineyyyy')
                            with tag('td', scope="col"):
                                text('tttt')
                            with tag('td', scope="col"):
                                text('aaaa xcvxcvxc')
                            with tag('td', scope="col"):
                                text('1')

            with tag('h5', onclick='switch_table_sujets_cette_annee()', klass='text-center mouse_hand'):
                text('Sujets attribués cette année ')
            with tag('div', id='div_titre_sujet'):
                # """Recherche tab titre"""
                # with tag('input', type='text', id='chercher_titre', onkeyup='recherche_titre()', placeholder='Chercher par titre', title='introduire un nom'):pass

                with tag('table', id='admin_sujets_atrib', klass="table table-striped table-bordered table-sm top-buffer", cellspacing="0", width="100%"):
                    with tag('thead'):
                        with tag('tr'):

                            with tag('th', cope="col"):
                                text('Titre')
                            with tag('th', scope="col"):
                                text('Programme')
                            with tag('th', scope="col"):
                                text('Filière')
                            with tag('th', scope="col"):
                                text('Etudiant')
                    with tag('tbody'):
                        """A FAIRE UNE BOUCLE POUR LES sujets"""
                        with tag('tr'):

                            with tag('td', scope="col"):
                                text('Titre')
                            with tag('td', scope="col"):
                                text('Programme')
                            with tag('td', scope="col"):
                                text('Filière')
                            with tag('td', scope="col"):
                                text('Etudiant')

            with tag('h5', onclick='switch_historique_sujet()', klass='text-center mouse_hand'):
                text('Historique des sujets atribués')
            with tag('div', id='div_historique'):
                with tag('table', id='table_etu_sujet', klass="table table-striped table-bordered table-sm top-buffer", cellspacing="0", width="100%"):
                    with tag('thead'):
                        with tag('tr'):

                            with tag('th', cope="col"):
                                text('Titre')
                            with tag('th', scope="col"):
                                text('Programme')
                            with tag('th', scope="col"):
                                text('Filière')
                            with tag('th', scope="col"):
                                text('Etudiant')
                            with tag('th', scope="col"):
                                text('Année scolaire')

                    with tag('tbody'):
                        """A FAIRE UNE BOUCLE POUR L'historique"""

                        with tag('tr'):

                            with tag('td', scope="col"):
                                text('Johniiii')
                            with tag('td', scope="col"):
                                text('Antoineyyyy')
                            with tag('td', scope="col"):
                                text('Programme2')
                            with tag('td', scope="col"):
                                text('wwww wwwww')
                            with tag('td', scope="col"):
                                text('2')

    with tag('script', src="./dist/js/admin_tableaub.js"):
        pass

    with tag('script', src="./dist/js/myjs.js"):
        pass

    with tag('script', src="./dist/js/datatables.min.js"):
        pass
    with tag('script', src="./dist/js/datatables.js"):
        pass
    return doc, tag, text


if __name__ == '__main__':
    page()
