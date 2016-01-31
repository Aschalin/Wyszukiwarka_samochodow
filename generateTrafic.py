#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint

import MySQLdb as mdb
import sys

from datetime import datetime, timedelta, date


def commentGenerator():
    i = 1
    while i > 0:
        text = "Automatycznie wygenerowany komentarz numer " + str(i)
        yield text
        i += 1

def dateGenerator(startDate):
    date = startDate
    delta = timedelta(days=1)
    while date < datetime.now().date():
        yield date
        date += delta


def datetimeGenerator(startDate):
    second = 0
    dategen = dateGenerator(startDate)
    while True:
        date = dategen.next()
        for hour in range(0, 24):
            for minute in range(0, 60):
                while second < 60:
                    time = "%02d:%02d:%02d" % (hour, minute, second)
                    #print str(date) + " " + time
                    yield str(date) + " " + time
                    second += randint(0, 6000)
                second -= 60

comment = commentGenerator()
dateTime = datetimeGenerator(date(2015, 1, 1))

def addUser(password, username, time):
    cur.execute("""INSERT INTO `auth_user` (`password`, `username`,`first_name`, `last_name`, `email`, `date_joined`, `is_superuser`, `is_staff`, `is_active`) VALUES
                    ('""" + password + "', '" + username + "', '', '', '', '" + time + """', 0, 0, 1)
                    """)

def addComment(site, text, time, id, rate):
    cur.execute("""INSERT INTO `wyszukiwarka_komentarze` (`site`, `Text`, `Time`, `idUser`, `Rate`) VALUES
                ('""" + str(site) + "', '" + text + "', '" + time + "', '" + str(id) + "', '" + str(rate) + """');
                """)

def generateUser(password, username):
    addUser(password, username, dateTime.next())
    cur.execute("SELECT MAX(id) FROM `auth_user`")
    id = cur.fetchone()[0]
    generateSamochodyComments(id)
    generateNadwoziaComments(id)
    generateParametryComments(id)

def generateSamochodyComments(id):
    cur.execute("SELECT id FROM `wyszukiwarka_samochody`")
    results = cur.fetchall()
    for row in results:
        site = row[0]
        text = comment.next()
        rate = randint(1, 5)
        addComment(site, text, dateTime.next(), id, rate)


def generateNadwoziaComments(id):
    cur.execute("SELECT idSamochod, id FROM `wyszukiwarka_nadwozia`")
    results = cur.fetchall()
    for row in results:
        site = str(row[0]) + "/" + str(row[1])
        text = comment.next()
        rate = randint(1, 5)
        addComment(site, text, dateTime.next(), id, rate)


def generateParametryComments(id):
    cur.execute("SELECT n.idSamochod, n.id, s.idSilnik FROM `wyszukiwarka_silniki_nadwozia` s join `wyszukiwarka_nadwozia` n on s.idNadwozie=n.id ")
    results = cur.fetchall()
    for row in results:
        site = str(row[0]) + "/" + str(row[1]) + "/" + str(row[2])
        text = comment.next()
        rate = randint(1, 5)
        addComment(site, text, dateTime.next(), id, rate)

def generateComment(user, site):
    text = comment.next()
    rate = randint(1, 5)
    addComment(site, text, dateTime.next(), user, rate)


def generateSamochodyList():
    samochody = []
    cur.execute("SELECT id FROM `wyszukiwarka_samochody`")
    results = cur.fetchall()
    for row in results:
        samochody.append(row[0])
    return samochody

def generateNadwoziaList():
    nadwozia = []
    cur.execute("SELECT idSamochod, id FROM `wyszukiwarka_nadwozia`")
    results = cur.fetchall()
    for row in results:
        nadwozia.append(str(row[0]) + "/" + str(row[1]))
    return nadwozia

def generateSilnikiList():
    silniki = []
    cur.execute("SELECT n.idSamochod, n.id, s.idSilnik FROM `wyszukiwarka_silniki_nadwozia` s join `wyszukiwarka_nadwozia` n on s.idNadwozie=n.id ")
    results = cur.fetchall()
    for row in results:
        silniki.append(str(row[0]) + "/" + str(row[1]) + "/" + str(row[2]))
    return silniki

print "Generating Trafic:"
try:
    con = mdb.connect('127.0.0.1', 'root', '', 'wyszukiwarka')

    with con:

        cur = con.cursor()
        cur.execute("SELECT MAX(id) FROM `auth_user`")
        id = cur.fetchone()[0] + 1
        if len(sys.argv)>1:
            num = int(sys.argv[1])
        else:
            num = 20
        end = id + num
        print "\tGenerating users...",
        for i in range(id, end):
            generateUser('password' + str(i), 'user' + str(i));
        print "OK"
        print "\tGenerating Comments...",
        sites = generateSamochodyList() + generateNadwoziaList() + generateSilnikiList()
        for i in range(0, num * len(sites) / 2):
            site = sites[randint(0,len(sites)-1)]
            user = randint(id,end-1)
            generateComment(user, site)
        print "OK"



except mdb.Error, e:
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)

finally:
    if con:
        con.close()