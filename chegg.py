import json
import requests
import time
import hashlib
import urllib.parse
import os
import urllib3
import linecache
import sys
import shutil
import base64
from json import loads , dumps
from bs4 import BeautifulSoup as s
import string
import os
import pymongo
import re
import random
import timeit
import urllib.parse as urlparse
from urllib.parse import parse_qs
from datetime import timedelta
import datetime
from requests_toolbelt.multipart.encoder import MultipartEncoder
import random,string

#point users
client2user = pymongo.MongoClient("mongodb+srv://mogahad:mogahad@cluster0.wufww.mongodb.net/mogahad?retryWrites=true&w=majority")
mydb= client2user["a"]

mycol = mydb["users"]
allgive="0"



linkapi=["https://api-bot-ans-chegg.mogahadmahmod.repl.co/p?tagId="]
myaccounts=["mxgyqvmycsyi@fexpost.com"]



list = ["1750254175","1205882498"]
listgrop = ["-1001575877663","-1001359948326"]
payload={}
emalss = loads(open('emails.json' , 'r').read())
counturls = loads(open('counturl.json' , 'r').read())




TOKEN = "1902808416:AAGIdkpfHrKa1Vte5-l9-PnIsaEm8GzLELY"

URL = "https://api.telegram.org/bot{}/".format(TOKEN)
hh1 = ''' <html>
                                                                                                             <head> 
                                                                                                            <meta charset="utf-8"/>        
                                                                                                             <meta name="viewport" content="width=device-width, initial-scale=1.0" /> 
                                                                                                                    </head>



                                                                                                                            <body    '''

hh2 = '''</body>
                                                                                                         </html>   '''

class ParseMode(object):
    MARKDOWN = 'Markdown'
    MARKDOWN_V2 = 'MarkdownV2'
    HTML = 'HTML'

def get_url(url):
    try:
        response = requests.get(url)
        content = response.content.decode("utf-8")
        return (content)
    except:
        pass

def post_url(urll , data, file=None):
    try:
        if file is not None:
            response = requests.post(urll, files=file , data=data)
            return json.loads(response.content.decode())
        else:
            response = requests.post(urll , data=data)
            return json.loads(response.content.decode())
    except:
        pass

def get_updates(offset=None):
    try:
        url = URL + "getUpdates?timeout=100"
        if offset:
            url += "&offset={}".format(offset)
        content = get_url(url)
        js = json.loads(content)
        return js
    except:
        pass

def get_last_update_id(updates):
    try:
        update_ids = []
        for update in updates["result"]:
            update_ids.append(int(update["update_id"]))
        return max(update_ids)
    except:
        pass


def countss():
    try:
        backaaa=counturls[str("id")]
        df=int(backaaa)
        if df > 25 :
            print("oh need chnge email")
            t=changemlls()
            counturls["id"] = str("0")
            file = open('counturl.json' , 'w')
            file.write(dumps(counturls))
            file.close()
        else:
            print("oh my emalss is good")
            totot=df+1
            counturls["id"] = str(totot)
            file = open('counturl.json' , 'w')
            file.write(dumps(counturls))
            file.close()
    except:
        pass
def out3(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele+'\n------------------\n'  
    
    # return string  
    return str1
def an():
    try:
        f=emalss[str("id")]
        print(f)
        for d in range(len(linkapi)):
            print(linkapi[int(f)])
            return str(linkapi[int(f)])
            break
    except:
        pass

def changemlls():
    try:
        f=emalss[str("id")]
        print(f)
        tot=int(f)+1
        remme=len(linkapi)-1
        if tot > remme :
            print("is out format")
            emalss["id"] = str("0")
            file = open('emails.json' , 'w')
            file.write(dumps(emalss))
            file.close()
        else:
            print("is in list")
            emalss["id"] = str(tot)
            file = open('emails.json' , 'w')
            file.write(dumps(emalss))
            file.close()
    except :
        pass


def send_msgr(txt,chat_id,message_id):
   token = "your_token"
   txt="⚠️ نفذت فرصك المجانية Your free chances run out ⚠️🔰"
   chat_id = str(chat_id)
   url_req = "https://api.telegram.org/bot" + TOKEN + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + txt +'&reply_to_message_id='+str(message_id)+'&parse_mode=Markdown'+'&reply_markup={"inline_keyboard": [[{"text": "🔰 اضغط هنا للاشتراك Subscribe 🔰", "url": "https://t.me/Nnlock140}]]}'
   results = requests.get(url_req)
   print(results.json())
#check is url is chegg or not


def get_id(qu_url):
    qu_url = qu_url.split('?')[0]
    qu_url = qu_url.split('&')[0]
    qu_url = qu_url.split('#')[0]
    qu_url = qu_url.split('%')[0]
    qid = ''
    ty = ''
    if ('solution' in qu_url) and ('chapter' in qu_url):  # and ('problem' in qu_url):
        if '-exc' in qu_url:
            exc = qu_url.rindex('-exc')
            if exc > 100:
                qu_url = qu_url[:exc]
            else:
                pass
        qid = qu_url[qu_url.rindex('help/') + 5:]
        ty = 't'
    elif '-q' in qu_url:
        try:
            qid = qu_url[qu_url.rindex('-q'):]
            ty = 'q'
        except Exception as e:
            if 'not found' in str(e):
                return 'Please make sure the link is correct 🤔😕'

    else:
        return 'Please make sure the link is correct 🤔😕'

    return [qid, ty]

#

def zro(repy_id):
    try:
        mydoc2 = mycol.find_one({ str(repy_id):str(repy_id)})
        print(mydoc2)
        print("is sub grube")
        g=[mydoc2]
        oldadd=int(g[0]['point'])
        newadd=int(g[0]['point'])
        clc=oldadd-newadd
        print("is clc sub  :"+str(clc))
        mydict77 = {  str(repy_id):str(repy_id), "point": str(clc) }
        mydict4 = { "$set":mydict77}
        mycol.update_one(mydoc2, mydict4)
        return str(clc)
    except:
        pass

#sub grupe
def sub_point(user_id):
    try:
        mydoc2 = mycol.find_one({ str(user_id):str(user_id)})
        print(mydoc2)
        print("is sub ")
        g=[mydoc2]
        oldadd=int(g[0]['point'])
        newadd=int("1")
        clc=oldadd-newadd
        print("is clc sub  :"+str(clc))
        mydict77 = {  str(user_id):str(user_id), "point": str(clc) }
        mydict4 = { "$set":mydict77}
        mycol.update_one(mydoc2, mydict4)
        return str(clc)
    except:
        pass



#add points
def add_point(repy_id ,add):
    try:
        #print("id group points :"+str(chat_id)+"and add point :"+str(add_point))
        mydoc2 = mycol.find_one({ str(repy_id):str(repy_id)})
        print(mydoc2)
        if  str(repy_id)  not in str(mydoc2):
            mydict = {  str(repy_id):str(repy_id), "point": str(add) }
            x = mycol.insert_one(mydict)
            return str(add)
        else:
            print("is old grupe")
            g=[mydoc2]
            oldadd=int(g[0]['point'])
            newadd=int(add)
            clc=oldadd+newadd
            print("is clc :"+str(clc))
            mydict77 = {  str(repy_id):str(repy_id), "point": str(clc) }
            mydict4 = { "$set":mydict77}
            mycol.update_one(mydoc2, mydict4)
            return str(clc)
    except:
        pass



#chuck point
def get_point(user_id):
    try:
        print("id  points :"+str(user_id))
        mydoc2 = mycol.find_one({ str(user_id):str(user_id)})
        print(mydoc2)
        if  str(user_id)  not in str(mydoc2):
            mydict = {  str(user_id):str(user_id), "point": allgive }
            x = mycol.insert_one(mydict)
            return allgive
        else:
            g=[mydoc2]
            print("user is old in file time :"+str(g[0]['point']))
            return str(g[0]['point'])
    except:
        pass



def Check(update):
    try:
        if not 'callback_query' in str(update) and not 'channel_post' in str(update):
            
            user_id = update["message"]["from"]["id"]
            chat_id = update["message"]["chat"]["id"]
            chat_type= update["message"]["chat"]["type"]
            message_text = update['message']['text']
            try:
                first_name = update["message"]["from"]["first_name"]
            except:
                first_name = ''
            try:
                last_name = update["message"]["from"]["last_name"]
            except:
                last_name = ''
            try:
                username = update["message"]["from"]["username"]
            except:
                username = ''
            
            message_id = update["message"]["message_id"]
            if message_text=='/get':
                pi=get_point(user_id)
                send_message('Number of points :'+str(pi),chat_id,message_id)
            elif message_text.startswith('/ch-')  and str(user_id) in list:
                string = str(message_text)
                pattern = '\d+'
                result = re.findall(pattern, string)
                print(result[0])
                remme=len(linkapi)-1
                if int(result[0]) > remme :
                    send_message("Wrong email number :"+str(result[0]), chat_id, message_id)
                else:
                    emalss["id"] = str(result[0])
                    file = open('emails.json' , 'w')
                    file.write(dumps(emalss))
                    file.close()
                    send_message("An account has been changed to a number :"+str(result[0]), chat_id, message_id)
            elif message_text==('/emails')  and str(user_id) in list:
                g=[]
                t=-1
                for s in myaccounts:
                    t=t+1
                    g.append(str(t)+" :"+s)
                print(g)
                remil=out3(g)
                send_message(str(remil) , chat_id, message_id)
            elif message_text==('/show')  and str(user_id) in list:
                print("is show")
                backa=emalss[str("id")]
                send_message("Email is now working in a bot :"+str(backa) , chat_id, message_id)
            elif message_text.startswith('/add-') and update["message"]['reply_to_message'] and str(user_id) in list:
                repy_id = update["message"]['reply_to_message']['from']['id']
                repy_msg_id= update["message"]['reply_to_message']['message_id']
                string = str(message_text)
                pattern = '\d+'
                result = re.findall(pattern, string)
                print(result)
                add=str(result[0])
                asd=add_point(repy_id ,add)
                send_message('🔰Points have been added to you 🔰   '+str(asd)+'🔰',chat_id,repy_msg_id)
            elif message_text=="/zero"  and update["message"]['reply_to_message'] and str(user_id) in list:
                repy_id = update["message"]['reply_to_message']['from']['id']
                zz=zro(repy_id)
                print(str(zz))
                send_message("Total points have been deleted",chat_id,message_id)
            elif message_text=="/id" :
                send_message("id :"+str(user_id)+"\n"+str(chat_id),chat_id,message_id)
            elif message_text=="/info"  :
                send_message( 'The number of database  :'+str(mycol.count()) , chat_id, message_id)

              

            elif 'text' in update['message'].keys():
                if message_text=='/start':
                    send_message('🔰You can subscribe to Chegg to get more answers ⬇️'+'\n\n🔰 يمكنك الاشتراك بموقع Chegg للحصول اجابات اكثر ⬇️'+'\n\n ',chat_id)
                    return True


                if 'entities' in update['message'].keys():
                    qu_url = ''
                    for entiti in update['message']['entities']:
                        if (entiti['type']=='url' or entiti['type']=='text_link'):
                            offset = entiti['offset']
                            length = entiti['length']
                            qu_url = message_text[offset: offset + length]
                    
                    if  qu_url and str(chat_id) in listgrop:
                        print("Question : ",qu_url)
                        cc=get_id(qu_url)
                        print(cc)
                        time.sleep(40)
                        if "Please make sure the link is correct" in  cc:
                            print("url is not chegg")
                        elif cc[0].startswith('-q'):
                            print("url is from Q and A")
                            pi=get_point(user_id)
                            print(pi)
                            ress=int(pi)
                            if ress==0 or ress<0:
                                txt="s"
                                snd=send_msgr(txt,chat_id,message_id)
                                #send_message('تم انتهاء نقاط \npoints expired\n\nMore points contact ',chat_id,message_id)
                            else:
                                resl =send_req(qu_url)
                                se = str(resl)
                                if se.startswith('here is your answer'):
                                    su=sub_point(user_id)
                                    i = open('./Answer.html', 'rb')
                                    url876 = ("https://api.telegram.org/bot"+TOKEN+"/sendDocument?chat_id="+str(chat_id)+'&caption='+str('This is your answer 🌚\n'+'\nRemaining points:'+str(su)+"\n✅ Join channel :"+'&reply_to_message_id='+str(message_id))+'&parse_mode=Markdown'+'&reply_markup={"inline_keyboard": [[{"text": "More", "url": "https://t.me/Nnlock140"}]]}')
                                    url_txt = requests.post(url876, files={'document': i})
                                else:
                                    send_message(resl, chat_id, message_id)
                        else:
                            print("now l can get answer")
                            pi=get_point(user_id)
                            print(pi)
                            ress=int(pi)
                            if ress==0 or ress<0:
                                txt="s"
                                snd=send_msgr(txt,chat_id,message_id)
                            else:
                                print("l am sore but not answer")
                                resl = ans_book(qu_url)
                                se = str(resl)
                                if se.startswith('here is your answer'):
                                    su=sub_point(user_id)
                                    i = open('./Answer.html', 'rb')
                                    url876 = ("https://api.telegram.org/bot"+TOKEN+"/sendDocument?chat_id="+str(chat_id)+'&caption='+str('This is your answer 🌚\n'+'\nRemaining points:'+str(su)+"\n✅ Join channel :"+'&reply_to_message_id='+str(message_id))+'&parse_mode=Markdown'+'&reply_markup={"inline_keyboard": [[{"text": "More", "url": "https://t.me/Nnlock140 "}]]}')
                                    url_txt = requests.post(url876, files={'document': i})
                                else:
                                    send_message(resl, chat_id, message_id)

    except:
        exc_type, exc_obj, tb = sys.exc_info()
        f = tb.tb_frame
        lineno = tb.tb_lineno
        filename = f.f_code.co_filename
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        print('Error EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))
    return True





chuk = {
         "User-Agent":"PostmanRuntime/7.28.0",
        "Accept": "*/*",
 "Cache-Control":"no-cache",
 "Postman-Token": "04d2a2c9-63ab-43bf-bfcb-e7f38a92beb4",
 "Host":"www.chegg.com",
 "Accept-Encoding":"gzip, deflate, br",
 "Connection": "keep-alive",
 "Cookie": "C=0;CSessionID=6f7a55cd-cf95-485c-ba1c-e3b122cd1d7b;O=0; PHPSESSID=837161d45166559ee95dfa1bdde1e371; U=0; V=ba35049ebce8516446423128043519ce6074891676d8c5.51631027; exp=A184A%7CA311C%7CA803B%7CC024A%7CA560B; expkey=BEE682351558F2E82EA91564D646A8A1; user_geo_location=%7B%22country_iso_code%22%3A%22US%22%2C%22country_name%22%3A%22United+States%22%2C%22region%22%3A%22VA%22%2C%22region_full%22%3A%22Virginia%22%2C%22city_name%22%3A%22Ashburn%22%2C%22postal_code%22%3A%2220149%22%2C%22locale%22%3A%7B%22localeCode%22%3A%5B%22en-US%22%5D%7D%7D"

}
# ans urls chegg book
def ans_book(qu_url):
    try:
        urk = str(qu_url)
        while True:

            ############
            r = requests.get(str(urk), headers=chuk)
            print(r)
            soup = s(r.content, 'html.parser')
            images4 = soup.find_all("script")
            cc = str(images4)
            zx = cc.find("isbn13")
            print(zx)
            print((cc[zx:(zx + 34)]))
            text = str(soup)
            start = text.find('''chapterData''') + 1
            end = text.find('''chapterMap''')
            cut_text = text[start:end].strip()
            print(cut_text)
            ###############################
            text = str(cut_text)
            start = text.find("problemId") + 1
            end = text.find('''''')
            cut_text3 = text[start:].strip()
            print(cut_text3)
            ####################
            text = str(cut_text)
            start = text.find('''chapterId''') + 1
            end = text.find('''problemData''')
            cut_text2 = text[start:end].strip()
            print(cut_text2)
            if zx == -1:
                continue
            else:
                # import requests
                import json
                import re
                # print((take[x:(x+20)]))
                # print((take[x2:(x2+26)]))
                # print((take[x3:(x3+22)]))
                string = str(cut_text2)
                pattern = '\d+'
                result = re.findall(pattern, string)
                print(result[0])
                z1 = result[0]
                ######
                string = (cc[zx:(zx + 34)])
                pattern = '\d+'
                result = re.findall(pattern, string)
                print(result[1])
                z2 = result[1]
                ##########
                string = str(cut_text3)
                pattern = '\d+'
                result = re.findall(pattern, string)
                print(result[0])
                z3 = result[0]
                ##################
                url = "https://www.chegg.com/study/_ajax/persistquerygraphql"

                headers = {
                    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0',
                    'Accept': 'application/json',
                    'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
                    'Referer': urk,
                    'Content-Type': 'application/json',
                    # 'Origin': 'https://www.chegg.com',
                    # 'Connection': 'keep-alive',
                    'Cookie': 'C=0; V=aa82912c5d5cc29a4d57f68e8252e0f160e737de9fbda8.32969436; optimizelyEndUserId=oeu1625765860030r0.7070627845458444; _omappvp=zGG0F2gpDXsv8t8mSVNtUskYlhgRPyG4MbMxGXImeA6kc825JULEADtBgEMoXMYBGxvg3UsXbFQn94cICxvdjwyLj5IWcstO; usprivacy=1YNY; _pxvid=3c460406-e013-11eb-90aa-0242ac120007; adobeujs-optin={"aam":true,"adcloud":true,"aa":true,"campaign":true,"ecid":true,"livefyre":true,"target":true,"mediaaa":true}; s_ecid=MCMID|71110436398969037660579109665680893622; _ga=GA1.2.1577396314.1625765885; _gcl_au=1.1.1187833818.1625765886; _rdt_uuid=1625765887702.c7af46ba-9bf4-405a-bf7a-400237fe361e; _fbp=fb.1.1625765889587.723136726; _ym_d=1625765890; _ym_uid=1625765890958668522; __gads=ID=b79215085d568c59:T=1625765902:S=ALNI_Mbh84jrr2zXqoWLu7B5VbjaGLgmmg; __ssid=5a6cbd6f0e3ff5d122ed0b06b3257ec; _vid=v3Z63N6HkRP1WgTzucfb; DFID=web|v3Z63N6HkRP1WgTzucfb; al_cell=main-1-control; _scid=a2d70133-0abd-43eb-b898-27ba7e913825; _cs_c=1; sbm_dma=0; _sctr=1|1625727600000; O=0GRT2KY0; omSeen-tgjg3ieouzbhy6fc0ctw=1625829119252; chgcsdmtoken={"user_uuid":"9de64bf2-3a90-41e3-b4d3-7d9bc61f0287","created_date":"2021-07-11T17:11:24.488Z","account_sharing_device_management":1}; chgcsastoken=XRbg1nqrE3f4JxAVAMBEE2Jf0YJG5m5CEzWA6gkhNkHoy-BB48Gz0uncd4cQ0MB4TxgjyYqEGSLMPwwuTob463Gw1MfNt6rHD7tZSfZByJn4yDV_Moe-rFBriMqvI39u; sbm_country=AM; __CT_Data=gpv=17&ckp=tld&dm=chegg.com&apv_79_www33=17&cpv_79_www33=17; _cs_id=33b24d83-d9fc-ad43-dbb0-3a69e2786528.1625770698.8.1626159376.1626159376.1.1659934698843.Lax.0; _sp_id.ad8a=baf447c9-d3ec-4aad-9498-c9d0a28504ab.1625776134.9.1626160294.1626040062.13735bff-d602-483c-af82-315b0684079d; user_geo_location={"country_iso_code":"IQ","country_name":"Iraq","region":"KI","region_full":"Kirkuk","city_name":"Kirkuk","locale":{"localeCode":["ar-IQ"]}}; AMCVS_3FE7CBC1556605A77F000101@AdobeOrg=1; CVID=1708b5c2-1eb7-46c1-abac-7c75311aeead; CSID=1626558358824; mcid=71110436398969037660579109665680893622; schoolapi=null; lok=0GRT2KY0; _gid=GA1.2.158331038.1626558440; _ym_isad=2; PHPSESSID=4tjrj35rjlss1g7dooj40a1q85; CSessionID=70941ec9-92fe-4203-b531-7a5f2cbbfab8; _px3=9ec8f5cdf0df8e403ac7c26195da6ef41d17de16bb6567a6c333b3cdc0dbcfdd:QND99F+IABIbuelXbGZnoMwWgFH7wFwJL42fnzGsfl4LtKugtyx8pG18g23nqkgeOBQVsTuRxeAz7Bj6VLBSPg==:1000:2BPipcY3dvWFpUK0hByfyvM6q8s4mNzQ1mUjrmOBxjtnnFAOwiGuvX7Mb2MRGcEV+tQYjbKgU097blw+5eQFkXNhADULbZMDuwm2VW9Wl9R5cB6RWSmrUY3Tsz+c4/xxbhof77VhmCcQw5t77TQKepIa/If5MvjqiXk7FhkGbP/BBZhsWTEKna3OlH3zgF9E8GcaWoHpVHdgK6CQnmENVA==; forterToken=ea9fd8b064424b8da749171b9af9af8e_1626558534198__UDF43-mnf_13ck; chgmfatoken=[ "account_sharing_mfa" => 1, "user_uuid" => 8e513937-6849-4a5c-bc45-34a7eae1ae1b, "created_date" => 2021-07-17T21:50:00.898Z ]; id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI4ZTUxMzkzNy02ODQ5LTRhNWMtYmM0NS0zNGE3ZWFlMWFlMWIiLCJhdWQiOiJDSEdHIiwiaXNzIjoiaHViLmNoZWdnLmNvbSIsImV4cCI6MTY0MjMyODc2NiwiaWF0IjoxNjI2NTU4NzY2LCJlbWFpbCI6Im14Z3lxdm15Y3N5aUBmZXhwb3N0LmNvbSJ9.myic2oqd-i3c8nO00_I2lfL4nb5J8Rsv2nxpeZCvh9mubQabCyKVwDA-uwboobRLhOfumoS9bUDpASgmSw-K27KQLbAJIkMdtd8yxFKrAlFGJe_1MpVzgUGPelhg7YNHj5IJdiDrz9CpkgZsn0J8HETsKenEJfD1o8jD14WwVcGDpg3zgiART2fy8G6rLlwq0r4zuxIe2FlAT0-edF7xT0doXoAo921TuJPUIl3o7lZvijJ60CFXSNkiV1xnAuM5qqebfVBSQm6xkKgHHP0eFAJtOTFN3D3azDxp1DbgSQmZdTpPc5bBnH2naGRZIfm0o6L5tEcgap6c13JRlMqW5Q; access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhUTkU0cWwxNTRxekZieTBBakxDdSJ9.eyJodHRwczovL3Byb3h5LmNoZWdnLmNvbS9jbGFpbXMvYXBwSWQiOiJOc1lLd0kwbEx1WEFBZDB6cVMwcWVqTlRVcDBvWXVYNiIsImlzcyI6Imh0dHBzOi8vY2hlZ2ctcHJvZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8OGU1MTM5MzctNjg0OS00YTVjLWJjNDUtMzRhN2VhZTFhZTFiIiwiYXVkIjpbImNoZWdnLW9pZGMiLCJodHRwczovL2NoZWdnLXByb2QudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYyNjU1ODc2NiwiZXhwIjoxNjI2NTYwMjA2LCJhenAiOiIzVFpiaGZzWndkZUhiaG9WTXhPdlpHYjM3TWN2YzBvOCIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgYWRkcmVzcyBwaG9uZSBvZmZsaW5lX2FjY2VzcyIsImd0eSI6InBhc3N3b3JkIn0.a5T0b_ik0-3I7d0n0ThjoVWsomntS5oMO9vG-D6wlAC4kGp1jYqBTOuiQrRWpGp-fsJLO97sMXClGROdlZQ4OyPJ_moZPwKCcdiWS6W8gUjPWSuH45kHiy4RJjW_P-Txf0sVSRoPELDBTp48Ms1KA7dc2BXCUPNQL0I8jKpQ0PWtB9WGNVgaEIkU7CeOlkOm2QxGVyU2SiQXS8xhdeAGX9VKnvljErylmG1jiXvA6zez6HDi6rScgdovEoXp2arPC8y2sCe5QOIwCcn90y5Sc8bBM_MzpjG7R0ji7HOTY--hrlMgloh8NnHYWeYkoEtt-E2f8yjhroTurOzd2Mufjw; access_token_expires_at=1626560206; refresh_token=ext.a0.t00.v1.MXh0qoPg2NkxPkFgxezeL3HQ3y1D4Tmvv69tZszRGTJJ8Msic86Du5BBqqkgOYOp41xleWe2ObJ-_dVSP7ns3xs; SU=dJ3INlpSMXKlYOzarvwIMs1E41YjSLCImqj-5Q5tY-IQilYKUpQBdfitwJQTfZYdTo7nBJeet92HE1A9iOJpjDoiFO0xTVl6kIiMX67XcKU9h6-GXIK9q19vgtJ__Hwm; U=ace6b5b4710a61142eaac97dcb28d303; gid=3449493; gidr=MA; exp=A311C|A803B|A560B|A209A|A212A|A259B|A735A|A110B|A448A|A890H|A966A|A270C|A278C|A315B|A360A; expkey=C3E6A42F2D918E628921D8C91EA995CC; _sdsat_cheggUserUUID=8e513937-6849-4a5c-bc45-34a7eae1ae1b; _sdsat_authState=Hard Logged In; AMCV_3FE7CBC1556605A77F000101@AdobeOrg=-408604571|MCIDTS|18826|MCMID|71110436398969037660579109665680893622|MCAAMLH-1627163591|6|MCAAMB-1627163591|RKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y|MCOPTOUT-1626565991s|NONE|MCAID|NONE|MCSYNCSOP|411-18824|vVersion|4.6.0|MCCIDH|2035083728; opt-user-profile=aa82912c5d5cc29a4d57f68e8252e0f160e737de9fbda8.32969436%2C19944471923%3A19963683656; sbm_a_b_test=1-control; _uetsid=94e7ae20e74811ebb9accf9b3e5f8b6e; _uetvid=414db3d0e01311eb8a54df6bf94b77c5; wcs_bt=s_4544d378d9e5:1626558813; intlPaQExitIntentModal=hide; s_pers= buFirstVisit=core%2Ccs%2Ctb%2Chelp%2Cothers|1783542528328; gpv_v6=chegg%7Cweb%7Ccs%7Cqa%7Cquestion%20page|1626560642059;; s_sess= s_sq=cheggincriovalidation%3D%2526pid%253Dchegg%25257Cweb%25257Ccore%25257Cfederated%252520search%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.chegg.com%25252Fhomework-help%25252Fquestions-and-answers%25252Fintroduction-electricity-magnetism-1-follo%2526ot%253DA; buVisited=core%2Ccs; s_ptc=; cheggCTALink=false; SDID=1F5CD888609A3CFC-085B69B781D3FFCB;; OptanonConsent=isIABGlobal=false&datestamp=Sat+Jul+17+2021+14:54:30+GMT-0700+(Pacific+Daylight+Time)&version=6.10.0&hosts=&consentId=b252f636-7de5-4013-a3f9-92a8b99aa543&interactionCount=1&landingPath=NotLandingPage&groups=snc:1,fnc:1,prf:1,SPD_BG:1,trg:1&AwaitingReconsent=false; _px3=76f29ad6e73b7675dee5cba237e37fbe1470715f3921001bf167cbfacd0ae570:KbibLRx7iwVgk/4XqTp853dhLUoTHuk8XGkMXRgG5Mhaejly5rmNJTZIDmHK3UWcSC3pU8i2WPHVpm4IlKi9lg==:1000:gMl9Wy4DRHnU6eq0W6EROgOq7cBzGVcgHYn3IlTGtXs69JakDInK8TInOFPlz8FvUX46nvbS5hcHujm95VLfEZIzD8gR9kS6UHoeU/ZAalNM680gm6P/WZaKx5RBbHZxxJ3Uhps9u5SEx9tozxAOvvyi6i6pYyte+u9ZvSsmCCAjuKBdPB9MQK2+HH3dVSEHWXJJTinxcYe9uUVhwPnmHg==; _px=KbibLRx7iwVgk/4XqTp853dhLUoTHuk8XGkMXRgG5Mhaejly5rmNJTZIDmHK3UWcSC3pU8i2WPHVpm4IlKi9lg==:1000:nnFxJdC11vdWwj97798qail+uYyHFu8aylAv448r7X7wbJkb/VVppoS1AzYf5IJgz0xMCDjn3M9W+7ZBjUEB4dGras5shP/6ycrcBoRbovD5OusLUiFxc6SHJCJV7ohaJWNmQ3vqx5VAUAc45L3N/hyDy1vQOnvTXgDYfEr2EPg69obQ/+v5XVaPviQp414PZgGK3+crVFGz9lSZeii49arPa9HxYc85cKhjKpR2Vgq9QFU1TX1aMV26nLoFGiUrcpI0ljeJieSIj6BwXou/ug==',
                    # 'Sec-GPC': '1',
                    # 'TE': 'Trailers'
                }

                r = requests.get(str("https://www.chegg.com/homework-help/follow-prob-7-39-students-measure-aerodynamic-drag-model-sub-chapter-7-problem-41p-solution-9780077295462-exc"),headers=headers, data=payload)
                soup = s(r.content, 'html.parser')

                f = open("nn2.txt", "w")
                f.write(str(soup))
                f.close
                f2 = open("./nn2.txt", "r")
                # f2.read()
                # print(f2.read())

                #############
                text = str(f2.read())
                start = text.find('''prod","token"''') + 1
                end = text.find('''userUuid''')
                cut_text2 = text[start:end].strip()
                print(cut_text2)
                vv = cut_text2.replace('''rod","token":"''', "")
                vv2 = vv.replace('''","''', "")
                print(str(vv2))
                ##################

                payload2 = json.dumps({
                    "query": {
                        "operationName": "getSolutionDetails",
                        "variables": {
                            "isbn13": z2,
                            "chapterId": z1,
                            "problemId": z3
                        }
                    },
                    "token": str(vv2)
                })
                response = requests.request("POST", url, headers=headers, data=payload2)
                print(response)
                if "problemHtml" not in str(response.text):
                    print("is can not get ans book")
                    return 'Something is wrong with the book getting resolved'
                else:
                    print("now l can get ans book")
                    # print(response.json()['data']['textbook_solution']['chapter'][0]['problems'][0]["problemHtml"])
                    xx = response.json()['data']['textbook_solution']['chapter'][0]['problems'][0]['solutionV2'][0]["totalSteps"]
                    xx2 = response.json()['data']['textbook_solution']['chapter'][0]['problems'][0]["problemHtml"]
                    for i in range(xx):
                        # print(response.json()['data']['textbook_solution']['chapter'][0]['problems'][0]['solutionV2'][0]['steps'][i]["html"])
                        # v="\n"+response.json()['data']['textbook_solution']['chapter'][0]['problems'][0]['solutionV2'][0]['steps'][i]["html"]
                        # print(str(v))
                        f = open('DD.html', 'a')
                        f.write("""<H3> <p style="color:RED;">""" + "Step " + str(i + 1) + " of " + str(
                            xx) + ":) </H3> </p>" + "\n" + str(
                            response.json()['data']['textbook_solution']['chapter'][0]['problems'][0]['solutionV2'][0][
                                'steps'][i]["html"]))
                        f.close()
                    # os.remove("DD.html")
                    f2 = open('DD.html', 'r')
                    f = open('Answer.html', 'w')
                    f.write(str(hh1) + """<H1> <p style="color:#2E97A6;">""" + " All Step " + str(
                        xx) + ":) </H1> </p> " + "\n" + str(xx2) + "\n" + f2.read() + str(hh2))
                    f.close()
                    os.remove("DD.html")
                    i = open('./Answer.html', 'rb')
                    # imgkit.from_file('Answer.html', 'Answer.jpg')
                    # i2 = open('./Answer.jpg', 'rb')
                    #########up file
                    url = "https://siasky.net/skynet/skyfile"

                    files = [
                        ('', ('Answer.html', open('./Answer.html', 'rb'), 'text/html'))
                    ]
                    headers7 = {
                        'referrer': 'https://siasky.net/'
                    }
                    #response = requests.request("POST", url, headers=headers7, data=payload, files=files)
                    #print(response.text)
                    if 'skylink' not in str("oooooo"):
                        return 'here is your answer :\n'
                    else:
                        #print(response.json()["skylink"])
                        #linkup = "https://siasky.net/" + response.json()["skylink"]
                        return 'here is your answer :\n' 
                    #i2 = open('./clients.json', 'rb')
                    #markdown = """✅ This is your answer 🌚\n✅ Join channel : @Taif_iraq\n✅ Remaining : 🔓""" + r + """🔓 """ + "\n✅ Time ⏱ : """ + str( mma) + "\n✅ Solution link: " + str(linkup) + """"""

                break




    except:
        pass

#ans url chegg H.w
#linkapi=""
def send_req(qu_url):
    try:
        print(qu_url)
        edsss=countss()
        r = requests.get(str(an()) + qu_url,data=payload)
        print(r)
        soup = s(r.content, 'html.parser')
        print(r)

        if "An expert answer will be posted here" in str(soup):
            return '⚠️ لم تتم الإجابة على هذا السؤال'+"\n⚠️ This question hasn't been answered"
        else:
            x0 = soup.find('div', '</div>', class_="ugc-base question-body-text")
            x1 = soup.find('div', '</div>', class_="answer-given-body ugc-base")
            if 'None' in str(x1):
                gge=changemlls()
                return "Something went wrong, send it at another time"
            else:
                for a in x0.findAll('img'):
                    if "https:" not in a['src']:
                        print("reo https")
                        a['src'] = "https:" + a['src']
                    else:
                        print("noo")
                s1 = str(x0)
                ###################
                for a in x1.findAll('img'):
                    if "https:" not in a['src']:
                        print("reo https")
                        a['src'] = "https:" + a['src']
                    else:
                        print("noo")
                s2 = str(x1)
                ############
                f = open('Answer.html', 'w')
                messagee = str("""

                <html><head><meta http-equiv="content-type" content="text/html; charset=UTF-8">
                                        <meta http-equiv="content-type" content="text/html; charset=UTF-8">
                                        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=yes">
                                            <link rel="preconnect" href="https://fonts.gstatic.com">
                                            <link href="https://fonts.googleapis.com/css2?family=Questrial&amp;display=swap" rel="stylesheet">
                                        <link rel="stylesheet" href="style.css">
                                        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">



                                        <style>
                                        h1 {
                                            font-family: 'Questrial', sans-serif;
                                                }

                                        p {
                                    font-family: 'Questrial', sans-serif;
                                            }

                                        td {
                                    font-family: 'Questrial', sans-serif;
                                            }  


                                        .content {
                                            width: 100%;
                                        margin: auto;
                                        background: white;
                                        padding: 10px;
                                            }


                                        img{
                                        max-width: 100%;
                                            }
                                            body {background-color: LightGray;
                                                overflow: scroll;}
                                        h1   {color: red;}

                                            </style>

                                            </head><body><div class="container"><div class="alert alert-danger alert-dismissible" role="alert">
                                            <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">×</span></button>
                                            <center><strong> <p><a href="https://t.me/Nnlock140/55">For All Answers Join channel : @Nnlock140</a></p></strong> 
                                            </center></div><div class="content" "=""><h1></h1><h1><font size="6"><strong>Q:</strong></font></h1><p></p><div id="mobile-question-style" style="font-family: Roboto; color:#333333; "><p dir="ltr"> """ + str(
                    s1) + """</p>
                </div><p dir="ltr">&nbsp; </p>
                <p></p><hr><h1><font size="6"><strong>A:</strong></font></h1><p></p><p> """ + str(s2) + """ </p><p></p> </div> </div></body></html>










                """)
                f.write(messagee)
                f.close()
                url = "https://siasky.net/skynet/skyfile"
                files = [
                    ('', ('Answer.html', open('./Answer.html', 'rb'), 'text/html'))
                ]
                headers7 = {
                    'referrer': 'https://siasky.net/'
                }
                #response = requests.request("POST", url, headers=headers7, data=payload, files=files)
                #print(response.text)
                if 'skylink' not in str(messagee):
                    return 'here is your answer :\n'
                else:
                    #print(response.json()["skylink"])
                    #linkup = "https://siasky.net/" + response.json()["skylink"]
                    return 'here is your answer :\n'
    except:
        pass


def editMessage(text, chat_id, text_id , inline_keyboard):
    try:
        url = URL + "editMessageText?chat_id={}&message_id={}&parse_mode=&text={} &reply_markup=".format(chat_id,text_id, text) + inline_keyboard
        r = get_url(url)
        return r
    except:
        pass

def deleteMessage(chat_id, message_id):
    try:
        url = URL + "deleteMessage?chat_id={}&message_id={}".format(chat_id, message_id)
        get_url(url)
    except:
        pass

def send_message(text, chat_id, text_id = None,inline_keyboard=None,parse_mode=None):
    try:
        data = {
            'text':text,
            'chat_id':chat_id,
            'reply_to_message_id':text_id,
            'reply_markup':inline_keyboard,
            'disable_web_page_preview':True,
            'parse_mode': parse_mode
        }
        r = post_url(URL + "sendMessage",data)
        return r
    except Exception as e:
        print(e)

def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        # print(updates)
        try:
            if len(updates["result"]) > 0:
                last_update_id = get_last_update_id(updates) + 1
                for i in updates['result']:
                    Check(i)
        except:
            try:
                print(updates['description'])
            except:
                pass




if __name__ == '__main__':
    main()
