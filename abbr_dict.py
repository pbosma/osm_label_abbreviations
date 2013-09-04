﻿abbreviations = {
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
        {'match':'\s+Court$',	 	 'replace':' Ct',	'concatenated':'no',	'separable':'n/a'},
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
        {'match':'\s+Lane$',	 	 'replace':' Ln',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Laneway$',	 	 'replace':' Lnwy',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Loop$',	 	 'replace':' Lp',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Lower$',	 	 'replace':' Lwr',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Meadow$',	 	 'replace':' Mdw',	'concatenated':'no',	'separable':'n/a' ,	'note':'also includes singular'},
        {'match':'\s+Meadows$',	 	 'replace':' Mdws',	'concatenated':'no',	'separable':'n/a' ,	'note':'also includes singular'},
        {'match':'\s+Military$',	 'replace':' Mil',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Motorway$',	 'replace':' Mwy',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Parkway$',	 	 'replace':' Pwy',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Plaza$',	 	 'replace':' Plz',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Road$',	 	 'replace':' Rd',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Roads$',	 	 'replace':' Rds',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Street$',	 	 'replace':' St',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Terrace$',	 	 'replace':' Ter',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Walk$',	 	 'replace':' Wlk',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Walkway$',	 	 'replace':' Wky',	'concatenated':'no',	'separable':'n/a'},
        {'match':'\s+Yard$',	 	 'replace':' Yd',	'concatenated':'no',	'separable':'n/a'}
    ],
    'french':[
        {'match':'(^|\s+)Allée(\s+|$)',	 'replace':'\\1All.\\2','concatenated':'no',	'separable':'n/a',	'note':'Example: Allée du Clos, Grande Allée and Grande Allée des Charmilles'},
        {'match':'(^|\s+)Avenue(\s+|$)', 'replace':'\\1Av.\\2',	'concatenated':'no',	'separable':'n/a',	'note':'Example: 11e Avenue, Petite Avenue de la Pyramide and Avenue du Nord'},
        {'match':'^Boulevard\s+$',	 'replace':'Bd ',	'concatenated':'no',	'separable':'n/a',	'note':'Example: Boulevard de la Gare'},
        {'match':'(^|\s+)Chemin(\s+|$)', 'replace':'\\1Che.\\2','concatenated':'no',	'separable':'n/a' ,	'note':'Grand-Chemin. Example: Chemin de Beauval, Rue du Chemin Vert and Petit Chemin'},
        {'match':'^Passage\s+$', 	 'replace':'Pass. ',	'concatenated':'no',	'separable':'n/a',	'note':'Example: Passage des Italiens'},
        {'match':'^Place\s+$',	 	 'replace':'PL ',	'concatenated':'no',	'separable':'n/a',	'note':'Example: Place des Fusillés de Châteaubriant'},
        {'match':'(\w+)place$',	 	 'replace':'\\1Pl.',	'concatenated':'yes',	'separable':'n/a' ,	'note':'Grand-place'},
        {'match':'^Saint\s+',	 	 'replace':'St ',	'concatenated':'yes',	'separable':'n/a' ,	'note':'Same as English'},
        {'match':'^Sainte\s+',	 	 'replace':'Ste ',	'concatenated':'yes',	'separable':'n/a'},
        {'match':'(^|\s+)Terrasse(\s+|$)', 'replace':'\\1TSSE\\2',	'concatenated':'no',	'separable':'n/a',	'note':'Example:Allée de la Terrasse and Terrasse Modigliani'},
        {'match':'(^|\s+)Terrasses(\s+|$)', 'replace':'\\1TSSE\\2',	'concatenated':'no',	'separable':'n/a'	'note':'Example:Avenue des Terrasses'},
    ],
    'german':[
	{'match':'\s+Platz$', 		 'replace':' Pl', 	'concatenated':'no', 	'separable':'yes'},
	{'match':'(\w+)platz$', 	 'replace':'\\1pl.', 	'concatenated':'yes', 	'separable':'yes'},
	{'match':'\s+Straße$', 		 'replace':' Str.', 	'concatenated':'no', 	'separable':'yes'},
        {'match':'\s+Strasse$',		 'replace':' Str.', 	'concatenated':'no', 	'separable':'yes'},
        {'match':'(\w+)straße$',	 'replace':'\\1str.', 	'concatenated':'yes', 	'separable':'yes'}, 
	{'match':'(\w+)strasse$',	 'replace':'\\1str.', 	'concatenated':'yes', 	'separable':'yes'}
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
