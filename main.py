from pypdf import PdfReader

from unit import Unit, Characteristic
import utils

file_name = "input/space-marines.pdf"
reader = PdfReader(file_name)


data = []
amount = reader._get_num_pages()
pages_to_process = (amount - 6) / 2

for i in range(6, amount, 2):
    datasheet = (
        reader.pages[i]
        .extract_text()
        .replace("\n", " ")
        .replace("\r", "")
        .replace("  ", " ")
    )
    datasheet_raw = reader.pages[i].extract_text()

    name = utils.get_substring(utils.name_pattern, datasheet)
    keywords = utils.get_substring(utils.keyword_pattern, datasheet).split(", ")
    ranged_weapons_raw = utils.get_substring(utils.ranged_weapon_pattern, datasheet)
    melee_weapons_raw = utils.get_substring(utils.melee_weapon_pattern, datasheet)
    characteristic_raw = utils.get_substring(
        utils.characteristic_pattern, datasheet
    ).split(" ")
    faction = utils.get_substring(utils.faction_pattern, datasheet)
    invuln = utils.get_substring(utils.invuln_pattern, datasheet)
    core_abilities = utils.get_substring(utils.core_ability_pattern, datasheet).split(
        ", "
    )
    faction_abilities = utils.get_substring(
        utils.faction_ability_pattern, datasheet_raw
    ).split(", ")
    unit_abilities = utils.get_substring(utils.unit_ability_pattern, datasheet_raw)

    if i == 8:
        print(datasheet)
        print(repr(datasheet_raw))
        print(unit_abilities)

    try:
        characteristic = Characteristic(
            characteristic_raw[0],
            characteristic_raw[1],
            characteristic_raw[2],
            characteristic_raw[3],
            characteristic_raw[4],
            characteristic_raw[5],
        )
        ranged_weapons_parsed = utils.parse_ranged_weapon(ranged_weapons_raw)
        melee_weapons_parsed = utils.parse_melee_weapon(melee_weapons_raw)
    except IndexError:
        print("Error for", i, name)

    unit = Unit(
        name,
        characteristic=characteristic,
        ranged_weapons=ranged_weapons_parsed,
        melee_weapons=melee_weapons_parsed,
        core_abilities=core_abilities,
        faction_abilities=faction_abilities,
        unit_abilities=[],
        keywords=keywords,
        faction=faction,
        invuln=invuln,
    )

    data.append(unit)
    # print(f"Parsed {i/2} of {pages_to_process}.", end="\r", flush=True)


utils.create_json(data, "space-marines")
