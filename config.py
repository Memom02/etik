import os
import heroku3
from telethon import TelegramClient, events

from pyrogram import Client
from pyrogram import filters
import logging
#
# Burayı gurcalama
# 
# 
api_id = int(os.environ.get("APP_ID" ,"17690310"))
api_hash = os.environ.get("API_HASH", "b665fb267cd854696948a79928a41f05")
bot_token = os.environ.get("TOKEN", "5546335075:AAHdkDKctu2WUl_c3H1NwYqKm7dahxjftOQ")

# Telethon 
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
#
USERNAME = os.environ.get("USERNAME", "blacketiketbot")
startmesaj = os.environ.get("startmesaj", "★**sᴇʟᴀᴍ ᴛᴇʟᴇɢʀᴀᴍᴅᴀ sᴏʀᴜʏʟᴀ ᴇᴛɪᴋᴇᴛ ᴀᴛᴀɴ ɪ̇ʟᴋ ᴠᴇ ᴛᴇᴋ ᴇᴛɪᴋᴇᴛ ʙᴏᴛᴜʏᴜᴍ**★__\n\n**ɢʀᴜᴘ ᴠᴇ ᴋᴀɴᴀʟʟᴀʀᴅᴀ ғᴀʀᴋʟı ᴍᴏᴅᴜ̈ʟʟᴇʀᴅᴇ sɪᴢɪɴ ɪᴄ̧ɪɴ ᴜ̈ʏᴇʟᴇʀɪ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇᴋ ɪᴄ̧ɪɴ ʙᴜʀᴅᴀʏıᴍ**")
komutlar = os.environ.get("komutlar", "\n**Selam** **ʙʟᴀᴄᴋ ᴋᴏᴍᴜᴛ ᴍᴇɴᴜ̈sᴜ̈ɴᴇ ʜᴏş ɢᴇʟᴅɪɴɪᴢ**〽️\n**➥/tag - Üyelere 5'li etiket atar.**\n**➥/atag - Yalnız adminleri etiketler**\n**➥/tektag - Üyeleri tek tek etiketler.**\n**➥/etag - Üyeleri emoji ile etiketler.**\n**➥/stag - Üyelere soru sorarak etiket atar.**\n**➥/rtag - Üyeleri renklerle etiketler.**\n**➥/mtag - Üyleri manalı sözlerle etiketle.**\n**➥/vtag - 15 saniye de bir rastgele nerdesin nasılsın gibi random sorularla etiket arar.**\n**➥/btag - Bayrak ile etiker atar.**\n**➥/ktag - sembollerle etiket atar.**\n**➥/sor - Üyelere random soru sorar.**\n**➥/cancel - Etiket işlemini durdurur.**\n**❕Komutları sadece adminler kullanabilir!**")
qrupstart = os.environ.get("qrupstart", "✅ **Selam!** 🕊️ **Beni Gruba Eklediğiniz için Teşekkürler**\n**Komutları görmek için komutlar butonuna basınız**")
support = os.environ.get("support", "blackbotdestek")
group = os.environ.get("group", "blackgameebot")
sahib = os.environ.get("sahib", "memokra")
ozel_list = int(os.environ.get("ozel_list", "5412574484"))
#
app = Client("GUNC",
             api_id=api_id,
             api_hash=api_hash,
             bot_token=bot_token
             )

# black 
# black 
# black 
