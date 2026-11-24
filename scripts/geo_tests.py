def build_tests(ctx):
    nodes = ctx['nodes']
    L = lambda ids: ' > '.join(nodes[i]['label'] for i in ids)
    ns_chain, ew_chain = ctx['ns_chain'], ctx['ew_chain']
    T = []

    # ------------------------------------------------------------ DIRECTION
    T.append(dict(
        id='D1', group='Direction', verdict='consistent',
        title='North/south and east/west statements form no loop',
        summary=f"{ctx['nns']} north-south and {ctx['new']} east-west statements were encoded. Treated as an ordering (A is north of B), they contain no cycle, with or without the weaker inferred ones, and one map satisfies all of them at once.",
        detail=[
            f"The longest north-to-south chain the text supports is: {L(ns_chain[0])}.",
            f"The longest west-to-east chain is: {L(ew_chain[0])}.",
            f"Cycles found: north-south {len(ctx['cyc']['ns_all'])}, east-west {len(ctx['cyc']['ew_all'])}. I then built a layout from the constraints; it violates {ctx['viol'][0]} of {ctx['n_ns_c']} north-south and {ctx['viol'][1]} of {ctx['n_ew_c']} east-west rules (see the Map view).",
            "Caveat: the text gives few absolute directions. Most are 'A is north of B' pairs, so this is a test for contradictions, not a proof that the map is unique."],
        rows=[dict(label='Desolation is north of Bountiful', v=['ALMA 22:31', '3 NEPHI 3:23']),
              dict(label='Zarahemla is south of Bountiful', v=['3 NEPHI 3:23', 'HELAMAN 1:23']),
              dict(label='The Lamanite land is south of Zarahemla', v=['ALMA 22:27', 'ALMA 50:7']),
              dict(label='Antionum is east of Zarahemla and south of Jershon', v=['ALMA 31:3']),
              dict(label='Jershon is south of Bountiful, on the east sea', v=['ALMA 27:22'])]))

    T.append(dict(
        id='D2', group='Direction', verdict='consistent',
        title="\"Up\" and \"down\" are used consistently",
        summary="Across about 60 verses, travel toward Nephi and the southern wilderness is always 'up', and travel toward Zarahemla, Jershon and Desolation is always 'down'. I found no reversal, so the usage is internally consistent. The Old World verses follow a separate usage: 'up' to Jerusalem and 'down' away from it into the wilderness. That Old World usage matches elevation and the Hebrew Bible idiom of going 'up' to Jerusalem, not a compass direction. The text alone does not settle whether the New World 'up/down' means elevation, direction, or both.",
        detail=["I searched every motion verb followed by 'up' or 'down' and a place name. Nephi and Zarahemla are the two best-attested endpoints, and the usage never flips.",
                "One edge case: 3 Nephi 6:25 has a complaint 'came up unto the land of Zarahemla'. The origin is not stated, so it cannot be tested.",
                "Mosiah 7:6 has Ammon go 'down into the land of Nephi' from the hill north of Shilom. That is a local descent into the city, so it fits.",
                "Mormon 4:1 has the Nephites go 'up' out of Desolation toward the Lamanites, while Mormon 3:7 and 4:19 have the Lamanites 'come down' on Desolation. That pattern matches the rest: the south is higher.",
                "The rule holds even in side remarks: Alma 22:31 has the Mulekites come 'up into the south wilderness' from the north, Alma 27:26 has the Ammonites go 'down into the land of Jershon' from the southern border, and Alma 2:24 calls Minon 'above the land of Zarahemla, in the course of the land of Nephi'.",
                "Untestable cases: Ether 7:5 and 14:11 have armies come 'up unto the land of Moron' without saying where from.",
                "Old World, checked against real geography: the Red Sea is south of Jerusalem, so 'came down by the borders near the shore of the Red Sea' (1 Nephi 2:5) cannot mean north. It fits elevation: Jerusalem sits in the hills at roughly 2,500 ft (750 m), and the route to the Gulf of Aqaba descends through the Judean wilderness and the Dead Sea and Arabah rift to sea level. 'Up to Jerusalem' also fits the common Hebrew idiom, which is used from any direction.",
                "Limit: in the New World I mapped 'up' to south and 'down' to north because that is how the verses line up. A higher Nephi would explain the same pattern, so the test shows the usage never flips, not which meaning the author intended. The north-south constraints rest on explicit 'northward' and 'southward' statements. The one place that leans on elevation-style wording is the inferred relation putting Minon south of Zarahemla ('above', Alma 2:24), which is already marked inferred."],
        rows=[dict(label=f"{d} {pl}: {sense}", v=vs) for d, pl, vs, sense in ctx['UPDOWN']]))

    T.append(dict(
        id='D3', group='Direction', verdict='consistent',
        title='Every river-Sidon crossing puts places on the right bank',
        summary="Zarahemla, Melek and Manti are on the west bank; Gideon, Hill Amnihu, Antionum, Nephihah and the 'south wilderness' crossed by Zoram are on the east. All crossing events agree with that.",
        detail=["No place is assigned to both banks and no journey crosses the river the wrong way for its endpoints.",
                "Two independent battle accounts agree. In Alma 16 raiders leaving Ammonihah (west bank) cross the Sidon beyond Manti and are met on the east side. In Alma 43 Lamanites coming from Antionum (east) go round by the head of the Sidon and must cross the river to reach Manti. Both put Manti on the west bank near the upper river, with the Lamanites using the east-bank south wilderness.",
                "Alma 22:27 independently puts Manti on the southern strip, 'by the head of the river Sidon', which is why Alma 17:1 travels 'southward' from Gideon to reach it.",
                "One close-reading point: Alma 43:22 says the Lamanites went 'by the head of the river Sidon', yet in 43:35 they still have to cross it. That would be odd if 'head' meant the river's source, which they would simply walk around. But Alma 56:25 speaks of crossing 'the head of Sidon', so the text uses 'head' for the upper river region, which can be crossed. Read that way the accounts agree."],
        rows=[dict(label='Hill Amnihu is east of the Sidon, and the Nephites cross the river back to Zarahemla', v=['ALMA 2:15', 'ALMA 2:26', 'ALMA 2:27']),
              dict(label='Zarahemla to Gideon is "over upon the east of the river Sidon"', v=['ALMA 6:7']),
              dict(label='Melek is on the west of the Sidon', v=['ALMA 8:3']),
              dict(label='Gideon south to Manti', v=['ALMA 17:1']),
              dict(label='Raiders cross the Sidon "beyond the borders of Manti"; Zoram meets them on the east side', v=['ALMA 16:6', 'ALMA 16:7']),
              dict(label='Lamanites go round the head of the Sidon to reach Manti; Moroni waits on the west bank, Lehi on the east', v=['ALMA 43:22', 'ALMA 43:27', 'ALMA 43:32', 'ALMA 43:35', 'ALMA 43:53']),
              dict(label='"cross the head of Sidon, over to the city of Nephihah"', v=['ALMA 56:25']),
              dict(label='The strip runs "through the borders of Manti, by the head of the river Sidon"', v=['ALMA 22:27'])]))

    T.append(dict(
        id='D4', group='Direction', verdict='consistent',
        title='Two "sea to sea" lines: the strip in the south, the neck in the north',
        summary="Alma 22 describes two different lines that each run from sea to sea. One is a narrow strip of wilderness south of Zarahemla; the other is the narrow neck at Bountiful and Desolation. The text keeps them apart, with Zarahemla and Bountiful between them.",
        detail=["The strip is described as wilderness dividing the Lamanite kingdom from Zarahemla (Alma 22:27). The neck is described as a land bridge with sea on both sides (Alma 22:32, 50:34, Ether 10:20).",
                "Terms are not mixed up: 'narrow strip' appears once, only for the southern wilderness (Alma 22:27), and 'neck', 'pass' and 'passage' appear only for the northern line (Alma 22:32, 50:34, 52:9, 63:5, Ether 10:20, Mormon 2:29, 3:5).",
                "3 Nephi 3:23 names the stretch between them: Zarahemla, 'the land which was between', and then the line between Bountiful and Desolation."],
        rows=[dict(label='Narrow strip of wilderness, sea east to sea west, south of Zarahemla', v=['ALMA 22:27', 'ALMA 50:11']),
              dict(label='Narrow neck: Bountiful (south) and Desolation (north)', v=['ALMA 22:31', 'ALMA 22:32']),
              dict(label='Narrow pass "by the sea, on the west and on the east"', v=['ALMA 50:34']),
              dict(label='Hagoth builds his ship at the neck and launches it into the west sea', v=['ALMA 63:5']),
              dict(label='The Jaredites build a great city "by the narrow neck... where the sea divides the land"', v=['ETHER 10:20']),
              dict(label='Mormon: city Desolation "by the narrow pass which led into the land southward"', v=['MORMON 3:5'])]))

    T.append(dict(
        id='D5', group='Direction', verdict='consistent',
        title='The east-coast cities fit one coastline',
        summary="Moroni is the southernmost coastal city, Lehi is north of it, Mulek is the last before Bountiful, and Jershon and Antionum sit along the same coast. Everything lines up, but the text never says how Jershon relates to the six cities.",
        detail=["Alma 51:26 lists six cities taken in one sweep, all 'on the east borders by the seashore'. Alma 51:28 then has the Lamanites reach 'the borders of the land Bountiful', so Bountiful is north of Mulek, and Alma 52:23 confirms it when Teancum retreats 'by the seashore, northward'.",
                "Alma 27:22 says Jershon joins Bountiful from the south, and Alma 31:3 puts Antionum south of Jershon. Alma 50:13 puts Moroni at the south line. So the six cities and Jershon must share the same stretch of coast.",
                "This is under-determined, not contradictory: the text does not say whether those cities are inside Jershon or a separate band."],
        rows=[dict(label='City Moroni by the east sea, on the south by the Lamanite line', v=['ALMA 50:13']),
              dict(label='Nephihah between Moroni and Aaron; Lehi built "on the north"', v=['ALMA 50:14', 'ALMA 50:15']),
              dict(label='Six cities on the east borders by the seashore', v=['ALMA 51:26']),
              dict(label='Mulek, then the borders of Bountiful', v=['ALMA 51:28', 'ALMA 52:2', 'ALMA 52:23']),
              dict(label='Jershon joins Bountiful from the south; Antionum is south of Jershon', v=['ALMA 27:22', 'ALMA 31:3'])]))

    # ------------------------------------------------------------ DISTANCE
    T.append(dict(
        id='N1', group='Distance', verdict='minor tension',
        title='The neck: "a day and a half" or "a day"?',
        summary="Alma 22:32 says the line between Bountiful and Desolation, east sea to west sea, is a day and a half's journey for a Nephite. Helaman 4:7 says the line the Nephites fortified from the west sea to the east is a day's journey for a Nephite.",
        detail=["This is the only place where two numbers are given for what may be the same span.",
                "Ways they could both be right: (1) it is not the same line, since Helaman 4:6-7 describes a defensive line inside Bountiful, to guard 'their north country', and the Alma line is the Bountiful-Desolation boundary; (2) 'a day's journey' is a round figure; (3) the two lines are at different places along a neck that narrows or widens.",
                "Ways they conflict: if both are the Bountiful-Desolation line, 1.5 versus 1 is a 50% difference.",
                "Verdict: not a hard contradiction, because the text never says they are the same line, but it is the one numeric tension in the geography."],
        rows=[dict(label='Bountiful-Desolation line: a day and a half', v=['ALMA 22:32']),
              dict(label='Nephite fortified line, west sea to east: a day', v=['HELAMAN 4:6', 'HELAMAN 4:7'])]))

    T.append(dict(
        id='N2', group='Distance', verdict='consistent',
        title='Nephi to Zarahemla: 20 days on one route, 40 when lost',
        summary="Alma's people took 8 days from Mormon to Helam, 1 day to the valley of Alma, and 12 more to Zarahemla: 21 days with flocks and families. Ammon's party took 40 days, but the text says they did not know the way.",
        detail=["Mosiah 23:3 gives eight days from Mormon to Helam. Mosiah 24:20 adds a full day to the valley of Alma, and 24:25 twelve days from there to Zarahemla. A route of about 21 days therefore exists; it is not stated to be direct (Helam was off the Lamanites' known roads, see Mosiah 23:35-37).",
                "Supporting detail: the Lamanites who chased Limhi's people lost the trail after two days (Mosiah 22:16), wandered 'many days', and ended up at Amulon and then Helam, where they had to ask Alma 'the way which led to the land of Nephi'. Helam being hard to find from Nephi fits Alma's people fleeing 8 days into unknown country.",
                "Mosiah 7:4-5 gives forty days for Ammon's sixteen men, with the explicit reason that they 'knew not the course'. A lost party taking twice as long as a guided one is no conflict.",
                "Limhi's people and Mosiah's sons are both given only 'many days'. A 20-day route is a reasonable reading of 'many'.",
                "No triangle test is possible: no pair of these places has two independent day counts."],
        rows=[dict(label='Mormon to Helam: eight days', v=['MOSIAH 23:3']),
              dict(label='First day: to the valley of Alma', v=['MOSIAH 24:20']),
              dict(label='Wilderness to Zarahemla: twelve days', v=['MOSIAH 24:25']),
              dict(label='Pursuers lose the trail after two days; later lost and must ask the way to Nephi', v=['MOSIAH 22:16', 'MOSIAH 23:30', 'MOSIAH 23:35', 'MOSIAH 23:36']),
              dict(label="Ammon's party: forty days, lost", v=['MOSIAH 7:4', 'MOSIAH 7:5']),
              dict(label="Limhi's people and Mosiah's sons: 'many days'", v=['MOSIAH 22:13', 'ALMA 17:9'])]))

    T.append(dict(
        id='N3', group='Distance', verdict='consistent',
        title='Melek to Ammonihah: three days north',
        summary="Ammonihah is three days north of Melek, which is on the west bank. Nothing else in the text gives a competing distance or direction for it.",
        detail=["Alma 8:3 puts Melek west of the Sidon, by the wilderness border. Alma 8:6 puts Ammonihah three days north. Alma 8:18 has Alma re-enter by the south side, which matches him returning from the south.",
                "The Lamanites reach Ammonihah 'upon the wilderness side' (Alma 16:2) and later approach it again (Alma 49:1), which fits a city at the western edge."],
        rows=[dict(label='Melek: west of Sidon', v=['ALMA 8:3']),
              dict(label='Ammonihah: three days north of Melek', v=['ALMA 8:6']),
              dict(label='Alma re-enters by the south road', v=['ALMA 8:18']),
              dict(label='Lamanites attack from the wilderness side', v=['ALMA 16:2'])]))

    T.append(dict(
        id='N4', group='Distance', verdict='consistent',
        title='The Old World route has no reversals',
        summary="Down to the Red Sea borders, three days in the wilderness to a valley by a river that empties into the Red Sea, four days south-southeast to Shazer, many days on 'nearly the same course' to Nahom, then 'nearly eastward' to Bountiful. The headings never double back.",
        detail=["The text's own stated headings are SSE, 'nearly the same course as in the beginning', and then 'nearly eastward'. Together they describe one turn, from south-southeast to east.",
                "The whole overland trip is given as eight years in the wilderness (1 Nephi 17:4), which is a duration and not comparable to the day counts.",
                "I did not map this onto any real-world place, as asked."],
        rows=[dict(label='Three days; valley by a river; near the Red Sea', v=['1 NEPHI 2:5', '1 NEPHI 2:6']),
              dict(label='Four days nearly south-southeast to Shazer', v=['1 NEPHI 16:13']),
              dict(label='Same course to Nahom', v=['1 NEPHI 16:33', '1 NEPHI 16:34']),
              dict(label='Nearly eastward to Bountiful by the sea', v=['1 NEPHI 17:1', '1 NEPHI 17:5', '1 NEPHI 17:6']),
              dict(label='Eight years in the wilderness', v=['1 NEPHI 17:4'])]))

    # ------------------------------------------------------------ CROSS-REFERENCE
    T.append(dict(
        id='X1', group='Cross-reference', verdict='consistent',
        title='Where did the Mulekites first land? The text answers it',
        summary="Alma 22:30-31 puts their first landing in the north, in the land of the Jaredite bones, and then says 'they came from there up into the south wilderness'. Helaman 6:10 agrees ('the Lord did bring Mulek into the land north'). Omni 1:16 is a compressed summary of the same history.",
        detail=["Correction to my first pass: I had flagged this as a minor tension and said no verse states the migration south. Alma 22:31 states it in its first clause. The 'they' follows directly from 'the people of Zarahemla... the place of their first landing', so it refers to them.",
                "Omni 1:16 says they were brought 'into the land where Mosiah discovered them; and they had dwelt there from that time forth'. Read against Alma 22:31, 'the land' is the land in general and the dwelling is from their arrival in it, with the move south left out.",
                "This also explains Omni 1:21: the people of Zarahemla were the ones who 'discovered' the last Jaredite, Coriantumr, which fits their having landed in the north."],
        rows=[dict(label='"the place of their first landing" (north, by Desolation)', v=['ALMA 22:30']),
              dict(label='"they came from there up into the south wilderness"', v=['ALMA 22:31']),
              dict(label='"the Lord did bring Mulek into the land north"', v=['HELAMAN 6:10']),
              dict(label='"into the land where Mosiah discovered them; and they had dwelt there from that time forth"', v=['OMNI 1:16']),
              dict(label='Coriantumr "was discovered by the people of Zarahemla"', v=['OMNI 1:21'])]))

    T.append(dict(
        id='X2', group='Cross-reference', verdict='consistent',
        title='The northern land is described the same way by five different writers',
        summary="The land northward is a land of 'many waters', 'large bodies of water' and 'many rivers', with cement houses because timber is scarce, from Mosiah through Mormon.",
        detail=["Limhi's scouts (Mosiah 8:8) describe a land among many waters. Alma 50:29 calls the land northward 'covered with large bodies of water'. Helaman 3:4 says the migrants reached 'large bodies of water and many rivers'. Mormon 6:4 puts Cumorah in 'a land of many waters, rivers, and fountains'.",
                "Helaman 3:5-11 explains the timber and cement detail in the same land, and Helaman 3:10 says timber was shipped north, which fits a land reachable by sea."],
        rows=[dict(label='Scouts: "a land among many waters"', v=['MOSIAH 8:8']),
              dict(label='Land northward "covered with large bodies of water"', v=['ALMA 50:29']),
              dict(label='"large bodies of water and many rivers"; cement houses', v=['HELAMAN 3:4', 'HELAMAN 3:7']),
              dict(label='Timber shipped north', v=['HELAMAN 3:10']),
              dict(label='Cumorah: "a land of many waters, rivers, and fountains"', v=['MORMON 6:4'])]))

    T.append(dict(
        id='X3', group='Cross-reference', verdict='consistent',
        title='The southern wilderness is a hunting ground in both Jaredite and Nephite accounts',
        summary="Ether 9 and 10 have flocks fleeing south from serpents and the Jaredites keeping the land southward 'for a wilderness, to get game'. Alma 22:31 describes Bountiful as a wilderness full of wild animals, 'a part of which had come from the land northward for food'.",
        detail=["Two authors, about the same stretch of land, separated by many centuries of narrative, agree on the detail that animals moved south from the north.",
                "Ether 9:31 even says this southern land was 'called by the Nephites Zarahemla', which agrees with Zarahemla being south."],
        rows=[dict(label='Flocks flee towards the land southward, "called by the Nephites Zarahemla"', v=['ETHER 9:31', 'ETHER 9:32']),
              dict(label='Land southward kept "for a wilderness, to get game"', v=['ETHER 10:19', 'ETHER 10:21']),
              dict(label='Bountiful: a wilderness "filled with all manner of wild animals", some from the north', v=['ALMA 22:31'])]))

    T.append(dict(
        id='X4', group='Cross-reference', verdict='consistent',
        title='The scouts: did they think they had found Zarahemla?',
        summary="Mosiah 8:8 says Limhi's scouts 'found not the land of Zarahemla'. Mosiah 21:26 says they found the bones land and, 'having supposed it to be the land of Zarahemla', went home.",
        detail=["On a closer reading this is not a tension. Mosiah 8:8 is Limhi speaking after Ammon has arrived, so he now knows the scouts missed Zarahemla. Mosiah 21:26 is the narrator explaining what the scouts believed at the time. Both statements are true together; I had over-flagged it in the first pass.",
                "It also shows the scouts were lost, which fits Mosiah 21:25."],
        rows=[dict(label='"found not the land of Zarahemla"', v=['MOSIAH 8:8']),
              dict(label='"having supposed it to be the land of Zarahemla"', v=['MOSIAH 21:26'])]))

    T.append(dict(
        id='X5', group='Cross-reference', verdict='consistent',
        title='Mormon-era retreat and treaty fit the earlier geography',
        summary="The Nephites retreat north in stages, make a treaty giving them the land northward to the narrow passage, and then gather at Desolation by the pass.",
        detail=["Mormon 2:3-6 retreats 'towards the north countries' through Angola, David and Joshua, which is in the borders west by the seashore. Mormon 2:20 reaches Shem 'northward'. Mormon 2:29 splits the land at the narrow passage: Nephites north, Lamanites south.",
                "Mormon 3:5 then places city Desolation in the borders by that same pass, and Mormon 4:3 puts the city Teancum near it on the seashore. This agrees with Alma 22:30-32, 52:9 and 63:5."],
        rows=[dict(label='Retreat to Angola, David, Joshua (west by the seashore)', v=['MORMON 2:3', 'MORMON 2:4', 'MORMON 2:5', 'MORMON 2:6']),
              dict(label='Shem, northward', v=['MORMON 2:20']),
              dict(label='Treaty: land northward to the narrow passage', v=['MORMON 2:29']),
              dict(label='Desolation by the narrow pass; Teancum by the seashore near it', v=['MORMON 3:5', 'MORMON 4:3'])]))

    T.append(dict(
        id='X6', group='Cross-reference', verdict='consistent',
        title='Hill Ramah (Jaredite) and Hill Cumorah (Nephite) are one hill',
        summary="Ether 15:11 calls it the hill Ramah, 'that same hill where my father Mormon did hide up the records'. Mormon 6:6 says he hid them in the hill Cumorah. Both sit in the northern land of many waters.",
        detail=["Ether 9:3 has Omer travel 'many days', pass the hill Shim, pass 'the place where the Nephites were destroyed', and go east to Ablom by the seashore. Mormon 1:3 quotes Ammaron saying the hill 'shall be called Shim', as if the name were still future, while Ether 9:3 (Moroni's abridgment) has Omer pass 'the hill of Shim' in Jaredite days. One reading is that Moroni uses the later name; the text does not say. It is a naming-time point, not a location conflict."],
        rows=[dict(label='Ramah is where Mormon hid the records', v=['ETHER 15:11']),
              dict(label='Mormon hides them in Cumorah', v=['MORMON 6:6']),
              dict(label='Cumorah: a land of many waters', v=['MORMON 6:4']),
              dict(label="Omer's route: Shim, the place of destruction, then east to Ablom", v=['ETHER 9:3']),
              dict(label='Hill Shim is in the land Antum, near Jashon', v=['MORMON 1:3', 'MORMON 2:17'])]))

    # ------------------------------------------------------------ NAMING
    T.append(dict(
        id='M1', group='Naming', verdict='note',
        title='Reused names for different places',
        summary="Several names mean different places depending on the speaker and chapter. They are not contradictions, but they can look like them.",
        detail=["Helaman 6:10 says the whole land south was called Lehi and the whole land north Mulek. Yet 'Lehi' is also a city on the Nephite east coast (Alma 50:15), and 'Mulek' is a city on that same coast just south of Bountiful (Alma 51:26), while the 'land called Mulek' is the whole land north of the neck.",
                "'Jerusalem' is also a Lamanite city near the borders of Mormon (Alma 21:1-2). 'Bountiful' is both the land by the sea at the neck and the first stop by the sea in the Old World (1 Nephi 17:5). 'Gideon', 'Manti', 'Nephi', 'Moroni', 'Aaron', 'Noah', 'Teancum', 'Mormon' and 'Helam' are people as well as places."],
        rows=[dict(label='Land south called Lehi, land north called Mulek', v=['HELAMAN 6:10']),
              dict(label='City Lehi, "in the north by the borders of the seashore"', v=['ALMA 50:15']),
              dict(label='City Mulek on the east borders by the seashore', v=['ALMA 51:26']),
              dict(label='Lamanite city Jerusalem, joining the borders of Mormon', v=['ALMA 21:1', 'ALMA 21:2']),
              dict(label='Old World Bountiful by the sea Irreantum', v=['1 NEPHI 17:5'])]))

    T.append(dict(
        id='M2', group='Naming', verdict='consistent',
        title='Around the first city of Nephi: three directions agree',
        summary="A hill north of Shilom (Mosiah 7:5, 11:13), a Lamanite host 'on the south of the land of Shilom' (9:14) and another that 'came up upon the north of the land of Shilom' (10:8) all fit one layout.",
        detail=["King Noah's tower near the temple overlooks both Shilom and Shemlon (Mosiah 11:12), and Lamanites appear 'within the borders' at Shemlon (Mosiah 19:6).",
                "The hill north of Shilom is the same hill in Mosiah 7:5, 7:16 and 11:13."],
        rows=[dict(label='Hill north of Shilom (Ammon pitches his tents there)', v=['MOSIAH 7:5', 'MOSIAH 7:16']),
              dict(label="Noah's tower on the hill north of Shilom; overlooks Shilom and Shemlon", v=['MOSIAH 11:12', 'MOSIAH 11:13']),
              dict(label='Lamanite host "on the south of the land of Shilom" and later "upon the north"', v=['MOSIAH 9:14', 'MOSIAH 10:8'])]))
    T.insert(5, dict(
        id='N0', group='Distance', verdict='note',
        title='Every travel-time number in the text',
        summary="The whole book gives only eleven numeric travel times. Only one pair of places, the two seas across the neck, gets two different numbers. That is why a triangle test of the kind 'A-B plus B-C versus A-C' cannot be run anywhere.",
        detail=["I searched every verse for a number followed by 'day', 'days' or 'day's' near travel words. The list: 1 Nephi 2:6 (3 days), 16:13 (4 days), Mosiah 7:4 (40 days, lost), 22:16 (2-day pursuit), 23:3 (8 days), 24:20 (one day, 'traveled all day'), 24:25 (12 days), Alma 8:6 (3 days), Alma 22:32 (a day and a half), Helaman 4:7 (a day), Ether 6:11 (344 days at sea). Everything else is 'many days' or a duration of a battle or a stay.",
                "Mosiah 23:3, 24:20 and 24:25 chain into one route (21 days), but no other route connects the same endpoints with a number, so there is nothing to check them against."],
        rows=[dict(label='Old World', v=['1 NEPHI 2:6', '1 NEPHI 16:13']),
              dict(label='Nephi to Zarahemla region', v=['MOSIAH 7:4', 'MOSIAH 22:16', 'MOSIAH 23:3', 'MOSIAH 24:20', 'MOSIAH 24:25']),
              dict(label='Melek to Ammonihah', v=['ALMA 8:6']),
              dict(label='Across the neck', v=['ALMA 22:32', 'HELAMAN 4:7']),
              dict(label='Jaredite crossing', v=['ETHER 6:11'])]))

    T.append(dict(
        id='X7', group='Cross-reference', verdict='tension',
        title='Nephihah: taken in Alma 51, or held until Alma 59?',
        summary="Alma 51:25 says Amalickiah would not let his army go against Nephihah. The next verse, 'And thus he went on', lists Nephihah first among the cities he took. Every other city on that list is later shown in Lamanite hands; Nephihah alone is later shown as Nephite, full of refugees from those same cities.",
        detail=["The clash is inside one sentence-flow. 51:25 describes the method: keep the army down by the seashore and leave a garrison in each city taken. 51:26 opens 'And thus he went on', meaning by that method, and then names the one city 51:25 said he avoided.",
                "The rest of the 51:26 list checks out against later chapters. Moroni was taken in 51:23 and is still the Lamanite base in 62:25 and 62:32-34. Mulek is held until Moroni retakes it (52:2, 52:26). Gid is held until Alma 55. Morianton is still a Lamanite stronghold in 55:33. Lehi is still Lamanite when Moroni marches on it after Nephihah (62:30). Omner is never mentioned again. Only Nephihah breaks the pattern.",
                "Positive evidence that Nephihah stayed Nephite. 51:24: refugees from Moroni flee to it. 56:25, in Helaman's account of the 26th-27th years: the western Lamanites 'durst not... cross the head of Sidon, over to the city of Nephihah', which only makes sense if it was not theirs. 59:5: its people are 'gathered together from the city of Moroni and the city of Lehi and the city of Morianton', the very cities the Lamanites took. 59:9: Moroni thought it 'easier to keep the city from falling... than to retake it', which assumes it had not fallen. 59:11: only now is it 'lost'.",
                "Correction to my earlier write-up: I leaned on the fact that no recapture of Nephihah is recorded between Alma 51 and 59. That is weak evidence. The book also never narrates the retaking of Morianton, Omner or Lehi; it only says Moroni pursued the Lamanites 'from city to city' (62:32). The positive statements above are what carry the case.",
                "Readings that would reconcile it, none stated in the text: (1) 51:26 is a summary list of the region and 'the city of Nephihah' was included by mistake, which is the simplest fit, since it is the only entry the later chapters contradict; (2) Nephihah fell soon after 51:25 and was retaken off the record before Helaman's 26th-27th-year report, a window of about a year; (3) 50:14 calls it 'the city, or the land, Nephihah', so the Lamanites might have taken part of the land and not the city. But 51:26 says 'the city of Nephihah' outright, so this reading is weak.",
                "Location side-note: 51:26 calls all six cities 'on the east borders by the seashore'. 51:25 contrasts Nephihah with the seashore, 50:14 puts it inland between Moroni and Aaron, and 62:25 has Lamanites flee from Nephihah 'into the land of Moroni, which was in the borders by the seashore'. Nephihah is again the outlier in that list.",
                "Verdict: a real tension that the text leaves unresolved. It reads most like a slip in one list, not a broken geography or timeline."],
        rows=[dict(label='Nephihah founded between Moroni and Aaron', v=['ALMA 50:13', 'ALMA 50:14']),
              dict(label='Moroni falls; its people flee to Nephihah; Lehi prepares', v=['ALMA 51:23', 'ALMA 51:24']),
              dict(label='Amalickiah will not go against Nephihah; keeps to the seashore; garrisons each city', v=['ALMA 51:25']),
              dict(label='"And thus he went on": Nephihah listed first among cities taken', v=['ALMA 51:26', 'ALMA 51:27']),
              dict(label='The other listed cities later shown in Lamanite hands', v=['ALMA 52:2', 'ALMA 55:7', 'ALMA 55:33', 'ALMA 62:30', 'ALMA 62:32']),
              dict(label='Western Lamanites "durst not" cross over to Nephihah', v=['ALMA 56:20', 'ALMA 56:25']),
              dict(label='Nephihah peopled by refugees of Moroni, Lehi, Morianton; Moroni expects it to hold; it falls', v=['ALMA 59:5', 'ALMA 59:9', 'ALMA 59:11']),
              dict(label='Moroni retakes it; Lamanites flee to Moroni "by the seashore"', v=['ALMA 62:14', 'ALMA 62:25', 'ALMA 62:26'])]))

    T.append(dict(
        id='X8', group='Cross-reference', verdict='consistent',
        title="Omer's route in Ether matches Mormon's retreat, centuries apart",
        summary="Ether 9:3 has Omer leave Moron (near Desolation), travel many days past the hill Shim, then past 'the place where the Nephites were destroyed', then east to the sea. Mormon's own retreat runs Desolation, Boaz, the hill Shim, Jordan, Cumorah: the same order.",
        detail=["The two accounts come from different writers about different peoples. Moron is placed 'near the land which is called Desolation by the Nephites' (Ether 7:6), Mormon fights at Desolation (Mormon 3:5, 4:19), and both sequences then reach Shim before the final hill.",
                "Mormon 2:16-17 also puts Jashon near Shim during the earlier retreat, and Mormon 2:20 then moves 'northward' to Shem. Both phases keep Shim north of the neck."],
        rows=[dict(label='Moron is near Desolation', v=['ETHER 7:6']),
              dict(label="Omer: many days, past Shim, past the Nephite destruction, east to Ablom", v=['ETHER 9:3']),
              dict(label='Desolation falls; flight to Boaz', v=['MORMON 4:19', 'MORMON 4:20']),
              dict(label='Mormon takes the records from Shim', v=['MORMON 4:23']),
              dict(label='Jordan, then Cumorah', v=['MORMON 5:3', 'MORMON 6:2', 'MORMON 6:4'])]))

    T.append(dict(
        id='X9', group='Cross-reference', verdict='consistent',
        title='The great destruction fits where the cities were',
        summary="In 3 Nephi 8-9 the city of Moroni sinks 'into the depths of the sea'. Alma 50:13 had placed it 'by the east sea'. The Lamanite city Jerusalem is covered by waters; Alma 21:1 had placed it 'joining the borders of Mormon', a place of waters.",
        detail=["The Moroni match is specific: a city founded on the coast is the one that goes into the sea. The Jerusalem match is weaker, since many cities in 3 Nephi 9 sink, but it points the same way.",
                "Zarahemla burns rather than sinks (3 Nephi 8:8, 9:3), and it is rebuilt later (4 Nephi 1:8), which also fits."],
        rows=[dict(label='City Moroni founded by the east sea', v=['ALMA 50:13']),
              dict(label='Moroni sinks into the sea', v=['3 NEPHI 8:9', '3 NEPHI 9:4']),
              dict(label='Lamanite Jerusalem joins the borders of Mormon; the waters of Mormon', v=['ALMA 21:1', 'MOSIAH 18:30']),
              dict(label='Jerusalem covered by waters', v=['3 NEPHI 9:7']),
              dict(label='Zarahemla burned, later rebuilt', v=['3 NEPHI 9:3', '4 NEPHI 1:8'])]))

    T.append(dict(
        id='D6', group='Direction', verdict='consistent',
        title='One meeting, told twice, at the same spot',
        summary="Alma 17:1 has Alma, going south from Gideon to Manti, meet the sons of Mosiah coming home. Ten chapters later Alma 27:14-16 tells the same meeting from their side: they reach the borders by the southern wilderness, go on into the land, and meet Alma 'over in the place of which has been spoken'.",
        detail=["For the two accounts to fit, the road between Gideon and Manti must lie on the way from the southern wilderness to Zarahemla. That is exactly what the rest of the text says: Manti is at the strip by the head of the Sidon (Alma 22:27), and Gideon is south-east of Zarahemla across the river (Alma 6:7, 17:1).",
                "The writer refers back to the earlier spot without restating it, across a long flashback."],
        rows=[dict(label='Alma journeying southward from Gideon to Manti meets them', v=['ALMA 17:1']),
              dict(label='They reach the southern border; Ammon goes on and meets Alma "over in the place of which has been spoken"', v=['ALMA 27:14', 'ALMA 27:16']),
              dict(label='Alma brings them back to Zarahemla', v=['ALMA 27:20'])]))

    T.append(dict(
        id='M3', group='Naming', verdict='note',
        title='East-coast order: Bountiful, Gid, then Mulek?',
        summary="Helaman 5:15 has Nephi and Lehi preach at Bountiful, then Gid, then Mulek. Elsewhere Mulek is the city next to Bountiful (Alma 51:28, 52:20), so the preachers went past Mulek or took another road.",
        detail=["Not a contradiction: travelling preachers need not go in map order, and the text never says which of Gid and Mulek is further north. I note it because Alma 51:26 lists the cities as the Lamanites took them heading north, and there Gid comes before Mulek."],
        rows=[dict(label='Bountiful, then Gid, then Mulek', v=['HELAMAN 5:14', 'HELAMAN 5:15']),
              dict(label='Mulek is last before Bountiful; "plains between the two cities"', v=['ALMA 51:26', 'ALMA 51:28', 'ALMA 52:20'])]))

    T.append(dict(
        id='M4', group='Naming', verdict='note',
        title='The city of Aaron is far from Ammonihah',
        summary="Alma 8:13 has Alma leave Ammonihah, west of the Sidon, heading for the city of Aaron. Alma 50:14 later places Nephihah between Aaron and the coastal city Moroni, which puts Aaron toward the east.",
        detail=["Either Alma set out on a long trip across the land, or there are two places called Aaron. The text says nothing about the distance, and Alma turns back 'speedily' after the angel appears (8:18), so this cannot be tested. I list it as an open point, not a tension."],
        rows=[dict(label='Alma heads from Ammonihah toward Aaron', v=['ALMA 8:13', 'ALMA 8:18']),
              dict(label='Nephihah between Moroni (east sea) and Aaron', v=['ALMA 50:13', 'ALMA 50:14'])]))
    order = {'Direction': 0, 'Distance': 1, 'Cross-reference': 2, 'Naming': 3}
    T.sort(key=lambda t: (order[t['group']], t['id'][0] != t['group'][0], t['id']))
    return T
