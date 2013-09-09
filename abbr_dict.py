﻿abbreviations = {
    'catalan':[
        {'match':'^Autopista\s+',	 'replace':'Auto. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Motorway'},
        {'match':'^Autovia\s+',	 	 'replace':'Autov. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Highway'},
        {'match':'^Avinguda\s+',	 'replace':'Av. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Avenue'},
        {'match':'^Baixada\s+',		 'replace':'Bda. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Baixos\s+',		 'replace':'Bxs. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Carrer\s+',		 'replace':'C. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Street'},
        {'match':'^Carreró\s+',		 'replace':'Cró. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Alleyway'},
        {'match':'^Carretera\s+',	 'replace':'Ctra. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Road'},
        {'match':'^Cantonada\s+',	 'replace':'Cant. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Correus\s+',		 'replace':'Corr. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Drecera\s+',		 'replace':'Drec. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Dreta\s+',		 'replace':'Dta. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Escala\s+',		 'replace':'Esc. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Església\s+',	 'replace':'Esgl. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Estació\s+',		 'replace':'Est. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Estacionament\s+',	 'replace':'Estac. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Facultat\s+',	 'replace':'Fac. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Finca\s+',		 'replace':'Fca. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Habitació\s+',	 'replace':'Hab. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Monestir\s+',	 'replace':'Mtir. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Mossèn\s+',		 'replace':'Mn. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Municipal\s+',	 'replace':'Mpal. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Nombre\s+',		 'replace':'Nre. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Número\s+',		 'replace':'Núm. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Sense número\s+',	 'replace':'S/N ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Parada\s+',		 'replace':'Par. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Passadís\s+',	 'replace':'Pdís. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Passatge\s+',	 'replace':'Ptge. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Alleway'},
        {'match':'^Passeig\s+',		 'replace':'Pg. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Parade'},
        {'match':'^Pavelló\s+',		 'replace':'Pav. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'(^|\s+)Plaça\s+',	 'replace':'\\1Pl. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Square'},
        {'match':'^Planta\s+',		 'replace':'Pl. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Població\s+',	 'replace':'Pobl. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Principal\s+',	 'replace':'Pral. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Pujada\s+',		 'replace':'Pda. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Rambla\s+',		 'replace':'Rbla. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Boulevard. Example: RAMBLA, carrer Rambla, Rambla del Sol, la rambla'},
        {'match':'\s+Rambla(\s+|$)',	 'replace':' Rbla.\\1',	'concatenated':'no',	'separable':'n/a' ,	'note':'Boulevard. Example: RAMBLA, carrer Rambla, Rambla del Sol, la rambla'},
        {'match':'^Ronda\s+',		 'replace':'Rda. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Roundabout. Example: Carrer de la Rotonda and Rotonda de Bellesguard'},
        {'match':'\s+Ronda(\s+|$)',	 'replace':' Rda.\\1',	'concatenated':'no',	'separable':'n/a' ,	'note':'Roundabout. Example: Carrer de la Rotonda and Rotonda de Bellesguard'},
        {'match':'^Sagrada\s+',		 'replace':'Sgda. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Sagrat\s+',		 'replace':'Sgt. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'(^|\s+)Sant\s+',	 'replace':'\\1St. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'(^|\s+)Santa\s+',	 'replace':'\\1Sta. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Sobreàtic\s+',	 'replace':'S/àt ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Travessera\s+',	 'replace':'Trav. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Travessia\s+',	 'replace':'Trav. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'},
        {'match':'^Via\s+',	 	 'replace':'V. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'???'}
    ],
    'czech':[
        {'match':'^(.{5,})\s+Ulice(\s+|$)','replace':'\\1 Ul.\\2',	'concatenated':'no',	'separable':'yes',	'note':'Example: Havířská ulice I, IV. ulice'},
        {'match':'^Náměstí\s+(.{4,})$',	 'replace':'Nám. \\1',	'concatenated':'no',	'separable':'yes',	'note':'Example: náměstí Karla IV.'},
        {'match':'^(.{4,})\s+Náměstí$',	 'replace':'\\1 Nám.',	'concatenated':'no',	'separable':'yes',	'note':'Example: Kozinovo náměstí'},
    ],
    'dutch':[
	{'match':'^Burgemeester\s+',	 'replace':'Burg. ',	'concatenated':'no',	'separable':'yes' ,	'note':'"Burg. Patijnlaan" = "Burgemeester Patijnlaan"'},
	{'match':'^Commandant\s+',	 'replace':'Cmdt. ',	'concatenated':'no',	'separable':'yes' ,	'note':'"Cmdt. Weynsstraat" = "Commandant Weynsstraat"'},
	{'match':'^doctor\s+',		 'replace':'dr ',	'concatenated':'no',	'separable':'yes'},
	{'match':'^Dokter\s+',	 	 'replace':'Dr. ',	'concatenated':'no',	'separable':'yes' ,	'note':'"Dokter Crasbornplein" (? Is this correct ?)'},
	{'match':'^Dominee\s+',	 	 'replace':'ds ',	'concatenated':'no',	'separable':'yes' ,	'note':'"Dominee Theodor Fliednerstraat"'},
	{'match':'^Gebroeders\s+',	 'replace':'Gebr. ',	'concatenated':'no',	'separable':'yes' ,	'note':'[brothers] "Gebr. Blommestr." = "Gebroeders Blommestraat"'},
	{'match':'^Generaal\s+',	 'replace':'Gen. ',	'concatenated':'no',	'separable':'yes' ,	'note':'"Gen. Drubbelstr." = "Generaal Drubbelstraat"'},
	{'match':'^(.+\w)gracht$',	 'replace':'\\1gr.',	'concatenated':'yes',	'separable':'yes' ,	'note':'[urban canal] "Herengr." = "Herengracht"'},
        {'match':'^Ingenieur\s+',	 'replace':'Ir. ',	'concatenated':'no',	'separable':'yes' ,	'note':'"Ir. Menneslaan" = "Ingenieur Menneslaan" = "ir Mennesln"'},
        {'match':'^Jonkheer\s+',	 'replace':'Jhr. ',	'concatenated':'no',	'separable':'yes' ,	'note':'"Jhr. Marcus van Gerwenlaan"'},
        {'match':'^Kolonel\s+',		 'replace':'Kol. ',	'concatenated':'no',	'separable':'yes' ,	'note':'"Kol. Silvertopstraat" = "Kolonel Silvertopstraat"'},
        {'match':'^Kanunnik\s+',	 'replace':'Kan. ',	'concatenated':'no',	'separable':'yes' ,	'note':'"Kan. Peetersstr." = "Kanunnik Peetersstraat"'},
        {'match':'^Kardinaal\s+',	 'replace':'Kard. ',	'concatenated':'no',	'separable':'yes' ,	'note':'"Kard. Cardijnln." = "Kardinaal Cardijnlaan"'},
        {'match':'^Korte\s+',		 'replace':'Kte. ',	'concatenated':'no',	'separable':'yes' ,	'note':'"Kte. Winkelstraat" = "Korte Winkelstraat"'},
        {'match':'^Koning\s+',		 'replace':'Kon. ',	'concatenated':'no',	'separable':'yes' ,	'note':'[king] "Kon. Albertlaan" = "Koning Albertlaan"'},
        {'match':'^Koningin\s+',	 'replace':'Kon. ',	'concatenated':'no',	'separable':'yes' ,	'note':'[queen] "Kon. Beatrixplein" = "Koningin Beatrixplein"'},
        {'match':'^Laan\s+',		 'replace':'ln. ',	'concatenated':'yes',	'separable':'yes'},
        {'match':'^Lange\s+',		 'replace':'L. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'"L. Leidsedwarsstraat" = "Lange Leidsedwarsstraat"'},
        {'match':'^Luitenant\s+',	 'replace':'Luit. ',	'concatenated':'no',	'separable':'yes' ,	'note':'"Luit. Lippenslaan" = "Luitenant Lippenslaan"'},
        {'match':'^(.+\w)markt$',	 'replace':'\\1mkt.',	'concatenated':'yes',	'separable':'yes' ,	'note':'"Vrijdagmkt." = "Vrijdagmarkt"'},
        {'match':'^Meester\s+',		 'replace':'Mr. ',	'concatenated':'no',	'separable':'yes' ,	'note':'"Mr. Richard Goossensstr." = "Meester Richard Goossensstraat"'},
        {'match':'^Mevrouw\s+',		 'replace':'Mevr. ',	'concatenated':'no',	'separable':'yes' ,	'note':'"Mevr. Courtmansstr." = "Mevrouw Courtmansstraat"'},
        {'match':'^Monseigneur\s+',	 'replace':'Mgr ',	'concatenated':'no',	'separable':'yes' ,	'note':'"Mgr. Nolensplein"'},
        {'match':'^Onze\-Lieve\-Vrouw(e)*\-',	 'replace':'O.L.V.-',	'concatenated':'yes',	'separable':'yes' ,	'note':'"O.L.V.-Waver" = "Onze-Lieve-Vrouw-Waver"'},
        {'match':'^Pastoor\s+',		 'replace':'Past. ',	'concatenated':'no',	'separable':'yes' ,	'note':'"Past. Wouterstr." = "Pastoor Wouterstraat"'},
        {'match':'^(.+\w)plein$',	 'replace':'\\1pln.',	'concatenated':'yes',	'separable':'yes'},
        {'match':'^President\s+',	 'replace':'Pres. ',	'concatenated':'yes',	'separable':'yes' ,	'note':'Pres. Kennedylaan'},
        {'match':'^Prins\s+',		 'replace':'Pr. ',	'concatenated':'no',	'separable':'yes' ,	'note':'[prince] "Prins Bernhardstraat"'},
        {'match':'^Prinses\s+',		 'replace':'Pr. ',	'concatenated':'no',	'separable':'yes' ,	'note':'[princess] "Prinses Beatrixlaan"'},
        {'match':'^Professor\s+',	 'replace':'Prof. ',	'concatenated':'no',	'separable':'yes' ,	'note':'"Prof. Willemsstraat"'},
        {'match':'^(.+\w)straat$',	 'replace':'\\1str.',	'concatenated':'yes',	'separable':'yes'},
        {'match':'^(.+\w)steenweg$',	 'replace':'\\1stwg.',	'concatenated':'yes',	'separable':'yes' ,	'note':'"Grotestwg." = "Grotesteenweg"'},
	{'match':'^Sint\-\s+',		 'replace':'St. ',	'concatenated':'yes',	'separable':'yes' ,	'note':'"St. Paulusstr." = "St.-Paulusstr." = "Sint-Paulusstraat"'},
	{'match':'^Van\s+',     	 'replace':'V. ',       'concatenated':'no',    'separable':'yes' ,     'note':'"V. Gentstraat" = "Van Gentstraat"'},
	{'match':'^(.+\w) van (.+)$',	 'replace':'\\1 v \\2',	'concatenated':'no',	'separable':'yes' ,	'note':'"Jan v Gentstraat" = "Jan van Gentstraat"'},
	{'match':'^Van De\s+',		 'replace':'V. D. ',	'concatenated':'no',	'separable':'yes' ,	'note':'"V. D. Sweepstraat" = "Van De Sweepstraat" ="vd Sweepstr."'},
	{'match':'^(.+\w)vliet\s+',	 'replace':'\\1vlt.',	'concatenated':'yes',	'separable':'yes' ,	'note':'"St.-Jansvlt." = "Sint-Jansvliet"'}
    ],
    'english':[
        {'match':'\s+Alley$',	 	 'replace':' Aly',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Alleyway$',	 'replace':' Alwy',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Apartments$',	 'replace':' Apts',	'concatenated':'no',	'separable':'n/a' ,	'note':'US'},
        {'match':'\s+Approach$',	 'replace':' Apch',	'concatenated':'no',	'separable':'n/a'},
        {'match':'(^|\s+)Avenue$',	 'replace':'\\1Ave',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Bend$',	 	 'replace':' Bnd',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Block$',	 	 'replace':' Blk',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Boardwalk$',	 'replace':' Bwlk',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Boulevard$',	 'replace':' Blvd',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Buildings$',	 'replace':' Bldgs',	'concatenated':'no',	'separable':'n/a' ,	'note':'also includes singular'},
        {'match':'\s+Causeway$',	 'replace':' Cway',	'concatenated':'no',	'separable':'n/a' ,	'note':'includes C\'way'},
        {'match':'\s+Center$',	 	 'replace':' Ctr',	'concatenated':'no',	'separable':'n/a' ,	'note':'USA'},
        {'match':'\s+Centre$',	 	 'replace':' Ctr',	'concatenated':'no',	'separable':'n/a' ,	'note':'UK, Australia'},
        {'match':'\s+Close$',	 	 'replace':' Cl',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^(.{2,})\s+Court$',	 'replace':'\\1 Ct',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Crossroad$',	 'replace':' Crd',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Crossway$',	 'replace':' Cowy',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Drive$',	 	 'replace':' Dr',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Driveway$',	 'replace':' Drwy',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Estate$',	 	 'replace':' Est',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Expressway$',	 'replace':' Expy',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Fairway$',	 	 'replace':' Fy',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Garden$',	 	 'replace':' Gdn',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Gardens$',	 	 'replace':' Gdn',	'concatenated':'no',	'separable':'n/a' ,	'note':'also includes singular'},
        {'match':'\s+Ground$',	 	 'replace':' Grnd',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Heights$',	 	 'replace':' Hgts',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Highroad$',	 'replace':' Hrd',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Highway$',	 	 'replace':' Hwy',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Junction$',	 'replace':' Jctn',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^(.{2,})\s+Lane$', 	 'replace':'\\1 Ln',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Laneway$',	 	 'replace':' Lnwy',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Loop$',	 	 'replace':' Lp',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Lower$',	 	 'replace':' Lwr',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Meadow$',	 	 'replace':' Mdw',	'concatenated':'no',	'separable':'n/a' ,	'note':'also includes singular'},
        {'match':'\s+Meadows$',	 	 'replace':' Mdws',	'concatenated':'no',	'separable':'n/a' ,	'note':'also includes singular'},
        {'match':'\s+Military$',	 'replace':' Mil',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Motorway$',	 'replace':' Mwy',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^(.{2,})\s+Parkway$',	 'replace':'\\1 Pwy',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Plaza$',	 	 'replace':' Plz',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^(.{2,})\s+Road$',	 'replace':'\\1 Rd',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^(.{2,})\s+Roads$',	 'replace':'\\1 Rds',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^(.{2,})\s+Street$',	 'replace':'\\1 St',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Terrace$',	 	 'replace':' Ter',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Walk$',	 	 'replace':' Wlk',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Walkway$',	 	 'replace':' Wky',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Yard$',	 	 'replace':' Yd',	'concatenated':'no',	'separable':'n/a'}
        {'match':'^North\s+(.{5,})$',	 'replace':'N \\1',	'concatenated':'no',	'separable':'n/a',	'note':'Example: west 1st st, east 75th st, north st, north 37th ave'},
        {'match':'^Northeast\s+(.{5,})$','replace':'NE \\1',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^Northwest\s+(.{5,})$','replace':'NW \\1',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^East\s+(.{5,})$',	 'replace':'E \\1',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^South\s+(.{5,})$',	 'replace':'S \\1',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^Southeast\s+(.{5,})$','replace':'SE \\1',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^Southwest\s+(.{5,})$','replace':'SW \\1',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^West\s+(.{5,})$',	 'replace':'W \\1',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^(.{5,})\s+North$',	 'replace':'\\1 N',	'concatenated':'no',	'separable':'n/a',	'note':'Example: 7th Street S, Kilmer Road N'},
        {'match':'^(.{5,})\s+Northeast$','replace':'\\1 NE',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^(.{5,})\s+Northwest$','replace':'\\1 NW',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^(.{5,})\s+East$',	 'replace':'\\1 E',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^(.{5,})\s+South$',	 'replace':'\\1 S',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^(.{5,})\s+Southeast$','replace':'\\1 SE',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^(.{5,})\s+Southwest$','replace':'\\1 SW',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^(.{5,})\s+West$',	 'replace':'\\1 W',	'concatenated':'no',	'separable':'n/a'},
    ],
    'french':[
        {'match':'(^|\s+)Allée(\s+|$)',	 'replace':'\\1All.\\2','concatenated':'no',	'separable':'n/a',	'note':'Example: Allée du Clos, Grande Allée and Grande Allée des Charmilles'},
        {'match':'(^|\s+)Avenue(\s+|$)', 'replace':'\\1Av.\\2',	'concatenated':'no',	'separable':'n/a',	'note':'Example: 11e Avenue, Petite Avenue de la Pyramide and Avenue du Nord'},
        {'match':'^Boulevard\s+',	 'replace':'Bd ',	'concatenated':'no',	'separable':'n/a',	'note':'Example: Boulevard de la Gare'},
        {'match':'(^|\s+)Chemin(\s+|$)', 'replace':'\\1Che.\\2','concatenated':'no',	'separable':'n/a' ,	'note':'Grand-Chemin. Example: Chemin de Beauval, Rue du Chemin Vert and Petit Chemin'},
        {'match':'^Passage\s+', 	 'replace':'Pass. ',	'concatenated':'no',	'separable':'n/a',	'note':'Example: Passage des Italiens'},
        {'match':'^Place\s+',	 	 'replace':'PL ',	'concatenated':'no',	'separable':'n/a',	'note':'Example: Place des Fusillés de Châteaubriant'},
        {'match':'(\w+)place$',	 	 'replace':'\\1Pl.',	'concatenated':'yes',	'separable':'n/a' ,	'note':'Grand-place'},
        {'match':'^Rue\s+',		 'replace':'R ',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^Saint\s+',	 	 'replace':'St ',	'concatenated':'yes',	'separable':'n/a' ,	'note':'Same as English'},
        {'match':'^Sainte\s+',	 	 'replace':'Ste ',	'concatenated':'yes',	'separable':'n/a'},
        {'match':'(^|\s+)Terrasse(\s+|$)', 'replace':'\\1TSSE\\2',	'concatenated':'no',	'separable':'n/a',	'note':'Example:Allée de la Terrasse and Terrasse Modigliani'},
        {'match':'(^|\s+)Terrasses(\s+|$)', 'replace':'\\1TSSE\\2',	'concatenated':'no',	'separable':'n/a',	'note':'Example:Avenue des Terrasses'},
    ],
    'german':[
	{'match':'^(.{5,})allee$', 	 'replace':'\\1Al.', 	'concatenated':'no', 	'separable':'yes',	'note':'Added for Austria. Example: lindenallee, lichte allee'},
	{'match':'^(.{5,})gasse$', 	 'replace':'\\1G', 	'concatenated':'no', 	'separable':'yes',	'note':'Added for Austria. Example: burggasse, karl-lowe-Gasse'},
	{'match':'\s+Platz$', 		 'replace':' Pl', 	'concatenated':'no', 	'separable':'yes'},
	{'match':'(\w+)platz$', 	 'replace':'\\1pl.', 	'concatenated':'yes', 	'separable':'yes'},
	{'match':'\s+Straße$', 		 'replace':' Str.', 	'concatenated':'no', 	'separable':'yes'},
        {'match':'\s+Strasse$',		 'replace':' Str.', 	'concatenated':'no', 	'separable':'yes'},
        {'match':'(\w+)straße$',	 'replace':'\\1str.', 	'concatenated':'yes', 	'separable':'yes'}, 
	{'match':'(\w+)strasse$',	 'replace':'\\1str.', 	'concatenated':'yes', 	'separable':'yes'}
    ],
    'italian':[
        {'match':'^Campo\s+',		 'replace':'C.po ',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^Corso\s+',		 'replace':'C.so ',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^Corte\s+',		 'replace':'C.te ',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^Fondamenta\s+',	 'replace':'F.ta ',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^Largo\s+',		 'replace':'L.go ',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^Località\s+',	 'replace':'Loc. ',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^Piazza\s+',		 'replace':'P.za ',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^Piazza\s+',		 'replace':'P.zza ',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^Piazzale\s+',	 'replace':'P.le ',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^Piazzetta\s+',	 'replace':'P.ta ',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^Ponte\s+',		 'replace':'P.te ',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^Porta\s+',		 'replace':'P.ta ',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^Salizada\s+',	 'replace':'S.da ',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^Strada Comunale\s+',	 'replace':'SC ',	'concatenated':'yes',	'separable':'yes'},
        {'match':'^Strada Provinciale\s+','replace':'SP ',	'concatenated':'yes',	'separable':'yes'},
        {'match':'^Strada Regionale\s+', 'replace':'SR ',	'concatenated':'yes',	'separable':'yes'},
        {'match':'^Strada Statale\s+',	 'replace':'SS ',	'concatenated':'yes',	'separable':'yes'},
        {'match':'^Via\s+',		 'replace':'V. ',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^Viale\s+',		 'replace':'V.le ',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^Vicolo\s+',		 'replace':'V.lo ',	'concatenated':'no',	'separable':'n/a'},
        {'match':'^Stazione\s+',	 'replace':'Staz. ',	'concatenated':'no',	'separable':'n/a'},
    ],
    'spanish':[
        {'match':'^Angosta\s+',	 	 'replace':'Angta. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Narrow passage'},
        {'match':'^Autopista\s+',	 'replace':'Auto. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Motorway'},
        {'match':'^Calle\s+',		 'replace':'C. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Street'},
        {'match':'^Callejón\s+',	 'replace':'Cjon. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Alleyway'},
        {'match':'^Carrera\s+',	 	 'replace':'Cra. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Street that was before a way'},
        {'match':'^Carrero\s+',	 	 'replace':'Cro. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Track or fingerprint that the people, the animals or the cars leave in the ways.'},
        {'match':'^Carretera\s+',	 'replace':'Ctra. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Road'},
        {'match':'^Carreterín\s+',	 'replace':'Ctrin. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Very very small road'},
        {'match':'^Carretil\s+',	 'replace':'Crtil. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Way that is destined for the traffic of carts or of other carriages.'},
        {'match':'^Carril\s+',		 'replace':'Crril. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Lane'},
        {'match':'^Costera\s+',		 'replace':'Coste. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Area in slope'},
        {'match':'^Cuadra\s+',		 'replace':'Cuadr. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Block'},
        {'match':'^Diagonal\s+',	 'replace':'Diag. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Diagonal street'},
        {'match':'\s+Mirador$',	 	 'replace':' Mrdor.',	'concatenated':'no',	'separable':'n/a' ,	'note':'Viewpoint. Example: Carrer del MIrador del Llac en Carrer del MIrador'},
        {'match':'^Pasadizo\s+',	 'replace':'Pzo. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Passageway Example: Pasadizo St Amelia'},
        {'match':'^Pasaje\s+',	 	 'replace':'Psaje. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Alleway. Example: Pasaje Dopla'},
        {'match':'^Paseo marítimo\s+',	 'replace':'Psmar. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Promenade'},
        {'match':'^Pasillo\s+',		 'replace':'Psllo. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Corridor'},
        {'match':'(^|\s+)Plaza\s+',	 'replace':'\\1Pl. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Square. Example: Plaza Avrillé and Mares de la Plaza de Mayo},
        {'match':'^Plazoleta\s+',	 'replace':'Pzta. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Small square'},
        {'match':'^Plazuela\s+(.{4,})$', 'replace':'Plzla. \\1','concatenated':'no',	'separable':'n/a' ,	'note':'Small square. Example: Plazuela à la gare and Plazuela St'},
        {'match':'\s+Prazuela(\s+|$)',	 'replace':' Przla.\\1','concatenated':'no',	'separable':'n/a' ,	'note':'Small square. Example: Del Prazuela Carmen and gente de la prazuela'},
        {'match':'^Rambla\s+',		 'replace':'Rbla. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Boulevard. Example: RAMBLA, carrer Rambla, Rambla del Sol, la rambla'},
        {'match':'\s+Rambla(\s+|$)',	 'replace':' Rbla.\\1',	'concatenated':'no',	'separable':'n/a' ,	'note':'Boulevard. Example: RAMBLA, carrer Rambla, Rambla del Sol, la rambla'},
        {'match':'^Rotonda\s+',		 'replace':'Rtda. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Roundabout. Example: Carrer de la Rotonda and Rotonda de Bellesguard'},
        {'match':'\s+Rotonda(\s+|$)',	 'replace':' Rtda.\\1',	'concatenated':'no',	'separable':'n/a' ,	'note':'Roundabout. Example: Carrer de la Rotonda and Rotonda de Bellesguard'},
        {'match':'^San\s+',	 	 'replace':'S. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Saint'},
        {'match':'(^|\s+)Santa\s+',	 'replace':'\\1Sta. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Female saint. Example: Santa Marta and Carrer de Santa Eulàlia'},
        {'match':'^Travesía\s+',	 'replace':'Trva. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Side street. Example: Travesía de la Primavera'},
        {'match':'^Viviendas\s+',	 'replace':'Vvdas. ',	'concatenated':'no',	'separable':'n/a' ,	'note':'Block of flats. Example: PROMOTORA de VIVIENDAS and Viviendas en la calle Bravo Murillo'},
        {'match':'\s+Viviendas(\s+|$)',	 'replace':' Vvdas.\\1','concatenated':'no',	'separable':'n/a' ,	'note':'Block of flats. Example: PROMOTORA de VIVIENDAS and Viviendas en la calle Bravo Murillo'},
    ],
    'swedish':[
        {'match':'^(.{5,})väg(en)*$',	 'replace':'\\1v.',	'concatenated':'yes',	'separable':'yes' ,	'note':'"way" Example: Ringvägen, Vågens gata'},
        {'match':'^(.{5,})gata(n)*$',	 'replace':'\\1g.',	'concatenated':'yes',	'separable':'yes' ,	'note':'"street" Example: Brunnsgatan, Hokens gata'},
        {'match':'^(.{4,})gränd(en)*$',	 'replace':'\\1gr.',	'concatenated':'yes',	'separable':'yes' ,	'note':'"ally" Example: Tullgränd, Pers gränd'},
        {'match':'^Gamla\s+(.{5,})$',	 'replace':'G:la\\1',	'concatenated':'yes',	'separable':'yes' ,	'note':'"old" Example: Gamla vägen'},
        {'match':'^(.{4,})stig(en)*$',	 'replace':'\\1st.',	'concatenated':'yes',	'separable':'yes' ,	'note':'"path" Example: Tjäderstigen, Harry Martinsons stig'},
        {'match':'^Sankt\s+(.{4,})$',	 'replace':'S:t \\1',	'concatenated':'yes',	'separable':'yes' ,	'note':'"saint" Example: Sankt Eriksplan'},
        {'match':'^(.{5,})plats(en)*$',	 'replace':'\\1pl',	'concatenated':'yes',	'separable':'yes' ,	'note':'"square" Example: Olof Palmes plats, Medborgarplatsen'},
        {'match':'^Södra\s+(.{4,})$',	 'replace':'S. \\1',	'concatenated':'yes',	'separable':'yes' ,	'note':'"south" Example: Södra Hamnvägen, Södra vägen'},
        {'match':'^Norra\s+(.{4,})$',	 'replace':'N. \\1',	'concatenated':'yes',	'separable':'yes' ,	'note':'"north" Example: Norra Agnegatan'},
        {'match':'^Östra\s+(.{4,})$',	 'replace':'Ö. \\1',	'concatenated':'yes',	'separable':'yes' ,	'note':'"east" Example: Östra Tegelviksslingan'},
        {'match':'^Västra\s+(.{4,})$',	 'replace':'V. \\1',	'concatenated':'yes',	'separable':'yes' ,	'note':'"west" Example: Västra Brobänken'},
    ],
    'turkish':[
        {'match':'\s+Sokak$',    	 'replace':' Sok',  'concatenated':'no',    'separable':'yes'},
        {'match':'\s+Sokağı$',   	 'replace':' Sk',   'concatenated':'no',    'separable':'yes', 		'note':'Example: Susam Sk.'},
        {'match':'\s+Sokağı$',   	 'replace':' Sok',  'concatenated':'no',    'separable':'yes'},
        {'match':'\s+Cadde$',    	 'replace':' Cd',   'concatenated':'no',    'separable':'yes', 		'note':'Mostly with numbers, Example: 3. Cadde'},
        {'match':'\s+Caddesi$',  	 'replace':' Cd',   'concatenated':'no',    'separable':'yes', 		'note':'Example: İnonü Caddesi'},
        {'match':'\s+Bulvar$',   	 'replace':' Bl',   'concatenated':'no',    'separable':'yes'},
        {'match':'\s+Bulvarı$',  	 'replace':' Bl',   'concatenated':'no',    'separable':'yes', 		'note':'Example: Atatürk Bulvarı'},
    ]
};
