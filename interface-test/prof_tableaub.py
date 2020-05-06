from datetime import datetime, date
from SHI.web import webPage, showField, readForm
from vues.personne import PersonPageView
import prof_menu
import parametres
import SHI.local_db as db
from yattag import Doc
if __name__ == '__main__':
    from SHIDev.session import loginRequired


def tableau_de_bord_page(doc, tag, text):
    doc, tag, text = Doc().tagtext()

    with tag('div', klass='wrapper'):
        doc, tag, text = prof_menu.sidebar(doc, tag, text)
        with tag('div', id='content'):

            with tag('h5', onclick="switch_table_etus_sujets()", klass='mouse_hand text-center'):
                text('Liste des étudiants qui ont choisi un de vos sujets')
                with tag('p', klass='collapse'):
                    pass
            with tag('div', id='div_chercher_nom_etu'):
                pass
                # """Recherche tab étuaints-sujet"""
                # with tag('input', type='text', id='chercher_nom_etu', onkeyup='recherche_etudiant()', placeholder='Chercher par nom', title='introduire un nom'):pass

            with tag('table', id='prof_table_sujets_profs', klass="table table-striped"):
                with tag('thead'):
                    with tag('tr'):
                        with tag('th',      klass="th-sm", scope="col"):
                            text('Nom')
                        with tag('th',      klass="th-sm",      scope="col"):
                            text('Prénom')
                        with tag('th',      klass="th-sm",      scope="col"):
                            text('Programme')
                        with tag('th',      klass="th-sm",      scope="col"):
                            text('Autres étudiant(s) par sujet')
                        with tag('th',      klass="th-sm",      scope="col"):
                            text('Sujets choisis')

                with tag('tbody'):
                    """A FAIRE UNE BOUCLE POUR LES ETUDIANTS"""

                    with tag('tr'):

                        with tag('td', scope="col"):
                            text('Johniiii')
                        with tag('td', scope="col"):
                            text('Antoineyyyy')
                        with tag('td', scope="col"):
                            text('Programme2')
                        with tag('td', scope='col'):
                            with tag('div', klass='numberCircle', onclick='mod_affiche_sujet_prof()'):
                                text('5')
                            with tag('div', id='nom-prenom-stud'):
                                # a faire une boucle
                                with tag('p'):
                                    text('Nom Prénom mail')
                                with tag('p'):
                                    text('Nom Prénom mail')
                                with tag('p'):
                                    text('Nom Prénom mail')
                                with tag('p'):
                                    text('Nom Prénom mail')
                                with tag('p'):
                                    text('Nom Prénom mail')
                        with tag('td', scope="col"):
                            text('wwww wwwww')

                    with tag('tr'):

                        with tag('td', scope="col"):
                            text('qaaaaa')
                        with tag('td', scope="col"):
                            text('Antoineyyyy')
                        with tag('td', scope="col"):
                            text('tttt')
                        with tag('td', scope='col'):
                            with tag('div', klass='numberCircle', onclick='mod_affiche_sujet_prof()'):
                                text('3')
                            with tag('div', id='nom-prenom-stud'):
                                # a faire une boucle
                                with tag('p'):
                                    text('Nom Prénom')
                                with tag('p'):
                                    text('Nom Prénom')
                                with tag('p'):
                                    text('Nom Prénom')
                        with tag('td', scope="col"):
                            text('aaaa xcvxcvxc')

            with tag('h5', onclick='switch_table_sujets_cette_annee()', klass='mouse_hand text-center'):
                text('Sujets attribués cette année ')
                with tag('p', klass='collapse'):
                    pass
            with tag('div', id='div_titre_sujet'):
                # """Recherche tab titre"""
                # with tag('input', type='text', id='chercher_titre', onkeyup='recherche_titre()', placeholder='Chercher par titre', title='introduire un nom'):pass

                with tag('table', id='table_sujets_cette_annee', klass="table table-striped table-bordered table-sm top-buffer", cellspacing="0", width="100%"):
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

            with tag('h5', onclick='switch_historique_sujet()', klass='mouse_hand text-center'):
                text('Historique des sujets atribués ')
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

    with tag('script', src="./dist/js/myjs.js"):
        pass
    with tag('script', src="./dist/js/prof_tab_bord.js"):
        pass
    with tag('script', src="./dist/js/datatables.min.js"):
        pass
    with tag('script', src="./dist/js/datatables.js"):
        pass

    return doc, tag, text
