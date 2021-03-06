
if __name__ == '__main__': from SHI.session import Session
from SHI.local_ldap import check_eID, readLDAP
from SHI.web import webPage, goTo, readForm
import SHI.local_db as db
from yattag import Doc
import parametres



def inputUser():
    """
    Ecran de saisie des coordonnées eID et mot de passe de l'utilisateur
    """
    doc, tag, text = Doc().tagtext()
    with tag('div', klass='container'):
        with tag('div', klass='row'):
            with tag('div', klass='modal-body col-md-4'):
                pass
            with tag('div', klass='modal-body col-md-4'):
                with tag('form', klass='form center-block', action='login.py', method='post'):
                    with tag('div', klass='form-group'):
                        doc.input('eID', type='text', klass="form-control input-lg", placeholder="Eid", id='eID', name='eID' )
                    with tag('div', klass='form-group'):
                        doc.input('password', type='password', klass="form-control input-lg", placeholder="Password", id='password', name='password')
                    with tag('div', klass='form-group'):
                        doc.stag('input', type='submit', id='btn_login', name='btn_login', value='Se connecter', klass='btn btn-primary btn-lg btn-block')
    webPage(doc)



def login():
    """
    Page d'identification.
    """
    FormResult = readForm()
    if 'eID' in FormResult:
        # db.logAction(FormResult['eID'], 'Personnalia', 'Tentative de connexion : {0}'.format(FormResult['eID'])') ## Exemple de log
        if 'password' in FormResult and check_eID(FormResult['eID'], FormResult['password']):
            db.logAction(FormResult['eID'], parametres.Database, 'Connexion réussie : {0}'.format(FormResult['eID']))
            infosUser = readLDAP(FormResult['eID'])
            S = Session(FormResult['eID'])
            if FormResult['eID']: S.Set('eID', FormResult['eID'])
            if 'sn' in infosUser: S.Set('nom', infosUser['sn'])
            if 'givenName' in infosUser: S.Set('prenom', infosUser['givenName'])
            if 'mail' in infosUser: S.Set('mail', infosUser['mail'])
        goTo('index.py')
    else:        
        inputUser()



if __name__ == '__main__':
    login()



