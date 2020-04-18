#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on 2020-01-10 Last Update 2020-02-04
@author : Jacques Gérard - UNamur (www.unamur.be)
@author : Fabrice Orbant - UNamur (www.unamur.be)
"""
import os
from SHI.session import loginRequired, session
from SHI.web import webPage, goTo, readForm
from SHI.local_redis import redisDelete
import SHI.local_db as db
from yattag import Doc
import parametres


@loginRequired
def logout(S = None):
    db.logAction(S.Get('eid'), parametres.Database, 'Connexion cloturée : {0}'.format(S.Get('eID')))
    redisDelete(os.environ["REMOTE_ADDR"])
    S.Kill()
    goTo('index.py')


if __name__ == '__main__':
    logout()
