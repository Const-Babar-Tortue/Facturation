from datetime import datetime, date
from SHI.web import webPage
from vues.personne import PersonPageView
import etu_menu
import parametres
from SHI.tools import sizingImage
import SHI.local_db as db
from yattag import Doc
if __name__ == '__main__':
    from SHIDev.session import loginRequired

programme = {'Finances': [' Sciences Politiques', ' Sciences éco', ' Plombier'],
             'Sciences': [' Physique', ' Math', 'Trigo']
             }


def tableau_de_bord_page(doc, tag, text):

    with tag('div', klass='wrapper'):
        # doc, tag, text = etu_menu.sidebar(doc, tag, text)

        with tag('div', id='content'):

            # with tag('table', id='prof_table_sujets_profs', klass="table table-striped"):
            #     with tag('thead'):
            #         with tag('tr'):
            #             with tag('th',      klass="th-sm", scope="col"):
            #                 text('Nom')
            #             with tag('th',      klass="th-sm",      scope="col"):
            #                 text('Prénom')
            #             with tag('th',      klass="th-sm",      scope="col"):
            #                 text('Programme')
            #             with tag('th',      klass="th-sm",      scope="col"):
            #                 text('Autres étudiant(s) par sujet')
            #             with tag('th',      klass="th-sm",      scope="col"):
            #                 text('Sujets choisis')

            #     with tag('tbody'):
            #         """A FAIRE UNE BOUCLE POUR LES ETUDIANTS"""

            #         with tag('tr'):

            #             with tag('td', scope="col"):
            #                 text('Johniiii')
            #             with tag('td', scope="col"):
            #                 text('Antoineyyyy')
            #             with tag('td', scope="col"):
            #                 text('Programme2')
            #             with tag('td', scope='col'):
            #                 with tag('div', klass='numberCircle', onclick='mod_affiche_sujet_prof()'):
            #                     text('5')
            #                 with tag('div', id='nom-prenom-stud'):
            #                     # a faire une boucle
            #                     with tag('p'):
            #                         text('Nom Prénom mail')
            #                     with tag('p'):
            #                         text('Nom Prénom mail')
            #                     with tag('p'):
            #                         text('Nom Prénom mail')
            #                     with tag('p'):
            #                         text('Nom Prénom mail')
            #                     with tag('p'):
            #                         text('Nom Prénom mail')
            #             with tag('td', scope="col"):
            #                 text('wwww wwwww')

            #         with tag('tr'):

            #             with tag('td', scope="col"):
            #                 text('qaaaaa')
            #             with tag('td', scope="col"):
            #                 text('Antoineyyyy')
            #             with tag('td', scope="col"):
            #                 text('tttt')
            #             with tag('td', scope='col'):
            #                 with tag('div', klass='numberCircle', onclick='mod_affiche_sujet_prof()'):
            #                     text('3')
            #                 with tag('div', id='nom-prenom-stud'):
            #                     # a faire une boucle
            #                     with tag('p'):
            #                         text('Nom Prénom')
            #                     with tag('p'):
            #                         text('Nom Prénom')
            #                     with tag('p'):
            #                         text('Nom Prénom')
            #             with tag('td', scope="col"):
            #                 text('aaaa xcvxcvxc')
            sujet_associe = "Macro-économie"
            prof_associe = "Antoine "
            mail_prof = "antoine@unamur.be"
            descriptif_sujet = "Descriptif du sujet Descriptif du sujetDescriptif du sujetDescriptif du sujetDescriptif du sujet Descriptif du sujetDescriptif du sujetDescriptif du sujetDescriptif du sujet Descriptif du sujetDescriptif du sujetDescriptif du sujetDescriptif du sujet Descriptif du sujetDescriptif du sujetDescriptif du sujetDescriptif du sujet Descriptif du sujetDescriptif du sujetDescriptif du sujetDescriptif du sujet Descriptif du sujetDescriptif du sujetDescriptif du sujetDescriptif du sujet Descriptif du sujetDescriptif du sujetDescriptif du sujetDescriptif du sujet Descriptif du sujetDescriptif du sujetDescriptif du sujetDescriptif du sujet Descriptif du sujetDescriptif du sujetDescriptif du sujetDescriptif du sujet Descriptif du sujetDescriptif du sujetDescriptif du sujetDescriptif du sujet Descriptif du sujetDescriptif du sujetDescriptif du sujetDescriptif du sujet Descriptif du sujetDescriptif du sujetDescriptif du sujetDescriptif du sujet Descriptif du sujetDescriptif du sujetDescriptif du sujetDescriptif du sujet Descriptif du sujetDescriptif du sujetDescriptif du sujetDescriptif du sujet Descriptif du sujetDescriptif du sujetDescriptif du sujetDescriptif du sujet Descriptif du sujetDescriptif du sujetDescriptif du sujetDescriptif du sujet Descriptif du sujetDescriptif du sujetDescriptif du sujetDescriptif du sujet Descriptif du sujetDescriptif du sujetDescriptif du sujetDescriptif du sujet Descriptif du sujetDescriptif du sujetDescriptif du sujetDescriptif du sujet Descriptif du sujetDescriptif du sujetDescriptif du sujetDescriptif du sujet Descriptif du sujetDescriptif du sujetDescriptif du sujetDescriptif du sujet Descriptif du sujetDescriptif du sujetDescriptif du sujet"
            date_fermeture_sujet = " 20.03.2020 15h"

            with tag('h4', klass='text-center bold'):
                with tag('span'):
                    text('Vos choix seront cloturés le ' + date_fermeture_sujet)

            with tag('br'):
                with tag('h5', klass='text-center bold'):
                    text('Votre sujet ')
                    with tag('span', klass='underline mouse_hand', id="myBtn"):
                        text(sujet_associe)
                    text(' vous a été assigné avec le professeur ')
                    with tag('span', klass='underline mouse_hand'):
                        with tag('a', href="mailto:" + mail_prof + "?subject={Mémoire}: " + sujet_associe):
                            text(prof_associe)

                    with tag('div', id='myModal', klass='modal'):

                        """A utiliser les modules de mise en forme automatique"""
                        with tag('div', klass='modal-content d-flex'):
                            with tag('span', klass='close'):
                                text("Fermer")

                            with tag('h4'):
                                text('Professeur : ' + prof_associe)

                            """Faire une boucle pour afficher tous les sujets des profs"""
                            with tag('br'):
                                with tag('h4', klass='color_sujet'):
                                    text('Sujet ' + sujet_associe)

                            with tag('br'):
                                with tag('h5'):
                                    text('Déscriptif:')
                                with tag('div'):
                                    text(descriptif_sujet)

                            with tag('br'):
                                with tag('h5'):
                                    text('Filiéres')
                                with tag('div'):
                                    text(
                                        'le sujet est dans les filiéres suivantes : ' + ' test ')

                            with tag('br'):
                                with tag('h5'):
                                    text('Annexe')
                                with tag('div'):
                                    with tag('img', src='./dist/images/eye.png', id="myBtn"):
                                        pass

            with tag('br'):

                with tag('h5', onclick='switch_table_sujets_cette_annee()', klass='text-center mouse_hand'):

                    # hide or show the chevron in order to recognize that the div si expendable
                    with tag('img', src='./dist/icons/chevron-down.svg', id='arrow_down_sujet_annee', klass='text-center'):
                        pass
                    with tag('img', src='./dist/icons/chevron-up.svg', id='arrow_up_sujet_annee', klass='text-center'):
                        pass

                    text('Sujets de cette année')

                with tag('div', id='div_titre_sujet'):

                    with tag('table', id='table_sujets_cette_annee', klass="table table-striped table-bordered table-sm top-buffer text-center", cellspacing="0", width="100%"):
                        with tag('h5', klass='text-center'):
                            text(
                                "Nous vous prions de définir les sujets que vous préferez, en ordre croissant.")
                        with tag('thead'):
                            with tag('tr', klass='text-center'):

                                with tag('th', cope="col", klass='text-center'):
                                    text('Choix')
                                with tag('th', cope="col", klass='text-center'):
                                    text('Titre')
                                with tag('th', scope="col", klass='text-center'):
                                    text('Descriptif')
                                with tag('th', scope="col", klass='text-center'):
                                    text('Annexe')
                                with tag('th', scope="col", klass='text-center'):
                                    text('Filiére')
                                with tag('th', scope="col", klass='text-center'):
                                    text('Programme')
                                with tag('th', scope="col", klass='text-center'):
                                    text('Professeur')
                                with tag('th', scope="col", klass='text-center'):
                                    text('Autres étudiants')

                        with tag('tbody'):
                            """A FAIRE UNE BOUCLE POUR LES sujets"""
                            with tag('tr'):
                                with tag('td', scope="col", klass='text-center'):

                                    with tag('div', klass='text-center'):
                                        doc.input(type='checkbox',
                                                  name="1" + "id", value='0')
                                        with tag('span', id='1'+"id"):
                                            text('1')

                                    with tag('div', klass='text-center'):
                                        doc.input(type='checkbox',
                                                  name="2" + "id", value='0')
                                        with tag('span', id='2'+"id"):
                                            text('2')

                                    with tag('div', klass='text-center'):
                                        doc.input(type='checkbox',
                                                  name="3" + "id", value='0')
                                        with tag('span', id='3'+"id"):
                                            text('3')

                                with tag('td', scope="col", klass='text-center'):
                                    text('Macro-économie')
                                with tag('td', scope="col", klass='text-center'):
                                    text(
                                        'Comment la macro-éco fnComment la macro-éco fnComment la macro-éco fnComment la macro-éco fnComment la macro-éco fnComment la macro-éco fnComment la macro-éco fnComment la Stop')
                                with tag('td', scope="col", klass='text-center'):
                                    with tag('img', src='./dist/images/eye.png', id="myBtnAnnexe"):
                                        pass
                                with tag('td', scope="col", klass='text-center'):
                                    text('Sciences éco')
                                with tag('td', scope="col", klass='text-center'):
                                    text('Macro-économie')
                                with tag('td', scope="col", klass='text-center'):
                                    text('Dr. Antoine ')
                                with tag('td', scope="col", klass='text-center'):
                                    with tag('div', klass='numberCircle', onclick='mod_affiche_sujet_prof()'):
                                        text('5')
                                    with tag('div', id='nom-prenom-stud'):
                                        # a faire une boucle
                                        with tag('p'):
                                            text('3 ' + 'fois' + ' choix 1 ')
                                        with tag('p'):
                                            text('1 ' + 'fois' + ' choix 2 ')
                                        with tag('p'):
                                            text('1 ' + 'fois' + ' choix 3 ')

            with tag('h5', onclick='switch_addsu()', klass='text-center mouse_hand'):

                # hide or show the chevron in order to recognize that the div si expendable
                with tag('img', src='./dist/icons/chevron-down.svg', id='arrow_down_addsu', klass='text-center'):
                    pass
                with tag('img', src='./dist/icons/chevron-up.svg', id='arrow_up_addsu', klass='text-center'):
                    pass

                text('Ajouter son propre sujet')

            with tag('div', id='div_addsu'):
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
                                                            type='checkbox', name=p, value='0', onclick='etu_afficherFilFin()')
                                                        with tag('span', id=p+'1'):
                                                            text(p)

                                """Afficher dynamiquement les filières"""
                                with tag('div', klass='col-6 text-center'):
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

                                with tag('div', klass='col-6 text-center'):
                                    """Ajouter fichier annexe"""
                                    with tag('div', klass='top-buffer row justify-content-center'):
                                        text('Ajouter un fichier annexe')
                                    with tag('br', klass='top-buffer row justify-content-center'):
                                        with tag('input', type='file'):
                                            pass

                                with tag('div', klass='col-6 text-center'):
                                    with tag('div', klass='top-buffer row justify-content-center'):
                                        text('Professeur responsable')
                                    with tag('div'):
                                        doc.input(type='checkbox',
                                                  name=p, value='0')
                                        with tag('span', id='Jacques Gerard'):
                                            text('Jacques Gerard')
                                    with tag('div'):
                                        doc.input(type='checkbox',
                                                  name=p, value='0')
                                        with tag('span', id='Fabrice Orbant'):
                                            text('Fabrice Orbant')
                                    with tag('div'):
                                        doc.input(type='checkbox',
                                                  name=p, value='0')
                                        with tag('span', id='John Travolta'):
                                            text('John Travolta')

                        """ligne pour bouton 'enregistrer"""
                        with tag('div', klass='row justify-content-center top-buffer'):
                            with tag('div'):
                                with tag('a', href=''):
                                    with tag('img', src="./dist/images/check.png"):
                                        pass

    with tag('script', src="./dist/js/mod_affiche_sujet_prof.js"):
        pass
    with tag('script', src="./dist/js/etu_tableaub.js"):
        pass
    with tag('script', src="./dist/js/myjs.js"):
        pass
    with tag('script', src="./dist/js/prof_tab_bord.js"):
        pass
    with tag('script', src="./dist/js/datatables.min.js"):
        pass
    with tag('stylesheet', src='./dist/css/modal.css'):
        pass

    return doc, tag, text
