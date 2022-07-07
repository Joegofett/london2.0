import statsapi


baseurl = statsapi.BASE_URL

# print(statsapi.ENDPOINTS)
standings = statsapi.standings_data(include_wildcard=True)


# print(standings[201])


# for info in standings:
#     print(info)
#     print("___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
#     print(standings[info])
#     print("_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________")
def organizingstandingstoread(divstandings):
    final_form = {}
    for info in divstandings:
        final_form[int(info['div_rank'])] = info

    return final_form


def ALWestDiscord():
    ALWaststandings = {}
    ALWaststandings = standings[200]
    teams     = ALWaststandings['teams']
    first_form = organizingstandingstoread(teams)
    final_form = dictionaryCleaning(first_form)
    return final_form



def ALEastDiscord():
    ALEaststandings = {}
    ALEaststandings = standings[201]
    teams     = ALEaststandings['teams']
    first_form = organizingstandingstoread(teams)
    final_form = dictionaryCleaning(first_form)
    return final_form



def ALCentralDiscord():
    ALcentralstandings = {}
    ALcentralstandings = standings[202]
    teams     = ALcentralstandings['teams']
    first_form = organizingstandingstoread(teams)
    final_form = dictionaryCleaning(first_form)
    return final_form



def NLWestDiscord():
    ALWeststandings = {}
    ALWeststandings = standings[203]
    teams     = ALWeststandings['teams']
    first_form = organizingstandingstoread(teams)
    final_form = dictionaryCleaning(first_form)
    return final_form





def NLEastDiscord():
    aleaststandings = {}
    aleaststandings = standings[204]
    teams     = aleaststandings['teams']
    first_form = organizingstandingstoread(teams)
    final_form = dictionaryCleaning(first_form)
    return final_form


def NLCentralDiscord():
    NLCentralstandings = {}
    NLCentralstandings = standings[205]
    teams     = NLCentralstandings['teams']
    first_form = organizingstandingstoread(teams)
    final_form = dictionaryCleaning(first_form)
    return final_form

def ALWest():
    ALWaststandings = {}
    ALWaststandings = standings[200]
    teams     = ALWaststandings['teams']
    first_form = organizingstandingstoread(teams)
    final_form = dictionaryCleaning(first_form)
    return final_form



def ALEast():
    ALEaststandings = {}
    ALEaststandings = standings[201]
    teams     = ALEaststandings['teams']
    first_form = organizingstandingstoread(teams)
    final_form = dictionaryCleaning(first_form)
    return final_form



def ALCentral():
    ALcentralstandings = {}
    ALcentralstandings = standings[202]
    teams     = ALcentralstandings['teams']
    first_form = organizingstandingstoread(teams)
    final_form = dictionaryCleaning(first_form)
    return final_form



def NLWest():
    ALWeststandings = {}
    ALWeststandings = standings[203]
    teams     = ALWeststandings['teams']
    first_form = organizingstandingstoread(teams)
    final_form = dictionaryCleaning(first_form)
    return final_form


def NLEast():
    aleaststandings = {}
    aleaststandings = standings[204]
    teams     = aleaststandings['teams']
    first_form = organizingstandingstoread(teams)
    final_form = dictionaryCleaning(first_form)
    return final_form


def NLCentral():
    NLCentralstandings = {}
    NLCentralstandings = standings[205]
    teams     = NLCentralstandings['teams']
    first_form = organizingstandingstoread(teams)
    final_form = dictionaryCleaning(first_form)
    return final_form



def LLBattingAvg():
    first_form = statsapi.league_leader_data('BattingAverage')
    final_form = stringCleaning(first_form)
    return final_form


def LLERALeader():
    first_form = statsapi.league_leader_data('earnedRunAverage')
    final_form = stringCleaning(first_form)
    return final_form


def OnBaseLeaders():
    first_form = statsapi.league_leader_data('onBase')
    final_form = stringCleaning(first_form)
    return final_form



def OnBasePlusSlugingLeaders():
    first_form = statsapi.league_leader_data('onBasePlusSlugging')
    final_form = stringCleaning(first_form)
    return final_form



def HomeRunsLeaders():
    first_form = statsapi.league_leader_data('homeRun')
    final_form = stringCleaning(first_form)
    print(final_form)
    return final_form

def WinsLeader():
    first_form = statsapi.league_leader_data('wins')
    final_form = stringCleaning(first_form)
    return final_form


# def SavesLeader():
#     first_form = statsapi.league_leader_data('saves')
#     print(final_form)

#     return final_form


def SavesLeader():
    first_form = statsapi.league_leader_data('saves')
    final_form = stringCleaning(first_form)
    # final_form = f"{practice[0]} {practice[1]} {practice[2]} {practice[3]} {practice[4]} {practice[5]} {practice[6]} {practice[7]} {practice[8]} {practice[9]}"
    return final_form


# def HoldLeaders():
#     final_form = statsapi.league_leader_data('holds')

#     return final_form

# must be said like spring cleaning
def stringCleaning(data):
    final_form = ""
    first_form = ""
    for info in data:
        first_form += str(info)
        new = first_form.strip("[")
        test = new.replace("'", "")
        practice = test.replace("]", " ")
        final_replace= practice.replace(",",":")
        final_form = final_replace.replace('[', "\n")
    return final_form

def moreCleaning(data):
    first_form = data.replace("{", "")
    final_form = first_form.replace("}", " \n ")
    return final_form


def dictionaryCleaning(data):
    first_form = ""
    for info in data:
        print(data[info])
        new_data = str(data[info])
        first_form += new_data
        second_form = stringCleaning(first_form)
        final_form = moreCleaning(second_form)
    return final_form