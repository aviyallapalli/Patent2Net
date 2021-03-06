# -*- coding: utf-8 -*-
"""
Created on Tue Avr 1 13:41:21 2014

@author: dreymond
"""
import networkx as nx

#from networkx_functs import *
import pickle
IPCRCodes = {'A':'HUMAN NECESSITIES', 'B':'PERFORMING OPERATIONS; TRANSPORTING', 'C':'CHEMISTRY; METALLURGY',
'D':'TEXTILES; PAPER', 'E':'FIXED CONSTRUCTIONS', 'F':'MECHANICAL ENGINEERING; LIGHTING; HEATING; WEAPONS; BLASTING',
'G':' PHYSICS', 'H':'ELECTRICITY'}
from OPS2NetUtils2 import getStatus2, getClassif,getCitations, getFamilyLenght, ContractList, quote, getPrior, getActiveIndicator, getRepresentative
from OPS2NetUtils2 import  change, symbole, ReturnBoolean, FormateGephi,GenereListeSansDate, GenereReseaux3, FindFather, GenereDateLiens
#from Ops3 import UnNest2List

DureeBrevet = 20
SchemeVersion = '20140101' #for the url to the classification scheme
import os, sys, datetime


ListeBrevet = []
#ouverture fichier de travail
#On récupère la requête et les noms des fichiers de travail
with open("..//Requete.cql", "r") as fic:
    contenu = fic.readlines()
    for lig in contenu:
        #if not lig.startswith('#'):
            if lig.count('request:')>0:
                requete=lig.split(':')[1].strip()
            if lig.count('DataDirectory:')>0:
                ndf = lig.split(':')[1].strip()
            if lig.count('GatherContent')>0:
                Gather = ReturnBoolean(lig.split(':')[1].strip())
            if lig.count('GatherBiblio')>0:
                GatherBiblio = ReturnBoolean(lig.split(':')[1].strip())
            if lig.count('GatherPatent')>0:
                GatherPatent = ReturnBoolean(lig.split(':')[1].strip())
            if lig.count('GatherFamilly')>0:
                GatherFamilly = ReturnBoolean(lig.split(':')[1].strip())
            if lig.count('InventorNetwork')>0:
                P2NInv = ReturnBoolean(lig.split(':')[1].strip())
            if lig.count('ApplicantNetwork')>0:
                AppP2N = ReturnBoolean(lig.split(':')[1].strip())
            if lig.count('ApplicantInventorNetwork')>0:
                P2NAppInv = ReturnBoolean(lig.split(':')[1].strip())
            if lig.count('InventorCrossTechNetwork')>0:
                P2NInvCT = ReturnBoolean(lig.split(':')[1].strip())
            if lig.count('CompleteNetwork')>0:
                P2NComp = ReturnBoolean(lig.split(':')[1].strip())    
            if lig.count('CountryCrossTechNetwork')>0:
                P2NCountryCT = ReturnBoolean(lig.split(':')[1].strip())
            if lig.count('FamiliesNetwork')>0:
                P2NFamilly = ReturnBoolean(lig.split(':')[1].strip())    
            if lig.count('FamiliesHierarchicNetwork')>0:
                P2NHieracFamilly = ReturnBoolean(lig.split(':')[1].strip())    


if P2NHieracFamilly:
    ResultPath = '..//DONNEES//'+ndf+'//PatentBiblios'
    ResultPathGephi = '..//DONNEES//'+ndf+'//GephiFiles'
    
    try:
        os.mkdir(ResultPathGephi)
    except:
        pass
    
    
    
    try:
        fic = open(ResultPath+ '//Families' + ndf, 'r')
        print "loading data file ", ndf+' from ', ResultPath, " directory."
        ListeBrevet = pickle.load(fic)
        fic.close()
        if isinstance(ListeBrevet, dict):
            DataBrevet = dict()
            data = ListeBrevet
            ListeBrevet = data['brevets']      
            if data.has_key('requete'): 
                DataBrevet['requete'] = data["requete"]
        print len(ListeBrevet), " patents loaded from file."
        print "Generating hierarchic and dynamic network."
        ficOk = True
    except:
        print "file ", ResultPath +"/"+ndf,"  missing or file ", ResultPath+ '//' + ndf, ' is corrupted destroy it.'
        ficOk = False
    
    inventeur = dict()
    applicant = dict()
    if ficOk:
        #TableCor = dict()
        dynamic = True # spécifie la date des brevets
        
    #    ListeBrevet = NettoiePays(ListeBrevet)   
    #    ListeBrevet = NettoieProprietes(ListeBrevet, "inventeur")
    #    ListeBrevet = NettoieProprietes(ListeBrevet, "applicant")
        lstTemp = []
        listeDates = []
        for Brev in ListeBrevet:
            listeDates.append(Brev['date'])

            memo = Brev['applicant']
            # remember applicant original writing form to reuse in the url property of the node
            # hope that copied list is in the sameorder than the original... else there might be some mixing data 
            
            if isinstance(Brev['applicant'], list):
                Brev['applicant'] =[FormateGephi(unicode(toto)) for toto in Brev['applicant']]
                for inv in range(len(Brev['applicant'])):
                    applicant[Brev['applicant'][inv]] = FormateGephi(unicode(memo[inv]))
            elif isinstance(Brev['applicant'], unicode):
                Brev['applicant'] = FormateGephi(Brev['applicant'])
                applicant[Brev['applicant']] = FormateGephi(unicode(memo))
            else:
                Brev['applicant'] = u'N/A'
            # remember inventor original writing form to reuse in the url property of the node
            memo = Brev['inventeur']
            if isinstance(Brev['inventeur'], list):
                Brev['inventeur'] =[FormateGephi(unicode(toto)) for toto in Brev['inventeur']]
                for inv in range(len(Brev['inventeur'])):
                    inventeur[Brev['inventeur'][inv]] = FormateGephi(unicode(memo[inv]))
            elif isinstance(Brev['inventeur'], unicode):
                Brev['inventeur'] = FormateGephi(Brev['inventeur'])
                inventeur[Brev['inventeur']] = FormateGephi(unicode(memo))
            else:
                Brev['inventeur'] =u'N/A'
    
    
            lstTemp.append(Brev)
        ListeBrevet = lstTemp
        Norm = dict()
        for Brev in ListeBrevet:
            norm = 0
            for cle in Brev.keys():
                if type(Brev[cle]) == type([]):
                    norm += len(Brev[cle])
                else:
                    norm += 1
            Brev['Norm'] = norm
            Norm[Brev['label']] = norm
            #les deux lignes suivante sont inutiles si l'on commente les bonnes lignes lors de la création des attributs du graphes...
        # c'est dans la todo-list car améliorerait grandement les perf sur des gros réseaux
        Pays, Inventeurs, LabelBrevet, Applicant = set(), set(), set(), set()
        Classification, IPCR1, IPCR3, IPCR4, IPCR7, IPCR11 = [], [], [], [], [], []
        
        Pays = set([(u) for u in GenereListeSansDate(ListeBrevet, 'pays')])
        Inventeurs = set([(u) for u in GenereListeSansDate(ListeBrevet, 'inventeur')])
        LabelBrevet = set([(u) for u in GenereListeSansDate(ListeBrevet, 'label')])
        Applicant = set([(u) for u in GenereListeSansDate(ListeBrevet, 'applicant')])
        
#        Classification = ContractList([(u) for u in GenereListeSansDate(ListeBrevet, 'classification')])
        IPCR1 = ContractList([(u) for u in GenereListeSansDate(ListeBrevet, 'IPCR1')])
        IPCR3 = ContractList([(u) for u in GenereListeSansDate(ListeBrevet, 'IPCR3')])
        IPCR4 = ContractList([(u) for u in GenereListeSansDate(ListeBrevet, 'IPCR4')])
        IPCR7 = ContractList([(u) for u in GenereListeSansDate(ListeBrevet, 'IPCR7')])
        IPCR11 = ContractList([(u) for u in GenereListeSansDate(ListeBrevet, 'IPCR11')])
        #status = ContractList([(u) for u in GenereListeSansDate(ListeBrevet, 'status')])
        listelistes = []
        listelistes.append(Pays)
        listelistes.append(Inventeurs)
        listelistes.append(LabelBrevet)
        listelistes.append(Applicant)
        #listelistes.append(Classification)
        listelistes.append(IPCR1)
        listelistes.append(IPCR3)
        listelistes.append(IPCR4)
        listelistes.append(IPCR7)
        listelistes.append(IPCR11)
        #listelistes.append(status)

        ListeNoeuds =[]
        for liste in listelistes:
            ListeNoeuds += [u for u in liste if u not in ListeNoeuds]
        try:
            for l in range(ListeNoeuds.count('N/A')):
    			ListeNoeuds.remove('N/A')
            for l in range(ListeNoeuds.count('')):
    			ListeNoeuds.remove('')
        except:
            pass
        G = nx.DiGraph() 
        
        appariement = dict() # dictionnaires des appariements selon les propriétés des brevets
        # sera envoyé en paramètres à la fonction GenereReseau3
        # un/comment hereafter for desired network creation
    #    appariement['Nation'] = ['label', 'pays']
    #    appariement['inventeur-label'] = ['inventeur', 'label']
    #    appariement['applicant-label'] = ['applicant', 'label']
    #    appariement['inventeur-inventeur'] = ['inventeur', 'inventeur']
    #    appariement['applicant-applicant'] = ['applicant', 'applicant']
    #    appariement['inventeur-applicant'] = ['inventeur', 'applicant']
    #    appariement['label-classification'] = ['label', 'classification']
    #    appariement[''] = ['','']
    #    appariement[''] = ['','']
        
        #appariement['IPCR-IPCR'] = ['classification', 'classification']
        lstCrit= ['inventeur', 'label', 'applicant', 'pays']
        for i in lstCrit:
            for j in lstCrit:
                appariement[change(i)+'-'+change(j)] = [i,j]
        lstCat = ['IPCR1', 'IPCR3', 'IPCR4', 'IPCR7', 'IPCR11']
        for i in lstCat:
            for j in lstCat:
                if i == j: #only same IPC level
                    appariement[change(i)+'-'+change(j)] = [i,j]
        for i in lstCrit:
            for j in lstCat: #cross technology networks
                appariement[change(i)+'-'+change(j)] = [i,j]
                appariement[change(j)+'-'+change(i)] = [j,i]
                 
    #    appariement['inventor-inventor'] = ['inventeur','inventeur']
    #    appariement['applicant-inventor'] = ['applicant','inventeur']
    #    appariement['applicant-'+change('pays')] = ['applicant','pays']
    #    appariement['applicant-label'] = ['applicant','label']
    #    appariement['label-IPCR1'] = ['label','IPCR1']
    #    appariement['IPCR1-IPCR3'] = ['IPCR1','IPCR3']
    #    appariement['IPCR3-IPCR4'] = ['IPCR3','IPCR4']
    #    appariement['IPCR4-IPCR7'] = ['IPCR4','IPCR7']
    #    
    #    appariement['IPCR7-IPCR11'] = ['IPCR7','IPCR11']
    #    appariement['applicant-IPCR1'] = ['applicant','IPCR1']
    #    appariement['label-status'] = ['label','status']
    #    appariement['applicant-IPCR11'] = ['applicant','IPCR11']
    #    appariement['inventor-IPCR11'] = ['inventor','IPCR11']
    
        
        
        #G= nx.DiGraph()
        for Brev in ListeBrevet:
            if 'date' not in Brev.keys():
                print Brev
                Brev['date'] = datetime.date(datetime.date.today(), 1, 1)
                
        G, reseau, Prop = GenereReseaux3(G, ListeNoeuds, ListeBrevet, appariement, dynamic)
        #
        #no loops (again ?)
        DateNoeud = dict()
        for lien in reseau:
            n1, n2, dat, pipo = lien
            
            if isinstance(n1, list) and isinstance(n2, list):
                for kk in n1:
                    if DateNoeud.has_key(kk) and dat not in DateNoeud[kk]:
                        DateNoeud[kk].append(dat)
                    elif not DateNoeud.has_key(kk):
                        DateNoeud[kk] = [dat]
                for kk in n2:
                    if DateNoeud.has_key(kk) and dat not in DateNoeud[kk]:
                        DateNoeud[kk].append(dat)
                    elif not DateNoeud.has_key(kk):
                        DateNoeud[kk] = [dat]
            
            elif isinstance(n1, list) and not isinstance(n2, list):
                for kk in n1:
                    if DateNoeud.has_key(kk) and dat not in DateNoeud[kk]:
                        DateNoeud[kk].append(dat)
                    elif not DateNoeud.has_key(kk):
                        DateNoeud[kk] = [dat]
                    if DateNoeud.has_key(n2) and dat not in DateNoeud[n2]:
                        DateNoeud[n2].append(dat)
                    elif not DateNoeud.has_key(n2):
                        DateNoeud[n2] = [dat]
            elif not isinstance(n1, list) and isinstance(n2, list):
                for kk in n2:
                    if DateNoeud.has_key(kk) and dat not in DateNoeud[kk]:
                        DateNoeud[kk].append(dat)
                    elif not DateNoeud.has_key(kk):
                        DateNoeud[kk] = [dat]
                    if DateNoeud.has_key(n1) and dat not in DateNoeud[n1]:
                        DateNoeud[n1].append(dat)
                    elif not DateNoeud.has_key(n1):
                        DateNoeud[n1] = [dat]
            else:
                if DateNoeud.has_key(n1) and dat not in DateNoeud[n1]:
                    DateNoeud[n1].append(dat)
                elif not DateNoeud.has_key(n1):
                    DateNoeud[n1] = [dat]
                if DateNoeud.has_key(n2) and dat not in DateNoeud[n2]:
                    DateNoeud[n2].append(dat)
                elif not DateNoeud.has_key(n2):
                    DateNoeud[n2] = [dat]     
    
        #avoid lists in nodes
        reseautemp = []
        cpt =0
        for lien in reseau:
            n1, n2, pipo, pipo2 = lien
            if n1 != n2:
                if isinstance(n1, list) and len(n1) >= 1:
                    if isinstance(n2, list) and len(n2) >= 1:
                        for i in n1:
                            for j in n2:
                                if i !=j :
                                    reseautemp.append((i, j, pipo, pipo2))
                    else:
                        for i in n1:
                            if i != n2:
                                reseautemp.append((i, n2, pipo, pipo2))
    
                elif isinstance(n2, list) and len(n2) >= 1:
                    for j in n2:
                        if j != n1 :
                            reseautemp.append((n1, j, pipo, pipo2))
                else:
                    reseautemp.append((n1,n2, pipo, pipo2))
            else:
                pass
               # cpt += 1
        reseau = reseautemp
        
        attr = dict() # dictionnaire des attributs des liens
        import datetime
        today = datetime.datetime.now().date().isoformat()
        dateMini = today
        dateMax = datetime.datetime(1700, 1, 1).isoformat()
        
        
        liendureseau = [(u, v) for u,v,b ,z in reseau]
        LinkedNodes = []
        for k in liendureseau:
            LinkedNodes.append(k[0])
            LinkedNodes.append(k[1])
            
        for noeud in ListeNoeuds:
        
            if noeud is not None and noeud !='':
                if noeud in Pays:
                    attr['label'] = 'pays'
                    attr['url'] = ''
        #            elif noeud in Classification:
        #                attr['label'] = 'IPCR'
        #                if noeud.count('/') > 0:
        #                    ind = noeud[4:].index('/')
        #                    mask = 4 - ind
        #                    mask2 = len(noeud[5+ind:len(noeud)-2])
        #                
        #                    attr['url'] = "http://web2.wipo.int/ipcpub#lang=fr&menulang=FR&refresh=symbol&notion=scheme&version=20140101&symbol="+noeud[0:4]+str(0)*mask+noeud[4:4+ind]+noeud[5+ind:len(noeud)-2]+'000' + (3-mask2)*str('0')
        #                else:
        #                    attr['url'] = "http://web2.wipo.int/ipcpub#lang=fr&menulang=FR&refresh=symbol&notion=scheme&version=20140101&symbol="+noeud[0:4]
                elif noeud in Inventeurs:
                    
                    attr['label'] = 'Inventeur'
                    attr['url'] ='http://worldwide.espacenet.com/searchResults?compact=false&ST=advanced&IN='+ quote('"'+ inventeur[noeud]+'"')+'&locale=en_EP&DB=EPODOC'
                    #attr['url'] = 'http://patentscope.wipo.int/search/en/result.jsf?currentNavigationRow=2&prevCurrentNavigationRow=1&query=IN:'+quote(noeud)+'&office=&sortOption=Pub%20Date%20Desc&prevFilter=&maxRec=38&viewOption=All'
                elif noeud in LabelBrevet:
                    attr['label'] = 'Brevet'
                    tempor = getStatus2(noeud, ListeBrevet)
                    if isinstance(tempor, list):
                        if isinstance(tempor[0], list):
                            attr['status'] = tempor[0][0] # no way for managing multiple status :(
                        else:
                            attr['status'] = tempor[0]
                    else:
                        attr['status'] = tempor
                    
                    attr['Class'] = getClassif(noeud, ListeBrevet)
                    attr['pid'] = getPrior(noeud, ListeBrevet)
                    attr['citations'] = getCitations(noeud, ListeBrevet)
                    attr['FamilyLenght'] = getFamilyLenght(noeud, ListeBrevet)
                    attr['Active'] = getActiveIndicator(noeud, ListeBrevet)
                    attr['Representative'] = getRepresentative(noeud, ListeBrevet)
                    tempotemp = "http://worldwide.espacenet.com/searchResults?compact=false&ST=singleline&query="+noeud+"&locale=en_EP&DB=EPODOC"
                    attr['url'] = tempotemp
                    if attr['Class'] is not None:
                        attr['ReductedClass'] = getClassif(noeud, ListeBrevet)[0:4]
                        
                    else:
                        attr['ReductedClass'] = ""
                elif noeud in Applicant:
                    attr['label'] = 'Applicant'
                    attr['url'] ='http://worldwide.espacenet.com/searchResults?compact=false&ST=advanced&locale=en_EP&DB=EPODOC&PA='+quote('"'+applicant[noeud]+'"')
                    #attr['url'] = 'http://patentscope.wipo.int/search/en/result.jsf?currentNavigationRow=2&prevCurrentNavigationRow=1&query=PA:'+quote(noeud)+'&office=&sortOption=Pub%20Date%20Desc&prevFilter=&maxRec=123897&viewOption=All'
                elif noeud in IPCR1:
                    if noeud in IPCRCodes.keys():
                        attr['label'] = 'IPCR1'
                        attr['name'] = IPCRCodes[noeud]
                        attr['url'] = 'http://web2.wipo.int/ipcpub#lang=enfr&menulang=FR&refresh=page&notion=scheme&version='+SchemeVersion+'&symbol=' +noeud
                    else:
                        pass #node is may be a status node
                elif noeud in IPCR7:
                    attr['label'] = 'IPCR7'
                    attr['url'] =  'http://web2.wipo.int/ipcpub#lang=enfr&menulang=FR&refresh=page&notion=scheme&version='+SchemeVersion+'&symbol='+ symbole(noeud)
                    try:                
                        attr['pid'] = ListeNoeuds.index(FindFather(noeud, IPCR4))
                    except:
                        pass
                elif noeud in IPCR3:
                    attr['label'] = 'IPCR3'
                    attr['url'] = 'http://web2.wipo.int/ipcpub#lang=enfr&menulang=FR&refresh=page&notion=scheme&version='+SchemeVersion+'&symbol=' +noeud
                    try:
                        attr['pid'] = ListeNoeuds.index(FindFather(noeud, IPCR1))
                    except:
                        pass
                elif noeud in IPCR4:
                    attr['label'] = 'IPCR4'
                    attr['url'] = 'http://web2.wipo.int/ipcpub#lang=enfr&menulang=FR&refresh=page&notion=scheme&version='+SchemeVersion+'&symbol=' +noeud
                    try:                
                        attr['pid'] = ListeNoeuds.index(FindFather(noeud, IPCR3))
                    except:
                        pass
                elif noeud in IPCR11 and noeud != '':
                    attr['label'] = 'IPCR11'
                    attr['url'] =  'http://web2.wipo.int/ipcpub#lang=enfr&menulang=FR&refresh=page&notion=scheme&version='+SchemeVersion+'&symbol=' +symbole(noeud)
                    try:
                        attr['pid'] = ListeNoeuds.index(FindFather(noeud, IPCR7))
                    except:
                        pass
    #           
    #                elif noeud in status:
    #                attr['label'] = 'status'
                    
                if noeud in ListeNoeuds:
                    G.add_node(ListeNoeuds.index(noeud))    
                    G.node[ListeNoeuds.index(noeud)]['label'] = noeud                
                    G.node[ListeNoeuds.index(noeud)]['category'] = attr['label']
                    G.node[ListeNoeuds.index(noeud)]['url'] = attr['url']
                    G.node[ListeNoeuds.index(noeud)]['weight'] = LinkedNodes.count(noeud)
                    #G.node[ListeNoeuds.index(noeud)]['start'] = min(DateNoeud[G.node[ListeNoeuds.index(noeud)]['label']]).isoformat()
                    #G.node[ListeNoeuds.index(noeud)]['end'] = max(DateNoeud[G.node[ListeNoeuds.index(noeud)]['label']]).isoformat()
                    if noeud in IPCR11 or noeud in IPCR7 or noeud in IPCR4 or noeud in IPCR3:
                        G.node[ListeNoeuds.index(noeud)]['pid'] = attr['pid']
                    if noeud in LabelBrevet:
                        if attr['pid'] != noeud:
                            G.node[ListeNoeuds.index(noeud)]['pid'] = ListeNoeuds.index(attr['pid'])
                        G.node[ListeNoeuds.index(noeud)]['citations'] = attr['citations']
                        G.node[ListeNoeuds.index(noeud)]['FamilyLenght'] = attr['FamilyLenght']
                        G.node[ListeNoeuds.index(noeud)]['Active'] = attr['Active']
                        G.node[ListeNoeuds.index(noeud)]['Representative'] = attr['Representative']
                        G.node[ListeNoeuds.index(noeud)]['Status'] = attr['status']
        
                    G.node[ListeNoeuds.index(noeud)]['time'] = []
                    dateNodes = [u for u in listeDates if u in set(DateNoeud[noeud])] # filtered againts patent dates
                    for d in dateNodes:
                        lsttemp = (dateNodes.count(d), d, today)                                            
                        if lsttemp not in G.node[ListeNoeuds.index(noeud)]['time']:
                            G.node[ListeNoeuds.index(noeud)]['time'].append(lsttemp)
                        #print dat
                    
                    lst = [u[1] for u in G.node[ListeNoeuds.index(noeud)]['time']]
                    lst.sort()
                    lsttemp = []
                    cpt=0
                    for kk in range(len(lst)):
                        for nb in range(len(G.node[ListeNoeuds.index(noeud)]['time'])):                 
                            if G.node[ListeNoeuds.index(noeud)]['time'][nb][1] == lst[kk]:
                                if G.node[ListeNoeuds.index(noeud)]['time'][nb] not in lsttemp:
                                    if cpt>0:
                                        
                                        lsttemp[cpt-1] = (lsttemp[cpt-1][0], lsttemp[cpt-1][1], G.node[ListeNoeuds.index(noeud)]['time'][nb][1] )#enddate is startdate of current datetime
                                    if len(lsttemp) ==0:
                                        lsttemp.append(G.node[ListeNoeuds.index(noeud)]['time'][nb])
                                    else:
                                        temporair = (G.node[ListeNoeuds.index(noeud)]['time'][nb][0] + lsttemp[len(lsttemp)-1][0],G.node[ListeNoeuds.index(noeud)]['time'][nb][1], G.node[ListeNoeuds.index(noeud)]['time'][nb][2])
                                        lsttemp.append(temporair)
                                    cpt+=1
                    G.node[ListeNoeuds.index(noeud)]['time'] = lsttemp 
                    
                    G.node[ListeNoeuds.index(noeud)]['deb'] = lst[0]#.isoformat()
                    G.node[ListeNoeuds.index(noeud)]['fin']= today
                    if noeud not in IPCR1:
                        pass
                    else:
                        G.node[ListeNoeuds.index(noeud)]['label'] = noeud + '-' +attr['name']
                else:
                    print "on devrait pas être là, never", noeud
                    #G.node[ListeNoeuds.index(noeud)]['end'] = ExtraitMinDate(G.node[ListeNoeuds.index(noeud)]) + DureeBrevet
                    #G.node[ListeNoeuds.index(noeud)]['start'] = 
        G.graph['defaultedgetype'] = "directed"
        G.graph['timeformat'] = "date"
        G.graph['mode'] = "dynamic"
        G.graph['start'] = dateMini
            
        G.graph['end'] = dateMax
    
                
        nx.write_gexf(G, ResultPathGephi+'\\'+ndf + ".gexf", version='1.2draft')
        fic = open(ResultPathGephi+'\\'+ndf+'.gexf', 'r')
        #
        # Next is a hack to correct the bad writing of the header of the gexf file
        # with dynamics properties
        fictemp=open(ResultPathGephi+'\\'+"Good"+ndf+'.gexf', 'w')
        fictemp.write("""<?xml version="1.0" encoding="utf-8"?><gexf version="1.2" xmlns="http://www.gexf.net/1.2draft" xmlns:viz="http://www.gexf.net/1.2draft/viz" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.w3.org/2001/XMLSchema-instance">
      <graph defaultedgetype="directed" mode="dynamic" timeformat="date">
        <attributes class="edge" mode="static">
          <attribute id="6" title="NormedWeight" type="double" />
          <attribute id="8" title="deb" type="string" />
          <attribute id="9" title="fin" type="string" />
          <attribute id="10" title="rel" type="string" />
        </attributes>
    	<attributes class="edge" mode="dynamic">
          <attribute id="7" title="time" type="integer" />
        </attributes>
        <attributes class="node" mode="static">
          <attribute id="0" title="category" type="string" />
          <attribute id="1" title="weight" type="integer" />
          <attribute id="3" title="url" type="string" />
          <attribute id="4" title="deb" type="string" />
          <attribute id="5" title="fin" type="string" />
    	  <attribute id="6" title="FamilyLenght" type="integer" />
          <attribute id="7" title="citations" type="integer" />
          <attribute id="8" title="Representative" type="integer" />
          <attribute id="9" title="Active" type="integer" />
        </attributes>
    	<attributes class="node" mode="dynamic">
    		<attribute id="2" title="time" type="integer" />
    	</attributes>
    #""")
        ecrit  =False
        for lig in fic.readlines():
            if lig.count('<nodes>'):
                ecrit = True
            if ecrit:
                fictemp.write(lig)
        fictemp.close()
        fic.close()
        os.remove(ResultPathGephi+'\\'+ndf+'.gexf')
        try:
            os.remove(ResultPathGephi+'\\'+ndf + "FamiliesHierarc.gexf")
        except:
            pass
        os.rename(ResultPathGephi+'\\'+"Good"+ndf+'.gexf', ResultPathGephi+'\\'+ndf+'FamiliesHierarc.gexf')
        print "Network file writen in ",  ResultPathGephi+' directory.\n See file: '+ndf + "FamiliesHierarc.gexf"