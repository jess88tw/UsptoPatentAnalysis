import re
#-----------------------------------------------------------------------------
#   data
#-----------------------------------------------------------------------------
dic_month = {
    'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06', 'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'
    }
dic_month_2 = {
    'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
    }
us_country_list  = [
    "Abingdon", "Acton", "Acworth", "Ada", "Adamstown", "Addison", "Aiken", "Akron", "Alabaster", "Alachua", "Alameda", "Albany", "Albuquerque", "Alexandria", "Alhambra", "Aliso Viejo", "Allen", "Allison Park", "Allston", "Alpharetta", "Alrington", "Altadena", "Alvin", "Amarillo", "Ames", "Amherst", "Anaheim", "Andover", "Ann Arbor", "Annandale", "Annapolis", "Antelope", "Apex", "Aptos", "Arcadia", "Ardmore", "Arena", "Arlington", "Armonk", "Arnold", "Arroyo Grande", "Ashland", "Astoria", "Athens", "Atherton", "Athol", "Atkinson", "Atlanta", "Attleboro", "Auburn", "Auburndale", "Augusta", "Aurora", "Austell", "Austin", "Avon", "Bahama", "Bainbridge Island", "Bala Cynwyd", "Ballston Spa", "Ballwin", "Baltimore", "Bar Harbor", "Baraboo", "Barrington", "Bartlett", "Basking Ridge", "Baton Rogue", "Baton Rouge", "Battleground", "Bay Village", "Bayville", "Beachwood", "Beaverton", "Bedford", "Bedminster", "Bee Cave", "Bel Air", "Belchertown", "Belford", "Belgrade", "Bellaire", "Belle Mead", "Belleville", "Bellevue", "Belmont", "Belton", "Benicia", "Bensalem", "Bentleyville", "Berkeley", "Bernardsville", "Berwyn", "Bethesda", "Bethpage", "Beverley Hills", "Beverly", "Beverly Hills", "Big Flats", "Binghamton", "Birmingham", "Bishop", "Blacksburg", "Blackssburg", "Blaine", "Bloomfield", "Bloomington", "Blue Ash", "Boca Raton", "Bohemia", "Boise", "Boonton Township", "Boothwyn", "Bordentown", "Boston", "Bothell", "Boulder", "Boulder Creek", "Bound Brook", "Bountiful", "Bowie", "Boxborough", "Boxford", "Boyds", "Boynton Beach", "Bozeman", "Bradford", "Branchburg", "Brandenburg", "Brandon", "Branford", "Brentwood", "Brewster", "Bridgewater", "Bridgwater", "Brier", "Brighton", "Brisbane", "Bristol", "Broadview Heights", "Bronx", "Bronxville", "Brookeville", "Brookfield", "Brookline", "Brooklyn", "Brooklyn Park", "Broomfield", "Brownsville", "Bryan", "Bryn Mawr", "Budd Lake", "Buellton", "Bueuton", "Buffalo", "Buffalo Grove", "Burlingame", "Burlington", "Burtonsville", "Cabin John", "Calabasas", "Califon", "Camarillo", "Camas", "Cambridge", "Campbell", "Canton", "Carbondale", "Cardiff", "Carlsbad", "Carlstadt", "Carmel", "Carmichael", "Carrboro", "Carrollton", "Carson City", "Cary", "Casselberry", "Castro Valley", "Cathedral City", "Cedar Park", "Centennial", "Cerritos", "Chagrin Falls", "Chalfont", "Champaign", "Chandler", "Chapel Hill", "Chappaqua", "Charleson", "Charleston", "Charlestown", "Charlotte", "Charlottesville", "Charlton", "Chatham", "Chelsea", "Cherry Hill", "Chesapeake", "Chesterfield", "Chesterton", "Chestnut", "Chestnut Hill", "Cheswick", "Chevy Chase", "Chiba", "Chicago", "Chino Hills", "Christianburg", "Christiansburg", "Chula Vista", "Chule Vista", "Chuluota", "Churchville", "Cincinatti", "Cincinnati", "Claremont", "Clarkesville", "Clarksburg", "Clarksville", "Claypool", "Clayton", "Clearwater", "Clemmons", "Clemson", "Clermont", "Cleveland", "Cleveland Heights", "Cliffside Park", "Cliffwood", "Clifton", "Clifton Park", "Clinton", "Closter", "Cochranton", "Cockeysville", "Coconut Creek", "Coconut Grove", "Colchester", "Cold Spring Harbor", "Colfax", "College Park", "College Station", "Collegeville", "Collierville", "Colma", "Colo", "Colorado Springs", "Colton", "Columbia", "Columbus", "Concord", "Conroe", "Coon Rapids", "Cooper City", "Coppell", "Coral Gables", "Coral Springs", "Coralville", "Corcoran", "Cordova", "Corning", "Corona Del Mar", "Coto de Caza", "Covina", "Cranbury", "Cranford", "Cranston", "Croton-on Hudson", "Croton-on-Hudson", "Crozet", "Culver City", "Cupertino", "Cuyahoga Falls", "Dallas", "Daly", "Daly City", "Danbury", "Danville", "Darien", "Darnestown", "Davis", "Dayton", "Decatur", "Dedham", "Deerfield", "Defiance", "Deforest", "Del Mar", "Delanson", "Delmar", "Delray Beach", "Denton", "Denver", "Denville", "Denwood", "Derwood", "Des Plaines", "Detroit", "Diamond Bar", "Dobbs Ferry", "Doral", "Dorchester", "Dowingtown", "Downington", "Downingtown", "Doylestown", "Draper", "Dresher", "Drexel Hill", "Dripping Springs", "Duarte", "Dublin", "Duluth", "Dunstable", "Durham", "Duxbury", "E. Sandwich", "Eagan", "Earlham", "Earlysville", "Earth City", "East Amherst", "East Bethal", "East Brunswick", "East Greenwich", "East Hanover", "East Haven", "East Lansing", "East Lyme", "East Palo Alto", "East Rutherford", "East Setauket", "East Syracuse", "East Windsor", "Easton", "Eatontown", "Eden Prairie", "Edina", "Edison", "Edmond", "Edmonds", "El Cajon", "El Cerrito", "El Granada", "El Marcero", "El Paso", "El Sobrante", "Elgin", "Elizabeth", "Elk Grove", "Elkhart", "Elkins Park", "Elkridge", "Ellicot City", "Ellicott City", "Elmhurst", "Elmira", "Elmont", "Elmsford", "Emerald Hills", "Emeryville", "Encinitas", "Encino", "Encintias", "Enfield", "Englewood", "Erie", "Escondido", "Etna", "Euclid", "Eugene", "Evans", "Evanston", "Evansville", "Ewa Beach", "Ewing", "Exton", "Fair Oaks", "Fairfax", "Fairfield", "Fairport", "Falcon Heights", "Fanwood", "Far Hills", "Farmington", "Fayetteville", "Federal Way", "Felton", "Finksburg", "Fitchburg", "Flagstaff", "Flemington", "Florham Park", "Flower Mound", "Floyd", "Fords", "Forest Hills", "Forest Knolls", "Forest Lake", "Forks Township", "Fort Collins", "Fort Detrick", "Fort Lee", "Fort Wayne", "Fort Worth", "Foster City", "Fountain Valley", "Framingham", "Franklin", "Franklin Drive", "Franklin Lakes", "Franklin Park", "Frederick", "Fremont", "Fresh Meadows", "Fresno", "Friendswood", "Ft. Thomas", "Ft. Wayne", "Gainesville", "Gaithersburg", "Gales Ferry", "Galveston", "Garrett Park", "Gary", "Georgetown", "Gering", "Germantown", "Gettysburg", "Gibsonia", "Glassboro", "Glen Allen", "Glen Arm", "Glen Mills", "Glen Ridge", "Glen Rock", "Glencoe", "Glendale", "Glenelg", "Glenshaw", "Glenview", "Gloucester", "Glouchester", "Glyndon", "Golden Valley", "Goleta", "Gowanda", "Granada Hills", "Grand Forks", "Grand Rapids", "Granger", "Grantham", "Grapevine", "Grayslake", "Great Neck", "Green Island", "Greenlawn", "Greensboro", "Greenville", "Greenwich", "Greenwood", "Greenwood Village", "Gretna", "Groton", "Guaynabo", "Guilford", "Hackensack", "Haiku", "Halethorpe", "Half Moon Bay", "Hamden", "Hamilton", "Hamilton Square", "Hampton", "Hanover", "Harbor Pittsboro", "Harrisburg", "Harrison", "Harrods Creek", "Harvest", "Hastings-on-Hudson", "Haverford", "Haverhill", "Havertown", "Haworth", "Hayward", "Heber City", "Helmetta", "Hercules", "Herndon", "Hershey", "Herzlia", "Hewitt", "Highland", "Highland Heights", "Highland Park", "Highland Village", "Highlands Ranch", "Hightstown", "Hilliard", "Hillsborough", "Hinsdale", "Hobart", "Hoboken", "Ho-Ho-Kus", "Holden", "Holladay", "Holliston", "Holly Springs", "Hollywood", "Holmdel", "Honolulu", "Hopkington", "Hopkins", "Hopkinton", "Horseheads", "Horsham", "Houghton", "Houston", "Howell", "Hubbardston", "Hudson", "Hummelstown", "Hungtington", "Hunt Valley", "Huntingdon Valley", "Huntington", "Huntington Beach", "Indiana", "Indianapolis", "Indianola", "Inner Grove Heights", "Inverness", "Iowa City", "Ipswich", "Irvine", "Irving", "Isanti", "Iselin", "Issaquah", "Itasca", "Ithaca", "Ithica", "Jackson", "Jacksonville", "Jamaica Plain", "Jamison", "Jamul", "Jasper", "Jefferson", "Jersey City", "Johnston", "Junction City", "Jupiter", "Kalamazoo", "Kansas City", "Katonah", "Katy", "Kaysvile", "Kearny", "Keller", "Kendall Park", "Kenmore", "Kennesaw", "Kensington", "Kent", "Key Biscayne", "King of Prussia", "Kirkland", "Kuilua", "Kyle", "La Canada", "La Crosse", "La Grande", "La Jolla", "La Mirada", "La Verne", "Lafayette", "Laguna Beach", "Laguna Hill", "Laguna Hills", "Laguna Niguel", "Lake Forest", "Lake Forest Park", "Lake Geneva", "Lake Oswego", "Lake Zurich", "Lakewood", "Lamoine", "Land O Lakes", "Land O' Lakes", "Land O'Lakes", "Lansdale", "Laramie", "Largo", "Larkspur", "Las Vegas", "Lauderdale", "Lawerence", "Lawrence", "Lawrenceville", "Laytonsville", "League City", "Lebanon", "Ledgewood", "Leominster", "Leonia", "Lexington", "Liberty", "Libertyville", "Liitle Rock", "Lilburn", "Lincoln", "Lincoln University", "Lincolnshire", "Linden", "Lino Lakes", "Lisle", "Little Falls", "Little Rock", "Littleton", "Livermore", "Liverpool", "Livingston", "Loma Linda", "Lombard", "London", "Long Branch", "Long Valley", "Longmont", "Loonta", "Los Alamitos", "Los Altos", "Los Altos Hills", "Los Angeles", "Los Gatos", "Louisa", "Louisville", "Loveland", "Lowell", "Lower Gwynedd", "Lubbock", "Luling", "Lunenburg", "Lutherville", "Lutz", "Lynn", "Lynnwood", "MaComb", "Macon", "Madison", "Magnolia", "Mahopac", "Malden", "Malibu", "Malvern", "Manalapan", "Manchester", "Mandeville", "Manhasset", "Manhattan", "Manhattan Beach", "Manlius", "Mansfield", "Maple Glen", "Maple Grove", "Mapleville", "Maplewood", "Marblehead", "Marietta", "Marlborough", "Marshall", "Martinez", "Martinsville", "Mason", "Mason Neck", "Matawan", "Mattapan", "Mayfield", "Mayfield Heights", "Maynard", "Mazomanie", "McFarland", "McLean", "Mebane", "Mechanicsville", "Medfield", "Medford", "Media", "Medina", "Medord", "Melrose", "Melville", "Memphis", "Mendham", "Mendon", "Menlo Park", "Mentor", "Merced", "Mercer Island", "Merion Station", "Merrimack", "Metuchen", "Mew York", "Miami", "Miami Beach", "Middleburg", "Middleton", "Middletown", "Midlothian", "Milan", "Milford", "Milford Kent Country", "Mililani", "Mill Valley", "Millbrae", "Millbury", "Millington", "Millrae", "Milltown", "Milpitas", "Milton", "Milwaukee", "Minneapolis", "Minnetonka", "Miramar", "Mission Hill", "Mission Viejo", "Missouri City", "Mobile", "Mocksville", "Monmouth Junction", "Monona", "Monroe", "Monrovia", "Monte Vista", "Monterey Park", "Montgomery", "Montvale", "Moorestown", "Moorpark", "Moraga", "Moreland Hills", "Morgan Hill", "Morgantown", "Morganville", "Morris Plains", "Morrison", "Morristown", "Morton Grove", "Moss Beach", "Mount Desert", "Mount Pleasant", "Mount Prospect", "Mount Vernon", "Mountain Lakes", "Mountain View", "Mountville", "Moutain View", "Moyie Springs", "Mpls", "Mt. Airy", "Mt. Horeb", "Mt. Pleasant", "Mukilteo", "Munster", "Murphys", "Myrtle Beach", "Mystic", "N. Bethesda", "N. Richland Hills", "Naperville", "Naples", "Narberth", "Narbeth", "Nashville", "Natic", "Natick", "Needham", "Needham Heights", "Neenah", "Neshanic Station", "New Albany", "New Brighton", "New Britain", "New Brunswick", "New Haven", "New Hope", "New Jersey", "New Market", "New Orleans", "New Providence", "New Richmond", "New Rochelle", "New Stanton", "New York", "Newark", "Newberry", "Newburgh", "Newbury Park", "Newburyport", "Newport Beach", "Newport Coast", "Newport News", "Newton", "Newton Center", "Newton Highlands", "Newtown", "Newtown Square", "Niskayuna", "Niwot", "Nolensville", "Norco", "Norcross", "Norfolk", "Norman", "Norristown", "North Bend", "North Bethesda", "North Brunswick", "North Chelmsford", "North Chicago", "North Liberty", "North Potomac", "North Providence", "North Reading", "North Riverside", "North Wales", "Northboro", "Northborough", "Northfield", "Norwalk", "Norwood", "Novato", "Novi", "Nutley", "Oak Hill", "Oak Park", "Oak Ridge", "Oakdale", "Oakland", "Ocean City", "Oceanside", "Odessa", "O'Fallon", "Oklahoma City", "Olathe", "Old Lyme", "Olney", "Omaha", "Oregon", "Oregon City", "Oreland", "Orinda", "Orlando", "Ottsville", "Overland Park", "Oviedo", "Owego", "Owings Mill", "Owings Mills", "Oxford", "Oyster Bay", "Pacific Palisades", "Pacifica", "Painted Post", "Palmetto Bay", "Palo Alto", "Palos Verdes Estates", "Park Ridge", "Parkland", "Parkville", "Parlin", "Parsippany", "Pasadena", "Patchogue", "Pawcatuck", "Pearland", "Pebble Beach", "Peirmont", "Pelham Manor", "Penfield", "Penn Valley", "Pennington", "Pennsburg", "Pepper Pike", "Perth Amboy", "Petaluma", "Pflugerville", "Pfulgerville", "Philadelphia", "Phoenix", "Phoenixville", "Picayune", "Piedmont", "Pierceton", "Pikesville", "Pine Meadow", "Pipersville", "Piscataway", "Pittsboro", "Pittsburg", "Pittsburgh", "Pittsfield", "Pittsford", "Pittstown", "Placentia", "Plainfield", "Plainsboro", "Plainview", "Plano", "Plant City", "Playa Del Rey", "Pleasant Hill", "Pleasant Prairie", "Pleasanton", "Plymouth", "Point Richmond", "Pomona", "Pompton Lakes", "Porollo Valley", "Port Angeles", "Port Jefferson", "Port Moody", "Port Orchard", "Portland", "Portola Valley", "Potomac", "Pottstown", "Poughkeepsie", "Poway", "Powell", "Preston", "Princeton", "Princeton Junction", "Prospect", "Providence", "Pt. Richmond", "Pullman", "Purchase", "Quakertown", "Queensbury", "Quincy", "Radnor", "Rahway", "Raleigh", "Ramona", "Ramsey", "Rancho Cordova", "Rancho Mirage", "Rancho Santa Fe", "Rancho Santa Margarita", "Rancho Sante Fe", "Randolph", "Raritan", "Raynham", "Reading", "Red Bank", "Red Lion", "Redlands", "Redmond", "Redwood City", "Redwood Court", "Redwood Shores", "Reisterstown", "Reno", "Rensselaer", "Renton", "Research Triangle Park", "Rexford", "Richardson", "Richboro", "Richfield", "Richland", "Richmond", "Ridgefield", "Ridgewood", "Ridgway", "Ridley Park", "River Forest", "Riverdale", "Riverside", "Robbinsville", "Rochester", "Rockaway", "Rockland", "Rockville", "Rockwall", "Roland", "Rolling Hills", "Rolling Hills Estates", "Rosemont", "Roseville", "Roslindale", "Roswell", "Rougemont", "Round", "Rowley", "Roxbury Crossing", "Royal Oak", "Royersford", "Rumson", "Ruskin", "Rutherford", "Ruxton", "Rydal", "Rye", "S. Setauket", "Sacramento", "Saint Louis", "Saint Paul", "Salem", "Saline", "Salt Lake City", "Sammamish", "San Antonio", "San Bernardino", "San Bruno", "San Carlos", "San Clemente", "San Deigo", "San Diego", "San Francicso", "San Francisco", "San Fransisco", "San Gabriel", "San Jose", "San Juan", "San Juan Capistrano", "San Leandro", "San Luis Obispo", "San Marcos", "San Marino", "San Mateo", "San Pablo", "San Rafael", "San Ramon", "Sandy Hook", "Sandy Spring", "Santa Ana", "Santa Barbara", "Santa Clara", "Santa Clarita", "Santa Cruz", "Santa Fe", "Santa Fe Spring", "Santa Fe Springs", "Santa Monica", "Santa Paula", "Santa Rosa", "Santa Rosa Valley", "Saratoga", "Saratoga Springs", "Sausalito", "Sayville", "Scarborough", "Schenectady", "Scituate", "Scotch Plains", "Scotia", "Scottsdale", "Sea Cliff", "Seal Cove", "Seattle", "Sebastopol", "Sedona", "Setauket", "Severna Park", "Sewickley", "Shaker Heights", "Shaker Hts.", "Shaker Mts", "Sharon", "Shelburne", "Shepherdston", "Sherborn", "Sherman Oaks", "Sherwood", "Shoreline", "Shoreview", "Shorline", "Short Hills", "Shreveport", "Shrewsbury", "Sicklerville", "Sierra Madre", "Silver Spring", "Silver Springs", "Simi Valley", "Sioux Falls", "Skillman", "Sleepy Hollow", "Slingerlands", "Smithtown", "Smyrna", "Snohomish", "Solana Beach", "Solon", "Somerset", "Somerville", "Sonoma", "Souderton", "Sounderton", "South Bend", "South Boston", "South Chatham", "South Hamilton", "South Lake Tahoe", "South Orange", "South Pasadena", "South Pasedena", "South Plainfield", "South San Francisco", "Southborough", "Southbridge", "Southfield", "Southlake", "Southwest Harbor", "Sparks", "Sparks Glencoe", "Sparta", "Spring", "Spring Hill", "Springfield", "St. Augustine", "St. George", "St. James", "St. Louis", "St. Louis Park", "St. Michael", "St. Paul", "St. Petersburg", "Stamford", "Standford", "Stanford", "Staten Island", "Sterling", "Stevensville", "Stewartsville", "Stillwater", "Stirling", "Stone Mountain", "Stoneham", "Stonington", "Stony Brook", "Stoughton", "Stow", "Stratford", "Studio City", "Sudbury", "Sugar Land", "Summit", "Summti", "Sun City", "Sun Prairie", "Sunderland", "Sunnyvale", "Superior Township", "Sutton", "Swampscott", "Swanton", "Sylvania", "Syracuse", "Takoma Park", "Tallahassee", "Tampa", "Tarrytown", "Tarzana", "Taunton", "Teaneck", "Temecula", "Tempe", "Temple", "Tenafly", "Tequesta", "Tewksbury", "The Woodlands", "Thousand Oaks", "Tiburon", "Tigard", "Timonium", "Titusville", "Topsfield", "Toronto", "Towaco", "Towson", "Troy", "Truckee", "Tualatin", "Tucson", "Tumwater", "Tunbridge", "Turnersville", "Turtle Creek", "Tuscaloosa", "Tuscon", "Tustin", "Twin Falls", "Twinsburg", "Two Harbors", "Tysons", "Umatilla", "Union Beach", "Union City", "University Heights", "University Park", "Upper Arlington", "Upton", "Urbana", "Urbandale", "Uxbridge", "Vacaville", "Valencia", "Vallejo", "Valley Cottage", "Valley Forge", "Vancouver", "Vancover", "Venice", "Ventura", "Vernon Hills", "Verona", "Villanova", "Virginia Beach", "Vista", "Volo", "W. Henrietta", "Waban", "Wadsworth", "Wakefield", "Walkersville", "Wallingford", "Walnut", "Walnut Creek", "Waltham", "Wappingers Falls", "Ware", "Warren", "Warrington", "Warsaw", "Warwick", "Washington", "Washington Crossing", "Washington Grove", "Watchung", "Watertown", "Watervliet", "Watkinsville", "Waunakee", "Wayland", "Wayne", "Waynesville", "Wayzata", "Webster", "Webster Groves", "Wellesley", "Wells", "Wenham", "West Babylon", "West Bloomfield", "West Chester", "West Covina", "West Friendship", "West Hartford", "West Hills", "West Lafayette", "West Lebanon", "West Melbourne", "West Monroe", "West Newbury", "West Newton", "West Nyack", "West Orange", "West Palm Beach", "West Plains", "West Roxbury", "West Windsor", "Westborough", "Western Springs", "Westfield", "Westford", "Westlake", "Westminister", "Westminster", "Weston", "Westwood", "Wexford", "Weymouth", "Wheaton", "Whippany", "White Bear Lake", "White Marsh", "White Plains", "Whitehouse Station", "Whitmore Lake", "Wickliffe", "Wilbraham", "Williamsville", "Wilmette", "Wilmington", "Wilton", "Wimberly", "Winchester", "Windham", "Winfield", "Winstom Salem", "Winston Salem", "Winston-Salem", "Winter Park", "Winters", "Woburn", "Woodbridge", "Woodbury", "Woodinville", "Woodland Hills", "Woodland Park", "Woodside", "Woodstock", "Worcester", "Worchester", "Worthington", "Wrentham", "Wyckoff", "Wyndmoor", "Wynnewood", "Xenia", "Yardley", "Yorba Linda", "York", "Yorktown Heights", "Ypsilanti", "Zachary", "Zephyr Cove", "Zionsville", "Zionville"
    ]
#-----------------------------------------------------------------------------
#   清理功能
#-----------------------------------------------------------------------------
#  用來正規化日期
def normalization_date(list_need_to_normalization):
    temp_list = []
    for i in list_need_to_normalization:
        if i == 'NULL':
            temp_list.append('NULL')
        else:
            for i_2 in dic_month:
                if i_2 in i :
                    if i[-8] != ' ':
                        temp_list.append(i[-4:-1] + i[-1] + '-' + dic_month[i_2] + '-' + i[-8] + i[-7])
                    else:
                        temp_list.append(i[-4:-1] + i[-1] + '-' + dic_month[i_2] + '-0' + i[-7])
    return temp_list
#  有的月份是簡寫
def normalization_date_2(list_need_to_normalization):
    temp_list = []
    for i in list_need_to_normalization:
        if i == 'NULL':
            temp_list.append('NULL')
        else:
            for i_2 in dic_month_2:
                if i_2 in i :
                    if i[-8] != ' ':
                        temp_list.append(i[-4:-1] + i[-1] + '-' + dic_month_2[i_2] + '-' + i[-8] + i[-7])
                    else:
                        temp_list.append(i[-4:-1] + i[-1] + '-' + dic_month_2[i_2] + '-0' + i[-7])
    return temp_list
def normalization_month(list_need_to_normalization):
    temp_list = []
    for i in list_need_to_normalization:
        if i != 'NULL':
            temp_list_2 = []
            for i_2 in i:
                temp_list_2.append(dic_month[i_2])
            temp_list.append(temp_list_2)
        else:
            temp_list.append('NULL')
    return temp_list
def normalization_month_2(list_need_to_normalization):
    temp_list = []
    for i in list_need_to_normalization:
        if i != 'NULL':
            temp_list_2 = []
            for i_2 in i:
                temp_list_2.append(dic_month_2[i_2])
            temp_list.append(temp_list_2)
        else:
            temp_list.append('NULL')
    return temp_list
#  用來切片 list
def list_to_list(big_list, small_list, regex,  words_need_to_delete):
    for i in big_list:
        m = re.findall(regex, i)
        if m != []:
            temp_m = m[0].replace(words_need_to_delete, '')
            small_list.append(temp_m)
        else:
            small_list.append('NULL')
#  客製index
def un_zip_index_list(aim_list, index_list_need_to_unzip):
    temp_list = []
    num = 0
    for i in aim_list:
        if i != 'NULL':
            num_2 = 0
            while num_2 < len(i):
                temp_list.append(index_list_need_to_unzip[num])
                num_2 += 1
            num +=  1
        else:
            temp_list.append(index_list_need_to_unzip[num])
            num +=  1
    return temp_list
#  [[],[],[],....[]] ---> []
def un_zip_list(list_need_to_unzip):
    temp_list = []
    for i in list_need_to_unzip:
        if i != 'NULL':
            for i_2 in i:
                temp_list.append(i_2)
        else:
            temp_list.append(i)
    return temp_list
#  正規化 State Country
def normalization_country(city_list, country_list):
    temp_list = []  #  country
    temp_list_2 = []  #  state
    k = 0
    for i in un_zip_list(city_list):
        if i in us_country_list:
            temp_list.append('US')
            temp_list_2.append(un_zip_list(country_list)[k])
        else:
            temp_list.append(un_zip_list(country_list)[k])
            if i != 'NULL':
                temp_list_2.append('NULL')
            else:
                temp_list_2.append('NULL')
        k += 1
    return [temp_list, temp_list_2]