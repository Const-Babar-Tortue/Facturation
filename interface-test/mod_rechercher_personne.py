
from SHI.web import webPage, readForm, htmlObject, htmlTable
import mod_menu
import parametres
from SHI.tools import sizingImage
import SHI.local_db as db
from yattag import Doc
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
        S.Set('eidOnWork', '')
        eleRecherche = Data['txt_recherche']
        Records = db.readRecords(S.Get('eID'), parametres.Database, 'Personne', [
                                 ('eid', '=', eleRecherche)], ['eid', 'nom', 'prenom'])
        with tag('div', klass='wrapper'):
            doc, tag, text = mod_menu.sidebar(doc, tag, text)
            with tag('div', id='content'):
                with tag('div', klass='container-fluid'):
                    if len(Records):
                        with tag('div', klass='list-group'):
                            text(str(Records))

                        with tag('div'):
                            with tag('div', klass='container-fluid ajouter'):

                                with tag('form'):
                                    """ajouter sujet"""
                                    with tag('row', id="ajouter_sujet"):

                                        with tag('row', klass='row justify-content-center top-buffer'):

                                            with tag('row', klass='col-sm-10 text-center mod_width_textarea'):
                                                with tag('textarea', placeholder='Titre'):
                                                    pass
                                            with tag('row', klass='col-sm-10 text-center mod_width_textarea'):
                                                with tag('textarea', placeholder='Descriptif'):
                                                    pass

                                        with tag('row', klass=' top-buffer'):

                                            with tag('div', klass='row col-sm-10 '):

                                                """Afficher dynamiquement les programmes"""
                                                with tag('div', klass='col-sm-2'):
                                                    with tag('div', id="programmes"):
                                                        text('Programmes : ')
                                                        with tag('div'):
                                                            for p in programme:
                                                                with tag('div'):
                                                                    with tag('label', klass='switch'):
                                                                        doc.input(
                                                                            type='checkbox', name=p, value='0', onclick='afficherFilFin()')
                                                                        with tag('span', klass='slider round', id=p+'1'):
                                                                            text(
                                                                                p)

                                                """Afficher dynamiquement les filières"""
                                                with tag('div', klass='filiere col-sm-2', id='FiliereFin'):
                                                    with tag('div'):
                                                        text('Filiére : ')
                                                        with tag('div'):
                                                            for f in programme['Finances']:
                                                                with tag('div'):
                                                                    with tag('label', klass='switch'):
                                                                        doc.input(
                                                                            type='checkbox', name=f, value='0')
                                                                        with tag('span', klass='slider round'):
                                                                            text(
                                                                                f)

                                        """Ajotuer fichier annexe"""
                                        with tag('div', klass='top-buffer row justify-content-center'):
                                            text('Ajouter un fichier annexe')
                                        with tag('div', klass='top-buffer row justify-content-center'):
                                            with tag('input', type='file'):
                                                pass

                                        """Etablir min et max etudiants"""
                                        # with tag('row', klass='row justify-content-center top-buffer'):
                                        # with tag('div', id='nbr_min_etus'):
                                        # with tag('input', type='number', placeholder='Nbr. min d\'étudiants'):pass

                                        with tag('row', klass='row justify-content-center top-buffer'):
                                            with tag('div', id='nbr_max_etus'):
                                                with tag('input', type='number', placeholder='Nbr. max d\'étudiants', min='1'):
                                                    pass

                                        """ligne pour bouton 'enregistrer"""
                                        with tag('row', klass='row justify-content-center top-buffer'):
                                            with tag('div'):
                                                with tag('a', href=''):
                                                    with tag('img', src="./dist/images/check.png"):
                                                        pass

                            """ZONE SUJET EXISTANTS MODIFIABLES"""
                            """AJOUTER UNE UNE BOUCLE POUR LE NBR DE SUJETS"""

                            with tag('div', klass='container-fluid '):
                                with tag('br'):
                                    with tag('h3', klass='text-center'):
                                        text('Sujet 1')

                                    with tag('label', klass='switch '):
                                        doc.input(type='checkbox',
                                                  name=p, value='1')
                                        with tag('span', klass='slider round', id=p+'1'):
                                            text('Actif')
                                with tag('form'):
                                    with tag('row', id="ajouter_sujet"):

                                        with tag('row', klass='row justify-content-center top-buffer'):

                                            with tag('row', klass='col-sm-10 text-center mod_width_textarea'):
                                                with tag('textarea', placeholder='Titre'):
                                                    pass
                                            with tag('row', klass='col-sm-10 text-center mod_width_textarea'):
                                                with tag('textarea', placeholder='Descriptif'):
                                                    pass

                                        with tag('row', klass=' top-buffer'):

                                            with tag('div', klass='row col-sm-10 '):

                                                """Afficher dynamiquement les programmes"""
                                                with tag('div', klass='col-sm-2'):
                                                    with tag('div', id="programmes"):
                                                        text('Programmes : ')
                                                        with tag('div'):
                                                            for p in programme:
                                                                with tag('div'):
                                                                    with tag('label', klass='switch'):
                                                                        doc.input(
                                                                            type='checkbox', name=p, value='0', onclick='afficherFilFin()')
                                                                        with tag('span', klass='slider round', id=p+'1'):
                                                                            text(
                                                                                p)

                                                """Afficher dynamiquement les filières"""
                                                with tag('div', klass='filiere col-sm-2', id='FiliereFin'):
                                                    with tag('div'):
                                                        text('Filiére : ')
                                                        with tag('div'):
                                                            for f in programme['Finances']:
                                                                with tag('div'):
                                                                    with tag('label', klass='switch'):
                                                                        doc.input(
                                                                            type='checkbox', name=f, value='0')
                                                                        with tag('span', klass='slider round'):
                                                                            text(
                                                                                f)

                                        """Ajotuer fichier annexe"""
                                        with tag('div', klass='top-buffer row justify-content-center'):
                                            text('Ajouter un fichier annexe')
                                        with tag('div', klass='top-buffer row justify-content-center'):
                                            with tag('input', type='file'):
                                                pass

                                        """Etablir min et max etudiants"""
                                        # with tag('row', klass='row justify-content-center top-buffer'):
                                        # with tag('div', id='nbr_min_etus'):
                                        # with tag('input', type='number', placeholder='Nbr. min d\'étudiants'):pass

                                        with tag('row', klass='row justify-content-center top-buffer'):
                                            with tag('div', id='nbr_max_etus'):
                                                with tag('input', type='number', placeholder='Nbr. max d\'étudiants', min='1'):
                                                    pass

                            with tag('div', klass='container-fluid '):
                                with tag('br'):
                                    with tag('h3', klass='text-center'):
                                        text('Sujet 2')

                                    with tag('label', klass='switch '):
                                        doc.input(type='checkbox',
                                                  name=p, value='1')
                                        with tag('span', klass='slider round', id=p+'1'):
                                            text('Actif')
                                with tag('form'):
                                    with tag('row', id="ajouter_sujet"):

                                        with tag('row', klass='row justify-content-center top-buffer'):

                                            with tag('row', klass='col-sm-10 text-center mod_width_textarea'):
                                                with tag('textarea', placeholder='Titre'):
                                                    pass
                                            with tag('row', klass='col-sm-10 text-center mod_width_textarea'):
                                                with tag('textarea', placeholder='Descriptif'):
                                                    pass

                                        with tag('row', klass=' top-buffer'):

                                            with tag('div', klass='row col-sm-10 '):

                                                """Afficher dynamiquement les programmes"""
                                                with tag('div', klass='col-sm-2'):
                                                    with tag('div', id="programmes"):
                                                        text('Programmes : ')
                                                        with tag('div'):
                                                            for p in programme:
                                                                with tag('div'):
                                                                    with tag('label', klass='switch'):
                                                                        doc.input(
                                                                            type='checkbox', name=p, value='0', onclick='afficherFilFin()')
                                                                        with tag('span', klass='slider round', id=p+'1'):
                                                                            text(
                                                                                p)

                                                """Afficher dynamiquement les filières"""
                                                with tag('div', klass='filiere col-sm-2', id='FiliereFin'):
                                                    with tag('div'):
                                                        text('Filiére : ')
                                                        with tag('div'):
                                                            for f in programme['Finances']:
                                                                with tag('div'):
                                                                    with tag('label', klass='switch'):
                                                                        doc.input(
                                                                            type='checkbox', name=f, value='0')
                                                                        with tag('span', klass='slider round'):
                                                                            text(
                                                                                f)

                                        """Ajotuer fichier annexe"""
                                        with tag('div', klass='top-buffer row justify-content-center'):
                                            text('Ajouter un fichier annexe')
                                        with tag('div', klass='top-buffer row justify-content-center'):
                                            with tag('input', type='file'):
                                                pass

                                        """Etablir min et max etudiants"""
                                        # with tag('row', klass='row justify-content-center top-buffer'):
                                        # with tag('div', id='nbr_min_etus'):
                                        # with tag('input', type='number', placeholder='Nbr. min d\'étudiants'):pass

                                        with tag('row', klass='row justify-content-center top-buffer'):
                                            with tag('div', id='nbr_max_etus'):
                                                with tag('input', type='number', placeholder='Nbr. max d\'étudiants', min='1'):
                                                    pass

                    else:
                        text('Personne ne correspond aux critères de recherche')
                    """Il faut faire la page avec une zone :
                        ajouter sujet SI click sur icone
                        sujet avec toutes ses caractérisitques et modifiable SI il y a des sujets
                        il ne faut pas oublier la case à cocher
                        """

        with tag('script', src="dist/js/myjs.js"):
            pass
        with tag('stylesheet', src='./dist/css/mycss.css'):
            pass

        webPage(Page=doc, Session=S)
    else:
        webPage(doc)


if __name__ == '__main__':
    page()
