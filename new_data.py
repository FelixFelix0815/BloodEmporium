from typing import List, Tuple, Dict

import requests

general_killer_perks = ["Bitter Murmur", "Deerstalker", "Distressing", "Hex: No One Escapes Death", "Insidious",
                        "Iron Grasp", "Monstrous Shrine", "Sloppy Butcher", "Spies from the Shadows", "Unrelenting",
                        "Whispers", "Shattered Hope", "Hex: Thrill of the Hunt"]

general_survivor_perks = ["Dark Sense", "Déjà Vu", "Hope", "Kindred", "Lightweight", "No One Left Behind",
                          "Plunderer's Instinct", "Premonition", "Resilience", "Slippery Meat", "Small Game",
                          "This Is Not Happening", "We'll Make It", "Spine Chill"]

survivorData: List[Tuple[str, str]] = [
    ("Dwight", "Dwight Fairfield"),
    ("Meg", "Meg Thomas"),
    ("Claudette", "Claudette Morel"),
    ("Jake", "Jake Park"),
    ("Nea", "Nea Karlsson"),
    ("Laurie", "Laurie Strode"),
    ("Ace", "Ace Visconti"),
    ("Bill", 'William "Bill" Overbeck'),
    ("Feng", "Feng Min"),
    ("David", "David King"),
    ("Quentin", "Quentin Smith"),
    ("Tapp", "Detective Tapp"),
    ("Kate", "Kate Denson"),
    ("Adam", "Adam Francis"),
    ("Jeff", "Jeff Johansen"),
    ("Jane", "Jane Romero"),
    ("Ash", "Ashley J. Williams"),
    ("Nancy", "Nancy Wheeler"),
    ("Steve", "Steve Harrington"),
    ("Yui", "Yui Kimura"),
    ("Zarina", "Zarina Kassir"),
    ("Cheryl", "Cheryl Mason"),
    ("Felix", "Felix Richter"),
    ("Elodie", "Élodie Rakoto"),
    ("Yun-Jin", "Yun-Jin Lee"),
    ("Jill", "Jill Valentine"),
    ("Leon", "Leon S. Kennedy"),
    ("Mikaela", "Mikaela Reid"),
    ("Jonah", "Jonah Vasquez"),
    ("Yoichi", "Yoichi Asakawa"),
    ("Haddie", "Haddie Kaur"),
    ("Ada", "Ada Wong"),
    ("Rebecca", "Rebecca Chambers"),
    ("Vittorio", "Vittorio Toscano"),
    ("Thalita", "Thalita Lyra"),
    ("Renato", "Renato Lyra"),
    ("Gabriel", "Gabriel Soma"),
    ("Nicolas", "Nicolas Cage"),
    ("Ellen", "Ellen Ripley"),
    ("Alan", "Alan Wake"),
    ("Sable", "Sable Ward"),
    ("Aestri", "Aestri Yazar"),
    ("Lara", "Lara Croft"),
    ("Trevor", "Trevor Belmont"),
    ("Taurie", "Taurie Cain"),
]

killerData: List[Tuple[str, str, str]] = [
    ("trapper", "Trapper", "Evan MacMillan"),
    ("wraith", "Wraith", "Philip Ojomo"),
    ("hillbilly", "Hillbilly", "Max Thompson Jr."),
    ("nurse", "Nurse", "Sally Smithson"),
    ("myers", "Shape", "Michael Myers"),
    ("hag", "Hag", "Lisa Sherwood"),
    ("doctor", "Doctor", "Herman Carter"),
    ("huntress", "Huntress", "Anna"),
    ("bubba", "Cannibal", "Bubba Sawyer"),
    ("freddy", "Nightmare", "Freddy Krueger"),
    ("pig", "Pig", "Amanda Young"),
    ("clown", "Clown", "Jeffrey Hawk"),
    ("spirit", "Spirit", "Rin Yamaoka"),
    ("legion", "Legion", "Frank, Julie, Susie, Joey"),
    ("plague", "Plague", "Adiris"),
    ("ghostface", "Ghost Face", "Danny Johnson"),
    ("demogorgon", "Demogorgon", "Demogorgon"),
    ("oni", "Oni", "Kazan Yamaoka"),
    ("deathslinger", "Deathslinger", "Caleb Quinn"),
    ("pyramidhead", "Executioner", "Pyramid Head"),
    ("blight", "Blight", "Talbot Grimes"),
    ("twins", "Twins", "Charlotte & Victor Deshayes"),
    ("trickster", "Trickster", "Ji-Woon Hak"),
    ("nemesis", "Nemesis", "Nemesis T-Type"),
    ("cenobite", "Cenobite", "Elliot Spencer"),
    ("artist", "Artist", "Carmina Mora"),
    ("onryo", "Onryō", "Sadako Yamamura"),
    ("dredge", "Dredge", "Dredge"),
    ("mastermind", "Mastermind", "Albert Wesker"),
    ("knight", "Knight", "Tarhocs Kovács"),
    ("skull merchant", "Skull Merchant", "Adriana Imai"),
    ("singularity", "Singularity", "HUX-A7-13"),
    ("xenomorph", "Xenomorph", "Xenomorph"),
    ("good guy", "Good Guy", "Charles Lee Ray"),
    ("unknown", "Unknown", "Unknown"),
    ("lich", "Lich", "Vecna"),
    ("dark lord", "Dark Lord", "Dracula"),
    ("houndmaster", "Houndmaster", "Portia Maye")
]

killerPerkMap: Dict[str, List[str]] = {
    'trapper': ['Unnerving Presence', 'Brutal Strength', 'Agitation'],
    'wraith': ['Predator', 'Bloodhound', 'Shadowborn'],
    'hillbilly': ['Enduring', 'Lightborn', 'Tinkerer'],
    'nurse': ['Stridor', 'Thanatophobia', "A Nurse's Calling"],
    'myers': ['Play with Your Food', 'Save the Best for Last', 'Dying Light'],
    'hag': ['Hex: The Third Seal', 'Hex: Ruin', 'Hex: Devour Hope'],
    'doctor': ['Overcharge', 'Monitor & Abuse', 'Overwhelming Presence'],
    'bubba': ['Knock Out', 'Barbecue & Chilli', "Franklin's Demise"],
    'huntress': ['Beast of Prey', 'Territorial Imperative', 'Hex: Huntress Lullaby'],
    'freddy': ['Fire Up', 'Remember Me', 'Blood Warden'],
    'pig': ["Scourge Hook: Hangman's Trick", 'Surveillance', 'Make Your Choice'],
    'clown': ['Bamboozle', 'Coulrophobia', 'Pop Goes the Weasel'],
    'spirit': ['Spirit Fury', 'Hex: Haunted Ground', 'Rancor'],
    'legion': ['Discordance', 'Mad Grit', 'Iron Maiden'],
    'plague': ['Corrupt Intervention', 'Infectious Fright', 'Dark Devotion'],
    'ghostface': ["I'm All Ears", 'Thrilling Tremors', 'Furtive Chase'],
    'demogorgon': ['Surge', 'Cruel Limits', 'Mindbreaker'],
    'oni': ['Zanshin Tactics', 'Blood Echo', 'Nemesis'],
    'deathslinger': ['Gearhead', "Dead Man's Switch", 'Hex: Retribution'],
    'pyramidhead': ['Forced Penance', 'Trail of Torment', 'Deathbound'],
    'blight': ["Dragon's Grip", 'Hex: Undying', 'Hex: Blood Favour'],
    'twins': ['Hoarder', 'Oppression', 'Coup de Grâce'],
    'trickster': ['Starstruck', 'Hex: Crowd Control', 'No Way Out'],
    'nemesis': ['Lethal Pursuer', 'Hysteria', 'Eruption'],
    'cenobite': ['Deadlock', 'Hex: Plaything', 'Scourge Hook: Gift of Pain'],
    'artist': ['Grim Embrace', 'Scourge Hook: Pain Resonance', 'Hex: Pentimento'],
    'onryo': ['Scourge Hook: Floods of Rage', 'Call of Brine', 'Merciless Storm'],
    'dredge': ['Dissolution', 'Darkness Revealed', 'Septic Touch'],
    'mastermind': ['Superior Anatomy', 'Awakened Awareness', 'Terminus'],
    'knight': ['Nowhere to Hide', 'Hex: Face the Darkness', 'Hubris'],
    'skull merchant': ['Game Afoot', 'THWACK!', 'Leverage'],
    'singularity': ['Genetic Limits', 'Forced Hesitation', 'Machine Learning'],
    'xenomorph': ['Ultimate Weapon', 'Rapid Brutality', 'Alien Instinct'],
    'good guy': ['Hex: Two Can Play', "Friends 'til the End", 'Batteries Included'],
    'unknown': ['Unbound', 'Unforeseen', 'Undone'],
    'lich': ['Weave Attunement', 'Languid Touch', 'Dark Arrogance'],
    'dark lord': ['Hex: Wretched Fate', 'Human Greed', 'Dominance'],
    'houndmaster': ['All-Shaking Thunder', 'Scourge Hook: Jagged Compass', 'No Quarter'],
}

survivorPerkMap: Dict[str, List[str]] = {
    'dwight': ['Bond', 'Leader', 'Prove Thyself'],
    'meg': ['Quick & Quiet', 'Sprint Burst', 'Adrenaline'],
    'claudette': ['Empathy', 'Botany Knowledge', 'Self-Care'],
    'jake': ['Iron Will', 'Calm Spirit', 'Saboteur'],
    'nea': ['Balanced Landing', 'Urban Evasion', 'Streetwise'],
    'bill': ['Left Behind', 'Borrowed Time', 'Unbreakable'],
    'laurie': ['Sole Survivor', 'Object of Obsession', 'Decisive Strike'],
    'ace': ['Open-Handed', 'Up the Ante', 'Ace in the Hole'],
    'feng': ['Technician', 'Lithe', 'Alert'],
    'david': ["We're Gonna Live Forever", 'Dead Hard', 'No Mither'],
    'quentin': ['Wake Up!', 'Pharmacy', 'Vigil'],
    'tapp': ['Tenacity', "Detective's Hunch", 'Stake Out'],
    'kate': ['Dance With Me', 'Windows of Opportunity', 'Boil Over'],
    'adam': ['Diversion', 'Deliverance', 'Autodidact'],
    'jeff': ['Breakdown', 'Aftercare', 'Distortion'],
    'jane': ['Solidarity', 'Poised', 'Head On'],
    'ash': ['Flip-Flop', 'Buckle Up', 'Mettle of Man'],
    'nancy': ['Better Together', 'Fixated', 'Inner Strength'],
    'steve': ['Babysitter', 'Camaraderie', 'Second Wind'],
    'yui': ['Lucky Break', 'Any Means Necessary', 'Breakout'],
    'zarina': ['Off the Record', 'Red Herring', 'For the People'],
    'cheryl': ['Soul Guard', 'Blood Pact', 'Repressed Alliance'],
    'felix': ['Visionary', 'Desperate Measures', 'Built to Last'],
    'elodie': ['Appraisal', 'Deception', 'Power Struggle'],
    'yun-jin': ['Fast Track', 'Smash Hit', 'Self-Preservation'],
    'jill': ['Counterforce', 'Resurgence', 'jine'],
    'leon': ['Bite the Bullet', 'Flashbang', 'Rookie Spirit'],
    'mikaela': ['Clairvoyance', 'Boon: Circle of Healing', 'Boon: Shadow Step'],
    'jonah': ['Overcome', 'Corrective Action', 'Boon: Exponential'],
    'yoichi': ['Parental Guidance', 'Empathic Connection', 'Boon: Dark Theory'],
    'haddie': ['Inner Focus', 'Residual Manifest', 'Overzealous'],
    'ada': ['Wiretap', 'Reactive Healing', 'Low Profile'],
    'rebecca': ['Better than New', 'Reassurance', 'Hyperfocus'],
    'vittorio': ['Potential Energy', 'Fogwise', 'Quick Gambit'],
    'thalita': ['Cut Loose', 'Friendly Competition', 'Teamwork: Power of Two'],
    'renato': ['Background Player', 'Blood Rush', 'Teamwork: Collective Stealth'],
    'gabriel': ['Troubleshooter', 'Made for This', 'Scavenger'],
    'nicolas': ['Dramaturgy', 'Scene Partner', 'Plot Twist'],
    'ellen': ['Lucky Star', 'Chemical Trap', 'Light-Footed'],
    'alan': ['Champion of Light', 'Boon: Illumination', 'Deadline'],
    'sable': ['Invocation: Weaving Spiders', 'Strength in Shadows', 'Wicked'],
    'aestri': ['Mirrored Illusion', 'Bardic Inspiration', 'Still Sight'],
    'lara': ['Finesse', 'Specialist', 'Hardened'],
    'trevor': ['Eyes of Belmont', 'Exultation', 'Moment of Glory'],
    'taurie': ['Invocation: Treacherous Crows', 'Clean Break', 'Shoulder the Burden']
}


class FetchedData:

    @property
    def survivorPerkMap(self) -> Dict[str, List[str]]:
        survivors_url = "https://dbd.tricky.lol/api/characters?role=survivor"
        perk_url = "https://dbd.tricky.lol/api/perks"
        survivors_response = requests.get(survivors_url)
        perk_response = requests.get(perk_url)
        remoteSurvivors = survivors_response.json()
        remotePerks = perk_response.json()

        survivor_perk_map: Dict[str, List[str]] = {}

        for perk_name in remotePerks:
            perk_data = remotePerks[perk_name]
            if perk_data["role"] != "survivor" or perk_data["character"] is None:
                continue

            char = remoteSurvivors[perk_data["character"]]
            local_alias = [surv for surv in survivorData if surv[1] == char["name"]][0][0]

            current_url = f'https://dbd.tricky.lol/api/perkinfo?perk={perk_name}'
            current_response = requests.get(current_url)
            current_data = current_response.json()

            survivor_perk_map.setdefault(local_alias, []).append(current_data["name"])

        return survivor_perk_map

    @property
    def killerPerkMap(self) -> Dict[str, List[str]]:
        killer_url = "https://dbd.tricky.lol/api/characters?role=killer"
        perk_url = "https://dbd.tricky.lol/api/perks"
        killer_response = requests.get(killer_url)
        perk_response = requests.get(perk_url)
        remoteKillers = killer_response.json()
        remotePerks = perk_response.json()

        killer_perk_map: Dict[str, List[str]] = {}

        for perk_name in remotePerks:
            perk_data = remotePerks[perk_name]
            if perk_data["role"] != "killer" or perk_data["character"] is None:
                continue

            char = remoteKillers[str(perk_data["character"])]
            local_alias = [killer for killer in killerData if killer[1] == char["name"][4:]][0][0]

            current_url = f'https://dbd.tricky.lol/api/perkinfo?perk={perk_name}'
            current_response = requests.get(current_url)
            current_data = current_response.json()

            killer_perk_map.setdefault(local_alias, []).append(current_data["name"])

        return killer_perk_map
