
from SHI.local_ldap import searchLDAP
from SHI.get_noe_identity import getNoeIdentity
import SHI.local_db as db
import parametres

# Fonction prévue uniquement sur base de l'eID existant.


def updatePerson(S, eid=''):

    if not eid:
        return 'No eID passed to function.'
    Records = db.readRecords(S.Get('eID'), parametres.Database, 'Personne', [
                             ('eid', '=', eid)])  # Lire dans la DB locale
    if len(Records) != 1:
        return 'No record found in local DB.'
    # Record = dictionnaire des données récupérées de Personnalia (DB locale)
    Record = Records[0]
    NewRecord = {}
    '''Vérification des données éventuellement manquantes en provenance du LDAP.'''
    pLDAP = searchLDAP(searchFilterList=[
                       ('uid', Record['eid'])])  # Sort une liste de dictionnaires
    if len(pLDAP) == 1:
        Ldap = pLDAP[0]
        for E in Ldap.keys():
            Ldap[E] = Ldap[E][0].decode()
        if 'fundpSOGoMail' in Ldap and Ldap['fundpSOGoMail'] and not Record['mail']:
            NewRecord['mail'] = Ldap['fundpSOGoMail']
        if 'sn' in Ldap and Ldap['sn'] and not Record['nom']:
            NewRecord['nom'] = Ldap['sn']
        if 'givenName' in Ldap and Ldap['givenName'] and not Record['prenom']:
            NewRecord['prenom'] = Ldap['givenName']
    '''Ajout à partir du résultat de la requête Noe.'''
    IsoPersCor = {'eid': 'eid', 'last_name': 'nom', 'first_name': 'prenom', 'mobile': 'gsm', 'gender': 'genre',
                  'email': 'mailprive', 'birthday': 'datenaissance', 'institutional_email': 'mail', 'mobile': 'telprive',
                  'photo': 'photo', 'national_number': 'numeroregistrenational'}
    if not (NoeData:= getNoeIdentity(Record['eid'])):
        # NoeData = dictionnaire des données récupérées de Noe)
        return 'Nothing found in Noe'
    for Key in NoeData:
        if Key == 'country_id':
            if not Record['pays']:
                NewRecord['pays'] = NoeData[Key][1].strip()
        elif Key == 'dpt_id':
            if not Record['departement']:
                NewRecord['departement'] = NoeData[Key][1].strip()
        elif Key == 'address_legal_id':
            try:
                Address = NoeData[Key][1].split(', ')
                if len(Address) == 6:
                    if Address[5].replace('-', '').strip().isdigit():
                        if not Record['adresse']:
                            NewRecord['adresse'] = (
                                Address[0] + ' ' + Address[1]).strip()
                        if not Record['cp']:
                            NewRecord['cp'] = Address[2].strip()
                        if not Record['localite']:
                            NewRecord['localite'] = Address[3].strip()
                        if not Record['pays']:
                            NewRecord['pays'] = Address[4].strip()
                        if not Record['telprive']:
                            NewRecord['telprive'] = Address[5].strip()
                elif len(Address) == 5:
                    if Address[4].replace('-', '').strip().isdigit():
                        if not Record['adresse']:
                            NewRecord['adresse'] = Address[0].strip()
                        if not Record['cp']:
                            NewRecord['cp'] = Address[1].strip()
                        if not Record['localite']:
                            NewRecord['localite'] = Address[2].strip()
                        if not Record['pays']:
                            NewRecord['pays'] = Address[3].strip()
                        if not Record['telprive']:
                            NewRecord['telprive'] = Address[4].strip()
                    else:
                        if not Record['adresse']:
                            NewRecord['adresse'] = (
                                Address[0] + ' ' + Address[1]).strip()
                        if not Record['cp']:
                            NewRecord['cp'] = Address[2].strip()
                        if not Record['localite']:
                            NewRecord['localite'] = Address[3].strip()
                        if not Record['pays']:
                            NewRecord['pays'] = Address[4].strip()
                else:
                    if not Record['adresse']:
                        NewRecord['adresse'] = NoeData[Key][1].strip()
            except:
                pass
        elif Key in IsoPersCor.keys():
            if not Record[IsoPersCor[Key]]:
                NewRecord[IsoPersCor[Key]] = NoeData[Key].strip()
    '''Si pas d'entrée dans le dictionnaire NewRecord, c'est qu'il n'y a pas de donnée supplémentaire dans Noe.'''
    if not NewRecord:
        return 'Nothing to update.'
    '''Si Quelque chose à mettre à jour, lancer la mise à jour dans la DB locale.'''
    try:
        R = db.updateRecords(S.Get('eID'), parametres.Database, 'Personne', [
                             ('eid', '=', eid)], NewRecord)
    except TypeError as Error:
        R = db.fullErrorMessage(Error)
    # Si ok, retourne le dictionnaire, sinon, retourne un string d'erreur.
    return NewRecord if R == None else R
