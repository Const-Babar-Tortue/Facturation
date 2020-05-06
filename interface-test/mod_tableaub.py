from datetime import datetime, date
from SHI.web import webPage, showField, readForm
from vues.personne import PersonPageView
import mod_menu
import parametres
import SHI.local_db as db
from yattag import Doc
if __name__ == '__main__':
    from SHIDev.session import loginRequired


def tableau_de_bord_page(S, doc, tag, text):
    doc, tag, text = Doc().tagtext()
    if S:
        Found = False

        with tag('br'):
            R9 = db.readRecords(
                S.Get('eID'), parametres.Database, 'personne', False)
        with tag('div', klass='wrapper'):
            doc, tag, text = mod_menu.sidebar(doc, tag, text)

        with tag('div', id='content'):

            with tag('div', klass="dropdown"):
                """Bouton menu"""
                with tag('button', klass="dropbtn"):
                    text('Choisir une filière ')
                """Menu descendant"""
                with tag('div', klass="dropdown-content"):

                    with tag('a', href=''):
                        text('Fil 1')

                    with tag('a', href=''):
                        text('Fil 2')

                    with tag('a', href=''):
                        text('Fil 3')

            with tag('h4', onclick='switch_table_profs_sujet()', klass="text-center"):
                text('Sujets proposés par les professeurs')

            with tag('div', id='div_profs_sujet'):

                with tag('table', id='mod_table_sujets_profs', klass="table table-striped"):

                    with tag('thead'):
                        with tag('tr', klass='text-center'):
                            with tag('th'):
                                text('Nom')
                            with tag('th'):
                                text('Mail')
                            with tag('th'):
                                text('Plus de détails')
                            with tag('th'):
                                text('Sujets')
                            with tag('th'):
                                text('Etudiants')

                    with tag('tbody'):
                        """A FAIRE UNE BOUCLE POUR LES PROFS"""
                        for el in R9:
                            with tag('tr', klass='text-center'):
                                with tag('td'):
                                    text(str(el["nom"]))
                                with tag('td'):
                                    text(str(el["mail"]))
                                with tag('td'):
                                    with tag('img', src='./dist/images/eye.png', id="myBtn"):
                                        pass
                                with tag('td'):
                                    with tag('div', klass='numberCircle', onclick='mod_affiche_sujets()'):
                                        text('3')
                                    with tag('div', id='mod-sujet-stud'):
                                        # a faire une boucle
                                        with tag('p'):
                                            text('Sujet vitesse')
                                        with tag('p'):
                                            text('Sujet test')
                                        with tag('p'):
                                            text('Sujet ok')
                                with tag('td'):
                                    with tag('div', klass='numberCircle', onclick='mod_affiche_sujet_prof()'):
                                        text('5')
                                    with tag('div', id='nom-prenom-stud'):
                                        # a faire une boucle
                                        with tag('p'):
                                            text('Nom Prénom')
                                        with tag('p'):
                                            text('Nom Prénom')
                                        with tag('p'):
                                            text('Nom Prénom')
                                        with tag('p'):
                                            text('Nom Prénom')
                                        with tag('p'):
                                            text('Nom Prénom')

                        """ MODAL """
                        with tag('div', id='myModal', klass='modal'):

                            """A utiliser les modules de mise en forme automatique"""
                            with tag('div', klass='modal-content d-flex'):
                                with tag('span', klass='close'):
                                    text("Fermer")

                                with tag('h4'):
                                    text('Professeur : ' + 'Nom du prof')

                                """Faire une boucle pour afficher tous les sujets des profs"""
                                with tag('div'):
                                    with tag('h4', klass='color_sujet'):
                                        text('Sujet ' + 'x')

                                with tag('div'):
                                    with tag('h5'):
                                        text('Titre :')
                                    with tag('div'):
                                        text('Ceci est un titre  qsdqsdqsdqsdqs')

                                with tag('div'):
                                    with tag('h5'):
                                        text('Déscriptif:')
                                    with tag('div'):
                                        text(
                                            'Ceci est un titre  déscriptif dqsdqsdqsdqs')

                                with tag('div'):
                                    with tag('h5'):
                                        text('Filiéres')
                                    with tag('div'):
                                        text(
                                            'le sujet est dans les filiéres suivantes : ' + ' test ')

                                with tag('div'):
                                    with tag('h5'):
                                        text('Nombre étudiants par sujet')
                                    with tag('div'):
                                        text(
                                            'X ' + ' étudiants ont choisi ce sujet. ')

                                """Faire une boucle pour afficher tous les sujets des profs"""

                with tag('br'):
                    pass
                with tag('div', klass='row'):
                    """Dates profs """
                    with tag('h5', klass='col-4 text-center'):
                        text(
                            'Dates d\'ouverture et fermeture dêpot sujet')

                    """Dates etus """
                    with tag('h5', klass='col-4 text-center'):
                        doc.input(type='checkbox', name='sujet-etu', value='0')
                        text('L\'étudiant peut ajouter son propre sujet')

                    # """Dates etus """
                    with tag('h5', klass='col-4 text-center'):
                        text(
                            'Dates d\'ouverture et fermeture choix sujet')

            # """Algos"""
            # with tag('h5', onclick='switch_algos()'):
            #     text('Algorithme à utiliser lors de l\'association + ')
            # with tag('div', id='choix_algos', klass='cache'):
            #     with tag('label', klass='container'):
            #         with tag('input', type='radio', name='radio' ):
            #             text('Munkres')
            #             with tag('span', klass='checkmark'):pass
            #     with tag('label', klass='container'):
            #         with tag('input', type='radio', name='radio' ):
            #             text('Gale et Shapley ')
            #             with tag('span', klass='checkmark'):pass
            #     with tag('label', klass='container'):
            #         with tag('input', type='radio', name='radio' ):
            #             text('Manuellement')
            #             with tag('span', klass='checkmark'):pass
    with tag('script', src="./dist/js/mod_tableaub.js"):
        pass
    with tag('script', src="./dist/js/myjs.js"):
        pass
    with tag('script', src="./dist/js/mod_affiche_sujet_prof.js"):
        pass
    with tag('script', src="./dist/js/mod_modal_oeil_tableaub.js"):
        pass
    with tag('script', src="./dist/js/datatables.min.js"):
        pass
    with tag('stylesheet', src='./dist/css/modal.css'):
        pass

    return doc, tag, text
