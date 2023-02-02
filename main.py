from dotenv import load_dotenv
from distutils.command.upload import upload
from bettercomm import uploadGJComment
import time,requests,random,os,base64
from json import loads
from threading import Thread
from better_profanity import profanity

envedit = input("Edit Configuration? (Yes/No): ")

if envedit == "Yes":
    os.system("nano .env")
elif envedit == "yes":
    os.system("nano .env")
else:
    os.system("echo 'WARNING! If you set nothing, It will error.'")
    os.system("sleep 2")


load_dotenv()

un = os.getenv("USERNAME")
pw = os.getenv("PASSWORD")
lvlid = os.getenv("LEVELID")

os.system("clear")
print("Bot started on level ID "+lvlid+" on the account "+un)

def commands(level):
    url=f"http://gdbrowser.com/api/comments/{level}?count=1"
    r=loads(requests.get(url).text)[0]
    u=r['username']
    com=r['content']
    perc=random.randint(1,100)
    bannedUsers=open("./Autoworks/bans.txt").read().splitlines()
    superusers=open("./Autoworks/superusers.txt").read().splitlines()

    yesNo=['Yes', 'No']
    ben=['Ben?', 'No.', 'Yes?', 'Oh-ho-ho!', 'Na-na-na-na-na.', 'Eurgh.']
    ships=['you hit an iceberg and die', 'you die due to food poisoning', 'you took an untrusted covid vaccine and suddenly died', 'you lived', 'you found your goofy ahh uncle and died', 'quandale dingle dipped you in hot oil and died', 'a furry jumped on you...... you died', 'pablo escobar shot you twenty times', '[RESPONSE NOT FOUND]', 'you woke up and it was a dream, and died', 'tweeted and got ratioed, then died', 'a phycho toddler killed you', '*windows xp shutdown sound*', 'joe biden was the driver, you died', 'got banned for violating the dress code', 'got in a crowd of 4chan users, you died', 'nikocado avocado ate you', 'ishowspeed yelled at you, you died of fear', 'got trolled, you died', 'someone posted fanart of your oc to e621', 'twitter cancelled you, suddenly died', 'the fbi made you eat pigs until you told them where the bodies were', 'you had a good time... NOT MY FAULT YOUR ALL DIRTY MINDED', 'got cbt, then died', 'edp445 was baking cupcakes, you drowned instead', 'twomad flopped on you saying goodnight girl', 'your mom grounded you', '404, response not found', 'the government was eating pickles', 'you farded and died', 'got a liver transplant with a tiktoker', 'nikocado avocado inhaled you, you died', 'freddy fazbear belly flopped on you and died', 'got kicked in the thighs by a naruto wannabe', 'thought this was a relationship command', 'got attacked by big fat men', '/e danced', 'got hit by baller and died', 'micheal jackson beated you with a stick', 'peter griffin suffocated you by his belly', 'someone got a glock from the rari', 'suddenly ankha zone plays', 'your uncle laughs from behind you', 'got noscoped by a call of duty player', 'furries started kissing you, did you even die?', 'npesta screamed at you']

    if(com.startswith("/hello")):
        try:
            uploadGJComment(un,pw,f"Hello, {u}",perc,level)
        except:
            return
    elif(com.startswith("/unban")):
        c=com.split("/unban ")
        unbanuser=c[1]
        try:
            if u in superusers:
                uploadGJComment(un,pw,f"@{u}, Unbanned {unbanuser}!",perc,level)
                time.sleep(4)
                os.system('gawk -i inplace !/'+unbanuser+'/ ./Autoworks/bans.txt')
            else:
                uploadGJComment(un,pw,f"@{u}, Permission Denied: Not in Array /listsu",perc,level)
        except:
            return
    elif(com.startswith("/ban")):
        c=com.split("/ban ")
        banuser=c[1]
        try:
            if u in superusers:
                uploadGJComment(un,pw,f"@{u}, Banned {banuser}!",perc,level)
                time.sleep(4)
                os.system('echo '+banuser+' >> ./Autoworks/bans.txt')
            else:
                uploadGJComment(un,pw,f"@{u}, Permission Denied: Not in Array /listsu",perc,level)
        except:
            return
    elif(com.startswith("/checkban")):
        c=com.split("/checkban ")
        banchk=c[1]
        try:
            if u in superusers:
                if banchk in bannedUsers:
                    uploadGJComment(un,pw,f"@{u}, Banned.",perc,level)
                else:
                    uploadGJComment(un,pw,f"@{u}, Not Banned.",perc,level)
            else:
                uploadGJComment(un,pw,f"@{u}, Permission Denied: Not in Array /listsu",perc,level)
        except:
            return
    elif(com.startswith("/cool")):
        try:
            if u in bannedUsers:
                uploadGJComment(un,pw,f"@{u}, Banned for Violation of Autoworks Rules.",perc,level)
            else:
                uploadGJComment(un,pw,f"@{u}, You are {perc}% cool!",perc,level)
        except:
            return
    elif(com.startswith("/poggers")):
        try:
            if u in bannedUsers:
                uploadGJComment(un,pw,f"@{u}, Banned for Violation of Autoworks Rules.",perc,level)
            else:
                uploadGJComment(un,pw,f"@{u}, You are {perc}% poggers",perc,level)
        except:
            return
    elif(com.startswith("/yesOrNo")):
        yN=random.choice(yesNo)
        try:
            if u in bannedUsers:
                uploadGJComment(un,pw,f"@{u}, Banned for Violation of Autoworks Rules.",perc,level)
            else:
                uploadGJComment(un,pw,f"@{u}, {yN}",perc,level)
        except:
            return
    elif(com.startswith("/say")):
        c=com.split("/say ")
        ccom = profanity.censor(c[1], '*')
        try:
            if u in bannedUsers:
                uploadGJComment(un,pw,f"@{u}, Banned for Violation of Autoworks Rules.",perc,level)
            else:
                uploadGJComment(un,pw,f"@{u}, {ccom}",perc,level)
        except:
            return
    elif(com.startswith("/poll")):
        c=com.split("/poll ")
        cc=c[1]
        try:
            if u in bannedUsers:
                uploadGJComment(un,pw,f"@{u}, Banned for Violation of Autoworks Rules.",perc,level)
            else:
                uploadGJComment(un,pw,f"{u}'s Poll > {cc} | Vote with Likes/Dislikes",perc,level)
        except:
            return
    elif(com.startswith("/help")):
        try:
            if u in bannedUsers:
                uploadGJComment(un,pw,f"@{u}, Banned for Violation of Autoworks Rules.",perc,level)
            else:
                uploadGJComment(un,pw,f"@{u}, /help usage: /h_[cmdlist] (Lists: fun, gd) - SU Help: /su",perc,level)
        except:
            return
    elif(com.startswith("/h_fun")):
        try:
            if u in bannedUsers:
                uploadGJComment(un,pw,f"@{u}, Banned for Violation of Autoworks Rules.",perc,level)
            else:
                uploadGJComment(un,pw,f"@{u}, /say | /yesOrNo | /hello | /cool | /poll | /talkingben | /ship | /furry",perc,level)
        except:
            return
    elif(com.startswith("/h_info")):
        try:
            if u in bannedUsers:
                uploadGJComment(un,pw,f"@{u}, Banned for Violation of Autoworks Rules.",perc,level)
            else:
                uploadGJComment(un,pw,f"@{u}, /listsu",perc,level)
        except:
            return
    elif(com.startswith("/h_gd")):
        try:
            if u in bannedUsers:
                uploadGJComment(un,pw,f"@{u}, Banned for Violation of Autoworks Rules.",perc,level)
            else:
                uploadGJComment(un,pw,f"@{u}, /gd | /pointercrate",perc,level)
        except:
            return
    elif(com.startswith("/h_other")):
        try:
            if u in bannedUsers:
                uploadGJComment(un,pw,f"@{u}, Banned for Violation of Autoworks Rules.",perc,level)
            else:
                uploadGJComment(un,pw,f"@{u}, /code",perc,level)
        except:
            return
    elif(com.startswith("/stats")):
        c=com.split("/stats ")
        try:
            if u in bannedUsers:
                uploadGJComment(un,pw,f"@{u}, Banned for Violation of Autoworks Rules.",perc,level)
            else:
                cc=c[1]
                shtats=loads(requests.get(f"http://gdbrowser.com/api/profile/{cc}").text)
                ccc=f"@{u}, {c[1]} has {shtats['stars']} Stars, {shtats['diamonds']} Diamonds, {shtats['coins']} Coins, {shtats['userCoins']} User Coins, {shtats['demons']} Demons and {shtats['cp']} Creator Points."
                uploadGJComment(un,pw,f"{ccc}",perc,level)
        except:
            return
    elif(com.startswith("/pointercrate")):
        c=com.split("/pointercrate ")
        d=loads(requests.get("http://pointercrate.com/api/v2/demons/listed?limit=100").text)
        d2=loads(requests.get("http://pointercrate.com/api/v2/demons/listed?after=100").text)
        d3=d+d2
        try:
            if u in bannedUsers:
                uploadGJComment(un,pw,f"@{u}, Banned for Violation of Autoworks Rules.",perc,level)
            else:
                cc=int(c[1])-1
                ccc=f"#{d3[cc]['position']}: {d3[cc]['name']} by {d3[cc]['publisher']['name']}, verified by {d3[cc]['verifier']['name']}"
                uploadGJComment(un,pw,f"@{u} {ccc}",perc,level)
        except:
            return
    elif(com.startswith("/ai")):
        c=com.split("/ai ")
        try:
            if u in bannedUsers:
                uploadGJComment(un,pw,f"@{u}, Banned for Violation of Autoworks Rules.",perc,level)
            else:
                resp = requests.get("http://api.brainshop.ai/get?bid=169422&key=4GCemcdYgy50PlZ2&uid=0&msg="+c[1], headers={'Accept': 'application/json'})
                jsonResp = resp.json()
                airesp = jsonResp["cnt"]
                uploadGJComment(un,pw,f"{u}, {airesp}",perc,level)
        except:
            return
    elif(com.startswith("/talkingben")):
        tb=random.choice(ben)
        try:
            if u in bannedUsers:
                uploadGJComment(un,pw,f"@{u}, Banned for Violation of Autoworks Rules.",perc,level)
            else:
                uploadGJComment(un,pw,f"@{u}, {tb}",perc,level)
        except:
            return
    elif(com.startswith("/code")):
        try:
            if u in bannedUsers:
                uploadGJComment(un,pw,f"@{u}, Banned for Violation of Autoworks Rules.",perc,level)
            else:
                uploadGJComment(un,pw,f"@{u}, Source Code: cutt.ly/T04h1fl",perc,level)
        except:
            return
    elif(com.startswith("/su")):
        try:
            if u in superusers:
                uploadGJComment(un,pw,f"@{u}, Superuser Commands: /ban [user] | /unban [user] | /checkban [user]",perc,level)
            else:
                uploadGJComment(un,pw,f"@{u}, Permission Denied: Not in Array /listsu",perc,level)
        except:
            return
    elif(com.startswith("/ship")):
        bruh = random.choice(ships)
        try:
            if u in bannedUsers:
                uploadGJComment(un,pw,f"@{u}, Banned for Violation of Autoworks Rules.",perc,level)
            else:
                uploadGJComment(un,pw,f"@{u}, you got on the cruise and {bruh}",perc,level)
        except:
            return
    elif(com.startswith("/furry")):
        furrypercent = random.randint(0,100)
        try:
            if u in bannedUsers:
                uploadGJComment(un,pw,f"@{u}, Banned for Violation of Autoworks Rules.",perc,level)
            else:
                uploadGJComment(un,pw,f"@{u}, you are {furrypercent}% a furry!",furrypercent,level)
        except:
            return

lvl=lvlid

while 1:
    try:
        t=Thread(target=commands,args=(lvl,))
        t.start()
        time.sleep(2)
    except:
        print("err")
