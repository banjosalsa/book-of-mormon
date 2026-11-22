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
        title='"Up" and "down" are used the same way throughout',
        summary="Going toward Nephi is always 'up'; coming toward Zarahemla is always 'down'; leaving Nephi is 'down out of'. None of the matching verses I found reverses this.",
        detail=["I searched every motion verb followed by 'up' or 'down' and a place name. Nephi and Zarahemla are the two best-attested endpoints, and the usage never flips.",
                "One edge case: 3 Nephi 6:25 has a complaint 'came up unto the land of Zarahemla'. The origin is not stated, so it cannot be tested.",
                "Mosiah 7:6 has Ammon go 'down into the land of Nephi' from the hill north of Shilom. That is a local descent into the city, so it fits.",
                "Mormon 4:1 has the Nephites go 'up' out of Desolation toward the Lamanites, while Mormon 3:7 and 4:19 have the Lamanites 'come down' on Desolation. That pattern matches the rest: the south is higher."],
        rows=[dict(label=f"{d} {pl}: {sense}", v=vs) for d, pl, vs, sense in ctx['UPDOWN']]))

    T.append(dict(
        id='D3', group='Direction', verdict='consistent',
        title='Every river-Sidon crossing puts places on the right bank',
        summary="Zarahemla, Melek and Manti are on the west bank; Gideon, Hill Amnihu, Antionum, Nephihah and the 'south wilderness' crossed by Zoram are on the east. All crossing events agree with that.",
        detail=["No place is assigned to both banks and no journey crosses the river the wrong way for its endpoints.",
                "Alma 16:6-7 requires the Lamanite raiders to cross the Sidon from west to east on their way home beyond Manti. That fits Lamanite lands on the east side too (Alma 22:29, Alma 25:5), so it is a constraint, not a conflict."],
        rows=[dict(label='Hill Amnihu is east of the Sidon, and the Nephites cross the river back to Zarahemla', v=['ALMA 2:15', 'ALMA 2:26', 'ALMA 2:27']),
              dict(label='Zarahemla to Gideon is "over upon the east of the river Sidon"', v=['ALMA 6:7']),
              dict(label='Melek is on the west of the Sidon', v=['ALMA 8:3']),
              dict(label='Gideon south to Manti', v=['ALMA 17:1']),
              dict(label='Raiders cross the Sidon "beyond the borders of Manti"; Zoram meets them on the east side', v=['ALMA 16:6', 'ALMA 16:7']),
              dict(label='Lamanites go round the head of the Sidon to reach Manti; Moroni waits on the west bank, Lehi on the east', v=['ALMA 43:22', 'ALMA 43:27', 'ALMA 43:32', 'ALMA 43:35', 'ALMA 43:53']),
              dict(label='"cross the head of Sidon, over to the city of Nephihah"', v=['ALMA 56:25'])]))

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
        summary="Alma's people took 8 days to reach Helam and 12 more to reach Zarahemla, about 20 days. Ammon's party took 40 days, but the text says they did not know the way.",
        detail=["Mosiah 23:3 gives eight days from the area of Mormon to Helam. Mosiah 24:25 gives twelve days from Helam to Zarahemla. A route of about 20 days therefore exists; it is not stated to be the shortest.",
                "Mosiah 7:4-5 gives forty days for Ammon's sixteen men, with the explicit reason that they 'knew not the course'. A lost party taking twice as long as a guided one is no conflict.",
                "Limhi's people and Mosiah's sons are both given only 'many days'. A 20-day route is a reasonable reading of 'many'.",
                "No triangle test is possible: no pair of these places has two independent day counts."],
        rows=[dict(label='Mormon to Helam: eight days', v=['MOSIAH 23:3']),
              dict(label='First day: to the valley of Alma', v=['MOSIAH 24:20']),
              dict(label='Wilderness to Zarahemla: twelve days', v=['MOSIAH 24:25']),
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
        summary="Three days to a valley by a river, four days south-southeast to Shazer, many days on 'nearly the same course' to Nahom, then 'nearly eastward' to Bountiful. The headings never double back.",
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
        id='X1', group='Cross-reference', verdict='minor tension',
        title='Where did the Mulekites first land?',
        summary="Alma 22:30 says the Jaredite bones land was 'the place of their first landing', and Helaman 6:10 says the Lord brought Mulek into the land north. Omni 1:16 says they crossed the waters 'into the land where Mosiah discovered them; and they had dwelt there from that time forth'.",
        detail=["Alma and Helaman put the first landing in the north, near Desolation. Omni reads most naturally as landing and dwelling in Zarahemla.",
                "A reconciliation exists: Omni 1:16 may compress an unrecorded migration south. Omni 1:21 also says Coriantumr 'was discovered by the people of Zarahemla', and Alma 22:30 says the bones land was 'discovered by the people of Zarahemla', so those people were in or near the north at some point.",
                "Nothing in the text states the migration, so this is a gap, not a contradiction."],
        rows=[dict(label='"the place of their first landing" (north, by Desolation)', v=['ALMA 22:30']),
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
        id='X4', group='Cross-reference', verdict='minor tension',
        title='The scouts: did they think they had found Zarahemla?',
        summary="Mosiah 8:8 says Limhi's scouts 'found not the land of Zarahemla'. Mosiah 21:26 says they found the bones land and, 'having supposed it to be the land of Zarahemla', went home.",
        detail=["This is a location-belief inconsistency in how the two verses describe the same trip. It is reconcilable: they did not find Zarahemla, but believed the ruined land to be it, which is what Mosiah 21:26 says.",
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
    return T
