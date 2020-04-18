"""
Created on 2020-01-10 Last Update 2020-01-23
@author : Jacques Gérard - UNamur (www.unamur.be)
@author : Fabrice Orbant - UNamur (www.unamur.be)
"""
if __name__ == '__main__': from SHIDev.session import loginRequired
from SHI.web import webPage,  readForm
from SHI.local_ldap import readLDAP, searchLDAP
from SHI.get_noe_identity import getNoeIdentity
from SHI.tools import htmlTable
import SHI.local_db as db
import parametres
from yattag import Doc



@loginRequired
def page(S = None):
    doc, tag, text = Doc().tagtext()
    if S:
        with tag('div',klass='wrapper'):
            with tag('nav', id='sidebar'):
                with tag('button', type='button', id='sidebarCollapse', klass='btn navbar-btn'):
                    doc.stag('input', type='image', id='Toggle', name='Toggle', src='./dist/icons/justify-left.svg')
                with tag('ul', klass='list-unstyled components'):
                    with tag('li'):
                        with tag('a', href='index.py'): text('Fiche personnelle')
                    with tag('li'):
                        with tag('a', href='ajouterPersonne.py'): text('Ajouter une personne')
                    with tag('li', klass='active'): 
                        text('Afficher la liste des personnes')
            with tag('div', id='content'):
                with tag('div', klass='container-fluid'):
                    with tag('div', klass='row'):
                        Records = db.readRecords(S.Get('eID'), parametres.Database, 'Personne', [], ['eid','nom','prenom', 'mail'])
                        doc.asis(htmlTable(Records))
        with tag('script',src="dist/js/sidebar.js"):pass
        #with tag('script',src="https://kit.fontawesome.com/a076d05399.js"):pass
        webPage(Page = doc, Session = S)
    else:
        webPage(doc)



if __name__ == '__main__':
    page()
