# Schematic map geometry and era data.
# Coordinates are hand-placed in a 0..1000 x 0..1200 box (north up) so that every
# stated north/south/east/west relation holds. analyze.py checks this. Nothing here is
# a claim about real-world locations, and the map is not to scale.
# The Old World and Jaredite-origin insets sit at negative x and are not placed
# relative to the main map.

POS = {
 # ---------- land northward ----------
 'land_north': (600, 80), 'many_waters': (545, 175), 'bones_land': (300, 300),
 'ripliancum': (470, 130), 'ogath': (485, 200), 'cumorah': (560, 240), 'ablom': (800, 225),
 'shurr': (650, 150), 'comnor': (690, 132), 'corihor': (290, 185), 'agosh': (700, 365),
 'jar_landing': (255, 115), 'jacobugath': (420, 70),
 'shem': (340, 250), 'jashon': (385, 325), 'shim': (435, 290), 'antum': (420, 300),
 'jordan': (600, 300), 'boaz': (520, 360),
 'moron': (395, 410), 'mulek_landing': (455, 395),
 'desolation': (505, 448), 'teancum_c': (595, 442),
 'neck': (500, 488),
 # ---------- Bountiful band ----------
 'hagoth': (447, 512), 'bountiful': (680, 560),
 # ---------- Zarahemla & the Sidon ----------
 'land_south': (300, 1128),
 'sidon': (515, 700), 'sidon_head': (466, 925),
 'zarahemla': (470, 722), 'sidom': (428, 700), 'minon': (472, 820),
 'gideon': (603, 765), 'amnihu': (582, 680),
 'melek': (360, 772), 'ammonihah': (350, 668), 'noah_l': (420, 640), 'hermounts': (262, 648),
 'manti': (420, 905), 'south_wild': (575, 968),
 'east_wild': (800, 762), 'strip': (500, 946),
 'angola': (420, 615), 'david': (330, 590), 'joshua': (215, 600),
 # ---------- east coast ----------
 'mulek_c': (790, 622), 'gid': (802, 680), 'omner': (815, 738), 'morianton': (790, 800),
 'lehi_c': (842, 822), 'moroni_c': (846, 905), 'nephihah': (760, 895), 'aaron': (680, 885),
 'jershon': (722, 690), 'antionum': (758, 852),
 'east_sea': (935, 760), 'west_sea': (65, 760),
 # ---------- south-west frontier ----------
 'judea': (300, 860), 'zeezrom': (362, 893), 'cumeni': (330, 918), 'antiparah': (228, 900),
 # ---------- land of Nephi ----------
 'nephi': (560, 1052), 'shilom': (645, 1048), 'hill_shilom': (645, 1008), 'shemlon': (715, 1080),
 'mormon': (492, 998), 'jeru_l': (432, 1042), 'helam': (360, 1002), 'valley_alma': (332, 968),
 'amulon': (300, 1045), 'ishmael': (735, 1118), 'middoni': (795, 1040), 'promised': (172, 1060),
 # ---------- Old World inset (x < 0, not placed relative to the map) ----------
 'jeru_ow': (-205, 95), 'lemuel_ow': (-215, 185), 'redsea': (-305, 235), 'shazer': (-185, 285),
 'nahom': (-165, 400), 'bounty_ow': (-70, 470), 'irreantum': (-40, 525),
 # ---------- Jaredite origins inset ----------
 'nimrod': (-275, 640), 'moriancumer': (-120, 655),
}

# How each place is drawn.  city = ball; land = region only (no ball); hill, valley, place = small marker;
# water = sea/lake/river label; feature = strip/neck/wilderness label; macro = land northward/southward label.
MARK = {
 'city': ['zarahemla','nephi','bountiful','desolation','gideon','manti','moroni_c','nephihah','lehi_c','morianton','omner','gid',
          'mulek_c','aaron','ammonihah','noah_l','judea','antiparah','cumeni','zeezrom','jeru_l','jashon','shem','angola','boaz',
          'jordan','teancum_c','jeru_ow','jacobugath'],
 'land': ['melek','jershon','antionum','sidom','minon','shilom','shemlon','helam','amulon','ishmael','middoni','antum','joshua',
          'david','moron','corihor','mormon'],
 'hill': ['amnihu','hill_shilom','shim','cumorah','comnor'],
 'valley': ['valley_alma','nimrod','shurr','lemuel_ow'],
 'place': ['hagoth','mulek_landing','promised','ablom','ogath','agosh','moriancumer','jar_landing','shazer','nahom','bounty_ow'],
 'water': ['sidon','sidon_head','east_sea','west_sea','ripliancum','irreantum','redsea','many_waters'],
 'feature': ['strip','neck','hermounts','east_wild','south_wild','bones_land'],
 'macro': ['land_north','land_south'],
}

# Coastline of the schematic landmass (clockwise from the north-west).
COAST = [(230,70),(420,40),(640,55),(800,90),(845,200),(825,320),(765,400),(625,440),(578,470),(568,506),(605,526),
         (760,532),(845,565),(872,650),(878,780),(882,900),(862,1000),(822,1100),(700,1150),(500,1162),(300,1152),
         (168,1112),(108,1000),(118,880),(138,760),(168,640),(232,560),(362,526),(432,506),(432,470),(382,442),
         (250,412),(180,330),(172,200)]
NECK_Y = 488

# The river Sidon: head in the south at the strip, running north past Zarahemla (west bank) and Gideon (east bank).
# The text never says where it ends, so the last points are drawn fading.
SIDON = [(466,925),(482,860),(500,792),(512,722),(526,652),(545,592),(562,560)]
# The narrow strip of wilderness, sea to sea (Alma 22:27).
STRIP = [(112,958),(240,950),(360,940),(466,935),(580,950),(700,942),(800,930),(878,936)]
# Fortified line across Bountiful (Helaman 4:7), and the Bountiful-Desolation line (Alma 22:32).
LINES = [
 dict(id='line_bd', label='Bountiful–Desolation line (1½ days, Alma 22:32)', pts=[(432,500),(568,500)], refs=['ALMA 22:32']),
 dict(id='line_hel4', label='Fortified line (1 day, Helaman 4:7)', pts=[(380,540),(780,545)], refs=['HELAMAN 4:7']),
]

# Regions drawn as soft blobs. members = node ids or explicit points. link = node whose verses the region opens.
REGIONS = [
 dict(id='r_zar', label='Land of Zarahemla', link='zarahemla', members=['zarahemla','sidom','minon',(440,660),(520,780)], pad=34, lxy=(470,860)),
 dict(id='r_gideon', label='Gideon', link='gideon', members=['gideon','amnihu'], pad=28),
 dict(id='r_melek', label='Melek', link='melek', members=['melek'], pad=34),
 dict(id='r_ammonihah', label='Ammonihah', link='ammonihah', members=['ammonihah'], pad=26),
 dict(id='r_noah', label='Noah', link='noah_l', members=['noah_l'], pad=22),
 dict(id='r_sidom', label='', link='sidom', members=['sidom'], pad=18),
 dict(id='r_manti', label='Manti', link='manti', members=['manti'], pad=28),
 dict(id='r_hermounts', label='Hermounts', link='hermounts', members=['hermounts'], pad=36, wild=True),
 dict(id='r_south_wild', label='South wilderness', link='south_wild', members=['south_wild',(530,960),(640,972)], pad=24, wild=True),
 dict(id='r_east_wild', label='East wilderness', link='east_wild', members=['east_wild','morianton','lehi_c','moroni_c','nephihah',(820,760)], pad=24, wild=True),
 dict(id='r_bountiful', label='Land Bountiful', link='bountiful', members=[(447,512),(560,515),(700,540),(820,575),(260,575),(380,535),(680,575)], pad=16),
 dict(id='r_desolation', label='Land Desolation', link='desolation', members=['desolation','teancum_c',(450,430),(560,428)], pad=18),
 dict(id='r_jershon', label='Jershon', link='jershon', members=['jershon',(690,650),(760,730)], pad=24),
 dict(id='r_antionum', label='Antionum', link='antionum', members=['antionum'], pad=30),
 dict(id='r_sw', label='South-west frontier', link='judea', members=['judea','antiparah','cumeni','zeezrom'], pad=26),
 dict(id='r_nephi_land', label='Land of Nephi (Lamanite kingdom)', link='nephi', members=[(180,1000),(400,985),(600,980),(840,985),(820,1100),(560,1130),(260,1110)], pad=14, lxy=(650,1142)),
 dict(id='r_lehinephi', label='Lehi-Nephi & Shilom', link='nephi', members=['nephi','shilom','hill_shilom'], pad=24),
 dict(id='r_shemlon', label='Shemlon', link='shemlon', members=['shemlon'], pad=22),
 dict(id='r_mormon', label='Mormon', link='mormon', members=['mormon'], pad=20),
 dict(id='r_helam', label='Helam', link='helam', members=['helam'], pad=22),
 dict(id='r_amulon', label='Amulon', link='amulon', members=['amulon'], pad=22),
 dict(id='r_ishmael', label='Ishmael', link='ishmael', members=['ishmael'], pad=28),
 dict(id='r_middoni', label='Middoni', link='middoni', members=['middoni'], pad=24),
 dict(id='r_first', label='First inheritance', link='promised', members=['promised'], pad=30),
 dict(id='r_antum', label='Antum', link='antum', members=['shim','jashon'], pad=26),
 dict(id='r_joshua', label='Joshua', link='joshua', members=['joshua'], pad=24),
 dict(id='r_david', label='David', link='david', members=['david'], pad=22),
 dict(id='r_moron', label='Moron', link='moron', members=['moron'], pad=26),
 dict(id='r_corihor', label='Corihor', link='corihor', members=['corihor'], pad=24),
 dict(id='r_cumorah', label='Land of Cumorah', link='cumorah', members=['cumorah','ogath',(600,265)], pad=24),
]

SIDES = {'nephite':'Nephite', 'lamanite':'Lamanite', 'jaredite':'Jaredite', 'mulekite':'People of Zarahemla',
         'contested':'Changing hands', 'wild':'Wilderness / unsettled', 'lost':'Destroyed or abandoned'}

# Each era: which places appear, who holds what, what happens (with verses), and journeys to draw.
# M_north / M_south tint the two halves of the landmass.
ERAS = [
 dict(id='jared', label='Jaredites', when='Ether: from the tower to Coriantumr',
  show=['nimrod','moriancumer','jar_landing','moron','corihor','shurr','comnor','agosh','ablom','ripliancum','ogath','cumorah',
        'shim','neck','land_north','land_south','many_waters','desolation','east_sea','west_sea'],
  control={'M_north':'jaredite','M_south':'wild','r_moron':'jaredite','r_corihor':'jaredite','r_cumorah':'jaredite'},
  notes=[("Barges from the seashore at Moriancumer: 344 days on the water", ['ETHER 2:13','ETHER 6:11']),
         ("Moron, where the kings dwelt, is near the land the Nephites later called Desolation", ['ETHER 7:6']),
         ("Lib builds a great city by the narrow neck; the land southward is kept as a wilderness for game", ['ETHER 10:20','ETHER 10:21']),
         ("Omer flees past the hill Shim and the later Nephite battlefield, then east to Ablom by the sea", ['ETHER 9:3']),
         ("The last war ends by the waters of Ripliancum and the hill Ramah, the same hill as Cumorah", ['ETHER 15:8','ETHER 15:10','ETHER 15:11'])],
  paths=[dict(nodes=['moron','shim','cumorah','ablom'], label="Omer's flight", refs=['ETHER 9:3']),
         dict(nodes=['ripliancum','ogath','cumorah'], label='Shiz flees south; last battle', refs=['ETHER 15:10','ETHER 15:11'])]),
 dict(id='lehi', label='Lehi & Nephi', when='1–2 Nephi: about 600 years before Christ (1 Nephi 10:4)',
  show=['jeru_ow','lemuel_ow','redsea','shazer','nahom','bounty_ow','irreantum','promised','nephi','mulek_landing','zarahemla',
        'land_north','land_south','east_sea','west_sea','neck','bones_land'],
  control={'r_first':'lamanite','r_lehinephi':'nephite','r_zar':'mulekite'},
  notes=[("Old World route: three days to a valley by a river into the Red Sea, four days south-southeast to Shazer, on to Nahom, then nearly east to Bountiful", ['1 NEPHI 2:6','1 NEPHI 2:8','1 NEPHI 16:13','1 NEPHI 16:34','1 NEPHI 17:1','1 NEPHI 17:5']),
         ("They sail many days to the promised land", ['1 NEPHI 18:23']),
         ("Nephi's party flees many days into the wilderness and names the place Nephi", ['2 NEPHI 5:5','2 NEPHI 5:7','2 NEPHI 5:8']),
         ("The Lamanites keep the land of first inheritance by the west seashore", ['ALMA 22:28']),
         ("The people of Zarahemla land in the north, then come up into the south", ['OMNI 1:15','ALMA 22:30','ALMA 22:31','HELAMAN 6:10'])],
  paths=[dict(nodes=['jeru_ow','lemuel_ow','shazer','nahom','bounty_ow'], label='Old World route', refs=['1 NEPHI 16:13','1 NEPHI 17:1']),
         dict(nodes=['bounty_ow',(-20,690),(70,1010),'promised'], label='Voyage (not to scale)', refs=['1 NEPHI 18:23'], sea=True),
         dict(nodes=['promised','nephi'], label="Nephi's flight", refs=['2 NEPHI 5:7']),
         dict(nodes=['mulek_landing','zarahemla'], label='Mulekites move south', refs=['ALMA 22:31'])]),
 dict(id='mosiah', label='Mosiah & Zeniff', when='Omni–Mosiah',
  show=['nephi','shilom','hill_shilom','shemlon','mormon','helam','valley_alma','amulon','zarahemla','bones_land','many_waters',
        'strip','land_north','land_south','east_sea','west_sea','neck'],
  control={'r_zar':'nephite','r_nephi_land':'lamanite','r_lehinephi':'contested','r_shemlon':'lamanite','r_mormon':'nephite',
           'r_helam':'contested','r_amulon':'lamanite'},
  notes=[("Mosiah leads his people out of Nephi through the wilderness down to Zarahemla; the two peoples unite", ['OMNI 1:12','OMNI 1:13','OMNI 1:19']),
         ("Zeniff goes up to resettle Lehi-Nephi and Shilom, later under Lamanite tribute", ['MOSIAH 9:3','MOSIAH 9:6','MOSIAH 19:15']),
         ("Ammon's party wanders forty days to the hill north of Shilom", ['MOSIAH 7:4','MOSIAH 7:5']),
         ("Limhi's scouts get lost and find a land of bones among many waters", ['MOSIAH 8:8','MOSIAH 21:26']),
         ("Alma flees 8 days to Helam, then 1 + 12 days to Zarahemla", ['MOSIAH 23:3','MOSIAH 24:20','MOSIAH 24:25']),
         ("Limhi's people slip round Shilom and reach Zarahemla after many days", ['MOSIAH 22:11','MOSIAH 22:13'])],
  paths=[dict(nodes=['nephi','zarahemla'], label="Mosiah I's exodus", refs=['OMNI 1:13']),
         dict(nodes=['mormon','helam','valley_alma','zarahemla'], label="Alma's people: 8 + 1 + 12 days", refs=['MOSIAH 23:3','MOSIAH 24:20','MOSIAH 24:25']),
         dict(nodes=['zarahemla','hill_shilom'], label="Ammon's 40 days (lost)", refs=['MOSIAH 7:4']),
         dict(nodes=['nephi','bones_land'], label="Limhi's scouts (lost)", refs=['MOSIAH 8:8'], dashed=True)]),
 dict(id='alma', label='Alma', when='Judges, years 1–18 (Alma 1–45)',
  show=['zarahemla','sidon','sidon_head','gideon','amnihu','minon','hermounts','melek','ammonihah','noah_l','sidom','manti',
        'south_wild','strip','jershon','antionum','bountiful','desolation','east_wild','nephi','ishmael','middoni','jeru_l',
        'mormon','shilom','shemlon','helam','amulon','east_sea','west_sea','land_north','land_south','neck','bones_land'],
  control={'r_zar':'nephite','r_gideon':'nephite','r_melek':'nephite','r_ammonihah':'lost','r_noah':'nephite','r_sidom':'nephite',
           'r_manti':'nephite','r_bountiful':'nephite','r_jershon':'nephite','r_antionum':'contested','r_east_wild':'lamanite',
           'r_south_wild':'lamanite','r_hermounts':'wild','r_nephi_land':'lamanite','r_lehinephi':'lamanite','r_ishmael':'lamanite',
           'r_middoni':'lamanite','r_shemlon':'lamanite','r_mormon':'lamanite','r_helam':'lamanite','r_amulon':'lamanite',
           'r_desolation':'wild','M_north':'wild'},
  lost=['ammonihah'],
  notes=[("Amlicites at the hill Amnihu east of the Sidon; Lamanites in Minon; the enemy flees west and north to Hermounts", ['ALMA 2:15','ALMA 2:24','ALMA 2:37']),
         ("Alma's circuit: Gideon, Zarahemla, Melek, three days north to Ammonihah, then Sidom", ['ALMA 6:7','ALMA 8:3','ALMA 8:6','ALMA 15:1']),
         ("Ammonihah is destroyed; the raiders cross the Sidon beyond Manti", ['ALMA 16:2','ALMA 16:6','ALMA 16:7']),
         ("The sons of Mosiah among the Lamanites: Ishmael, Middoni, Nephi", ['ALMA 17:19','ALMA 20:2','ALMA 22:1']),
         ("The king's proclamation lays out the strip, Bountiful, Desolation and the neck", ['ALMA 22:27','ALMA 22:31','ALMA 22:32']),
         ("The Ammonites are given Jershon; the Zoramites gather in Antionum", ['ALMA 27:22','ALMA 27:26','ALMA 31:3']),
         ("Zerahemnah marches round by the head of the Sidon to Manti", ['ALMA 43:22','ALMA 43:35'])],
  paths=[dict(nodes=['zarahemla','melek','ammonihah','sidom','zarahemla'], label="Alma's mission", refs=['ALMA 8:3','ALMA 8:6','ALMA 15:1','ALMA 15:18']),
         dict(nodes=['nephi','strip','jershon'], label='Ammonites to Jershon', refs=['ALMA 27:14','ALMA 27:26']),
         dict(nodes=['antionum','south_wild','sidon_head','manti'], label="Zerahemnah's march", refs=['ALMA 43:22','ALMA 43:24'])]),
 dict(id='moroni', label='Captain Moroni', when='Judges, years 19–36 (Alma 46–62)',
  show=['zarahemla','sidon','sidon_head','gideon','melek','ammonihah','noah_l','manti','strip','jershon','antionum','bountiful',
        'desolation','neck','east_wild','moroni_c','nephihah','lehi_c','morianton','omner','gid','mulek_c','aaron','judea','antiparah',
        'cumeni','zeezrom','nephi','east_sea','west_sea','land_north','land_south','many_waters'],
  control={'r_zar':'nephite','r_gideon':'nephite','r_melek':'nephite','r_ammonihah':'nephite','r_noah':'nephite','r_manti':'contested',
           'r_bountiful':'nephite','r_desolation':'nephite','r_jershon':'nephite','r_antionum':'lamanite','r_east_wild':'contested',
           'r_sw':'contested','r_nephi_land':'lamanite','r_lehinephi':'lamanite'},
  notes=[("Moroni clears the east wilderness and founds Moroni, Nephihah and Lehi; a fortified line from the west sea by the head of the Sidon", ['ALMA 50:7','ALMA 50:11','ALMA 50:13','ALMA 50:15']),
         ("Morianton's people head north and are stopped at the narrow pass", ['ALMA 50:29','ALMA 50:34']),
         ("Amalickiah takes the coastal cities and is stopped at Bountiful", ['ALMA 51:23','ALMA 51:26','ALMA 51:28','ALMA 51:32']),
         ("In the south-west, Manti, Zeezrom, Cumeni and Antiparah are lost, then retaken by Helaman", ['ALMA 56:14','ALMA 58:28','ALMA 58:31']),
         ("Nephihah: listed as taken in 51:26, yet still Nephite until it falls in Alma 59 (see tension X7)", ['ALMA 51:25','ALMA 51:26','ALMA 59:11']),
         ("Moroni goes from Gideon down to Zarahemla, then to Nephihah, Lehi and the land of Moroni", ['ALMA 62:7','ALMA 62:18','ALMA 62:30','ALMA 62:32'])],
  paths=[dict(nodes=['moroni_c','lehi_c','morianton','omner','gid','mulek_c','bountiful'], label="Amalickiah's sweep", refs=['ALMA 51:23','ALMA 51:26','ALMA 51:28']),
         dict(nodes=['morianton','desolation'], label="Morianton's flight", refs=['ALMA 50:33','ALMA 50:34']),
         dict(nodes=['gideon','zarahemla','nephihah','lehi_c','moroni_c'], label="Moroni's return", refs=['ALMA 62:7','ALMA 62:18','ALMA 62:30','ALMA 62:32'])]),
 dict(id='helaman', label='Helaman to 3 Nephi', when='Judges year 37 to 34 years after the sign of Christ',
  show=['zarahemla','sidon','bountiful','desolation','neck','hagoth','land_north','land_south','many_waters','moroni_c','jeru_l',
        'mormon','gid','mulek_c','east_sea','west_sea','jacobugath','strip'],
  control={'M_north':'nephite','r_zar':'contested','r_bountiful':'nephite','r_desolation':'nephite','r_nephi_land':'lamanite',
           'r_east_wild':'lost'},
  notes=[("Hagoth's ships sail north from the neck; thousands move to the land northward", ['ALMA 63:4','ALMA 63:5','ALMA 63:6']),
         ("Migrants reach large bodies of water and build in cement; timber is shipped north", ['HELAMAN 3:3','HELAMAN 3:4','HELAMAN 3:7','HELAMAN 3:10']),
         ("Coriantumr takes Zarahemla and marches toward Bountiful, but is cut off", ['HELAMAN 1:20','HELAMAN 1:23','HELAMAN 1:29']),
         ("The Lamanites take Zarahemla; the Nephites hold a one-day line across Bountiful, later regaining half their lands", ['HELAMAN 4:5','HELAMAN 4:7','HELAMAN 4:10']),
         ("Lachoneus gathers everyone between Zarahemla and the Bountiful–Desolation line", ['3 NEPHI 3:23','3 NEPHI 3:24']),
         ("Destruction: Zarahemla burns, Moroni sinks into the sea, Jerusalem is covered by waters, Jacobugath burns", ['3 NEPHI 8:8','3 NEPHI 8:9','3 NEPHI 9:7','3 NEPHI 9:9']),
         ("The multitude gathers at the temple in Bountiful", ['3 NEPHI 11:1'])],
  paths=[dict(nodes=['zarahemla','bountiful'], label="Coriantumr's march (stopped)", refs=['HELAMAN 1:23','HELAMAN 1:29']),
         dict(nodes=['zarahemla','neck','many_waters'], label='Migration north', refs=['ALMA 63:4','HELAMAN 3:3','HELAMAN 3:4']),
         dict(nodes=['hagoth',(330,486),(150,400),(118,225)], label="Hagoth's ships sail north", refs=['ALMA 63:6'], sea=True)],
  lost=['moroni_c','jeru_l','zarahemla','jacobugath']),
 dict(id='mormon', label='Mormon', when='322–385 years after Christ (Mormon 1–6)',
  show=['zarahemla','sidon','angola','david','joshua','jashon','shim','antum','shem','neck','desolation','teancum_c','boaz','jordan',
        'cumorah','many_waters','land_north','land_south','east_sea','west_sea','bountiful'],
  control={'M_north':'nephite','M_south':'lamanite','r_antum':'nephite','r_desolation':'contested','r_cumorah':'nephite',
           'r_joshua':'contested','r_david':'contested','r_zar':'lamanite','r_bountiful':'lamanite'},
  notes=[("Mormon is carried south to Zarahemla at eleven; war by the waters of Sidon", ['MORMON 1:6','MORMON 1:10']),
         ("Retreat toward the north countries: Angola, David, Joshua by the west seashore", ['MORMON 2:3','MORMON 2:4','MORMON 2:5','MORMON 2:6']),
         ("Jashon, near Ammaron's hill, then northward to Shem", ['MORMON 2:16','MORMON 2:17','MORMON 2:20']),
         ("Treaty: the Nephites get the land northward up to the narrow passage, the Lamanites the land southward", ['MORMON 2:29']),
         ("Stand at Desolation by the pass, and Teancum by the seashore", ['MORMON 3:5','MORMON 4:3']),
         ("Boaz; Mormon takes the records from Shim; Jordan", ['MORMON 4:20','MORMON 4:23','MORMON 5:3']),
         ("The last gathering at Cumorah, a land of many waters", ['MORMON 6:2','MORMON 6:4','MORMON 6:6'])],
  paths=[dict(nodes=['zarahemla','angola','david','joshua'], label='Retreat north', refs=['MORMON 2:3','MORMON 2:6']),
         dict(nodes=['jashon','shem'], label='Driven northward', refs=['MORMON 2:20']),
         dict(nodes=['desolation','boaz','shim','jordan','cumorah'], label='Final retreat', refs=['MORMON 4:20','MORMON 4:23','MORMON 5:3','MORMON 6:4'])]),
]
