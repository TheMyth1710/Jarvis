import bot
import os
import operator as op
import requests, json
from urllib.request import urlopen
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
country_codes = {"BD": "Bangladesh", "BE": "Belgium", "BF": "Burkina Faso", "BG": "Bulgaria", "BA": "Bosnia and Herzegovina", "BB": "Barbados", "WF": "Wallis and Futuna", "BL": "Saint Barthelemy", "BM": "Bermuda", "BN": "Brunei", "BO": "Bolivia", "BH": "Bahrain", "BI": "Burundi", "BJ": "Benin", "BT": "Bhutan", "JM": "Jamaica", "BV": "Bouvet Island", "BW": "Botswana", "WS": "Samoa", "BQ": "Bonaire, Saint Eustatius and Saba ", "BR": "Brazil", "BS": "Bahamas", "JE": "Jersey", "BY": "Belarus", "BZ": "Belize", "RU": "Russia", "RW": "Rwanda", "RS": "Serbia", "TL": "East Timor", "RE": "Reunion", "TM": "Turkmenistan", "TJ": "Tajikistan", "RO": "Romania", "TK": "Tokelau", "GW": "Guinea-Bissau", "GU": "Guam", "GT": "Guatemala", "GS": "South Georgia and the South Sandwich Islands", "GR": "Greece", "GQ": "Equatorial Guinea", "GP": "Guadeloupe", "JP": "Japan", "GY": "Guyana", "GG": "Guernsey", "GF": "French Guiana", "GE": "Georgia", "GD": "Grenada", "GB": "United Kingdom", "GA": "Gabon", "SV": "El Salvador", "GN": "Guinea", "GM": "Gambia", "GL": "Greenland", "GI": "Gibraltar", "GH": "Ghana", "OM": "Oman", "TN": "Tunisia", "JO": "Jordan", "HR": "Croatia", "HT": "Haiti", "HU": "Hungary", "HK": "Hong Kong", "HN": "Honduras", "HM": "Heard Island and McDonald Islands", "VE": "Venezuela", "PR": "Puerto Rico", "PS": "Palestinian Territory", "PW": "Palau", "PT": "Portugal", "SJ": "Svalbard and Jan Mayen", "PY": "Paraguay", "IQ": "Iraq", "PA": "Panama", "PF": "French Polynesia", "PG": "Papua New Guinea", "PE": "Peru", "PK": "Pakistan", "PH": "Philippines", "PN": "Pitcairn", "PL": "Poland", "PM": "Saint Pierre and Miquelon", "ZM": "Zambia", "EH": "Western Sahara", "EE": "Estonia", "EG": "Egypt", "ZA": "South Africa", "EC": "Ecuador", "IT": "Italy", "VN": "Vietnam", "SB": "Solomon Islands", "ET": "Ethiopia", "SO": "Somalia", "ZW": "Zimbabwe", "SA": "Saudi Arabia", "ES": "Spain", "ER": "Eritrea", "ME": "Montenegro", "MD": "Moldova", "MG": "Madagascar", "MF": "Saint Martin", "MA": "Morocco", "MC": "Monaco", "UZ": "Uzbekistan", "MM": "Myanmar", "ML": "Mali", "MO": "Macao", "MN": "Mongolia", "MH": "Marshall Islands", "MK": "Macedonia", "MU": "Mauritius", "MT": "Malta", "MW": "Malawi", "MV": "Maldives", "MQ": "Martinique", "MP": "Northern Mariana Islands", "MS": "Montserrat", "MR": "Mauritania", "IM": "Isle of Man", "UG": "Uganda", "TZ": "Tanzania", "MY": "Malaysia", "MX": "Mexico", "IL": "Israel", "FR": "France", "IO": "British Indian Ocean Territory", "SH": "Saint Helena", "FI": "Finland", "FJ": "Fiji", "FK": "Falkland Islands", "FM": "Micronesia", "FO": "Faroe Islands", "NI": "Nicaragua", "NL": "Netherlands", "NO": "Norway", "NA": "Namibia", "VU": "Vanuatu", "NC": "New Caledonia", "NE": "Niger", "NF": "Norfolk Island", "NG": "Nigeria", "NZ": "New Zealand", "NP": "Nepal", "NR": "Nauru", "NU": "Niue", "CK": "Cook Islands", "XK": "Kosovo", "CI": "Ivory Coast", "CH": "Switzerland", "CO": "Colombia", "CN": "China", "CM": "Cameroon", "CL": "Chile", "CC": "Cocos Islands", "CA": "Canada", "CG": "Republic of the Congo", "CF": "Central African Republic", "CD": "Democratic Republic of the Congo", "CZ": "Czech Republic", "CY": "Cyprus", "CX": "Christmas Island", "CR": "Costa Rica", "CW": "Curacao", "CV": "Cape Verde", "CU": "Cuba", "SZ": "Swaziland", "SY": "Syria", "SX": "Sint Maarten", "KG": "Kyrgyzstan", "KE": "Kenya", "SS": "South Sudan", "SR": "Suriname", "KI": "Kiribati", "KH": "Cambodia", "KN": "Saint Kitts and Nevis", "KM": "Comoros", "ST": "Sao Tome and Principe", "SK": "Slovakia", "KR": "South Korea", "SI": "Slovenia", "KP": "North Korea", "KW": "Kuwait", "SN": "Senegal", "SM": "San Marino", "SL": "Sierra Leone", "SC": "Seychelles", "KZ": "Kazakhstan", "KY": "Cayman Islands", "SG": "Singapore", "SE": "Sweden", "SD": "Sudan", "DO": "Dominican Republic", "DM": "Dominica", "DJ": "Djibouti", "DK": "Denmark", "VG": "British Virgin Islands", "DE": "Germany", "YE": "Yemen", "DZ": "Algeria", "US": "United States", "UY": "Uruguay", "YT": "Mayotte", "UM": "United States Minor Outlying Islands", "LB": "Lebanon", "LC": "Saint Lucia", "LA": "Laos", "TV": "Tuvalu", "TW": "Taiwan", "TT": "Trinidad and Tobago", "TR": "Turkey", "LK": "Sri Lanka", "LI": "Liechtenstein", "LV": "Latvia", "TO": "Tonga", "LT": "Lithuania", "LU": "Luxembourg", "LR": "Liberia", "LS": "Lesotho", "TH": "Thailand", "TF": "French Southern Territories", "TG": "Togo", "TD": "Chad", "TC": "Turks and Caicos Islands", "LY": "Libya", "VA": "Vatican", "VC": "Saint Vincent and the Grenadines", "AE": "United Arab Emirates", "AD": "Andorra", "AG": "Antigua and Barbuda", "AF": "Afghanistan", "AI": "Anguilla", "VI": "U.S. Virgin Islands", "IS": "Iceland", "IR": "Iran", "AM": "Armenia", "AL": "Albania", "AO": "Angola", "AQ": "Antarctica", "AS": "American Samoa", "AR": "Argentina", "AU": "Australia", "AT": "Austria", "AW": "Aruba", "IN": "India", "AX": "Aland Islands", "AZ": "Azerbaijan", "IE": "Ireland", "ID": "Indonesia", "UA": "Ukraine", "QA": "Qatar", "MZ": "Mozambique"}
alphabets = [" ","a",'b','c','d','e','f','g','h','i','j'',k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
operations={'squared':'**2','cubed':'**3','add':"+",'addition':"+",'plus':"+",'multiply':'x','into':'x','multiplied by':'x',"multiply":'x',"product":'x',"divided by":"/","divide":"/","div":"/",'mod':'%','remainder':'%','modulus':'%'}
nums = ["0",'1','2','3','4','5','6','7','8','9','+','-','x','/','.','**','%']
def get_month(month_int):
 global months
 if type(month_int) == int:
    if month_int > 0 and month_int<= 12:
        current_month = months[month_int-1]
        #print("The month is:",current_month)
        return current_month
 else:
     print("Please specify a value between 1 - 12 to get the desired month!")
     print(f"You entered '{month_int}' which is not an acceptable input!")


def repeat():
    while True:
        bot.query = bot.userCommand()
        bot.speak(bot.query)  
        if 'exit now' in bot.query or 'quit now' in bot.query:
            break
days = ["first", "second", "third","fourth","fifth","sixth","seventh","eighth","nineth","tenth","eleventh","twelfth","thirteenth","fourteenth","fifteenth","sixteenth","seventeenth","eighteenth","nineteenth","twentieth","twenty first","twenty second","twenty third","twenty fourth","twenty fifth","twenty sixth","twenty seventh","twenty eigth","twenty nineth","thirtieth","thirty first"]  

def get_day(day_int):
    global days
    if type(day_int) == int:
        if day_int > 0 and day_int <=31:
            current_day = days[day_int-1]
            #print("The day is:",current_day)
            return current_day
    else:
        print("Please specify a value between 1 - 31 to get the desired day!")
        print(f"You entered '{day_int} which is not an acceptable input!")

#LOCATION FUNCTION
def get_location(input):
    myURL = urlopen('http://ipinfo.io/json')
    data = json.load(myURL)

    IP=data['ip']
    org=data['org']
    city = data['city']
    country=data['country']
    region=data['region']
    if "ip" in input:
        return IP
    if "org" in input:
        return org
    if "city" in input:
        return city
    if "country" in input:
        return country
    if "region" in input:
        return region

#WEATHER FUNCTION
def weather(input):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = get_location("city")
    API_KEY = "28f1923a522ef499c716231b9139dce8"
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    # HTTP request
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = round(main['temp'] - 273.15,1)
        humidity = main['humidity']
        pressure = main['pressure']
        report = data['weather'][0]['description']
        if "temperature" in input:
         return temperature
        if "humidity" in input:
         return humidity
        if "pressure" in input:
         return pressure
        if "report" in input:
         return report
    else:
        # showing the error message
        print("Error in the HTTP request")
def hypixel_mode(query:list):
    api_key = '9a9dfe41-1e50-4c3b-8eb5-848484513929'
    mode = query[-1]
    del query[-1]
    ign = ''.join(query).casefold()
    msg = ''
    if ign == 'me':
        ign = 'mastermudith'
    try:
        mojang_api = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{ign}').json()
    except:
        mojang_api = {'error':'Not Found'}
    try:
        if mojang_api['error'] == 'Not Found':
            msg = "That's not a valid username try again!"
    except KeyError:
        proper_ign = mojang_api['name']
        uuid = mojang_api['id']
        if mode in ['bedwars','bedwar','bw','bad words','bad was','bad boss','bed']:
            data = requests.get(f'https://api.hypixel.net/player?key={api_key}&uuid={uuid}').json()
            if data['success']: 
                if data['player'] is not None:
                    stats = data['player']['stats']['Bedwars']
                    star = data['player']['achievements']['bedwars_level']
                    fkdr = round(stats['final_kills_bedwars']/stats['final_deaths_bedwars'],1)
                    wlr = round(stats['wins_bedwars']/stats['losses_bedwars'],1)
                    kdr = round(stats['kills_bedwars']/stats['deaths_bedwars'],1)
                    bblr = round(stats['beds_broken_bedwars']/stats['beds_lost_bedwars'],1)
                    msg = f'Showing bedwars stats for {proper_ign}: Star {star}, FKDR {fkdr}, WLR {wlr}, KDR {kdr}, BBLR {bblr}'
                    print(msg)
                else:
                    msg = "That's not a valid username, try again!"
            else:
                msg = "Couldn't access the Hypixel API!"
        else:
            msg =f"Please enter a valid mode! You entered {mode}."  
    return msg
def str_to_num(text):
    text = text.replace("left bracket".casefold(),"(").replace("right bracket".casefold(),")").replace("hyphen","-").replace("exclamation mark","!").replace("question mark","?").replace("full stop",".").replace("comma",",").replace("hastag","#").replace("underscore","_")
    nums = {"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9","ten":"10","eleven":"11","twelve":"12","thirteen":"13","fifteen":"15","twenty":"20","thirty":"30","forty":"40","fifty":"50"}
    #Replacing text to nums
    for k,v in nums.items():
    #Teen...
        if f'{k}teen' in text:
            text = text.replace(f"{k}teen",f"1{v}")
        if f"{k}ty" in text:
            text = text.replace(f"{k}ty",f"{v}0")
        if k in text:
            text = text.replace(k,v)   
    return text