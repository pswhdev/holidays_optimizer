# List of countries
countries = [
    "Albania",
    "Algeria",
    "American Samoa",
    "Andorra",
    "Angola",
    "Argentina",
    "Armenia",
    "Aruba",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Bolivia",
    "Bosnia and Herzegovina",
    "Botswana",
    "Brazil",
    "Brunei",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Chad",
    "Chile",
    "China",
    "Colombia",
    "Costa Rica",
    "Croatia",
    "Cuba",
    "Curacao",
    "Cyprus",
    "Czechia",
    "Denmark",
    "Djibouti",
    "Dominican Republic",
    "Ecuador",
    "Egypt",
    "El Salvador",
    "Estonia",
    "Eswatini",
    "Ethiopia",
    "Finland",
    "France",
    "Gabon",
    "Georgia",
    "Germany",
    "Ghana",
    "Greece",
    "Guam",
    "Guatemala",
    "Honduras",
    "Hong Kong",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran",
    "Ireland",
    "Isle of Man",
    "Israel",
    "Italy",
    "Jamaica",
    "Japan",
    "Jersey",
    "Kazakhstan",
    "Kenya",
    "Kuwait",
    "Kyrgyzstan",
    "Laos",
    "Latvia",
    "Lesotho",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Malta",
    "Marshall Islands",
    "Mexico",
    "Moldova",
    "Monaco",
    "Montenegro",
    "Morocco",
    "Mozambique",
    "Namibia",
    "Netherlands",
    "New Zealand",
    "Nicaragua",
    "Nigeria",
    "Northern Mariana Islands",
    "North Macedonia",
    "Norway",
    "Pakistan",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Poland",
    "Portugal",
    "Puerto Rico",
    "Romania",
    "Russia",
    "San Marino",
    "Saudi Arabia",
    "Serbia",
    "Seychelles",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "South Africa",
    "South Korea",
    "Spain",
    "Sweden",
    "Switzerland",
    "Taiwan",
    "Tanzania",
    "Thailand",
    "Timor Leste",
    "Tonga",
    "Tunisia",
    "Turkey",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom",
    "United States of America",
    "United States Virgin Islands",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Vatican City",
    "Venezuela",
    "Vietnam",
    "Virgin Islands",
    "Zambia",
    "Zimbabwe",
]

# Dict with countries with holidays varying with the state and the state/district/province/territory lists
states_by_country = {
    "Australia": ["ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"],
    "Austria": [
        "Burgenland",
        "Kärnten",
        "Niederösterreich",
        "Oberösterreich",
        "Salzburg",
        "Steiermark",
        "Tirol",
        "Vorarlberg",
        "Wien",
    ],
    "Bolivia": ["B", "C", "H", "L", "N", "O", "P", "S", "T"],
    "Bosnia and Herzegovina": ["BIH", "BRC", "SRP"],
    "Brazil": [
        "AC",
        "AL",
        "AM",
        "AP",
        "BA",
        "CE",
        "DF",
        "ES",
        "GO",
        "MA",
        "MG",
        "MS",
        "MT",
        "PA",
        "PB",
        "PE",
        "PI",
        "PR",
        "RJ",
        "RN",
        "RO",
        "RR",
        "RS",
        "SC",
        "SE",
        "SP",
        "TO",
    ],
    "Canada": [
        "AB",
        "BC",
        "MB",
        "NB",
        "NL",
        "NS",
        "NT",
        "NU",
        "ON",
        "PE",
        "QC",
        "SK",
        "YT",
    ],
    "Chile": [
        "AI",
        "AN",
        "AP",
        "AR",
        "AT",
        "BI",
        "CO",
        "LI",
        "LL",
        "LR",
        "MA",
        "ML",
        "NB",
        "RM",
        "TA",
        "VS",
    ],
    "El Salvador": [
        "AH",
        "CA",
        "CH",
        "CU",
        "LI",
        "MO",
        "PA",
        "SA",
        "SM",
        "SO",
        "SS",
        "SV",
        "UN",
        "US",
    ],
    "France": [
        "BL",
        "GES",
        "GP",
        "GY",
        "MF",
        "MQ",
        "NC",
        "PF",
        "RE",
        "WF",
        "YT",
    ],
    "Germany": [
        "BB",
        "BE",
        "BW",
        "BY",
        "BYP",
        "HB",
        "HE",
        "HH",
        "MV",
        "NI",
        "NW",
        "RP",
        "SH",
        "SL",
        "SN",
        "ST",
        "TH",
    ],
    "India": [
        "AN",
        "AP",
        "AR",
        "AS",
        "BR",
        "CG",
        "CH",
        "DD",
        "DH",
        "DL",
        "GA",
        "GJ",
        "HP",
        "HR",
        "JH",
        "JK",
        "KA",
        "KL",
        "LA",
        "LD",
        "MH",
        "ML",
        "MN",
        "MP",
        "MZ",
        "NL",
        "OR",
        "PB",
        "PY",
        "RJ",
        "SK",
        "TN",
        "TR",
        "TS",
        "UK",
        "UP",
        "WB",
    ],
    "Italy": [
        "AG",
        "AL",
        "AN",
        "AO",
        "AP",
        "AQ",
        "AR",
        "AT",
        "AV",
        "BA",
        "BG",
        "BI",
        "BL",
        "BN",
        "BO",
        "BR",
        "BS",
        "BT",
        "BZ",
        "CA",
        "CB",
        "CE",
        "CH",
        "CL",
        "CN",
        "CO",
        "CR",
        "CS",
        "CT",
        "CZ",
        "EN",
        "FC",
        "FE",
        "FG",
        "FI",
        "FM",
        "FR",
        "GE",
        "GO",
        "GR",
        "IM",
        "IS",
        "KR",
        "LC",
        "LE",
        "LI",
        "LO",
        "LT",
        "LU",
        "MB",
        "MC",
        "ME",
        "MI",
        "MN",
        "MO",
        "MS",
        "MT",
        "NA",
        "NO",
        "NU",
        "OR",
        "PA",
        "PC",
        "PD",
        "PE",
        "PG",
        "PI",
        "PN",
        "PO",
        "PR",
        "PT",
        "PU",
        "PV",
        "PZ",
        "RA",
        "RC",
        "RE",
        "RG",
        "RI",
        "RM",
        "RN",
        "RO",
        "SA",
        "SI",
        "SO",
        "SP",
        "SR",
        "SS",
        "SU",
        "SV",
        "TA",
        "TE",
        "TN",
        "TO",
        "TP",
        "TR",
        "TS",
        "TV",
        "UD",
        "VA",
        "VB",
        "VC",
        "VE",
        "VI",
        "VR",
        "VT",
        "VV",
    ],
    "Malaysia": [
        "JHR",
        "KDH",
        "KTN",
        "KUL",
        "LBN",
        "MLK",
        "NSN",
        "PHG",
        "PJY",
        "PLS",
        "PNG",
        "PRK",
        "SBH",
        "SGR",
        "SWK",
        "TRG",
    ],
    "New Zealand": [
        "AUK",
        "BOP",
        "CAN",
        "CIT",
        "GIS",
        "HKB",
        "MBH",
        "MWT",
        "NSN",
        "NTL",
        "OTA",
        "STL",
        "TAS",
        "TKI",
        "WGN",
        "WKO",
        "WTC",
    ],
    "Nicaragua": [
        "AN",
        "AS",
        "BO",
        "CA",
        "CI",
        "CO",
        "ES",
        "GR",
        "JI",
        "LE",
        "MD",
        "MN",
        "MS",
        "MT",
        "NS",
        "RI",
        "SJ",
    ],
    "Portugal": [
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "20",
        "30",
    ],
    "Spain": [
        "AN",
        "AR",
        "AS",
        "CB",
        "CE",
        "CL",
        "CM",
        "CN",
        "CT",
        "EX",
        "GA",
        "IB",
        "MC",
        "MD",
        "ML",
        "NC",
        "PV",
        "RI",
        "VC",
    ],
    "Switzerland": [
        "AG",
        "AI",
        "AR",
        "BL",
        "BS",
        "BE",
        "FR",
        "GE",
        "GL",
        "GR",
        "JU",
        "LU",
        "NE",
        "NW",
        "OW",
        "SG",
        "SH",
        "SZ",
        "SO",
        "TG",
        "TI",
        "UR",
        "VD",
        "VS",
        "ZG",
        "ZH",
    ],
    "United Kingdom": ["ENG", "NIR", "SCT", "WLS"],
    "United States of America": [
        "AK",
        "AL",
        "AR",
        "AS",
        "AZ",
        "CA",
        "CO",
        "CT",
        "DC",
        "DE",
        "FL",
        "GA",
        "GU",
        "HI",
        "IA",
        "ID",
        "IL",
        "IN",
        "KS",
        "KY",
        "LA",
        "MA",
        "MD",
        "ME",
        "MI",
        "MN",
        "MO",
        "MP",
        "MS",
        "MT",
        "NC",
        "ND",
        "NE",
        "NH",
        "NJ",
        "NM",
        "NV",
        "NY",
        "OH",
        "OK",
        "OR",
        "PA",
        "PR",
        "RI",
        "SC",
        "SD",
        "TN",
        "TX",
        "UM",
        "UT",
        "VA",
        "VI",
        "VT",
        "WA",
        "WI",
        "WV",
        "WY",
    ],
}
