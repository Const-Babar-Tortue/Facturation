
from vues.personne import PersonPageView
import mod_menu
import parametres
from SHI.tools import sizingImage, getUrlFields
import SHI.local_db as db
from yattag import Doc
from SHI.web import webPage, readForm
if __name__ == '__main__':
    from SHIDev.session import loginRequired


programme = {'Finances': ['inge', 'sciences éco', 'plombier'],
             'Sciences': ['math', 'physique', 'trigo']
             }


@loginRequired
def page(S=None):
    doc, tag, text = Doc().tagtext()
    doc, tag, text = mod_menu.sidebar(doc, tag, text)
    if S:
        with tag('div', klass='text-center'):
            with tag('form', action='mod_rechercher_personne.py', method="post", name="formSaisie", enctype="multipart/form-data"):
                with tag('label'):
                    with tag('a'):
                        text('Rechercher une personne')
                    with tag('div', klass='input-group mb-3'):
                        doc.input(type="text", id="txt_recherche", klass="form-control input-lg",
                                  name="txt_recherche", minlength="3", maxlength="80", placeholder="Eid/Nom")
                        with tag('div', klass='input-group-append'):
                            with tag('span', klass='input-group-text'):
                                doc.stag('input', type='image', id='Search',
                                         name='Search', src='./dist/icons/search.svg')

        ###########################################

        with tag('br', klass='container-fluid ajouter'):

            with tag('h4'):
                text('Liste des sujets')

            with tag('table', id='table_prof_sujet', klass="table table-striped table-bordered table-sm top-buffer", cellspacing="0", width="100%"):
                with tag('thead'):
                    with tag('tr', klass='text-center'):
                        with tag('th', cope="col"):
                            text('Actif')
                        with tag('th', cope="col"):
                            text('Titre')
                        with tag('th', scope="col"):
                            text('Programme')
                        with tag('th', scope="col"):
                            text('Filière')
                        with tag('th', scope="col", klass='text-center'):
                            text('Modifier')
                        with tag('th', scope="col", klass='text-center'):
                            text('Supprimer')

                with tag('tbody'):
                    """A FAIRE UNE BOUCLE POUR LES sujets"""
                    with tag('tr'):
                        with tag('td', scope="col", klass='text-center'):
                            with tag('input', type='checkbox', value='0'):
                                pass
                        with tag('td', scope="col"):
                            with tag('textarea', klass='disable_text text', placeholder='Sujet sur les tomates'):
                                pass
                        with tag('td', scope="col"):
                            with tag('textarea', klass='disable_text text', placeholder='Agriculture'):
                                pass
                        with tag('td', scope="col"):
                            with tag('textarea', klass='disable_text text', placeholder='Eco'):
                                pass
                        with tag('td', scope="col", klass='mouse_hand text-center'):
                            with tag('img', src='./dist/images/pencil.png', id="myBtn"):
                                pass
                        with tag('td', scope="col", klass='mouse_hand text-center'):
                            with tag('img', src='./dist/images/bin.png', onclick='change()'):
                                pass

                        """ MODAL """
                        with tag('div', id='myModal', klass='modal'):
                            with tag('div', klass='modal-content'):
                                with tag('span', klass='close'):
                                    text("Fermer")

                                with tag('row', klass='row justify-content-center top-buffer'):

                                    with tag('form'):
                                        """ajouter sujet"""
                                        with tag('row', id="ajouter_sujet", klass='cacher'):

                                            # """Demander si le sujet sera actif pendant des années"""
                                            # with tag('div', klass='row justify-content-center top-buffer'):
                                            # with tag('div', klass='col-sm-4 text-center'):
                                            # with tag('label', klass='switch'):
                                            # doc.input( type = 'checkbox', name = 'valable_des_annees', value = '0')
                                            # with tag('span',klass='slider round'):
                                            # text('Sujet valable plusieures années ?')

                                            with tag('row', klass='row justify-content-center top-buffer'):

                                                with tag('row', klass='col-sm-10 text-center mod_width_textarea'):
                                                    with tag('textarea', placeholder='Titre'):
                                                        pass
                                                with tag('row', klass='col-sm-10 text-center mod_width_textarea'):
                                                    with tag('textarea', placeholder='Descriptif'):
                                                        pass

                                            with tag('row', klass=' top-buffer'):

                                                with tag('div', klass='row'):

                                                    """Afficher dynamiquement les programmes"""
                                                    with tag('div', klass='col-6 text-center'):
                                                        with tag('div', id="programmes"):
                                                            text(
                                                                'Programmes : ')
                                                            with tag('div'):
                                                                for p in programme:
                                                                    with tag('div'):
                                                                        # , klass='switch'):
                                                                        with tag('label'):
                                                                            doc.input(
                                                                                type='checkbox', name=p, value='0', onclick='afficherFilFin()')
                                                                            with tag('span', id=p+'1'):
                                                                                text(
                                                                                    p)

                                                    """Afficher dynamiquement les filières"""
                                                    with tag('div', klass='filiere col-6 text-center', id='FiliereFin'):
                                                        with tag('div'):
                                                            text(
                                                                'Filiére : ')
                                                            with tag('div'):
                                                                for f in programme['Finances']:
                                                                    with tag('div'):
                                                                        with tag('label'):
                                                                            doc.input(
                                                                                type='checkbox', name=f, value='0')
                                                                            with tag('span'):
                                                                                text(
                                                                                    f)

                                            with tag('div', klass='row'):

                                                with tag('div', klass='col-4 text-center'):
                                                    """Ajouter fichier annexe"""
                                                    with tag('div', klass='top-buffer row justify-content-center'):
                                                        text(
                                                            'Ajouter un fichier annexe')
                                                    with tag('br', klass='top-buffer row justify-content-center'):
                                                        with tag('input', type='file'):
                                                            pass

                                                """Etablir min et max etudiants"""
                                                # with tag('row', klass='row justify-content-center top-buffer'):
                                                # with tag('div', id='nbr_min_etus'):
                                                # with tag('input', type='number', placeholder='Nbr. min d\'étudiants'):pass
                                                with tag('div', klass='col-4 text-center'):
                                                    with tag('div', klass='top-buffer row justify-content-center'):
                                                        text(
                                                            'Décider le nombre d\'étudiant qui pourront avoic ce sujet')
                                                    with tag('br', klass='row justify-content-center top-buffer'):
                                                        with tag('div', id='nbr_max_etus'):
                                                            with tag('input', type='number', placeholder='Nbr. max d\'étudiants', min='1'):
                                                                pass

                                                with tag('div', klass='col-4 text-center'):
                                                    with tag('div', klass='top-buffer row justify-content-center'):
                                                        text(
                                                            'Année académique pour laquelle le sujet sera disponible')
                                                    with tag('div'):
                                                        doc.input(type='checkbox',
                                                                  name=p, value='0')
                                                        with tag('span', id='2020-2021'):
                                                            text(
                                                                '2020-2021')
                                                    with tag('div'):
                                                        doc.input(type='checkbox',
                                                                  name=p, value='0')
                                                        with tag('span', id='2021-2022'):
                                                            text(
                                                                '2021-2022')
                                                    with tag('div'):
                                                        doc.input(type='checkbox',
                                                                  name=p, value='0')
                                                        with tag('span', id='2022-2023'):
                                                            text(
                                                                '2022-2023')

                                            """ligne pour bouton 'enregistrer"""
                                            with tag('div', klass='row justify-content-center top-buffer'):
                                                with tag('div'):
                                                    with tag('a', href=''):
                                                        with tag('img', src="./dist/images/check.png"):
                                                            pass

        ###########################################

        with tag('h4', onclick="switch_table_etus_sujets()", klass='mouse_hand'):
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
        with tag('br'):

            with tag('h4', onclick='switch_table_sujets_cette_annee()', klass='mouse_hand'):
                text('Sujets attribués cette année')
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
            with tag('br'):
                with tag('h4', onclick='switch_historique_sujet()', klass='mouse_hand'):
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


####################################################################

        with tag('script', src="./dist/js/prof_sujets.js"):
            pass
        with tag('script', src="./dist/js/prof_tab_bord.js"):
            pass
        with tag('script', src="./dist/js/prof_modal.js"):
            pass
        with tag('script', src="./dist/js/datatables.min.js"):
            pass
        with tag('script', src="./dist/js/datatables.js"):
            pass
        with tag('script', src='./dist/js/responsive.min.js'):
            pass
        webPage(Page=doc, Session=S, CSS='dist/css/mycss.css', JS='myjs.js')
    else:
        webPage(doc)


if __name__ == '__main__':
    page()
