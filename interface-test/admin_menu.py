

from SHI.web import webPage
from yattag import Doc


def sidebar(doc, tag, text):

    with tag('div', klass="dropdown"):
        """Bouton menu"""
        with tag('button', klass="dropbtn"):
            text('Menu')
        """Menu descendant"""
        with tag('div', klass="dropdown-content"):

            with tag('a', href="index.py"):
                text('Tableau de bord')

            with tag('a', href="admin_prendre_place.py"):
                text('Prendre la place')

            with tag('a', href="admin_association.py"):
                text('Association')

    return doc, tag, text


if __name__ == '__main__':
    sidebar()

    # with tag('div', klass="left-sidebar-pro"):
    # with tag('nav', id="sidebar"):
    # with tag('div', klass="sidebar-header"):
    # with tag('a', href="index.py"):
    # doc.stag('img', klass="main-logo", src="imgahes/unamur_logo.png", alt="")
    # with tag('div', klass="left-custom-menu-adp-wrap comment-scrollbar"):
    # with tag('nav', klass="sidebar-nav left-sidebar-menu-pro"):
    # with tag('ul', klass="metismenu", id="menu1"):
    # with tag('li', klass="active"):
    # with tag('a', href="index.py"):
    # with tag('i', klass="icon nalika-home icon-wrap"):
    # with tag('span', klass="mini-click-non"): text('Tableau de bord')
    # with tag('li'):
    # with tag('a', ('aria-expanded', "false"), klass="has-arrow", href="sujets.py"):
    # with tag('i', klass="icon nalika-diamond icon-wrap"):
    # with tag('span', klass="mini-click-non"): text('Sujets')
    # with tag('ul', ('aria-expanded', "false"), klass="submenu-angle"):
    # with tag('li'):
    # with tag('a', title="Actifs", href="sujetsActifs.py"):
    # with tag('span', klass="mini-sub-pro"): text('Actifs')
    # with tag('li'):
    # with tag('a', title="Actifs", href="sujetsAnciens.py"):
    # with tag('span', klass="mini-sub-pro"): text('Anciens')
    # with tag('li'):
    # with tag('a', title="Ajouter nouveau", href="sujetsNouveaux.py"):
    # with tag('span', klass="mini-sub-pro"): text('Ajouter nouveau')
    # with tag('li'):
    # with tag('a', ('aria-expanded', "false"), href="statistiques.py"):
    # with tag('i', klass="icon nalika-pie-chart icon-wrap"):
    # with tag('span', klass="mini-click-non"): text('Statistiques')
    # with tag('li'):
    # with tag('a', ('aria-expanded', "false"), href="sujets.py", klass="has-arrow"):
    # with tag('i', klass="icon nalika-user nalika-user-rounded header-riht-inf"): pass
    # with tag('span' , klass="mini-click-non"): text('NOM DE LA PERS')
    # with tag('ul',  ('aria-expanded', "false"), klass="submenu-angle"):
    # with tag('li'):
    # with tag('a', title="Deconnexion", href="sujetsActifs.py"):
    # with tag('span', klass="mini-sub-pro"): text('Déconnexion')
    # """Bouton pour cacher le menu"""
    # with tag('div', klass="all-content-wrapper"):
    # with tag('div', klass="header-advance-area"):
    # with tag('div', klass="header-top-area"):
    # with tag('div', klass="container-fluid"):
    # with tag('div', klass="row"):
    # with tag('div', klass="col-lg-12 col-md-12 col-sm-12 col-xs-12"):
    # with tag('div', klass="header-top-wraper"):
    # with tag('div', klass="row"):
    # with tag('div', klass="col-lg-1 col-md-0 col-sm-1 col-xs-12"):
    # with tag('div', klass='menu-switcher-pro'):  """"""
    # with tag('button', type="button", id="sidebarCollapse", klass="btn bar-button-pro header-drl-controller-btn btn-info navbar-btn"):
    # with tag('i', klass="icon nalika-menu-task"):pass
# <li>
    # <a class="has-arrow" href="sujets.py" aria-expanded="false"><i class="icon nalika-user nalika-user-rounded header-riht-inf"></i> <span class="mini-click-non">NOM DE LA PERS</span></a>
    # <ul class="submenu-angle" aria-expanded="false">
    # <li><a title="Deconnexion" href="sujetsActifs.py"><span class="mini-sub-pro">DÃ©connexion</span></a></li>
    # </ul>
    # </li>
    # """Menu Mobile OK - il manque le CSS"""
    # with tag('div', klass='mobile-menu-area'):
    # with tag('div', klass='container mean-area'):
    # with tag('div',klass='mean-bar'):
    # with tag('a', href='#nav', klass='meanmenu-reveal'):pass
    # with tag('nav', klass='mean-nav'):
    # with tag('ul', klass='mobile-menu-nav'):pass
    # with tag('div', klass='row'):
    # with tag('div', klass='col-lg-12 col-md-12 col-sm-12 col-xs-12'):
    # with tag('div', klass='mobile-menu'):
    # with tag('nav', id='dropdown', klass='mean-nav'):
    # with tag('ul', klass='mobile-menu-nav'):
    # with tag('li'):
    # with tag('a', href="index.py"):
    # text('Tableau de bord')
    # with tag('li'):
    # with tag('a', title="Sujets", href='sujets.py'):
    # text('Sujets')
    # with tag('ul', klass='dropdown-header-top'):
    # with tag('li'):
    # with tag('a', title="Actifs", href='sujetsActifs.py'):
    # text('Sujets Actifs')
    # with tag('li'):
    # with tag('a', title="Anciens", href='sujetsAnciens.py'):
    # text('Sujets Anciens')
    # with tag('li'):
    # with tag('a', title="Ajouter", href='sujetsAjouter.py'):
    # text('Ajouter sujet')
    # with tag('li'):
    # with tag('a', href="statistiques.py"):
    # text('Statistiques')
