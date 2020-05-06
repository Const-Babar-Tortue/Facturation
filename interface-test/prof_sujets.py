from SHI.web import webPage, readForm
from vues.personne import PersonPageView
import prof_menu
import parametres
from SHI.tools import sizingImage, getUrlFields
import SHI.local_db as db
from yattag import Doc
if __name__ == '__main__':
    from SHIDev.session import loginRequired


programme = {'Finances': ['inge', 'sciences éco',
                          'plombier'], 'Sciences': ['math', 'physique', 'trigo']}


@loginRequired
def page(S=None):
    doc, tag, text = Doc().tagtext()
    if S:
        with tag('div', klass='wrapper'):
            doc, tag, text = prof_menu.sidebar(doc, tag, text)
            with tag('div', id='content'):
                with tag('div', klass='container-fluid ajouter'):

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

                                """MODAL FIN"""

                            # """ICI IL FAUT UNE BOUCLE QUI VA GENERER LES SUJETS"""
                            # with tag('tr'):
                                # with tag('td', klass='col-lg-8 top buffer-top'):
                                # with tag('input', type='checkbox', value='0', onchange='sujet_actif()'):pass
                                # with tag('td', klass='col-lg-8 top buffer-top'):
                                # with tag('textarea', name = 'titre', klass='disable_text '):
                                # text('Titre : ' + 'Ceci est un titre')
                                # with tag('td', klass='col-lg-1'):
                                # with tag('img', src='./dist/images/down_arrow_small.png', onclick='afficher_details_sujet()'):pass
                                # with tag('td', klass='col-lg-1'):
                                # with tag('img', src="./dist/images/pencil.png"):pass
                                # with tag('td', klass='col-lg-1 content-center', id='nbr_etus'):

                                # """IL FAUT ALLER CHERCHER LA SOMMES DES ETUS PAR SUJET"""

                                # with tag('div', klass="nbr_etus"):
                                # with tag('input', name = 'nbr_etus', type='number', klass='disable_text hover', value="5"):pass

                                # with tag('td', klass='col-lg-1'):
                                # with tag('img', src="./dist/images/bin.png"):pass

                            # with tag('tr', id = 'details_sujet'):

                                # with tag('row'):
                                # with tag('div'):

                                # with tag('td', klass='col-sm-9'):
                                # with tag('textarea', name = 'descriptif', placeholder = 'Descriptif : ' + 'qsdqsdqsdqsdqsdqsdqsd', klass='disable_text '):
                                # text('Descriptif : ' + 'Ceci est un descriptif')

                                # with tag('td', klass='col-sm-1'):
                                # """Afficher dynamiquement les programmes"""
                                # with tag('div', klass='top-buffer col-sm-1'):
                                # text('Programmes : ')
                                # with tag('div'):
                                # for p in programme:
                                # with tag('div'):
                                # with tag('label', klass='switch'):
                                # doc.input( type = 'checkbox', name = p, value = '0', onclick='afficherFil()')
                                # with tag('span', klass='slider round', id=p+'1'):
                                # text(p)

                                # with tag('td', klass='col-sm-1'):
                                # """Afficher dynamiquement les filières"""
                                # with tag('div', klass='top-buffer filiere col-sm-1', id='FiliereInfo'):
                                # text('Filiére : ')
                                # with tag('div'):
                                # for f in programme['Finances']:
                                # with tag('div'):
                                # with tag('label', klass='switch'):
                                # doc.input( type = 'checkbox', name = f, value = '0')
                                # with tag('span',klass='slider round'):
                                # text(f)

                                # with tag('td', klass='col-sm-1'):pass

                                # with tag('td', klass='col-sm-1'):pass

        with tag('script', src="./dist/js/prof_sujets.js"):
            pass
        with tag('script', src="./dist/js/prof_modal.js"):
            pass
        with tag('script', src="./dist/js/datatables.min.js"):
            pass
        with tag('script', src="./dist/js/datatables.js"):
            pass
        with tag('script', src='./dist/js/responsive.min.js'):
            pass
        with tag('stylesheet', src='./dist/css/modal.css'):
            pass

        webPage(Page=doc, Session=S, CSS='dist/css/mycss.css', JS='myjs.js')
    else:
        webPage(doc)


if __name__ == '__main__':
    page()
