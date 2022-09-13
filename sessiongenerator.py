import os
os.system("cls")

telegram = int(input("""Tool generator 
1: telethon
2: pyrogram
3: exit script

copyright by @KillatoDev

scegli la modalità: """))

if telegram == 1:
    from telethon.sync import TelegramClient
    from telethon.sessions import StringSession
    import os
    os.system("cls")
    print("""Hai scelto telethon!
    
Bene ora vai su my.telegram.org
1) inserisci il tuo numero con il prefisso ad esempio +1
2) inserisci il codice web che ti arriva su telegram
3) clicca su api developments""")
    APP_ID = int(input("Inserisci API_ID: "))
    API_HASH = input("Inserisci API_HASH: ")

    with TelegramClient(
            StringSession(),
            APP_ID,
            API_HASH
    ) as client:
        session_str = client.session.save()
        sendmessage = client.send_message("me", session_str)
        print("Season mandata nei messaggi salvati. ")

elif telegram == 2:
    import os
    os.system("cls")
    print("""Hai scelto pyrogram!
    
Bene ora vai su my.telegram.org
1) inserisci il tuo numero con il prefisso ad esempio +1
2) inserisci il codice web che ti arriva su telegram
3) clicca su api developments""")
    APP_ID = int(input("Inserisci API_ID: "))
    API_HASH = input("Inserisci API_HASH: ")
    import pyrogram
    developerit = pyrogram.Client(":memory:", api_id=APP_ID, api_hash=API_HASH)
    developerit.start()
    season = developerit.export_session_string()
    sendmessage = developerit.send_message("me", season)
    developerit.stop()
    print("mandato in chat privata controlla su telegram!")

elif telegram == 3:
    exit("uscito...")


