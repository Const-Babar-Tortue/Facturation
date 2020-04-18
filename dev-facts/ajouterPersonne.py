"""
Created on 2020-01-10 Last Update 2020-01-23
@author : Jacques Gérard - UNamur (www.unamur.be)
@author : Fabrice Orbant - UNamur (www.unamur.be)
"""
if __name__ == '__main__': from SHIDev.session import loginRequired
from SHI.web import webPage,  readForm
from SHI.local_ldap import readLDAP, searchLDAP
from SHI.tools import htmlTable, htmlObject
import SHI.local_db as db
import parametres, menu
from yattag import Doc
from noe import updatePerson

''' To do
Vérifier les accents et les majuscules
'''

def addPersonInDB(S = None, Data = {}, Person = {}):
    '''Fonction qui va ajouter une personne dans notre base de données.
    
    Structure des données:
    ['id_per', 'eid', 'nom', 'prenom', 'gsm', 'gsmvisible', 'genre', 'mailprive', 'mailprivevisible', 'remarque', 'datenaissance', \
    'datenaissancevisible', 'localite', 'cp', 'mail', 'pays', 'adresse', 'adressevisible', 'datearrivee', 'datedepart', 'telprive', \
    'telprivevisible', 'accesprint', 'cloud', 'vpn', 'wifi', 'agenda', 'ad', 'langue']'''
    ToAdd = dict()
    if Data['txt_eid']: ToAdd['eid'] = Data['txt_eid']
    if Data['txt_nom']: ToAdd['nom'] = Data['txt_nom']
    if Data['txt_prenom']: ToAdd['prenom'] = Data['txt_prenom']
    if 'uid' in Person and Person['uid']: ToAdd['eid'] = Person['uid']
    if 'fundpSOGoMail' in Person and Person['fundpSOGoMail']: ToAdd['mail'] = Person['fundpSOGoMail']
    if 'sn' in Person and Person['sn']: ToAdd['nom'] = Person['sn']
    if 'givenName' in Person and Person['givenName']: ToAdd['prenom'] = Person['givenName']
    try:
        R = db.insertRecord(S.Get('eID'), parametres.Database, 'Personne', ToAdd)
        if 'uid' in Person and Person['uid']:
            R = updatePerson(S, Person['uid'])
    except TypeError as Error:
        return db.fullErrorMessage(Error)
    return R



def checkBD(S = None, Data=[]): ## On ne gère pas l'exception d'une homonymie (nom, prénom). Sera géré manuellement par le Correspondant
    '''Fonction qui vérifie si la personne via son eid ou son nom et prénom exacte se trouve dans notre BD.
    
    Attention aux accents et aux majuscules.
    Si la personne est déjà dans la bd, on ne fait rien, sinon on récupère les datas du ldap (nom, prenom, eid, e-mail).
    '''
    if Data['txt_eid']:
        Search=[('eid','=',Data['txt_eid'])]
        searchFilterList = [('uid', Data['txt_eid'])]
    else:
        Search=[('nom','=',Data['txt_nom']),('prenom','=',Data['txt_prenom'])]
        searchFilterList = [('givenName', Data['txt_prenom']), ('sn', Data['txt_nom'])]
    query = db.readRecords(S.Get('eID'), parametres.Database, Table = 'Personne', Search=Search, ToRead=['eid','nom','prenom'])
    if query: return False
    personneLDAP = searchLDAP(searchFilterList = searchFilterList) ## Sort une liste de dictionnaires
    Person = {}
    if len(personneLDAP) == 1:
        Person = personneLDAP[0]
        for E in Person.keys(): Person[E] = Person[E][0].decode()
        if not Data['txt_eid'] and Data['txt_nom'].upper() != Person['sn'].upper():
            return 'erreur'
    else:
        return 'erreur : ' + str(searchFilterList) + ' : ' + str(len(personneLDAP)) + ' found'
    return addPersonInDB(S, Data, Person)



@loginRequired
def page(S = None):
    '''Fonction permettant l'ajout de personne.
    Si l'eid est encodé, recherche sur l'eid, sinon sur le nom prénom.
    Si il y a des informations dans le ldap sur la personne, elles sont ajoutées.
    Si on a l'eid, recherche d'informations dans Noé.
    '''
    doc, tag, text = Doc().tagtext()
    Data = readForm()
    if S:
        with tag('div',klass='wrapper'):
            doc, tag, text = menu.sidebar(doc, tag, text)
            with tag('div', id='content'):
                with tag('div', klass='container-fluid'):
                    with tag('h2'):
                        text('Ajout d\'une personne')
                    with tag('div', klass='row justify-content-center modal-body'):
                        if 'button' in Data and ((Data['txt_nom'] and Data['txt_prenom']) or Data['txt_eid']):
                            Ret = checkBD(S, Data)
                            with tag ('div', klass='row justify-content-center modal-body col-12'):
                                if isinstance(Ret, bool):
                                    with tag('div', klass='bg-danger text-white text-center'):
                                        text('La personne est déjà présente dans la base de données')
                                        doc.asis('br')
                                        text('Lien vers la fiche de la personne')
                                elif 'erreur' in Ret:
                                    with tag('div', klass='bg-danger text-white text-center'):
                                        text('L\'eid ne correspondat pas au nom indiqué. Veuillez n\'indiquez que l\'eid ou le nom et le prénom')
                                        doc.stag('br')
                                        text(Ret)
                                else: 
                                    with tag('div', klass='bg-success text-white text-center'):
                                        text('Voici les informations engistrées')
                                        doc.asis('<br>')
                                        text('Lien vers la fiche de la personne')
                            with tag ('div', klass='row justify-content-center modal-body col-12'):
                                if Data['txt_eid']:
                                    Records = db.readRecords(S.Get('eID'), parametres.Database, 'Personne', [('eid', '=', Data['txt_eid'])])
                                elif (Data['txt_nom'] and Data['txt_prenom']):
                                    Records = db.readRecords(S.Get('eID'), parametres.Database, 'Personne', [('nom', '=', Data['txt_nom']), ('prenom', '=', Data['txt_prenom'])])
                                if isinstance(Records,list) and len(Records) == 1:
                                    doc.asis(htmlObject(Records[0]))
                        else:
                            with tag('form', action='ajouterPersonne.py', method="post", name="formSaisie", enctype="multipart/form-data"):
                                with tag('div',klass='form-group'):
                                    doc.input(type="text", id="txt_eid", klass="form-control input-lg", name="txt_eid", maxlength="80", placeholder="Eid")
                                with tag('div',klass='form-group text-center'):
                                    text ('---- OU ----') 
                                with tag('div',klass='form-group'):
                                    doc.input(type="text", id="txt_nom", klass="form-control input-lg", name="txt_nom", maxlength="80", placeholder="Nom")
                                with tag('div',klass='form-group'):
                                    doc.input(type="text", id="txt_prenom", klass="form-control input-lg", name="txt_prenom", maxlength="80", placeholder="Prénom")
                                with tag('div',klass='form-group'):
                                    doc.stag('input', type="submit", id='button', name='button', value="Envoyer", klass='btn btn-primary btn-lg btn-block') 
        webPage(Page = doc, Session = S)
    else:
        webPage(doc)



if __name__ == '__main__':
    page()
