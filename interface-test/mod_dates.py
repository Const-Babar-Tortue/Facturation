
from SHI.web import webPage, readForm, goTo, showField
from vues.personne import PersonPageView
import mod_menu
import parametres
import SHI.local_db as db
from yattag import Doc
if __name__ == '__main__':
    from SHIDev.session import loginRequired

programme = {'Finances': ['inge', 'sciences éco', 'plombier'],
             'Sciences': ['math', 'physique', 'trigo']
             }


@loginRequired
def page(S=None):
    doc, tag, text = Doc().tagtext()
    Data = readForm(Blank=True)
    if S:
        with tag('div', klass='wrapper'):
            doc, tag, text = mod_menu.sidebar(doc, tag, text)
            with tag('div', id='content'):
                M = MissionPageView(S, 'jgerard')
                # if 'modify' in Data: ## Récupération de l'objet à modifier
                # text(str(M.SaveFromForm(Data))) ## Enregistrement des changements opérés dans le formulaire vers la DB
                # doc.stag('br')
                # doc.stag('br')
                # text(str(M.ResultKey))
                # doc.stag('br')
                # doc.stag('br')
                # text(str(M.MissionRecords))
                # doc.stag('br')
                # doc.stag('br')
                # text(str(M._Records))
                # doc.stag('br')
                # doc.stag('br')
                # text(str(Data))
                # doc.stag('br')
                # doc.stag('br')
                # text(str(M._Modified))
                # goTo('index.py')
                # text(str(Data))
                # RefererPage = os.environ["HTTP_REFERER"].split('/')[-1]
                # if RefererPage in ['logout.py', 'login.py']:
                # goTo('index.py')
                # else:
                # goTo(RefererPage)
                # else:
                # with tag('div',klass='wrapper'):
                # with tag('div', id='content'):
                # with tag('div', klass='container-fluid'):
                # with tag('div', klass='row'):
                # with tag('form', action=thisFileName(), method="post", name="formSaisie", enctype="multipart/form-data"):
                # for Id in M.Missions:
                # with tag('h4'): text('Mission ' + str(Id))
                # for Key in M.Fields:
                # if not Key in ['id_per', 'id_ent', 'id_bud', 'id_mis', 'id_fon']:
                # with tag('div',klass='row'): doc, tag, text = showField(doc, tag, text, M.Show(Id, Key))
                # else:
                # doc.input(type="hidden", id='txt_'+Key, name='txt_'+Key, value=M.Get(Id, Key))
                # doc.stag('hr')
                # doc.stag('br')
                # doc.input(type="hidden", id='EID', name='EID', value=S.Get('eid'))
                # doc.stag('input', type="submit", id='modify', name='modify', value="Mettre à jour", style="width:150px")
        with tag('script', src="dist/js/myjs.js"):
            pass
        with tag('stylesheet', src='./dist/css/mycss.css'):
            pass

        webPage(Page=doc, Session=S, CSS='dist/css/mycss.css', JS='myjs.js')
    else:
        webPage(doc)


if __name__ == '__main__':
    page()
