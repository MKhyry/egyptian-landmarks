"""
data/landmarks_data.py
======================
PURPOSE: Pure data file — contains all Egyptian landmark info.
         No database logic here. Just a Python list of dictionaries.

HOW IT CONNECTS:
  scripts/seed_landmarks.py  →  imports LANDMARKS from this file
                             →  inserts each entry into MongoDB

HOW TO ADD A NEW LANDMARK:
  1. Add a new dict to the LANDMARKS list below
  2. Make sure landmark_id matches your dataset folder name exactly
  3. Run:  python scripts/seed_landmarks.py

landmark_id naming rule:
  dataset folder name → landmark_id
  "karnak_temple/"    → "karnak_temple"
  "abu_simbel/"       → "abu_simbel"
  All lowercase, underscores, no spaces.
"""


    # ══════════════════════════════════════════════════════════════════════
    # TEMPLATE — copy and fill this for each landmark you add
    # ══════════════════════════════════════════════════════════════════════
    # {
    #     "landmark_id": "your_folder_name",
    #     "name": "Display Name",
    #     "arabic_name": "الاسم بالعربي",
    #     "location": "City, Governorate, Egypt",
    #     "governorate": "Governorate name",
    #     "coordinates": {"lat": 0.0, "lng": 0.0},
    #     "built_year": "~XXXX BCE",
    #     "dynasty": "Xth Dynasty",
    #     "pharaoh": "Pharaoh Name",
    #     "period": "Historical Period",
    #     "landmark_type": "pyramid / temple / tomb / mosque / fortress / museum",
    #     "unesco_listed": True / False,
    #     "description": "Main description paragraph...",
    #     "historical_facts": [
    #         "Fact one",
    #         "Fact two",
    #         ...
    #     ],
    #     "gallery_images": [
    #         "/gallery/your_folder_name/1.jpg",
    #         "/gallery/your_folder_name/2.jpg",
    #     ],
    #     "thumbnail": "/gallery/your_folder_name/1.jpg",
    #     "tags": ["tag1", "tag2"],
    #     "visitor_info": {
    #         "open_hours": "8:00 AM – 5:00 PM",
    #         "entry_fee_egp": 160,
    #         "entry_fee_usd_approx": 3.3,
    #         "best_time": "October to April",
    #         "nearest_city": "Cairo",
    #         "tips": "Arrive early to avoid crowds."
    #     },
    # },


    # ══════════════════════════════════════════════════════════════════════
    # YOUR LANDMARKS GO HERE — share the names and I will fill these in
    # ══════════════════════════════════════════════════════════════════════

    # {
    #     "landmark_id": "PLACEHOLDER_1",
    #     ...
    # },


LANDMARKS = [
    # ─────────────────────────────────────────────────────────────────────
    # 1. Abu Simbel Temple
    # ─────────────────────────────────────────────────────────────────────
    {
        "landmark_id": "abu_simbel_temple",
        "name": "Abu Simbel Temple",
        "arabic_name": "معبد أبو سمبل",
        "location": "Abu Simbel, Aswan Governorate, Southern Egypt",
        "governorate": "Aswan",
        "coordinates": {"lat": 22.3372, "lng": 31.6258},
        "built_year": "~1264 BCE",
        "dynasty": "19th Dynasty",
        "pharaoh": "Ramesses II",
        "period": "New Kingdom",
        "landmark_type": "temple",
        "unesco_listed": True,
        "description": (
            "Abu Simbel is one of Egypt's most awe-inspiring ancient sites, consisting of two "
            "massive rock-cut temples carved directly into a sandstone cliff on the western "
            "bank of Lake Nasser. Commissioned by Pharaoh Ramesses II to celebrate his "
            "claimed victory at the Battle of Kadesh and to intimidate his Nubian neighbors, "
            "the Great Temple is guarded by four colossal 20-meter seated statues of Ramesses "
            "himself. The smaller temple beside it was dedicated to his beloved queen, "
            "Nefertari, and the goddess Hathor. In one of the greatest feats of modern "
            "archaeological engineering, both temples were painstakingly dismantled and "
            "relocated 65 meters uphill between 1964 and 1968 to save them from the rising "
            "waters of Lake Nasser created by the Aswan High Dam."
        ),
        "historical_facts": [
            "The four colossal seated statues of Ramesses II at the Great Temple entrance each stand 20 meters tall",
            "Twice a year, on February 22 and October 22, sunlight penetrates 65 meters into the inner sanctuary and illuminates the statues of Ramesses and two gods — the fourth statue of Ptah, god of darkness, remains in shadow",
            "The relocation project (1964–1968) cost approximately $80 million USD, equivalent to around $700 million today",
            "The temples were cut into over 1,000 numbered blocks and reassembled with millimeter precision on an artificial hill",
            "The smaller Temple of Nefertari is one of only two temples in ancient Egypt dedicated to a queen",
            "Abu Simbel was unknown to the outside world until Swiss explorer Johann Ludwig Burckhardt rediscovered it in 1813",
            "The site was a UNESCO World Heritage Site even before the relocation — the rescue operation became a model for international heritage preservation",
        ],
        "tags": ["ramesses", "rock-cut", "aswan", "UNESCO", "colossal", "nefertari", "nubia", "new kingdom"],
        "visitor_info": {
            "open_hours": "5:00 AM – 6:00 PM",
            "entry_fee_egp": 360,
            "best_time": "February 22 or October 22 for the sun alignment phenomenon",
            "nearest_city": "Aswan",
            "tips": "Most visitors fly from Aswan (45 min) or join an overnight bus tour. Arrive early to avoid crowds.",
        },
    },

    # ─────────────────────────────────────────────────────────────────────
    # 2. Agiba Beach
    # ─────────────────────────────────────────────────────────────────────
    {
        "landmark_id": "agiba_beach",
        "name": "Agiba Beach",
        "arabic_name": "شاطئ عجيبة",
        "location": "Marsa Matrouh, North Coast, Egypt",
        "governorate": "Matrouh",
        "coordinates": {"lat": 31.3167, "lng": 27.1833},
        "built_year": None,
        "dynasty": None,
        "pharaoh": None,
        "period": "Natural landmark",
        "landmark_type": "natural",
        "unesco_listed": False,
        "description": (
            "Agiba Beach, whose name means 'miracle' or 'wonder' in Arabic, is widely "
            "regarded as one of the most spectacular natural beaches on Egypt's Mediterranean "
            "coast. Situated about 24 kilometers west of Marsa Matrouh, the beach is nestled "
            "inside a dramatic rocky cove, accessible only by descending a narrow stone "
            "staircase carved into the limestone cliffs. The crystal-clear turquoise waters, "
            "sheltered by towering white and ochre rock formations on three sides, create "
            "an almost enclosed lagoon of extraordinary beauty. The isolation of the beach "
            "means it remains far less crowded than other Mediterranean resorts, and the "
            "surrounding cliffs glow in shades of white, beige, and gold, particularly "
            "striking at sunset."
        ),
        "historical_facts": [
            "The name 'Agiba' (عجيبة) means 'miracle' or 'wonder' in Arabic, reflecting the stunning natural scenery",
            "The beach is accessible only via a steep staircase cut into the cliff face, which limits visitor numbers and preserves its natural character",
            "The area around Marsa Matrouh was the site of major World War II battles between Allied and Axis forces in 1942",
            "The nearby town of Marsa Matrouh was historically known as Amunia in ancient times and served as a resort for Egyptian royalty",
            "The limestone cliffs surrounding Agiba are part of the same geological formation that creates the famous White Desert further inland",
            "The beach is known for its exceptionally calm and transparent water, with visibility reaching several meters below the surface",
        ],
        "tags": ["beach", "mediterranean", "matrouh", "nature", "coastal", "turquoise", "cliffs"],
        "visitor_info": {
            "open_hours": "Open daily, daylight hours",
            "entry_fee_egp": 20,
            "best_time": "June to September for swimming; avoid peak summer weekends",
            "nearest_city": "Marsa Matrouh",
            "tips": "Wear rubber shoes for the rocky descent. Bring your own shade — no facilities on the beach itself.",
        },
    },

    # ─────────────────────────────────────────────────────────────────────
    # 3. Bibliotheca Alexandrina
    # ─────────────────────────────────────────────────────────────────────
    {
        "landmark_id": "bibliotheca_alexandrina",
        "name": "Bibliotheca Alexandrina",
        "arabic_name": "مكتبة الإسكندرية",
        "location": "Corniche, Alexandria, Egypt",
        "governorate": "Alexandria",
        "coordinates": {"lat": 31.2089, "lng": 29.9092},
        "built_year": "2002 CE (opened)",
        "dynasty": None,
        "pharaoh": None,
        "period": "Modern",
        "landmark_type": "museum",
        "unesco_listed": False,
        "description": (
            "The Bibliotheca Alexandrina is a spectacular modern library and cultural center "
            "built on the site of the legendary ancient Library of Alexandria, once the "
            "greatest repository of knowledge in the ancient world. Inaugurated in 2002, "
            "the building was designed by the Norwegian architectural firm Snøhetta and is "
            "immediately recognizable by its tilted circular roof, measuring 160 meters in "
            "diameter, covered in panels inscribed with characters from 120 different writing "
            "systems of the world. The library can hold up to 8 million books and houses "
            "several specialized museums, research institutes, art galleries, a planetarium, "
            "and a manuscript restoration lab. It stands as both a tribute to the ancient "
            "library destroyed by fire and a bold statement of Egypt's cultural ambitions "
            "for the 21st century."
        ),
        "historical_facts": [
            "The original Library of Alexandria was founded around 295 BCE under Ptolemy I and was the largest library in the ancient world",
            "The ancient library's destruction — whether by Julius Caesar's fire, later Roman edicts, or Arab conquest — remains one of history's great scholarly debates",
            "The modern building was designed by Norwegian firm Snøhetta, winning an international competition in 1989",
            "The circular roof is inscribed with characters from 120 different writing systems representing human knowledge across civilizations",
            "The main reading room can accommodate 2,000 readers simultaneously across eleven cascading terraces",
            "The library houses six specialized libraries, four museums, four art galleries, fifteen permanent exhibitions, and a planetarium",
            "Construction cost approximately $220 million USD, funded jointly by Egypt, UNESCO, and international donors",
        ],
        "tags": ["library", "alexandria", "modern", "culture", "knowledge", "architecture", "mediterranean"],
        "visitor_info": {
            "open_hours": "Saturday–Thursday 10:00 AM – 7:00 PM, Friday 2:00 PM – 7:00 PM",
            "entry_fee_egp": 70,
            "best_time": "Weekday mornings for a quieter experience",
            "nearest_city": "Alexandria",
            "tips": "The planetarium and manuscript museum require separate tickets. Allow at least 3 hours for a full visit.",
        },
    },

    # ─────────────────────────────────────────────────────────────────────
    # 4. Cairo Tower
    # ─────────────────────────────────────────────────────────────────────
    {
        "landmark_id": "cairo_tower",
        "name": "Cairo Tower",
        "arabic_name": "برج القاهرة",
        "location": "Gezira Island, Cairo, Egypt",
        "governorate": "Cairo",
        "coordinates": {"lat": 30.0444, "lng": 31.2243},
        "built_year": "1961 CE",
        "dynasty": None,
        "pharaoh": None,
        "period": "Modern",
        "landmark_type": "tower",
        "unesco_listed": False,
        "description": (
            "Cairo Tower is a freestanding concrete lattice tower standing 187 meters tall "
            "on Gezira Island in the Nile River, making it the tallest structure in Egypt "
            "and all of North Africa for over four decades after its construction. Designed "
            "by Egyptian architect Naoum Shebib and completed in 1961 under President Gamal "
            "Abdel Nasser, the tower's exterior is clad in carved concrete panels in the "
            "form of a lotus plant, Egypt's ancient national symbol. At its summit, the "
            "tower features a revolving restaurant and an open-air observation deck that "
            "offers a sweeping 360-degree panorama of Cairo — from the Giza pyramids shimmering "
            "on the western horizon to the minarets of Islamic Cairo in the east, and the "
            "green ribbon of the Nile winding through the city below."
        ),
        "historical_facts": [
            "At 187 meters, Cairo Tower was the tallest structure in Africa from its completion in 1961 until the early 2000s",
            "The tower's lattice exterior is modeled on the lotus flower, a powerful symbol in ancient Egyptian iconography representing creation and rebirth",
            "It was built using $3 million reportedly received from the American CIA as a bribe to President Nasser — Nasser publicly used the money to build the tower as a deliberate insult",
            "Egyptian architect Naoum Shebib designed the tower inspired by pharaonic motifs while embracing modernist concrete construction",
            "The revolving restaurant at the top completes a full rotation in approximately 70 minutes",
            "On a clear day, the pyramids of Giza are clearly visible from the observation deck 30 kilometers to the southwest",
        ],
        "tags": ["tower", "cairo", "modern", "nile", "panorama", "observation", "architecture"],
        "visitor_info": {
            "open_hours": "9:00 AM – 1:00 AM (midnight)",
            "entry_fee_egp": 150,
            "best_time": "Sunset for golden light over the Nile, or after dark for city lights",
            "nearest_city": "Cairo",
            "tips": "The elevator is fast but queues form on weekends. The revolving restaurant requires a separate reservation.",
        },
    },

    # ─────────────────────────────────────────────────────────────────────
    # 5. Egyptian Museum
    # ─────────────────────────────────────────────────────────────────────
    {
        "landmark_id": "egyptian_museum",
        "name": "Egyptian Museum",
        "arabic_name": "المتحف المصري",
        "location": "Tahrir Square, Cairo, Egypt",
        "governorate": "Cairo",
        "coordinates": {"lat": 30.0478, "lng": 31.2336},
        "built_year": "1902 CE",
        "dynasty": None,
        "pharaoh": None,
        "period": "Modern (houses ancient artifacts)",
        "landmark_type": "museum",
        "unesco_listed": False,
        "description": (
            "The Egyptian Museum in Cairo, also known as the Museum of Egyptian Antiquities, "
            "is the oldest and most storied archaeological museum in the world dedicated to "
            "ancient Egyptian history. Housed in a grand neo-classical pink building on the "
            "northern edge of Tahrir Square, the museum opened in 1902 and today holds over "
            "170,000 artifacts spanning more than 5,000 years of Egyptian civilization. Its "
            "most celebrated treasure is the complete contents of Tutankhamun's intact tomb, "
            "including the iconic solid gold death mask weighing 11 kilograms. Visitors move "
            "through rooms dense with royal mummies, colossal statues, jeweled sarcophagi, "
            "painted papyrus scrolls, and delicate ceremonial objects — an overwhelming "
            "testament to the sophistication of ancient Egyptian culture."
        ),
        "historical_facts": [
            "The museum holds over 170,000 artifacts, of which only about 50,000 are on permanent display — the rest are in storage",
            "Tutankhamun's solid gold death mask weighs 11 kilograms and is made of 22-karat gold inlaid with lapis lazuli, quartz, and obsidian",
            "The Royal Mummy Room houses 27 royal mummies including Ramesses II, Seti I, and Queen Hatshepsut",
            "The building itself was designed by French architect Marcel Dourgnon and opened in 1902, replacing an earlier museum in Bulaq",
            "Howard Carter donated many Tutankhamun artifacts to the museum after the 1922 discovery",
            "The museum was targeted during the 2011 revolution; some artifacts were damaged or stolen but most were recovered",
            "Many of its most famous artifacts are being transferred to the new Grand Egyptian Museum at Giza",
        ],
        "tags": ["museum", "cairo", "tutankhamun", "mummies", "tahrir", "artifacts", "ancient"],
        "visitor_info": {
            "open_hours": "9:00 AM – 5:00 PM daily",
            "entry_fee_egp": 200,
            "best_time": "Weekday mornings before tour groups arrive",
            "nearest_city": "Cairo",
            "tips": "The Royal Mummy Room and Tutankhamun galleries require an additional ticket. Photography inside requires a camera ticket.",
        },
    },

    # ─────────────────────────────────────────────────────────────────────
    # 6. Grand Egyptian Museum
    # ─────────────────────────────────────────────────────────────────────
    {
        "landmark_id": "grand_egyptian_museum",
        "name": "Grand Egyptian Museum",
        "arabic_name": "المتحف المصري الكبير",
        "location": "Giza Plateau, Cairo, Egypt",
        "governorate": "Giza",
        "coordinates": {"lat": 29.9883, "lng": 31.1134},
        "built_year": "2023 CE (soft opening)",
        "dynasty": None,
        "pharaoh": None,
        "period": "Modern (houses ancient artifacts)",
        "landmark_type": "museum",
        "unesco_listed": False,
        "description": (
            "The Grand Egyptian Museum, known as GEM, is the largest archaeological museum "
            "in the world, purpose-built on 117 acres adjacent to the Giza Plateau with a "
            "direct view of the pyramids. Designed by the Irish firm Heneghan Peng Architects "
            "after winning an international competition in 2002, the museum's translucent "
            "stone facade filters natural light into its vast galleries like sunlight through "
            "alabaster. The centerpiece of the museum is the complete Tutankhamun collection "
            "— all 5,398 objects from the boy king's tomb displayed together for the first "
            "time since their discovery in 1922. The entrance atrium is dominated by a "
            "massive 11-meter quartzite statue of Ramesses II, relocated from central Cairo. "
            "With over 100,000 artifacts on display across 90 exhibition halls, GEM represents "
            "Egypt's most ambitious cultural infrastructure project in a century."
        ),
        "historical_facts": [
            "At over 480,000 square meters of total area, GEM is the largest museum in the world dedicated to a single civilization",
            "The museum cost approximately $1 billion USD to construct and equip over more than two decades",
            "All 5,398 objects from Tutankhamun's tomb are displayed together here for the very first time since 1922",
            "The 11-meter quartzite statue of Ramesses II in the atrium was relocated from Ramesses Square in central Cairo in 2006",
            "The translucent exterior panels are made from Egyptian alabaster, allowing natural light to diffuse through the facade",
            "The museum sits 2 kilometers from the Great Pyramid, offering panoramic pyramid views from its terrace",
            "Construction began in 2012; a partial soft opening was held in 2023 with the full museum opening to follow",
        ],
        "tags": ["museum", "giza", "tutankhamun", "modern", "largest", "artifacts", "ramesses"],
        "visitor_info": {
            "open_hours": "9:00 AM – 9:00 PM daily",
            "entry_fee_egp": 600,
            "best_time": "Weekday mornings; evenings for a quieter experience with pyramid views",
            "nearest_city": "Cairo / Giza",
            "tips": "Book tickets online in advance. The Tutankhamun galleries and the Children's Museum require separate tickets.",
        },
    },

    # ─────────────────────────────────────────────────────────────────────
    # 7. Great Sphinx
    # ─────────────────────────────────────────────────────────────────────
    {
        "landmark_id": "great_sphinx",
        "name": "Great Sphinx of Giza",
        "arabic_name": "أبو الهول",
        "location": "Giza Plateau, Cairo, Egypt",
        "governorate": "Giza",
        "coordinates": {"lat": 29.9753, "lng": 31.1376},
        "built_year": "~2500 BCE",
        "dynasty": "4th Dynasty",
        "pharaoh": "Khafre",
        "period": "Old Kingdom",
        "landmark_type": "statue",
        "unesco_listed": True,
        "description": (
            "The Great Sphinx of Giza is the largest monolithic statue on Earth — a "
            "reclining lion with the head of a human, carved entirely from a single ridge "
            "of natural limestone bedrock on the Giza Plateau. Measuring 73 meters in length, "
            "20 meters in height, and 19 meters in width, it faces due east toward the "
            "rising sun and is believed to represent Pharaoh Khafre, whose pyramid rises "
            "directly behind it. The Sphinx serves as the eternal guardian of the Giza "
            "necropolis, watching over the pyramids and the mortuary temples of the 4th "
            "Dynasty pharaohs. For much of its existence it lay buried to the shoulders in "
            "desert sand, and the 'Dream Stele' erected between its paws by Thutmose IV "
            "around 1401 BCE recounts his vision of the Sphinx promising him the throne "
            "of Egypt in exchange for clearing the sand."
        ),
        "historical_facts": [
            "At 73 meters long and 20 meters tall, the Great Sphinx is the largest monolithic statue ever created",
            "The entire statue was carved from a single limestone ridge that was already present in the Giza Plateau quarry",
            "For centuries the Sphinx was buried up to its neck in sand; Thutmose IV partially excavated it around 1401 BCE",
            "The missing nose was NOT shot off by Napoleon's soldiers — drawings from 1737, decades before Napoleon, already show it absent",
            "The Sphinx faces precisely due east, aligning with the rising sun at the spring and autumn equinoxes",
            "The 'Dream Stele' between its paws, placed by Thutmose IV, is one of the earliest recorded examples of a restoration project",
            "Erosion patterns on the Sphinx's body have led some geologists to propose it may be far older than 2500 BCE, though most Egyptologists disagree",
        ],
        "tags": ["sphinx", "giza", "ancient", "statue", "old kingdom", "khafre", "UNESCO", "limestone"],
        "visitor_info": {
            "open_hours": "8:00 AM – 5:00 PM daily",
            "entry_fee_egp": 160,
            "best_time": "Early morning before tour buses; evening sound-and-light show",
            "nearest_city": "Cairo / Giza",
            "tips": "Included in the Giza Plateau ticket. The sound and light show runs nightly and narrates the Sphinx's story.",
        },
    },

    # ─────────────────────────────────────────────────────────────────────
    # 8. Hatshepsut Temple
    # ─────────────────────────────────────────────────────────────────────
    {
        "landmark_id": "hatshepsut_temple",
        "name": "Hatshepsut Temple",
        "arabic_name": "معبد حتشبسوت",
        "location": "Deir el-Bahari, West Bank of Luxor, Upper Egypt",
        "governorate": "Luxor",
        "coordinates": {"lat": 25.7380, "lng": 32.6073},
        "built_year": "~1479–1458 BCE",
        "dynasty": "18th Dynasty",
        "pharaoh": "Hatshepsut",
        "period": "New Kingdom",
        "landmark_type": "temple",
        "unesco_listed": True,
        "description": (
            "The Mortuary Temple of Hatshepsut, known as Djeser-Djeseru meaning 'Holy of "
            "Holies,' is one of the greatest architectural achievements of ancient Egypt, "
            "rising in three magnificent colonnaded terraces against the sheer limestone "
            "cliffs of Deir el-Bahari on Luxor's west bank. Built for the only female "
            "pharaoh to rule Egypt in her own right, Queen Hatshepsut, the temple seamlessly "
            "integrates with the natural rock face behind it in a design far ahead of its "
            "time. Its walls are covered with brightly painted reliefs depicting Hatshepsut's "
            "divine birth — portraying her as the daughter of the god Amun — her famous "
            "trading expedition to the Land of Punt, and elaborate funerary rites. After "
            "her death, her successor Thutmose III attempted to erase her memory by defacing "
            "her images and name throughout the temple, though many survived."
        ),
        "historical_facts": [
            "Hatshepsut was Egypt's most successful female pharaoh, ruling for approximately 20 years from around 1479 to 1458 BCE",
            "The temple's design by architect Senenmut is considered one of the finest examples of ancient Egyptian architecture",
            "Hatshepsut dressed in male pharaonic regalia including a false beard and was depicted as a man in many official images",
            "The Punt expedition reliefs show the first detailed depiction of a foreign land in Egyptian art, including trees, animals, and the Queen of Punt",
            "Thutmose III later defaced and removed Hatshepsut's image and name from the temple in an effort to erase her from history",
            "The temple was converted into a Christian monastery called Deir el-Bahari ('Monastery of the North') in early Christian times",
            "In 1997, 62 tourists were massacred at the temple by Islamic extremists in one of Egypt's worst modern terrorist attacks",
        ],
        "tags": ["temple", "hatshepsut", "female pharaoh", "luxor", "new kingdom", "UNESCO", "colonnade"],
        "visitor_info": {
            "open_hours": "6:00 AM – 5:00 PM daily",
            "entry_fee_egp": 200,
            "best_time": "Early morning before the sun reflects off the cliffs; the light at 7–9 AM is spectacular",
            "nearest_city": "Luxor",
            "tips": "Combine with the Valley of the Kings on the same day — both are on the west bank. Take the ferry across the Nile from Luxor city.",
        },
    },

    # ─────────────────────────────────────────────────────────────────────
    # 9. High Dam (Aswan High Dam)
    # ─────────────────────────────────────────────────────────────────────
    {
        "landmark_id": "high_dam",
        "name": "Aswan High Dam",
        "arabic_name": "السد العالي",
        "location": "Aswan, Upper Egypt",
        "governorate": "Aswan",
        "coordinates": {"lat": 23.9700, "lng": 32.8772},
        "built_year": "1970 CE",
        "dynasty": None,
        "pharaoh": None,
        "period": "Modern",
        "landmark_type": "engineering",
        "unesco_listed": False,
        "description": (
            "The Aswan High Dam is one of the greatest engineering achievements of the "
            "20th century and a defining symbol of modern Egypt. Stretching 3,830 meters "
            "across the Nile River near Aswan, the dam was constructed between 1960 and "
            "1970 with Soviet technical and financial assistance under President Gamal "
            "Abdel Nasser. The dam created Lake Nasser, the world's largest artificial "
            "reservoir by surface area, stretching over 500 kilometers into Sudan. It "
            "transformed Egypt's economy by enabling year-round irrigation of agricultural "
            "land, protecting against the catastrophic annual Nile floods, and generating "
            "the hydroelectric power that electrified Egyptian cities and villages. However, "
            "its construction necessitated the displacement of over 100,000 Nubian people "
            "and the submersion of dozens of ancient monuments — prompting the UNESCO-led "
            "rescue of Abu Simbel and other temples."
        ),
        "historical_facts": [
            "The dam is 3,830 meters long, 111 meters high, and 980 meters wide at its base",
            "Construction employed approximately 30,000 Egyptian workers and was completed in 1970",
            "Lake Nasser holds approximately 169 cubic kilometers of water — one of the world's largest artificial reservoirs",
            "The dam's 12 Soviet-supplied turbines generate 2,100 megawatts of electricity, which in the 1970s provided half of Egypt's total electricity",
            "Over 100,000 Nubian people were displaced from their ancestral homelands, which were submerged under Lake Nasser",
            "The UNESCO campaign to save Nubian monuments led to the relocation of 24 ancient temples, including Abu Simbel",
            "Before the dam, the annual Nile flood destroyed crops and killed thousands; the dam ended millennia of destructive flooding",
        ],
        "visitor_info": {
            "open_hours": "7:00 AM – 5:00 PM daily",
            "entry_fee_egp": 35,
            "best_time": "Morning, combined with a Nile cruise or visit to Philae Temple",
            "nearest_city": "Aswan",
            "tips": "Photography of the dam structure is permitted from the visitor overlook. Military zones nearby are strictly off-limits.",
        },
    },

    # ─────────────────────────────────────────────────────────────────────
    # 10. Hurghada
    # ─────────────────────────────────────────────────────────────────────
    {
        "landmark_id": "hurghada",
        "name": "Hurghada",
        "arabic_name": "الغردقة",
        "location": "Red Sea Governorate, Eastern Egypt",
        "governorate": "Red Sea",
        "coordinates": {"lat": 27.2579, "lng": 33.8116},
        "built_year": None,
        "dynasty": None,
        "pharaoh": None,
        "period": "Modern resort city",
        "landmark_type": "natural",
        "unesco_listed": False,
        "description": (
            "Hurghada is Egypt's premier Red Sea resort city, stretching over 40 kilometers "
            "along the Egyptian Red Sea coast. Once a small fishing village, it has grown "
            "since the 1980s into one of the world's most popular beach destinations, famous "
            "for its year-round sunshine, warm crystalline waters, and extraordinary coral "
            "reef ecosystems. The Red Sea off Hurghada is considered among the top ten "
            "diving destinations in the world, with reefs teeming with parrotfish, sea "
            "turtles, reef sharks, dolphins, and hundreds of species of coral and fish. "
            "The city offers everything from five-star all-inclusive beach resorts to "
            "budget-friendly hostels, along with snorkeling trips, glass-bottom boat tours, "
            "windsurfing, kitesurfing, submarine tours, and excursions into the surrounding "
            "Eastern Desert mountains."
        ),
        "historical_facts": [
            "Hurghada was a tiny fishing village of only a few hundred people before the oil industry and later tourism began in the 1970s and 1980s",
            "The Red Sea corridor off Hurghada was a major ancient trade route connecting Egypt, Arabia, India, and East Africa",
            "The Giftun Islands Marine Park, accessible by boat from Hurghada, contains some of the best-preserved coral reefs in the Red Sea",
            "Water temperature in Hurghada never drops below 20°C, making it a year-round diving destination",
            "The city hosts the Hurghada International Airport, one of Egypt's busiest, with direct flights to over 50 countries",
            "Dolphins frequently accompany diving and snorkeling boats in the open waters outside the bay",
        ],
        "tags": ["beach", "red sea", "diving", "snorkeling", "coral", "resort", "tourism"],
        "visitor_info": {
            "open_hours": "City is open year-round",
            "entry_fee_egp": None,
            "best_time": "March to May and September to November for mild weather; avoid midsummer heat",
            "nearest_city": "Hurghada itself",
            "tips": "Book diving excursions with licensed PADI dive centers. Bargain for snorkeling boat trips at the marina.",
        },
    },

    # ─────────────────────────────────────────────────────────────────────
    # 11. Jabal Musa (Mount Sinai)
    # ─────────────────────────────────────────────────────────────────────
    {
        "landmark_id": "jabal_musa",
        "name": "Mount Sinai (Jabal Musa)",
        "arabic_name": "جبل موسى",
        "location": "South Sinai Governorate, Sinai Peninsula, Egypt",
        "governorate": "South Sinai",
        "coordinates": {"lat": 28.5392, "lng": 33.9750},
        "built_year": None,
        "dynasty": None,
        "pharaoh": None,
        "period": "Religious / Natural landmark",
        "landmark_type": "natural",
        "unesco_listed": False,
        "description": (
            "Jabal Musa, meaning 'Mountain of Moses' in Arabic, is one of the most sacred "
            "mountains in the three Abrahamic religions — Judaism, Christianity, and Islam. "
            "Rising 2,285 meters above sea level in the rugged granite landscape of the "
            "south Sinai Peninsula, it is traditionally identified as the biblical Mount "
            "Sinai where the Prophet Moses received the Ten Commandments from God. Pilgrims "
            "and hikers from around the world make the ascent, either via the 3,750 Steps "
            "of Repentance carved by a monk or via the longer camel path, to reach the "
            "small chapel and mosque at the summit. The reward is a sunrise of breathtaking "
            "beauty over an endless sea of granite peaks glowing in shades of rose, amber, "
            "and gold. At the base of the mountain sits Saint Catherine's Monastery, the "
            "oldest continuously inhabited Christian monastery in the world."
        ),
        "historical_facts": [
            "At 2,285 meters, Jabal Musa is the highest peak in the traditional Mount Sinai area and the third-highest mountain in Egypt",
            "The 3,750 Steps of Repentance leading to the summit were carved by a single monk as an act of penance",
            "The mountain is sacred to Judaism, Christianity, and Islam — making it one of the world's most universally revered sites",
            "Saint Catherine's Monastery at its base has been continuously inhabited since the 6th century CE",
            "The monastery library holds the second largest collection of early Christian manuscripts in the world, after the Vatican",
            "A burning bush in the monastery grounds is claimed by monks to be the very bush from which God spoke to Moses",
            "The summit contains both a small Greek Orthodox chapel dedicated to the Holy Trinity and a small mosque",
        ],
        "tags": ["mountain", "sinai", "religious", "pilgrimage", "moses", "sunrise", "hiking"],
        "visitor_info": {
            "open_hours": "Accessible year-round; summit typically reached before dawn",
            "entry_fee_egp": None,
            "best_time": "Start the ascent at 2:00 AM to reach the summit for sunrise — the most popular and rewarding experience",
            "nearest_city": "Sharm el-Sheikh (2 hours) or Saint Catherine town",
            "tips": "Bring a warm jacket — summit temperatures near freezing even in summer. Hire a local Bedouin guide for safety.",
        },
    },

    # ─────────────────────────────────────────────────────────────────────
    # 12. Karnak Temple
    # ─────────────────────────────────────────────────────────────────────
    {
        "landmark_id": "karnak",
        "name": "Karnak Temple",
        "arabic_name": "معبد الكرنك",
        "location": "Luxor (ancient Thebes), Upper Egypt",
        "governorate": "Luxor",
        "coordinates": {"lat": 25.7188, "lng": 32.6573},
        "built_year": "~2055 BCE – 100 CE",
        "dynasty": "Middle Kingdom through Roman Period",
        "pharaoh": "Multiple pharaohs over 2,000 years",
        "period": "Middle Kingdom to Roman Period",
        "landmark_type": "temple",
        "unesco_listed": True,
        "description": (
            "Karnak is the largest ancient religious complex ever built — a staggering 200-acre "
            "city of temples, chapels, pylons, obelisks, and sacred lakes that grew over "
            "2,000 continuous years of construction by successive pharaohs, each trying to "
            "outdo their predecessors. Dedicated primarily to the powerful god Amun-Ra, "
            "Karnak was the center of Egyptian religious life throughout the New Kingdom "
            "period. Its most iconic space is the Great Hypostyle Hall — a forest of 134 "
            "colossal sandstone columns spread across 5,000 square meters, their surfaces "
            "covered in brightly painted hieroglyphs and reliefs. An avenue of ram-headed "
            "sphinxes once stretched all the way from Karnak to Luxor Temple three kilometers "
            "away. The complex rewards slow exploration — every corner reveals a new obelisk, "
            "sacred pool, painted sanctuary, or ancient inscription."
        ),
        "historical_facts": [
            "Karnak covers approximately 200 acres, making it larger than some ancient cities and the largest ancient religious site in the world",
            "The Great Hypostyle Hall contains 134 columns, the tallest of which reach 23 meters — each wide enough for 100 people to stand on top",
            "Construction on the site began around 2055 BCE and continued for over 2,000 years until the Roman period",
            "Queen Hatshepsut erected two of the tallest obelisks in Egypt at Karnak, each weighing around 320 tonnes",
            "The sacred lake within the complex covers 80 by 40 meters and was used by priests for ritual purification",
            "The Avenue of Sphinxes connected Karnak to Luxor Temple 3 kilometers away — archaeologists have excavated the full route",
            "Karnak's night sound and light show is considered the finest in Egypt, narrating 4,000 years of history as the monuments are dramatically lit",
        ],
        "tags": ["temple", "luxor", "amun", "new kingdom", "hypostyle", "UNESCO", "obelisk"],
        "visitor_info": {
            "open_hours": "6:00 AM – 5:30 PM; Sound & Light Show evenings",
            "entry_fee_egp": 200,
            "best_time": "6:00–8:00 AM before tour groups arrive; or the evening sound and light show",
            "nearest_city": "Luxor",
            "tips": "Buy a combined ticket with the Luxor Museum. Wear comfortable shoes — the complex is enormous and requires extensive walking.",
        },
    },

    # ─────────────────────────────────────────────────────────────────────
    # 13. Pyramids of Giza
    # ─────────────────────────────────────────────────────────────────────
    {
        "landmark_id": "pyramids_of_giza",
        "name": "Pyramids of Giza",
        "arabic_name": "أهرامات الجيزة",
        "location": "Giza Plateau, Cairo, Egypt",
        "governorate": "Giza",
        "coordinates": {"lat": 29.9792, "lng": 31.1342},
        "built_year": "~2560–2510 BCE",
        "dynasty": "4th Dynasty",
        "pharaoh": "Khufu, Khafre, and Menkaure",
        "period": "Old Kingdom",
        "landmark_type": "pyramid",
        "unesco_listed": True,
        "description": (
            "The Pyramids of Giza are the last surviving wonder of the Seven Wonders of the "
            "Ancient World and perhaps the most iconic structures ever built by human hands. "
            "The complex on the Giza Plateau consists of three main pyramids — built for "
            "pharaohs Khufu, Khafre, and Menkaure — along with the Great Sphinx, three "
            "smaller queens' pyramids, mortuaries temples, and workers' villages. The Great "
            "Pyramid of Khufu, completed around 2560 BCE, stood as the tallest structure on "
            "Earth for 3,800 years. It is built from approximately 2.3 million stone blocks, "
            "each averaging 2.5 tonnes, assembled with a precision that astonishes modern "
            "engineers. The perfectly flat base deviates by only 2.1 centimeters across its "
            "230-meter sides. Together, the three pyramids represent the pinnacle of ancient "
            "Egyptian architectural achievement and the extraordinary organizational capacity "
            "of Old Kingdom civilization."
        ),
        "historical_facts": [
            "The Great Pyramid of Khufu was the tallest human-made structure in the world for 3,800 years, from ~2560 BCE until Lincoln Cathedral in England surpassed it in 1311 CE",
            "The pyramid contains an estimated 2.3 million stone blocks weighing between 2.5 and 80 tonnes each",
            "The base of the Great Pyramid is so precisely level that it deviates by only 2.1 centimeters across all four sides",
            "Workers were not slaves — archaeological evidence shows they were paid skilled laborers who received wages, medical care, and a high-quality diet",
            "The pyramids are aligned with extraordinary precision to the cardinal points of the compass, deviating by less than 0.1 degrees",
            "Interior shafts inside the Great Pyramid point toward specific stars — Orion's Belt and Thuban — possibly for religious or navigational purposes",
            "Khafre's pyramid appears taller than Khufu's because it is built on higher ground, though it is actually 3 meters shorter",
        ],
        "tags": ["pyramid", "giza", "ancient wonder", "khufu", "old kingdom", "UNESCO", "pharaoh"],
        "visitor_info": {
            "open_hours": "8:00 AM – 5:00 PM daily",
            "entry_fee_egp": 160,
            "best_time": "Early morning (8:00–9:00 AM) for cool temperatures and soft light; avoid midday heat",
            "nearest_city": "Cairo / Giza",
            "tips": "Enter the pyramids separately (additional ticket required). Hire a licensed guide to understand the engineering and history. Beware of unlicensed touts.",
        },
    },

    # ─────────────────────────────────────────────────────────────────────
    # 14. Qaitbay Citadel
    # ─────────────────────────────────────────────────────────────────────
    {
        "landmark_id": "qaitbay_citadel",
        "name": "Qaitbay Citadel",
        "arabic_name": "قلعة قايتباي",
        "location": "Eastern Harbor, Alexandria, Egypt",
        "governorate": "Alexandria",
        "coordinates": {"lat": 31.2138, "lng": 29.8854},
        "built_year": "1477 CE",
        "dynasty": None,
        "pharaoh": None,
        "period": "Mamluk Sultanate",
        "landmark_type": "fortress",
        "unesco_listed": False,
        "description": (
            "The Citadel of Qaitbay is a magnificent 15th-century Mamluk fortress built "
            "directly on the site of the ancient Lighthouse of Alexandria, one of the Seven "
            "Wonders of the Ancient World. Constructed between 1477 and 1479 by Sultan "
            "Al-Ashraf Qaitbay to defend Alexandria's harbor against Ottoman expansion, the "
            "fortress is a masterpiece of Islamic military architecture. Its thick golden "
            "sandstone walls rise from a narrow peninsula that juts into the Mediterranean, "
            "surrounded on three sides by sea. The sultan used stones from the ruins of the "
            "ancient lighthouse — which had collapsed in earthquakes during the 14th century — "
            "to build the fortress walls, meaning that ancient Hellenistic stone is embedded "
            "throughout the citadel. Today it houses a small naval museum and offers "
            "sweeping views of Alexandria's harbor and the open Mediterranean."
        ),
        "historical_facts": [
            "The citadel was built directly on the foundation of the ancient Lighthouse of Alexandria, one of the Seven Wonders of the Ancient World",
            "Sultan Qaitbay incorporated fallen limestone blocks from the ruined lighthouse into the fortress walls",
            "The ancient Lighthouse of Alexandria, built around 280 BCE, stood approximately 100–130 meters tall — one of the tallest structures in the ancient world",
            "The citadel was besieged but never captured by Ottoman forces; it eventually fell to a negotiated settlement",
            "Napoleon Bonaparte's French expedition used the citadel as a base during the Egyptian Campaign of 1798–1801",
            "Underwater archaeologists in the 1990s discovered massive ancient stone blocks — believed to be lighthouse remains — in the harbor just below the citadel",
            "The fortress was heavily restored in the 1980s and now functions as both a museum and a military heritage site",
        ],
        "tags": ["citadel", "alexandria", "mamluk", "fortress", "mediterranean", "lighthouse", "harbor"],
        "visitor_info": {
            "open_hours": "9:00 AM – 5:00 PM daily",
            "entry_fee_egp": 70,
            "best_time": "Late afternoon when the Mediterranean light turns golden on the stone walls",
            "nearest_city": "Alexandria",
            "tips": "The harbor walk around the citadel is free and equally beautiful. Watch for fishing boats returning in the late afternoon.",
        },
    },

    # ─────────────────────────────────────────────────────────────────────
    # 15. Ras Mohammed National Park
    # ─────────────────────────────────────────────────────────────────────
    {
        "landmark_id": "ras_mohammed_national_park",
        "name": "Ras Mohammed National Park",
        "arabic_name": "محمية رأس محمد",
        "location": "Southern tip of Sinai Peninsula, South Sinai, Egypt",
        "governorate": "South Sinai",
        "coordinates": {"lat": 27.7339, "lng": 34.2467},
        "built_year": "1983 CE (declared protected area)",
        "dynasty": None,
        "pharaoh": None,
        "period": "Natural protected area",
        "landmark_type": "natural",
        "unesco_listed": False,
        "description": (
            "Ras Mohammed National Park, located at the very tip of the Sinai Peninsula "
            "where the Gulf of Aqaba meets the Gulf of Suez, is Egypt's first national park "
            "and one of the most extraordinary marine ecosystems on the planet. Established "
            "in 1983, the park protects a spectacular meeting point of deep ocean trenches "
            "and shallow coral reefs, creating conditions of exceptional marine biodiversity. "
            "The coral walls here plunge over 80 meters into crystal-clear water and are "
            "home to over 1,000 species of fish and 150 species of coral. The Shark Reef "
            "and Yolanda Reef are considered among the world's finest dive sites, offering "
            "encounters with grey reef sharks, hammerheads, barracuda schools, sea turtles, "
            "and spectacular coral gardens. Above the water, the park also protects mangrove "
            "channels, fossil coral terraces, salt lakes, and nesting seabird colonies."
        ),
        "historical_facts": [
            "Ras Mohammed was declared Egypt's first national park in 1983 and was later expanded to cover 480 square kilometers of land and sea",
            "The meeting point of two seas — the Gulf of Aqaba and the Gulf of Suez — creates nutrient-rich upwellings that sustain extraordinary marine life",
            "The Yolanda Reef takes its name from a cargo ship, the MV Yolanda, that sank there in 1980 — its cargo of toilets and bathroom fittings is now a famous novelty dive",
            "The coral walls at Shark Reef drop vertically for over 80 meters, one of the most dramatic reef structures in the Red Sea",
            "Over 1,000 species of fish have been recorded in the park — more species per square kilometer than almost anywhere else on Earth",
            "The mangrove channels on the Gulf of Suez coast are rare examples of mangrove ecosystems in an arid environment",
            "The park attracts hundreds of thousands of divers annually; dive sites include Shark Reef, Yolanda, Anemone City, and Jackfish Alley",
        ],
        "tags": ["national park", "sinai", "diving", "coral reef", "red sea", "marine", "sharks"],
        "visitor_info": {
            "open_hours": "7:00 AM – 5:00 PM daily",
            "entry_fee_egp": 105,
            "best_time": "March to May and September to November; water visibility is best in these months",
            "nearest_city": "Sharm el-Sheikh (30 minutes by road)",
            "tips": "Most visitors join organized dive or snorkel trips from Sharm el-Sheikh. Bring your own mask and fins if possible — rental quality varies.",
        },
    },

    # ─────────────────────────────────────────────────────────────────────
    # 16. Rixos Alamein (landmark as tourism/architecture)
    # ─────────────────────────────────────────────────────────────────────
    {
        "landmark_id": "rixos_al_alamein",
        "name": "El Alamein & North Coast",
        "arabic_name": "ريكسوس العلمين",
        "location": "El Alamein, Matrouh Governorate, North Coast, Egypt",
        "governorate": "Matrouh",
        "coordinates": {"lat": 30.8331, "lng": 28.9500},
        "built_year": None,
        "dynasty": None,
        "pharaoh": None,
        "period": "WWII historical / Modern resort",
        "landmark_type": "natural",
        "unesco_listed": False,
        "description": (
            "El Alamein on Egypt's North Coast is a place of dual significance — a pristine "
            "Mediterranean coastline of white sand beaches and turquoise water, and the site "
            "of the decisive Second Battle of El Alamein in 1942, one of the most pivotal "
            "engagements of World War II. The area is now home to the Rixos Premium Alamein "
            "resort — part of a massive new coastal development — as well as the El Alamein "
            "War Museum and cemeteries maintained by the Commonwealth War Graves Commission, "
            "the German War Cemetery, and the Italian Memorial. The North Coast from El "
            "Alamein westward to Marsa Matrouh features some of the most beautiful and "
            "unspoiled Mediterranean beaches in Egypt, increasingly popular with Egyptian "
            "tourists escaping summer Cairo heat. The combination of natural beauty, "
            "historical weight, and luxury infrastructure makes this stretch of coast one "
            "of Egypt's fastest-developing tourism destinations."
        ),
        "historical_facts": [
            "The Second Battle of El Alamein (October–November 1942) was the turning point of the North Africa Campaign, halting the German advance toward Egypt and the Suez Canal",
            "Field Marshal Erwin Rommel, the 'Desert Fox,' commanded the German-Italian forces; he was defeated by British General Bernard Montgomery",
            "Over 11,000 Allied soldiers are buried in the El Alamein War Cemetery maintained by the Commonwealth War Graves Commission",
            "The El Alamein War Museum houses tanks, artillery, aircraft, and personal artifacts from the 1942 battles",
            "The North Coast beaches west of Alexandria experience temperatures 5–8°C cooler than Cairo in summer, making them Egypt's most popular domestic summer destination",
            "The ancient city of Amunia, near modern Marsa Matrouh, was reportedly where Cleopatra and Mark Antony had a summer palace",
        ],
        "tags": ["north coast", "mediterranean", "WWII", "beach", "alamein", "resort", "history"],
        "visitor_info": {
            "open_hours": "El Alamein War Museum: 8:00 AM – 4:00 PM daily",
            "entry_fee_egp": 40,
            "best_time": "June to September for beach season; October for WWII commemorations",
            "nearest_city": "Alexandria (2.5 hours east)",
            "tips": "Combine a visit to the war museum and cemeteries with beach time. Book North Coast accommodations months in advance for July–August.",
        },
    },

    # ─────────────────────────────────────────────────────────────────────
    # 17. Siwa Oasis Salt Lake
    # ─────────────────────────────────────────────────────────────────────
    {
        "landmark_id": "siwa_oasis_salt_lake",
        "name": "Siwa Oasis Salt Lake",
        "arabic_name": "بحيرة الملح بواحة سيوة",
        "location": "Siwa Oasis, Matrouh Governorate, Western Desert, Egypt",
        "governorate": "Matrouh",
        "coordinates": {"lat": 29.2036, "lng": 25.5195},
        "built_year": None,
        "dynasty": None,
        "pharaoh": None,
        "period": "Natural landmark",
        "landmark_type": "natural",
        "unesco_listed": False,
        "description": (
            "Siwa Oasis, nestled deep in the Egyptian Western Desert near the Libyan border, "
            "is one of Egypt's most isolated and extraordinary natural wonders. The oasis "
            "contains several salt lakes — most notably Lake Siwa (Birket Siwa) and the "
            "smaller Fatnas Lake — whose hypersaline waters create a natural buoyancy that "
            "allows visitors to float effortlessly, similar to the Dead Sea. The lakes "
            "shimmer in hues of turquoise, jade, and deep blue against a backdrop of golden "
            "sand dunes, palm groves heavy with dates, and ancient mud-brick ruins. The "
            "surrounding Siwa Oasis has been inhabited for millennia and was famous in "
            "antiquity for the Oracle of Amun, which Alexander the Great consulted in "
            "331 BCE and which declared him a son of the gods. The unique Siwi people "
            "maintain their own Berber language and culture."
        ),
        "historical_facts": [
            "Alexander the Great made a dangerous desert journey to Siwa in 331 BCE to consult the Oracle of Amun, which reportedly confirmed his divine parentage",
            "Lake Siwa's salt concentration is so high that visitors float naturally on the surface without effort",
            "The Siwa Oasis lies 18 meters below sea level in the Qattara Depression, one of the lowest points in Africa",
            "The Siwi people speak Siwi, a unique Berber language unrelated to Arabic, distinct from all other Egyptian communities",
            "The ancient Shali Fortress in the center of Siwa town was built of kershif (salt rock and mud) in the 13th century and partially dissolved in heavy rains in 1926",
            "Siwa produces some of Egypt's finest dates and olives, which have been cultivated here for thousands of years",
            "The area around Siwa contains ancient rock art, prehistoric fossils, and the ruins of the Temple of the Oracle of Amun",
        ],
        "tags": ["oasis", "salt lake", "western desert", "siwa", "floating", "berber", "oracle"],
        "visitor_info": {
            "open_hours": "Open year-round",
            "entry_fee_egp": None,
            "best_time": "October to April when desert temperatures are bearable; avoid summer heat",
            "nearest_city": "Marsa Matrouh (300 km) or directly from Cairo by bus (9 hours)",
            "tips": "Float in the salt lake at Fatnas Island for the best experience. Rent a bicycle in Siwa town to explore the oasis. Bring cash — no ATMs in remote areas.",
        },
    },

    # ─────────────────────────────────────────────────────────────────────
    # 18. White Desert
    # ─────────────────────────────────────────────────────────────────────
    {
        "landmark_id": "white_desert",
        "name": "White Desert",
        "arabic_name": "الصحراء البيضاء",
        "location": "Farafra, New Valley Governorate, Western Desert, Egypt",
        "governorate": "New Valley",
        "coordinates": {"lat": 27.3667, "lng": 28.0667},
        "built_year": None,
        "dynasty": None,
        "pharaoh": None,
        "period": "Natural landmark",
        "landmark_type": "natural",
        "unesco_listed": False,
        "description": (
            "Egypt's White Desert National Park is one of the most surreal and otherworldly "
            "landscapes on Earth — a vast expanse of chalk-white rock formations sculpted "
            "by millennia of wind erosion into extraordinary shapes resembling giant "
            "mushrooms, ice cream cones, inselbergs, and abstract sculptures rising from a "
            "flat sandy floor. The formations are composed of chalk deposits laid down when "
            "this region was covered by a shallow Cretaceous sea 80 million years ago. As "
            "the desert wind stripped away the surrounding sandstone, the harder chalk "
            "cores were left standing, creating the current fantastical landscape. At sunrise "
            "and sunset, the white formations glow in shades of pink, orange, and gold, "
            "then turn a ghostly luminous white under the full moon — making the White "
            "Desert particularly famous as a camping destination under the stars. It was "
            "declared a national park in 2002."
        ),
        "historical_facts": [
            "The chalk formations of the White Desert were created by wind erosion over millions of years, starting from chalk seabeds deposited 80 million years ago",
            "The area was declared the White Desert National Park in 2002, covering approximately 3,010 square kilometers",
            "Fossils of ancient marine creatures — sea urchins, ammonites, and prehistoric fish — are found throughout the chalk formations",
            "Nearby Crystal Mountain (40 km away) is a ridge of solid quartz crystal, one of the rarest geological formations in the world",
            "The chalk formations glow luminously in moonlight, making full-moon nights especially magical for campers",
            "Temperature in the White Desert can swing 30°C between midday and midnight, requiring both sun protection and warm camping gear",
            "Bedouin guides from Farafra town have led visitors through the desert for generations and are essential for safe navigation",
        ],
        "tags": ["desert", "white desert", "chalk", "formations", "western desert", "camping", "surreal"],
        "visitor_info": {
            "open_hours": "Open year-round; camping overnight is the primary experience",
            "entry_fee_egp": 5,
            "best_time": "October to April; avoid the scorching summer months. Full moon nights are magical.",
            "nearest_city": "Farafra Oasis (45 km); access via the town of Bahariya or Farafra",
            "tips": "Overnight camping inside the national park is the definitive experience. Hire a 4WD vehicle and Bedouin guide from Bahariya Oasis.",
        },
    },

    # ─────────────────────────────────────────────────────────────────────
    # 19. Hanging Church
    # ─────────────────────────────────────────────────────────────────────
    {
        "landmark_id": "hanging_church",
        "name": "The Hanging Church",
        "arabic_name": "الكنيسة المعلقة",
        "location": "Coptic Cairo, Old Cairo, Egypt",
        "governorate": "Cairo",
        "coordinates": {"lat": 30.0053, "lng": 31.2296},
        "built_year": "~7th century CE (built over a 3rd century gatehouse)",
        "dynasty": None,
        "pharaoh": None,
        "period": "Coptic / Early Christian",
        "landmark_type": "church",
        "unesco_listed": False,
        "description": (
            "The Hanging Church, known in Arabic as Al-Muallaqah meaning 'the suspended,' "
            "is one of the oldest and most celebrated Christian churches in Egypt and the "
            "world. It earned its distinctive name because it was built directly above the "
            "southern gatehouse of the ancient Roman Babylon Fortress, with its nave "
            "suspended over the two towers of the gatehouse on 13 wooden beams — giving "
            "the impression of a church floating in the air. The church is dedicated to "
            "the Virgin Mary and is the seat of the Coptic Catholic Patriarchate. Its "
            "interior is a treasury of early Christian art, featuring 110 icons, wooden "
            "screens inlaid with ivory in geometric Coptic designs, and a remarkable "
            "collection of 8th–13th century manuscript pages. Located in the heart of "
            "Coptic Cairo alongside ancient churches, synagogues, and mosques, it "
            "embodies the deep Christian heritage of Egyptian civilization."
        ),
        "historical_facts": [
            "The Hanging Church is built above the gatehouse of the Roman Fortress of Babylon, which dates to the 1st century CE",
            "The church's nave is literally suspended over the twin towers of the Roman gatehouse on 13 wooden beams",
            "It is one of the oldest churches in Egypt and has served as the seat of the Coptic Patriarch for many centuries",
            "The church contains 110 icons, some dating back to the 8th century, representing some of the finest Coptic religious art",
            "The intricate wooden screens and pulpit, inlaid with ivory in geometric patterns, date from the 11th and 13th centuries",
            "According to Coptic tradition, the Holy Family (Mary, Joseph, and the infant Jesus) sheltered in the area of Coptic Cairo during their flight into Egypt",
            "Coptic Cairo contains the highest concentration of early Christian sites in Egypt, including several churches, a synagogue, and an early Christian crypt",
        ],
        "tags": ["church", "coptic", "christian", "old cairo", "roman fortress", "ancient", "icons"],
        "visitor_info": {
            "open_hours": "9:00 AM – 4:00 PM daily; closed during services",
            "entry_fee_egp": 0,
            "best_time": "Weekday mornings; attend a Sunday Coptic service for a deeply moving experience",
            "nearest_city": "Cairo (Old Cairo / Mar Girgis metro station)",
            "tips": "Combine with the nearby Coptic Museum, Ben Ezra Synagogue, and Church of St. Sergius — all within walking distance.",
        },
    },

    # ─────────────────────────────────────────────────────────────────────
    # 20. Saladin Citadel
    # ─────────────────────────────────────────────────────────────────────
    {
        "landmark_id": "saladin_citadel",
        "name": "Saladin Citadel of Cairo",
        "arabic_name": "قلعة صلاح الدين",
        "location": "Mokattam Hill, Islamic Cairo, Egypt",
        "governorate": "Cairo",
        "coordinates": {"lat": 30.0286, "lng": 31.2601},
        "built_year": "1183 CE (begun)",
        "dynasty": None,
        "pharaoh": None,
        "period": "Ayyubid / Mamluk",
        "landmark_type": "fortress",
        "unesco_listed": True,
        "description": (
            "The Citadel of Saladin is a massive medieval Islamic fortress perched dramatically "
            "on a spur of the Mokattam hills overlooking the entirety of Cairo, with the "
            "Giza pyramids visible on the western horizon. Begun in 1176 CE by the legendary "
            "Kurdish-Muslim ruler Saladin (Salah ad-Din Yusuf ibn Ayyub) as a defensive "
            "fortification against Crusader attack, the citadel served as the seat of Egyptian "
            "government for nearly 700 years, from the Ayyubid period through the Mamluk "
            "sultanate and the Ottoman viceroyalty, until the 19th century. Within its walls "
            "rise three mosques, three palaces (now converted to museums), and extensive "
            "medieval fortifications. The dominant structure is the stunning Ottoman-era "
            "Muhammad Ali Mosque, completed in 1848, whose twin minarets and alabaster "
            "exterior dome are visible from across the city."
        ),
        "historical_facts": [
            "Construction was begun by Saladin in 1176 CE and continued by his successors for decades",
            "The citadel served as the seat of Egyptian government and the residence of Egypt's rulers for approximately 700 years",
            "Muhammad Ali Pasha ordered the assassination of the last Mamluk rulers in the Citadel's courtyard in 1811 in what became known as the Massacre of the Mamluks",
            "The Muhammad Ali Mosque (completed 1848) was modeled on the Sultan Ahmed Blue Mosque in Istanbul, reflecting Ottoman architectural influence",
            "Stone blocks for the citadel's construction were taken from the outer casing of the smaller Giza pyramids",
            "The Citadel contains the National Military Museum, the Police Museum, and the Al-Gawhara Palace Museum",
            "Napoleon's army occupied the Citadel during the French occupation of Egypt (1798–1801)",
        ],
        "tags": ["citadel", "cairo", "saladin", "ayyubid", "mamluk", "ottoman", "mosque", "UNESCO"],
        "visitor_info": {
            "open_hours": "8:00 AM – 5:00 PM daily",
            "entry_fee_egp": 180,
            "best_time": "Morning for clear views of Cairo and the pyramids; avoid Friday midday prayers",
            "nearest_city": "Cairo (Islamic Cairo district)",
            "tips": "Combine with the nearby Khan el-Khalili bazaar and Al-Azhar Mosque for a full Islamic Cairo day.",
        },
    },

    # ─────────────────────────────────────────────────────────────────────
    # 21. Sahaba Mosque Sharm el-Sheikh
    # ─────────────────────────────────────────────────────────────────────
    {
        "landmark_id": "sahaba_mosque_sharm",
        "name": "Al-Sahaba Mosque, Sharm el-Sheikh",
        "arabic_name": "مسجد الصحابة بشرم الشيخ",
        "location": "Naama Bay, Sharm el-Sheikh, South Sinai, Egypt",
        "governorate": "South Sinai",
        "coordinates": {"lat": 27.9158, "lng": 34.3300},
        "built_year": "2009 CE",
        "dynasty": None,
        "pharaoh": None,
        "period": "Modern Islamic",
        "landmark_type": "mosque",
        "unesco_listed": False,
        "description": (
            "The Al-Sahaba Mosque in Sharm el-Sheikh is one of the most architecturally "
            "striking modern mosques in Egypt, serving as the principal mosque of this "
            "internationally renowned Red Sea resort city. Completed in 2009, the mosque "
            "features a design that draws on classical Islamic architectural traditions "
            "while incorporating contemporary elements — its brilliant white exterior, "
            "ornate minarets, and geometric tilework creating a landmark visible throughout "
            "Naama Bay. The mosque is designed to reflect Islamic architecture from across "
            "the Muslim world, combining Andalusian, Ottoman, and Fatimid design elements "
            "in a harmonious whole. It stands adjacent to a Coptic Christian church in a "
            "symbol of Egypt's interfaith heritage. The Al-Sahaba Mosque welcomes Muslim "
            "worshippers and non-Muslim respectful visitors alike, and its interior features "
            "beautifully crafted wooden minbar, geometric stained glass, and calligraphic "
            "inscriptions throughout."
        ),
        "historical_facts": [
            "The mosque was completed in 2009 and can accommodate up to 3,000 worshippers at a time",
            "It is named 'Al-Sahaba' in honor of the Companions (Sahaba) of the Prophet Muhammad",
            "The mosque's design incorporates elements from Andalusian, Ottoman, and Fatimid Islamic architectural traditions",
            "It stands adjacent to a Coptic Christian church, symbolizing Egypt's tradition of religious coexistence",
            "The mosque serves the large expatriate Muslim workforce in Sharm el-Sheikh as well as local residents",
            "Sharm el-Sheikh sits on the Red Sea in the southernmost tip of the Sinai Peninsula, at a location inhabited since antiquity",
        ],
        "tags": ["mosque", "sharm el-sheikh", "islamic", "modern", "sinai", "architecture", "red sea"],
        "visitor_info": {
            "open_hours": "Open daily for prayers; non-Muslim visitors welcome outside prayer times",
            "entry_fee_egp": 0,
            "best_time": "Afternoon for beautiful interior light; avoid the five daily prayer times",
            "nearest_city": "Sharm el-Sheikh",
            "tips": "Dress modestly — shoulders and knees covered. Women should bring a headscarf. Remove shoes at the entrance.",
        },
    },

    # ─────────────────────────────────────────────────────────────────────
    # 22. Nubia
    # ─────────────────────────────────────────────────────────────────────
    {
        "landmark_id": "nubia",
        "name": "Nubia",
        "arabic_name": "النوبة",
        "location": "Aswan Governorate, Southern Egypt",
        "governorate": "Aswan",
        "coordinates": {"lat": 23.9700, "lng": 32.8772},
        "built_year": None,
        "dynasty": None,
        "pharaoh": None,
        "period": "Ancient to present — oldest continuous culture in Egypt",
        "landmark_type": "natural",
        "unesco_listed": False,
        "description": (
            "Nubia is not a single monument but an entire civilization and cultural landscape "
            "stretching along the Nile south of Aswan, representing one of the world's oldest "
            "and most continuous human cultures. The Nubian people have lived along this "
            "stretch of the Nile for over 5,000 years, predating even pharaonic Egypt, "
            "and their colorful painted villages, distinctive music, rich cuisine, and "
            "vibrant handicraft traditions remain alive today. Much of the original Nubian "
            "homeland was submerged under Lake Nasser following the construction of the "
            "Aswan High Dam in 1970, displacing over 100,000 people. Today, Nubian villages "
            "on the west bank of the Nile near Aswan — with their characteristic brightly "
            "painted houses decorated with crocodiles, fish, and geometric patterns — "
            "welcome visitors who arrive by felucca. The Nubian Museum in Aswan tells the "
            "full story of this extraordinary civilization."
        ),
        "historical_facts": [
            "Nubia was home to the Kingdom of Kush, which conquered Egypt and ruled as the 25th Dynasty of Pharaohs from around 750 to 656 BCE",
            "Over 100,000 Nubians were displaced from their ancestral lands when Lake Nasser was created by the Aswan High Dam in 1970",
            "Nubian culture is distinct from mainstream Egyptian culture, with its own Nubian language (Nobiin and Kenzi dialects), music, dance, and cuisine",
            "The Nubian Museum in Aswan, opened in 1997, houses artifacts spanning 3,000 years of Nubian civilization and won the Aga Khan Award for Architecture",
            "Ancient Nubia controlled the gold trade routes between sub-Saharan Africa and Egypt — the word 'Nubia' is believed to derive from the ancient Egyptian word for gold, 'nub'",
            "Nubian pyramids at Meroe in Sudan number over 200 — more pyramids than in all of Egypt — reflecting Nubia's own rich pharaonic tradition",
            "Traditional Nubian houses are painted with vivid colors and decorated with images of crocodiles, fish, and geometric patterns as protective symbols",
        ],
        "tags": ["nubia", "aswan", "culture", "nile", "village", "history", "displaced"],
        "visitor_info": {
            "open_hours": "Villages open year-round; Nubian Museum 9:00 AM – 6:00 PM",
            "entry_fee_egp": 80,
            "best_time": "October to April; arrive by felucca for the most authentic experience",
            "nearest_city": "Aswan",
            "tips": "Take a felucca from Aswan to reach the west bank Nubian villages. Try Nubian tea and crocodile encounters at the guesthouses.",
        },
    },

    # ─────────────────────────────────────────────────────────────────────
    # 23. Saint Catherine Monastery
    # ─────────────────────────────────────────────────────────────────────
    {
        "landmark_id": "saint_catherine_monastery",
        "name": "Saint Catherine's Monastery",
        "arabic_name": "دير سانت كاترين",
        "location": "Saint Catherine, South Sinai, Egypt",
        "governorate": "South Sinai",
        "coordinates": {"lat": 28.5560, "lng": 33.9760},
        "built_year": "548–565 CE",
        "dynasty": None,
        "pharaoh": None,
        "period": "Byzantine / Early Christian",
        "landmark_type": "monastery",
        "unesco_listed": True,
        "description": (
            "Saint Catherine's Monastery is the oldest continuously inhabited Christian "
            "monastery in the world, founded between 548 and 565 CE by order of Byzantine "
            "Emperor Justinian I at the foot of Mount Sinai. Built on the site traditionally "
            "believed to be the location of the Burning Bush through which God spoke to "
            "Moses, the monastery has been in continuous operation for nearly 1,500 years. "
            "Its massive granite walls, largely unchanged since the Byzantine era, shelter "
            "one of the world's great repositories of early Christian art and manuscripts: "
            "2,000 icons (the largest collection outside Moscow), a library holding the "
            "second largest collection of early Christian manuscripts in the world after "
            "the Vatican, and extraordinary Byzantine mosaics in the Basilica of the "
            "Transfiguration. The monastery is sacred to Orthodox Christianity, Roman "
            "Catholicism, and Islam, as the Prophet Muhammad is said to have granted it "
            "protection in a letter still preserved within its walls."
        ),
        "historical_facts": [
            "Saint Catherine's is the oldest continuously inhabited Christian monastery in the world, continuously occupied for nearly 1,500 years",
            "The library holds approximately 3,500 manuscripts — the second largest collection of early Christian manuscripts in the world after the Vatican",
            "The Codex Sinaiticus, one of the oldest and most complete manuscripts of the Christian Bible, was discovered here in 1844 and is now in the British Library",
            "The monastery's collection of 2,000 Byzantine icons is the largest anywhere in the world outside of Moscow",
            "The monastery claims to preserve the original Burning Bush mentioned in the Book of Exodus; a living bush still grows on the site",
            "Emperor Justinian I built the monastery as both a religious retreat and a fortified refuge for Christian hermits who had been living there since the 3rd century",
            "A letter attributed to the Prophet Muhammad, granting the monastery protection and exemption from taxes, is preserved in Istanbul's Topkapi Palace",
        ],
        "tags": ["monastery", "sinai", "christian", "byzantine", "UNESCO", "manuscripts", "icons"],
        "visitor_info": {
            "open_hours": "Monday–Thursday and Saturday 9:00 AM – 12:00 PM (closed Friday and Sunday)",
            "entry_fee_egp": 0,
            "best_time": "Early morning; the monastery is only open for a few hours",
            "nearest_city": "Saint Catherine town (3 km); Sharm el-Sheikh (210 km)",
            "tips": "Combine with the Mount Sinai sunrise climb — start up the mountain at 2 AM and visit the monastery on the way back. Dress conservatively.",
        },
    },

    # ─────────────────────────────────────────────────────────────────────
    # 24. Baron Palace
    # ─────────────────────────────────────────────────────────────────────
    {
        "landmark_id": "baron_palace",
        "name": "Baron Empain Palace",
        "arabic_name": "قصر البارون",
        "location": "Heliopolis, Cairo, Egypt",
        "governorate": "Cairo",
        "coordinates": {"lat": 30.0888, "lng": 31.3372},
        "built_year": "1911 CE",
        "dynasty": None,
        "pharaoh": None,
        "period": "Modern / Belle Époque",
        "landmark_type": "palace",
        "unesco_listed": False,
        "description": (
            "Baron Empain Palace is one of the most extraordinary and eccentric architectural "
            "fantasies in all of Egypt — a Hindu-Cambodian temple palace rising incongruously "
            "in the elegant suburb of Heliopolis, Cairo. Commissioned by Belgian industrialist "
            "Édouard Louis Joseph Empain, the man who built Heliopolis as a planned suburb "
            "and built Cairo's first tram network, the palace was designed by French architect "
            "Alexandre Marcel and completed in 1911. Its design is directly inspired by the "
            "Hindu temples of Angkor Wat in Cambodia and the Orissa temples of India, featuring "
            "tiered towers, writhing serpentine balustrades, carved elephants, and mythological "
            "reliefs covering every surface. The palace rotated on a mechanical base so Baron "
            "Empain could always face the sun, though the mechanism was later disabled. "
            "After decades of abandonment and decay — fueling countless urban legends — the "
            "palace underwent a major restoration and reopened to the public in 2020."
        ),
        "historical_facts": [
            "Baron Édouard Empain was the Belgian industrialist who built the entire suburb of Heliopolis as Egypt's first planned city in the early 1900s",
            "The palace was designed by French architect Alexandre Marcel to resemble the Hindu temples of Cambodia's Angkor Wat and India's Orissa temples",
            "According to original plans, the palace was built to rotate on its base so Baron Empain could always orient himself toward the sun",
            "The palace was abandoned after Empain's death and Egyptian nationalization in the 1950s, falling into severe disrepair",
            "For decades, the abandoned palace inspired numerous urban legends about hauntings, curses, and mysterious disappearances",
            "A major Egyptian government restoration project began in 2019 and the palace reopened as a museum and cultural venue in 2020",
            "The carved stone exterior depicts scenes from Hindu mythology, including gods, goddesses, elephants, and celestial dancers",
        ],
        "tags": ["palace", "heliopolis", "cairo", "belle époque", "architecture", "hindu", "restored"],
        "visitor_info": {
            "open_hours": "9:00 AM – 5:00 PM, Tuesday–Sunday (closed Monday)",
            "entry_fee_egp": 50,
            "best_time": "Morning or late afternoon when the carved stone catches interesting light",
            "nearest_city": "Cairo (Heliopolis district)",
            "tips": "The recently restored interior is now open. Look for the carved elephants and serpents on the exterior balustrades — remarkable detail.",
        },
    },

    # ─────────────────────────────────────────────────────────────────────
    # 25. Al Montazah Palace & Gardens
    # ─────────────────────────────────────────────────────────────────────
    {
        "landmark_id": "al_montazah",
        "name": "Al Montazah Palace & Gardens",
        "arabic_name": "المنتزه",
        "location": "Montazah, Eastern Alexandria, Egypt",
        "governorate": "Alexandria",
        "coordinates": {"lat": 31.2917, "lng": 30.0194},
        "built_year": "1892 CE (original Salamlek palace)",
        "dynasty": None,
        "pharaoh": None,
        "period": "Khedival / Royal",
        "landmark_type": "palace",
        "unesco_listed": False,
        "description": (
            "Al Montazah is a stunning royal estate on Alexandria's eastern Mediterranean "
            "coast, encompassing 155 acres of landscaped gardens, private beaches, two "
            "historic palaces, and a lighthouse on a rocky promontory overlooking the sea. "
            "The estate was originally built by Khedive Abbas II in 1892 as a summer hunting "
            "lodge, and was subsequently expanded by King Fuad I and King Farouk into an "
            "elaborate royal retreat. The Haramlek Palace served as the private royal "
            "residence — it is now a luxury hotel — while the nearby Salamlek Palace, built "
            "in a Florentine-Turkish architectural style, hosts distinguished guests. "
            "The gardens, planted with palms, bougainvillea, and formal European hedgerows, "
            "lead down to a sheltered bay with private beaches. Since the Egyptian Revolution "
            "of 1952 the gardens and beaches have been open to the public, making Montazah "
            "one of Alexandria's most beloved and treasured public spaces."
        ),
        "historical_facts": [
            "The estate was founded by Khedive Abbas II in 1892 as a simple summer palace and hunting retreat",
            "King Farouk, Egypt's last reigning monarch before the 1952 revolution, used Montazah as his primary summer residence",
            "The estate covers 155 acres of gardens, woods, and beaches on a rocky peninsula jutting into the Mediterranean",
            "The Haramlek Palace, built in 1932, is now operated as a luxury hotel by Sofitel; the original royal rooms are largely preserved",
            "A picturesque Ottoman-style lighthouse stands on the rocky point at the eastern end of the estate",
            "Following the 1952 revolution that ended the monarchy, President Nasser opened the gardens and beaches to the Egyptian public",
            "The gardens contain over 150 species of plants from across the Mediterranean and tropical world, planted by royal gardeners",
        ],
        "tags": ["palace", "alexandria", "royal", "gardens", "beach", "khedive", "mediterranean"],
        "visitor_info": {
            "open_hours": "Gardens open 7:00 AM – 11:00 PM daily",
            "entry_fee_egp": 35,
            "best_time": "Late afternoon for a seaside walk when the sea breeze cools the gardens",
            "nearest_city": "Alexandria (eastern end of the Corniche road)",
            "tips": "The public beach within the grounds requires a separate ticket. The gardens alone are worth the entry. Combine with a seafood dinner on the Montazah bay.",
        },
    },

    # ─────────────────────────────────────────────────────────────────────
    # 26. Al-Azhar Mosque
    # ─────────────────────────────────────────────────────────────────────
    {
        "landmark_id": "al_azhar_mosque",
        "name": "Al-Azhar Mosque",
        "arabic_name": "المسجد الأزهر",
        "location": "Khan el-Khalili, Islamic Cairo, Egypt",
        "governorate": "Cairo",
        "coordinates": {"lat": 30.0461, "lng": 31.2628},
        "built_year": "972 CE",
        "dynasty": None,
        "pharaoh": None,
        "period": "Fatimid",
        "landmark_type": "mosque",
        "unesco_listed": True,
        "description": (
            "Al-Azhar Mosque is one of the most important mosques in the Islamic world and "
            "home to Al-Azhar University — the oldest continuously operating university in "
            "the world, founded in 975 CE. Built by the Fatimid general Jawhar al-Siqilli "
            "in 972 CE as the congregational mosque of the new Fatimid capital of Cairo, "
            "Al-Azhar quickly became the center of Islamic scholarship. Al-Azhar University, "
            "founded within the mosque, has educated Muslim scholars from across the globe "
            "for over a thousand years and remains today the world's foremost institution "
            "of Islamic learning, issuing religious rulings that guide the faith of over "
            "a billion Muslims. The mosque's architecture is a layered masterpiece of "
            "Islamic styles across 1,000 years: the original Fatimid core augmented by "
            "Mamluk expansions, minarets, and ornate gateways. The harmonious courtyard "
            "surrounded by carved stone arcades, its white marble flooring cool and serene, "
            "offers a profound sense of peace in the heart of bustling Cairo."
        ),
        "historical_facts": [
            "Al-Azhar was founded in 972 CE — making it and its associated university over 1,050 years old",
            "Al-Azhar University, established in 975 CE within the mosque, is recognized as the oldest continuously operating university in the world",
            "The name 'Al-Azhar' means 'the most resplendent' in Arabic and may be a reference to Fatima al-Zahra, daughter of the Prophet Muhammad",
            "The mosque was originally built as a Shia Ismaili mosque by the Fatimid dynasty; after Saladin's conquest in 1171, it was converted to Sunni Islam",
            "Al-Azhar issues fatwas (religious rulings) that are respected and followed by Sunni Muslims worldwide",
            "Napoleon Bonaparte visited Al-Azhar during the French occupation of Egypt and attempted to cultivate the mosque's scholars as political allies",
            "The mosque has five minarets added across different centuries — each reflects the distinct architectural style of its period",
        ],
        "tags": ["mosque", "islamic", "cairo", "fatimid", "university", "UNESCO", "oldest", "scholarship"],
        "visitor_info": {
            "open_hours": "9:00 AM – 8:00 PM daily; closed during Friday prayers (11:00 AM – 1:00 PM)",
            "entry_fee_egp": 0,
            "best_time": "Morning on a weekday for a peaceful experience; avoid Friday midday",
            "nearest_city": "Cairo (Islamic Cairo, next to Khan el-Khalili bazaar)",
            "tips": "Dress conservatively. Women must wear a hijab inside — free headscarves are provided at the entrance. Remove shoes. Combine with Khan el-Khalili market next door.",
        },
    },
]