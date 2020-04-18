"""
Created on 2020-01-10 Last Update 2020-02-05
@author : Jacques Gérard - UNamur (www.unamur.be)
@author : Fabrice Orbant - UNamur (www.unamur.be)
"""
if __name__ == '__main__': from SHIDev.session import loginRequired
from SHI.web import webPage, readForm
from yattag import Doc
import SHI.local_db as db
from SHI.tools import sizingImage, getUrlFields
import parametres
import menu
from vues.personne import PersonPageView

@loginRequired
def page(S = None):
    doc, tag, text = Doc().tagtext()
    if S:
        Get = getUrlFields()
        eID = Get['eidRecherche']
        
        P = PersonPageView(S, eID)
        
        with tag('div',klass='wrapper'):
            doc, tag, text = menu.sidebar(doc, tag, text)
            with tag('div', id='content'):
                with tag('div', klass='container-fluid'):
                    with tag('div', klass='row infopersonne'):
                        with tag('div', klass='col-sm-4'):
                            with tag('div', klass='row'):
                                with tag('div', klass='col-sm-3'):
                                    if P.Get('photo'):
                                        Width, Height = sizingImage(P.Get('photo'), H = 100)
                                        doc.stag('input', type='image', klass='photo', alt='Photo', src='data:image/jpg;base64,' + P.Get('photo'), width=Width, height=Height)
                                with tag('div', klass='col-sm-9 perso'):
                                    with tag('h4'):
                                        text(P.Get('prenom') + ' ' + P.Get('nom'))
                                    doc.stag('br')
                                    text (P.Get('eid'))
                                    doc.stag('br')
                                    text (P.Get('mail'))
                        with tag('div', klass='col-sm-3'):
                            with tag('h6'):
                                text('Informations UNamur')
                            klassgenre=''
                            if str.rstrip(P.Get('genre')) == 'male':
                                klassgenre = 'fa fa-male genre'
                            elif str.rstrip(P.Get('genre')) == 'female':
                                klassgenre = 'fa fa-famale genre'
                            with tag('i',klass=klassgenre):pass
                            with tag('i',klass='fab fa-cotton-bureau'):
                                text(' Bureau ...')
                            with tag('i',klass='fas fa-phone fa-sm'):
                                text(' Phone ...')
                        with tag('div', klass='col-sm-5'):
                            with tag('h6'):
                                text('Informations personnelles')
                                with tag('i',klass='fas fa-address-card fa-sm'):
                                    if P.Get('adresse') and P.Get('cp') and P.Get('localite'):
                                        text(' ' + P.Get('adresse') + ' - ' + P.Get('cp') + ' ' + P.Get('localite'))
                                with tag('i',klass='fas fa-at fa-sm'):
                                    if P.Get('mailprive'):
                                        text(' ' + P.Get('mailprive'))
                                with tag('i',klass='fas fa-phone fa-sm'):
                                    if P.Get('telprive'):
                                        text(' ' + P.Get('telprive'))  
                                with tag('i',klass='fas fa-atom fa-sm'):
                                    if P.Get('datenaissance'):
                                        text(' ' + str(P.Get('datenaissance')))
        webPage(Page = doc, Session = S)
    else:
        webPage(doc)



if __name__ == '__main__':
    page()
