"""
Created on 2020-01-10 Last Update 2020-02-04
@author : Jacques Gérard - UNamur (www.unamur.be)
@author : Fabrice Orbant - UNamur (www.unamur.be)
"""
if __name__ == '__main__': from SHIDev.session import loginRequired
from SHI.web import webPage, readForm, goTo
from SHIDev.tools import showField, thisFileName
from yattag import Doc
import os
from vues.personne import PersonPageView



@loginRequired 
def page(S = None):
    doc, tag, text = Doc().tagtext()
    Data = readForm(Blank = True)
    if S:
        with tag('div',klass='wrapper'):
            with tag('div', id='content'):
                with tag('div', klass='container-fluid'):
                    with tag('div', klass='row'):
                        if 'modify' in Data and (P := PersonPageView(S, Data['EID'])): ## Récupération de l'objet à modifier
                            for Key in Data:
                                if 'txt_' in Key: P.Set(Key[4:], Data[Key]) ## Création de l'objet modifié
                            P.Save() ## Enregistrement dans la DB
                            goTo('index.py')
                        elif (P := PersonPageView(S, S.Get('eID'))): ## S = Utilisateur connecté et demande. P = la personne à gérer.
                            '''__file__.split('\\')[-1] = le nom de ce fichier comme thisFileName qui est dans tools.'''
                            with tag('form', action=thisFileName(), method="post", name="formSaisie", enctype="multipart/form-data"):
                                for Key in P.Fields(): doc, tag, text = showField(doc, tag, text, P.Show(Key)) ## Affichage de tous les champs à modifier
                                doc.stag('br')
                                doc.input(type="hidden", id='EID', name='EID', value=P.Get('eid'))
                                doc.stag('input', type="submit", id='modify', name='modify', value="Mettre à jour", style="width:150px")
        webPage(Page = doc, Session = S)
    else:
        webPage(doc)



if __name__ == '__main__':
    page()










