
from SHI.web import webPage, readForm
from vues.personne import PersonPageView
import prof_menu
import parametres
from SHI.tools import sizingImage, getUrlFields
import SHI.local_db as db
from yattag import Doc
if __name__ == '__main__':
    from SHIDev.session import loginRequired

programme = {'Finances': [' Sciences Politiques', ' Sciences éco', ' Plombier'],
             'Sciences': [' Physique', ' Math', 'Trigo']
             }


@loginRequired
def page(S=None):
    doc, tag, text = Doc().tagtext()
    if S:
        with tag('div', klass='wrapper'):
            doc, tag, text = prof_menu.sidebar(doc, tag, text)
            with tag('div', id='content'):
                with tag('div', klass='container-fluid ajouter'):

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
                                            text('Programmes : ')
                                            with tag('div'):
                                                for p in programme:
                                                    with tag('div'):
                                                        # , klass='switch'):
                                                        with tag('label'):
                                                            doc.input(
                                                                type='checkbox', name=p, value='0', onclick='afficherFilFin()')
                                                            with tag('span', id=p+'1'):
                                                                text(p)

                                    """Afficher dynamiquement les filières"""
                                    with tag('div', klass='filiere col-6 text-center', id='FiliereFin'):
                                        with tag('div'):
                                            text('Filiére : ')
                                            with tag('div'):
                                                for f in programme['Finances']:
                                                    with tag('div'):
                                                        with tag('label'):
                                                            doc.input(
                                                                type='checkbox', name=f, value='0')
                                                            with tag('span'):
                                                                text(f)

                            with tag('div', klass='row'):

                                with tag('div', klass='col-4 text-center'):
                                    """Ajouter fichier annexe"""
                                    with tag('div', klass='top-buffer row justify-content-center'):
                                        text('Ajouter un fichier annexe')
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
                                            text('2020-2021')
                                    with tag('div'):
                                        doc.input(type='checkbox',
                                                  name=p, value='0')
                                        with tag('span', id='2021-2022'):
                                            text('2021-2022')
                                    with tag('div'):
                                        doc.input(type='checkbox',
                                                  name=p, value='0')
                                        with tag('span', id='2022-2023'):
                                            text('2022-2023')

                            """ligne pour bouton 'enregistrer"""
                            with tag('div', klass='row justify-content-center top-buffer'):
                                with tag('div'):
                                    with tag('a', href=''):
                                        with tag('img', src="./dist/images/check.png"):
                                            pass

        with tag('script', src="dist/js/myjs.js"):
            pass
        with tag('stylesheet', src='./dist/css/mycss.css'):
            pass

        webPage(Page=doc, Session=S, CSS='dist/css/mycss.css', JS='myjs.js')
    else:
        webPage(doc)


if __name__ == '__main__':
    page()
