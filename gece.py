#################################
# Black Tagger Bot #
#################################
#  Sahib - @memokra 
# Reponu Öz Adına Çıxaran Peysərdi
# Reponu Açığ Görüm Oğurlama Oğlum
##################################
import heroku3
import random
import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.events import StopPropagation
from config import client, USERNAME, startmesaj, qrupstart, komutlar, sahib, support, group

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)


anlik_calisan = []

gece_tag = []


#tektag
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global gece_tag
  gece_tag.remove(event.chat_id)
  
  
# Başlanğıc Mesajı
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await client.send_message(-1001856291634, f"ℹ️ **Yeni Kullanıcı -** {ad}")
     await event.reply(f"{ad} {startmesaj}", buttons=(
                      [
                       Button.inline("✍ Komutlar", data="help")
                      ],
                      [Button.url('🌱 Beni Gruba Ekle', f'https://t.me/{USERNAME}?startgroup=a')],
                     [Button.url('📣 Oyun Botumuz', f'https://t.me/blackgameebot')],
                      [Button.url('📣 Kanal', f'https://t.me/{support}')],
                       [Button.url('👨🏻‍💻 Sahip', f'https://t.me/{sahib}')]
                    ),
                    link_preview=False)


  if event.is_group:
    return await client.send_message(event.chat_id, f"{qrupstart}")

# Başlanğıc Button
@client.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
    return await event.reply(f"{ad} {startmesaj}", buttons=(
                      [
                       Button.inline("✍ Komutlar", data="help")
                      ],
                      [Button.url('🌱 Beni Gruba Ekle', f'https://t.me/{USERNAME}?startgroup=a')],
                     [Button.url('📣 Oyun Botumuz', f'https://t.me/blackgameebot')],
                      [Button.url('📣 Kanal', f'https://t.me/{support}')],
                       [Button.url('👨🏻‍💻 Sahip', f'https://t.me/{sahib}')]
                    ),
                    link_preview=False)

# gece kusu
@client.on(events.callbackquery.CallbackQuery(data="help"))
async def handler(event):
    await event.edit(f"{komutlar}", buttons=(
                      [
                      Button.inline("◀️ Geri", data="start")
                      ]
                    ),
                    link_preview=False)

# 5 li etiketleme modulü
@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"{noqrup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("özel mesajları göremiyorum ! (bu mesaj beni gruba eklendiğinde görünür)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Tag mesajı yazmadın!__")
  else:
    return await event.respond("__Etiket atmam için birşeyler yaz kanka!__")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "❄️ Etiket Başladı\n⏱️ İnterval - 2 saniye",
                    buttons=(
                      [
                      Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  ) 
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"➢ [{usr.first_name}](tg://user?id={usr.id})\n "
      if event.chat_id not in gece_tag:
        await event.respond("⛔ Etiket işlemi durduruldu",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  )
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"**{usrtxt} {msg}**")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

    

#########################

# admin etiketleme modülü
@client.on(events.NewMessage(pattern="^/atag ?(.*)"))
async def mentionalladmin(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"{noqrup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__özel mesajları göremiyorum ! (bu mesaj məni qrupa əlavə etməmişdən qabaq yazılıb)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Tag mesajı yazmadın!__")
  else:
    return await event.respond("__Etiket atmam için birşeyler yaz kanka!__")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "❄️ Admin etiket başladı\n⏱️ İnterval - 2 saniye",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  ) 
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in gece_tag:
        await event.respond("⛔ Admin Etiket İşlemi Durduruldu",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  )
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"**{usrtxt} {msg}**")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

    

#########################

# tek tek etiketleme modülü
@client.on(events.NewMessage(pattern="^/tektag ?(.*)"))
async def tektag(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"{noqrup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__özel mesajları göremiyorum ! (bu mesaj məni qrupa əlavə etməmişdən qabaq yazılıb)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Tag mesajı yazmadın!__")
  else:
    return await event.respond("__Etiket atmam için birşeyler yaz kanka!__")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "❄️ Tek-tek etiket başladı\n⏱️ İnterval - 2 saniye",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  ) 
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in gece_tag:
        await event.respond("⛔ Teker teker Etiket İşlemi Durduruldu",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  )
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"**{usrtxt} {msg}**")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

    

#########################

# Emoji ile etiketleme modülü

anlik_calisan = []

tekli_calisan = []




bayrak = "🏴󠁧󠁢󠁷󠁬󠁳󠁿 🏴󠁧󠁢󠁳󠁣󠁴󠁿 🏴󠁧󠁢󠁥󠁮󠁧󠁿 🇿🇼 🇿🇲 🇿🇦 🇾🇹 🇾🇪 🇽🇰 🇼🇸 🇼🇫 🇻🇺 🇻🇳 🇻🇮 🇻🇬 🇻🇪 🇻🇨 🇻🇦 🇺🇿 🇺🇾 🇺🇸 🇺🇳 🇺🇲 🇺🇬 🇺🇦 🇹🇿 🇹🇼 🇹🇻 🇹🇹 🇹🇷 🇹🇷 🇹🇷 🇹🇷 🇹🇴 🇹🇳 🇹🇲 🇹🇱 🇹🇰 🇹🇯 🇹🇭 🇹🇬 🇹🇫 🇹🇩 🇹🇨 🇹🇦 🇸🇿 🇸🇾 🇸🇽 🇸🇻 🇸🇹 🇸🇸 🇸🇷 🇸🇴 🇸🇳 🇸🇲 🇸🇱 🇸🇰 🇸🇯 🇸🇮 🇸🇭 🇸🇬 🇸🇪 🇸🇩 🇸🇨 🇸🇧 🇸🇦 🇷🇼 🇷🇺 🇷🇸 🇷🇴 🇷🇪 🇶🇦 🇵🇾 🇵🇼 🇵🇹 🇵🇸 🇵🇷 🇵🇳 🇵🇲 🇵🇱 🇵🇰 🇵🇭 🇵🇬 🇵🇫 🇵🇪 🇵🇦 🇴🇲 🇳🇿 🇳🇺 🇳🇷 🇳🇵 🇳🇴 🇳🇱 🇳🇮 🇳🇬 🇳🇫 🇳🇪 🇳🇨 🇳🇦 🇲🇿 🇲🇾 🇲🇽 🇲🇼 🇲🇻 🇲🇺 🇲🇹 🇲🇸 🇲🇷  🇲🇶 🇲🇵 🇲🇴 🇲🇳 🇲🇲 🇲🇱 🇲🇰 🇲🇭 🇲🇬 🇲🇫 🇲🇪 🇲🇩 🇲🇨 🇲🇦 🇱🇾 🇱🇻 🇱🇺 🇱🇹 🇱🇸 🇱🇷  🇱🇰 🇱🇮 🇱🇨 🇱🇧 🇱🇦 🇰🇿 🇰🇾 🇰🇼 🇰🇷 🇰🇵 🇰🇳 🇰🇲 🇰🇮 🇰🇭 🇰🇬 🇰🇪 🇯🇵 🇯🇴 🇯🇲 🇯🇪 🇮🇹 🇮🇸 🇮🇷 🇮🇶 🇮🇴 🇮🇳 🇮🇲 🇮🇱 🇮🇪 🇮🇩 🇮🇨 🇭🇺 🇭🇹 🇭🇷 🇭🇳 🇭🇲 🇭🇰 🇬🇾 🇬🇼 🇬🇺 🇬🇹 🇬🇸 🇬🇷 🇬🇶 🇬🇵 🇬🇳 🇬🇲 🇬🇱 🇬🇮 🇬🇭 🇬🇬 🇬🇫 🇬🇪 🇬🇩 🇬🇧 🇬🇦 🇫🇷 🇫🇴 🇫🇲 🇫🇰 🇫🇯 🇫🇮 🇪🇺 🇪🇹 🇪🇸 🇪🇷 🇪🇭 🇪🇬 🇪🇪 🇪🇨 🇪🇦 🇩🇿 🇩🇴 🇩🇲 🇩🇰 🇩🇯 🇩🇬 🇩🇪 🇨🇿 🇨🇾 🇨🇽 🇨🇼 🇨🇻 🇨🇺 🇨🇷 🇨🇵 🇨🇴 🇨🇳 🇨🇲 🇨🇱 🇨🇰 🇨🇮 🇨🇭 🇨🇬 🇨🇫 🇨🇩 🇨🇨 🇨🇦 🇧🇿 🇧🇾 🇧🇼 🇧🇻 🇧🇹 🇧🇸 🇧🇷 🇧🇶 🇧🇴 🇧🇳 🇧🇲 🇧🇱 🇧🇯 🇧🇮 🇧🇭 🇧🇬 🇧🇫 🇧🇪 🇧🇩 🇧🇧 🇧🇦 🇦🇿 🇦🇽 🇦🇼 🇦🇺 🇦🇹 🇦🇸 🇦🇷 🇦🇶 🇦🇴 🇦🇲 🇦🇱 🇦🇮 🇦🇬 🇦🇫 🇦🇪 🇦🇩 🇦🇨 🏴‍☠️ 🏴‍☠️ 🏳️‍⚧️ 🏳️‍🌈 🇹🇷 🇹🇷 🇱🇾".split(" ")

@client.on(events.NewMessage(pattern="^/btag ?(.*)"))
async def btag(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"{noqrup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski mesajları göremiyorum ! (bu mesaj məni qrupa əlavə etməmişdən qabaq yazılıb)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Tag mesajı yazmadın!__")
  else:
    return await event.respond("__Etiket atmam için birşeyler yaz kanka !__")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "❄️ Bayrak ile Etiket başladı\n⏱️ İnterval - 2 saniye",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  ) 
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(bayrak)}](tg://user?id={usr.id}) "
      if event.chat_id not in gece_tag:
        await event.respond("⛔ Bayrak ile Etiket İşlemi Durduruldu",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  )
        return
      if usrnum == 3:
        await client.send_message(event.chat_id, f"**{usrtxt} {msg}**")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

    

#########################

# Emoji ile etiketleme modülü

anlik_calisan = []

tekli_calisan = []




emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 🍨".split(" ")

@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def etag(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"{noqrup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski mesajları göremiyorum ! (bu mesaj məni qrupa əlavə etməmişdən qabaq yazılıb)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Tag mesajı yazmadın!__")
  else:
    return await event.respond("__Etiket atmam için birşeyler yaz kanka !__")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "❄️ Emoji li  Etiket başladı\n⏱️ İnterval - 2 saniye",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  ) 
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in gece_tag:
        await event.respond("⛔ Emoji  li Etiket İşlemi Durduruldu",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  )
        return
      if usrnum == 3:
        await client.send_message(event.chat_id, f"**{usrtxt} {msg}**")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

    

#########################

# söz ile etiketleme modülü

soz =(

'Telefonunda en son aradığın şey neydi?',
'Birisi kız arkadaşın / erkek arkadaşından ayrılmak için sana 1 milyon tl önerseydi, yapar mıydın?',
'Bu grupda en az kimi seviyorsun ve neden?',
'Grupta gizli aşkın var mı ? ',
'Hiç sınıfta rezil oldun mu?',
'Yerden bir şeyi alıp hiç yedin mi?',
'Bu grupta kimsenin arkasından konuştun mu ?',
'Gruptaki sırdaşın kim ? ',
'Gruptaki en sevgiğin admin kim ? ',
'Grupta ki sevmedeğin kişiyi etiketler misin ? ',
'Grubu ne kadar seviyorsun ? ',
'Grubun olmazsa olmaz dediğin şeyi nedir ? ',
'Grup adminlerinden aşık olduğun oldumu ? ',
'Grupta ağzını burnunu kırarım dediğin kimse var mı ? ',
'Grubu seviyor musun ? ',
'Gruptan uzak kaç dakika durabilirsin ? ',
'Grubun en güzel kızı kim ? ',
'Grubun en yakışıklısı kim ? ',
'Grubun en cimrisi kim? ',
'Grupta kimle çay içmek isterdin ? ',
'Grupta hangi oyunu seviyorsun ? ',
'Kurt mu kelime oyunu mu ? ',
'Grubun en gıcığı kim ? ',
'Grubun en pisliği kim ? ',  
'Grubun en dertlisi kim ? ',
'Grubun ağır abisi kim ? ',
'Grubun en egoisti kim ? ',
'Grupta değişmesi gereken şey var mı? ',
'Grupta oynanan oyunları beğeniyor musun ? ',
'Sen admin olsan neyi değiştirirdin ? ',
'Grupta kimin yerinde olmak isterdin ? ',
'Grupta birinin yanında 3 gün kalma şansın olsa kim olurdu ? ',
'Grupta admin olsan kimi banlardın neden ? ',
'Grupta kimin yerinde olmak isterdin ? ',
'Gruptaki en gizemli kişi kim ? ',
'Gruptaki kimin yanına görünmez olarak gitmek istersin ? ',
'Grupta keşke abim/ablam olsaydı dediğin kimse var mı ? ',
'Gizliden gizliden sadece onun için geldiğin kimse var mı grupta ? ',
'Real hayatta tanımak istediğin kimse var mı grupta ? ',
'Grupta bulunan en uyuz kişi kim ? ',
'Real görüştüğün biri var mı grupta ? ',
'Akrabalarından kimseyi davet ettin mi gruba ? ',
'Ailenden biri seni bu grupta görse ne olur ? ',
'Hayatınla ilgili telegramda ne yalan söyledin ? ',
'Grubu gerçekten seviyor musun? ',
'Grupta samimi olduğun kim var etiketlermisin ? ',
'Sevmeyipte seviyormuş gibi davrandığın kimse var mı? ',
'Bir gün karşı cins olarak uyanırsan, ilk yapacağın şey nedir?',
'Büyüyen hayali bir arkadaşınız var mıydı?',
'En kötü alışkanlığınız nedir?',
'Grubun delisi kim etiketler misin?',
'Toplumda en utanç verici anınız neydi?',
'Aynada kendinle hiç konuştun mu?',
'Web geçmişinizi, birileri görürse utanacağınız şey ne olurdu?',
'Uykunda konuşur musun?',
'Gizli aşkın kim?',
'Bu grupta kimle çıkardın?',
'Grubun kralı kim?',
'Son attığın mesaj neydi?',
'İnsanları yanan bir binadan kurtarıyor olsaydınız ve bir kişiyi bu grupdan geride bırakmak zorunda kalırsanız, kim olurdu?',
'Bu gruptaki kim bugüne kadarki en kötü insan olurdu? Neden?',
'Yeniden doğmuş olsaydın, hangi yüz yılda doğmak isterdin?',
'Söylediğiniz veya yaptığınız bir şeyi silmek için zamanda geriye gidebilseydiniz, bu hangi yıl olurdu?',
'Erkek arkadaşın veya kız arkadaşın seni hiç utandırdı mı?',
'Birdenbire görünmez olsaydın ne yapardın?',
'Grupta sevdiğin üç arkadaşını etiketle',
'Şimdiye kadar gördüğüm en garip rüyayı anlat.',
'Hala yaptığın en çocukça şey nedir?',
'Hangi çocuk filmini tekrar tekrar izleyebilirsin?',
'Grupta ki en değerli kişi senin için kim?',
'Saçma takma adların var mı?',
'Telefonunuzda hangi uygulamada en çok zaman harcıyorsunuz?',
'Tek bir oturuşta yediğin en çok yemek ne?',
'Tek başınayken dans ediyor musun?',
'Karanlıktan korkar mısın?',
'Bütün gün evdeysen ne yapardın?',
'Günde kaç öz çekim yapıyorsunuz?',
'En son ne zaman dişlerini fırçaladın?',
'En sevdiğin pijamalar neye benziyor?',
'Hiç yerden bir şey yedin mi?',
'Yapmaman gereken bir şeyi yaparken hiç yakalandın mı?',
'Vücudunun hangi bölümünü seviyorsun, hangi kısmından nefret ediyorsun?',
'Grupta ki kankalarını etiketler misin ?',
'Pantolonunu hiç kestin mi?',
'Kurt oyununu seviyor musun?',
'Kimsenin senin hakkında bilmediği bir şey nedir?',
'Burda ki kimseye yalan söyledin mi?',
'Dirseğini yalayabilir misin?',
'Eğer buradaki herkesi yanan bir binadan kurtarmaya çalışıyor olsaydın ve birini geride bırakmak zorunda kalırsan, kimi geride bırakırdın?',
'Telefonda aradığın son şey neydi?',
'Bir uygulamayı telefonunuzdan silmek zorunda kalsanız hangisini silerdiniz?',
'Bir ilişkideki en büyük korkun nedir?',
'Gruptaki her bir kişi hakkında bir tane olumlu, bir tane olumsuz şey söyleyin.',
'Sevmediğin kötü huyun var mı?',
'Hayatında yaptığın en çılgın şey nedir?',
'Üç gün boyunca bir adada mahsur kalmış olsaydınız, bu grupdan kimleri seçerdiniz?',
'Bu odadaki en sinir bozucu kişi kim?',
'Bu grupdan biriyle evlenmek zorunda kalsan kim olurdu?',
'En uzun ilişkiniz ne kadar sürdü?',
'Bir ünlü Instagram’da seni takip etseydi bu ünlünün kim olmasını isterdin?',
'Instagram’da 5 kişiyi silmek zorunda olsan kimleri silerdin?',
'Kaç çocuk sahibi olmak istersin?',
'Hayallerinizdeki kişiyi tarif edin.',
'Messi mi Ronaldo mu?',
'Pes mi Fifa mı?',
'İlk işin neydi?',
'Üniversite hakkındaki en büyük korkun nedir?',
'En iyi arkadaşının seninle aynı üniversiteye gitmesini ister misin?',
'Mevcut erkek arkadaşının ya da kız arkadaşının seninle aynı üniversiteye gitmesini ister misin?',
'Hayalindeki iş ne?',
'Hiç bir dersten başarısız oldun mu?',
'Hiç kopya çektin mi?',
'Hiç sınıfta uyudun mu?',
'Sınıfta asla yanında oturmak istemeyeceğin kim?',
'Derse hiç geç kaldın mı?',
'Bir öğretmenin önünde yaptığın en utanç verici şey nedir?',
'Hiç masanın altına sakız attın mı?',
'Hiç okulda kavga ettin mi?',
'Bir sınavdan aldığın en kötü puan neydi?',
'Sınıfta hiç uyuya kaldın mı?',
'Hiç gözaltına alındın mı?',
'Eğer görünmez olsaydın hangi derse gizlice girerdin?',
'En kötü grup hangisidir?',
'Bu grupdaki sır tutma  konusunda en çok zorlanan kişi kimdir?',
'Söylediğin en son yalan neydi?',
'Spor yapar mısın?',
'Hayatının geri kalanında sadece bir kıyafet giyebilseydin, bu kıyafetin hangi renk olurdu?',
'Sizce Türkiye’nin eğitim sisteminde yapılması gereken en önemli değişiklik nedir?',
'Karanlıktan/yükseklikten korkar mısın?',
'Kendi görünuşünü 1 ile 10 arasında puanla :)',
'Yaptıgın en yasadışı şey neydi?',
'Şimdi sana bir evlenme teklifi gelse ve sevmediğin biri olsa, ve bu sana son gelecek evlilik teklifi olsa kabul edermiydin?',
'Şu anki ruh haline bakarak ne tür film izlersin (aksiyon/dram/bilim kurgu/romantik komedi/biyografi/fantastik)',
'Kendini en ezik hissettiğin an hangisiydi ?',
'ilerde çocuğun olursa ne isim koymak istersin?',
'Unicorun mu olmasını isterdin ejderhan mı?',
'Kaç sevgilin oldu?',
'Hayatta unutmadığın biri var mı?',
'en sevdiğin şarkı?',
'Yapmaman gereken bir şeyi yaparken hiç yakalandın mı?',
'En sevdiğin sanatçı kim?',
'karşı cinste ilk dikkatini çeken ne?',
'bu yıl hayatında neyi değişmeyi uygun görüyorsun?',
'Birinin telefonunda gördüğün en tuhaf şey nedir?',
'Süper kahramanlar gerçekten var olsaydı Dünya nasıl bir yer olurdu?',
'Hayatın size öğrettiği en önemli ders nedir?',
'Kültürümüzün en çok sevdiğiniz yanı nedir?',
'Ailenizin uyguladığı en tuhaf gelenek nedir?',
'Aileniz dışında, yaşamınız üzerinde en büyük etkisi olan kişi kimdir?',
'Kadın/Erkek olmanın en kötü ve en iyi yanı nedir?',
'Beynini bir robota yerleştirebilir ve sonsuza kadar bu şekilde yaşayabilsedin,bunu yapar mıydın?',
'Evinizde ağırladığın en kötü misafir kimdi ve ne oldu?',
'İnsanların size ne sormasından bıktınız?',
'En tuhaf korkunuz nedir?',
'En sevdiğiniz TV programı hangisidir?',
'Girdiğiniz en saçma tartışma nedir?',
'En son söylediğin yalan nedir?',
'Biriyle çıkarken yaptığın en utanç verici şey neydi?',
'Hiç arabanla (varsa) yanlışlıkla bir şeye birine çarptın mı?',
'Hoşuna gittiğini düşündüğün ama bir türlü açılamadığın biri oldu mu?',
'En tuhaf takma adın nedir?',
'Fiziksel olarak sana en acı veren deneyimin ne oldu?',
'Hangi köprüleri yakmak seni rahatlattı?',
'Toplu taşıma araçlarında yaptığın en çılgınca şey neydi?',
'Şişeden bir cin çıksa üç dileğin ne olurdu?',
'Dünyadaki herhangi birini Türkiye’nin başkanı yapabilseydin bu kim olurdu?',
'Şimdiye kadar bir başkasına söylediğin en acımasızca şey neydi?',
'Birini öperken kendini hiç kötü hissettin mi?',
'Hiçbir sonucu olmayacağını bilsen ne yapmak isterdin?',
'Bir aynanın önünde yaptığın en çılgınca şey nedir?',
'Şimdiye kadar başkasına söylediğin en anlamlı şey neydi?',
'Arkadaşlarınla yapmayı sevdiğin ama sevgilinin önünde asla yapmayacağın şey nedir?',
'Bu hayatta en çok kimi kıskanıyorsun?',
'Grupta neyi değiştirmek isterdin?',
'Bir buluşmadan kaçmak için hiç hasta numarası yaptın mı?',
'Çıktığın en yaşlı kişi kim?',
'Günde kaç tane özçekim yaparsın?',
'Aşk için her şeyi yaparım ama “bunu” yapmam dediğin şey nedir?',
'Haftada kaç kez aynı pantolonu giyiyorsun?',
'Bugün şansın olsa lise aşkınla çıkar mısın?',
'Vücudunun hangi bölümlerinden gıdıklanıyorsun?',
'Çeşitli batıl inançların var mı? Varsa onlar neler?',
'Sevdiğini itiraf etmekten utandığın film hangisidir?',
'En utan verici kişisel bakım alışkanlığın nedir?',
'En son ne zaman ve ne için özür diledin?',
'Sözlü destanlar hakkında ne düşünüyorsun?',
'Grupta ki üç kankanı etiketler misin?',
'Hiç sevgilini aldatmayı düşündün mü?',
'Hiç sevgilini biriyle aldattın mı?',
'Grupta kimin hesabına girmek istersin?',
'Hiç kimseyi özelden rahatsız ettin mi?',
'Saçlarını uzatmayı düşünsen ne kadar uzatırdın?',
'Kimsenin bilmeyeceği garanti olsa kimi öldürmek isterdin?',
'Başkası için aldığın en ucuz hediye nedir?',
'Zamanının çoğunu en çok hangi uygulamada harcıyorsun?',
'Otobüste yaptığın en tuhaf şey nedir?',
'Grupta nefret ettiğin biri var mı?',
'Günde ne kadar dedikodu yaparsın?',
'Çıkmak isteyeceğin en genç kişi kaç yaşında olurdu?',
'kendinde beğendiğin en iyi özellerin nelerdir?',
'Hiç yaşın hakkında yalan söyledin mi?',
'Telefonundan bir uygulamayı silmek zorunda olsan bu hangisi olurdu?',
'Gece geç saatte yaptığın en utanç verici şey nedir?',
'Grup senin için ne ifade ediyor?',
'Hiç sahte kimlik kullandın mı?',
'Kırmızı halıda beraber yürümek istediğin ünlü isim kim?',
'Grubun neşesi kim?',
'Bir cin sana üç dilek hakkı sunsaydı neler dilerdin? ',
'Bir gün karşı cins olarak uyansan yapacağın ilk iş ne olurdu? ',
'Bu gruptaki insanlardan kiminle hayatını değiştirmek isterdin? ',
'Büyürken hiç hayali arkadaşın oldu mu',
'Telefonunuzda aradığın son şey neydi? ',
'Issız bir adaya düşsen yanına alacağın beş şey ne olurdu? ',
'Tam anlamıyla en son ne zaman yalan söyledin',
'Bu hayatta seni en çok kızdıran şey nedir',
'Bu hayatta sahip olduğun en büyük pişmanlık nedir',
'Gördüğün en garip rüya neydi? ',
'Grupta hoşlandığın biri var mı ? ',
'Senin hakkındaki en büyük yanılgı nedir? ',
'Grubun olmazsa olmazı sence kim etiketler misin? ',
'İnsanların senin hakkında bilmesini istediğin şey nedir? ',
'Kötü bir ilişkiden kaçmak için hiç yalan söyledin mi? ',
'İçinde bulunduğun en büyük sorun neydi? ',
'Grupta olmamasını istediğin kişiyi etiketler misin? ',
'Hakkında yalan söylediğin en kötü şey nedir? ',
'Keşke onun hakkında yalan söyleseydim dediğin şey nedir? ',
'Sana bugüne kadar verilen en iyi tavsiye nedir? ',
'Grupta kimden gıcık alıyorsun? ',
'Kilo aldırıp aldırmaması önemli değil, bir oturuşta hepsini yerim dediğin yemek nedir? ',
'Grupta gizli sevdiğin kimse var mı? ',
'Bir böcek istilası gerçekleşse hangi arkadaşın hayatta kalmayı başarır? ',
'Bir arkadaşınla plan yaparken bir başka arkadaşını ektiğin oldu mu? ',
'Şimdiye kadar hiç aralıksız 12 saatten fazla uyuduğun oldu mu? ',
'Hatırladığın kadarıyla ilk aşık olduğun ünlü kimdi? ',
'Hiç yasaya aykırı bir şeyler yaptığın oldu mu? ',
'Grupta en sevdiğin arkadaşını etiketler misin? ',
'Bu hayattaki en büyük güvensizliğin nedir? ',
'Hiç sırf fayda sağladığı için biriyle arkadaş kaldığın oldu mu? ',
'Bu hayatta şimdiye kadar yaptığın en büyük hata nedir? ',
'Bu hayatta şimdiye kadar yaptığın en iğrenç şey nedir? ',
'Oyunu oynayan oyuncu grubunda yer alanlardan kimi öpmek istersin? ',
'En son ne zaman hüngür hüngür ağladığını hatırlıyor musun? ',
'Ailenin senin hakkında bilmediğine sevindiğin şey nedir? ',
'Bu hayatta seni seni en çok ne gıcık eden ve çileden çıkaran şey nedir? ',
'Bir odada uzun bir süre hapsolacağını düşünsen yanında olmasını istediğin üç şey ne olurdu? ',
'Bu hayatta hiç kimseye söylemediğin bir sırrın var mı? ',
'İnsanların senin hakkında bildiği ama en nefret ettiğin şey nedir? ',
'Alışverişin dibine vururken en çok harcama yaptığın gün hangisiydi? ',
'Onsuz bu hayat çekilmezdi dediğin favori bir arkadaşın var mı etiketler misin? ',

) 


@client.on(events.NewMessage(pattern="^/stag ?(.*)"))
async def stag(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"{noqrup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski mesajları göremiyorum ! (bu mesaj məni qrupa əlavə etməmişdən qabaq yazılıb)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Tag mesajı yazmadın!__")
  else:
    return await event.respond("__Etiket atmam için birşeyler yaz kanka!__")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "❄️ Soru ile etiket başladı\n⏱️ İnterval - 2 saniye",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  ) 
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in gece_tag:
        await event.respond("⛔ Soru ile Etiket İşlemi Durduruldu",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  )
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"**{usrtxt} {random.choice(soz)}**")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

    
#########################

#cumlelerle tag

mana =(
'𝐾𝑎𝑙𝑏𝑖 𝑔ü𝑧𝑒𝑙 𝑜𝑙𝑎𝑛ı𝑛 𝑔ö𝑧ü𝑛𝑑𝑒𝑛 𝑦𝑎ş 𝑒𝑘𝑠𝑖𝑘 𝑜𝑙𝑚𝑎𝑧𝑚ış', 
'İ𝑦𝑖𝑦𝑖𝑚 𝑑𝑒𝑠𝑒𝑚 𝑖𝑛𝑎𝑛𝑎𝑐𝑎𝑘 𝑜 𝑘𝑎𝑑𝑎𝑟 ℎ𝑎𝑏𝑒𝑟𝑠𝑖𝑧 𝑏𝑒𝑛𝑑𝑒𝑛', 
'𝑀𝑒𝑠𝑎𝑓𝑒𝑙𝑒𝑟 𝑈𝑚𝑟𝑢𝑚𝑑𝑎 𝐷𝑒ğ𝑖𝑙, İç𝑖𝑚𝑑𝑒 𝐸𝑛 𝐺ü𝑧𝑒𝑙 𝑌𝑒𝑟𝑑𝑒𝑠𝑖𝑛',
'𝐵𝑖𝑟 𝑀𝑢𝑐𝑖𝑧𝑒𝑦𝑒 İℎ𝑡𝑖𝑦𝑎𝑐ı𝑚 𝑉𝑎𝑟𝑑ı 𝐻𝑎𝑦𝑎𝑡 𝑆𝑒𝑛𝑖 𝐾𝑎𝑟şı𝑚𝑎 Çı𝑘𝑎𝑟𝑑ı', 
'Ö𝑦𝑙𝑒 𝑔ü𝑧𝑒𝑙 𝑏𝑎𝑘𝑡ı 𝑘𝑖 𝑘𝑎𝑙𝑏𝑖 𝑑𝑒 𝑔ü𝑙üşü𝑛 𝑘𝑎𝑑𝑎𝑟 𝑔ü𝑧𝑒𝑙 𝑠𝑎𝑛𝑚ış𝑡ı𝑚', 
'𝐻𝑎𝑦𝑎𝑡 𝑛𝑒 𝑔𝑖𝑑𝑒𝑛𝑖 𝑔𝑒𝑟𝑖 𝑔𝑒𝑡𝑖𝑟𝑖𝑟 𝑛𝑒 𝑑𝑒 𝑘𝑎𝑦𝑏𝑒𝑡𝑡𝑖ğ𝑖𝑛 𝑧𝑎𝑚𝑎𝑛ı 𝑔𝑒𝑟𝑖 𝑔𝑒𝑡𝑖𝑟𝑖𝑟', 
'𝑆𝑒𝑣𝑚𝑒𝑘 𝑖ç𝑖𝑛 𝑠𝑒𝑏𝑒𝑝 𝑎𝑟𝑎𝑚𝑎𝑑ı𝑚 ℎ𝑖ç 𝑠𝑒𝑠𝑖 𝑦𝑒𝑡𝑡𝑖 𝑘𝑎𝑙𝑏𝑖𝑚𝑒', 
'𝑀𝑢𝑡𝑙𝑢𝑦𝑢𝑚 𝑎𝑚𝑎 𝑠𝑎𝑑𝑒𝑐𝑒 𝑠𝑒𝑛𝑙𝑒', 
'𝐵𝑒𝑛 ℎ𝑒𝑝 𝑠𝑒𝑣𝑖𝑙𝑚𝑒𝑘 𝑖𝑠𝑡𝑒𝑑𝑖ğ𝑖𝑚 𝑔𝑖𝑏𝑖 𝑠𝑒𝑣𝑖𝑛𝑑𝑖𝑚', 
'𝐵𝑖𝑟𝑖 𝑣𝑎𝑟 𝑛𝑒 ö𝑧𝑙𝑒𝑚𝑒𝑘𝑡𝑒𝑛 𝑦𝑜𝑟𝑢𝑙𝑑𝑢𝑚 𝑛𝑒 𝑠𝑒𝑣𝑚𝑒𝑘𝑡𝑒𝑛', 
'Ç𝑜𝑘 𝑧𝑜𝑟 𝑏𝑒 𝑠𝑒𝑛𝑖 𝑠𝑒𝑣𝑚𝑒𝑦𝑒𝑛 𝑏𝑖𝑟𝑖𝑛𝑒 𝑎şı𝑘 𝑜𝑙𝑚𝑎𝑘', 
'Ç𝑜𝑘 ö𝑛𝑒𝑚𝑠𝑒𝑑𝑖𝑘 𝑖ş𝑒 𝑦𝑎𝑟𝑎𝑚𝑎𝑑ı 𝑎𝑟𝑡ı𝑘 𝑏𝑜ş𝑣𝑒𝑟𝑖𝑦𝑜𝑟𝑢𝑧', 
'𝐻𝑒𝑟𝑘𝑒𝑠𝑖𝑛 𝑏𝑖𝑟 𝑔𝑒ç𝑚𝑖ş𝑖 𝑣𝑎𝑟, 𝐵𝑖𝑟𝑑𝑒 𝑣𝑎𝑧𝑔𝑒ç𝑚𝑖ş𝑖', 
'𝐴şı𝑘 𝑜𝑙𝑚𝑎𝑘 𝑔ü𝑧𝑒𝑙 𝑏𝑖𝑟 ş𝑒𝑦 𝑎𝑚𝑎 𝑠𝑎𝑑𝑒𝑐𝑒 𝑠𝑎𝑛𝑎', 
'𝐴𝑛𝑙𝑎𝑦𝑎𝑛 𝑦𝑜𝑘𝑡𝑢, 𝑆𝑢𝑠𝑚𝑎𝑦ı 𝑡𝑒𝑟𝑐𝑖ℎ 𝑒𝑡𝑡𝑖𝑚', 
'𝑆𝑒𝑛 ç𝑜𝑘 𝑠𝑒𝑣 𝑑𝑒 𝑏ı𝑟𝑎𝑘ı𝑝 𝑔𝑖𝑑𝑒𝑛 𝑦𝑎𝑟 𝑢𝑡𝑎𝑛𝑠ı𝑛', 
'𝑂 𝑔𝑖𝑡𝑡𝑖𝑘𝑡𝑒𝑛 𝑠𝑜𝑛𝑟𝑎 𝑔𝑒𝑐𝑒𝑚 𝑔ü𝑛𝑑ü𝑧𝑒 ℎ𝑎𝑠𝑟𝑒𝑡 𝑘𝑎𝑙𝑑ı', 
'𝐻𝑒𝑟 ş𝑒𝑦𝑖𝑛 𝑏𝑖𝑡𝑡𝑖ğ𝑖 𝑦𝑒𝑟𝑑𝑒 𝑏𝑒𝑛𝑑𝑒 𝑏𝑖𝑡𝑡𝑖𝑚 𝑑𝑒ğ𝑖ş𝑡𝑖𝑛 𝑑𝑖𝑦𝑒𝑛𝑙𝑒𝑟𝑖𝑛 𝑒𝑠𝑖𝑟𝑖𝑦𝑖𝑚', 
'𝐺ü𝑣𝑒𝑛𝑚𝑒𝑘 𝑠𝑒𝑣𝑚𝑒𝑘𝑡𝑒𝑛 𝑑𝑎ℎ𝑎 𝑑𝑒ğ𝑒𝑟𝑙𝑖, 𝑍𝑎𝑚𝑎𝑛𝑙𝑎 𝑎𝑛𝑙𝑎𝑟𝑠ı𝑛', 
'İ𝑛𝑠𝑎𝑛 𝑏𝑎𝑧𝑒𝑛 𝑏ü𝑦ü𝑘 ℎ𝑎𝑦𝑒𝑙𝑙𝑒𝑟𝑖𝑛𝑖 𝑘üçü𝑘 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟𝑙𝑎 𝑧𝑖𝑦𝑎𝑛 𝑒𝑑𝑒𝑟', 
'𝐾𝑖𝑚𝑠𝑒 𝑘𝑖𝑚𝑠𝑒𝑦𝑖 𝑘𝑎𝑦𝑏𝑒𝑡𝑚𝑒𝑧 𝑔𝑖𝑑𝑒𝑛 𝑏𝑎ş𝑘𝑎𝑠ı𝑛ı 𝑏𝑢𝑙𝑢𝑟, 𝑘𝑎𝑙𝑎𝑛 𝑘𝑒𝑛𝑑𝑖𝑛𝑖', 
'𝐺üç𝑙ü 𝑔ö𝑟ü𝑛𝑒𝑏𝑖𝑙𝑖𝑟𝑖𝑚 𝑎𝑚𝑎 𝑖𝑛𝑎𝑛 𝑏𝑎𝑛𝑎 𝑦𝑜𝑟𝑔𝑢𝑛𝑢𝑚', 
'Ö𝑚𝑟ü𝑛ü𝑧ü 𝑠𝑢𝑠𝑡𝑢𝑘𝑙𝑎𝑟ı𝑛ı𝑧ı 𝑑𝑢𝑦𝑎𝑛  𝑏𝑖𝑟𝑖𝑦𝑙𝑒 𝑔𝑒ç𝑖𝑟𝑖𝑛', 
'𝐻𝑎𝑦𝑎𝑡 𝑖𝑙𝑒𝑟𝑖𝑦𝑒 𝑏𝑎𝑘ı𝑙𝑎𝑟𝑎𝑘 𝑦𝑎ş𝑎𝑛ı𝑟 𝑔𝑒𝑟𝑖𝑦𝑒 𝑏𝑎𝑘𝑎𝑟𝑎𝑘 𝑎𝑛𝑙𝑎şı𝑙ı𝑟', 
'𝐴𝑟𝑡ı𝑘 ℎ𝑖ç𝑏𝑖𝑟 ş𝑒𝑦 𝑒𝑠𝑘𝑖𝑠𝑖 𝑔𝑖𝑏𝑖 𝑑𝑒ğ𝑖𝑙 𝐵𝑢𝑛𝑎 𝑏𝑒𝑛𝑑𝑒 𝑑𝑎ℎ𝑖𝑙𝑖𝑚', 
'𝐾ı𝑦𝑚𝑒𝑡 𝑏𝑖𝑙𝑒𝑛𝑒 𝑔ö𝑛ü𝑙𝑑𝑒 𝑣𝑒𝑟𝑖𝑙𝑖𝑟 ö𝑚ü𝑟𝑑𝑒', 
'𝐵𝑖𝑟 ç𝑖ç𝑒𝑘𝑙𝑒 𝑔ü𝑙𝑒𝑟 𝑘𝑎𝑑ı𝑛 𝑏𝑖𝑟 𝑙𝑎𝑓𝑙𝑎 ℎü𝑧ü𝑛', 
'𝑈𝑠𝑙ü𝑝 𝑘𝑎𝑟𝑎𝑘𝑡𝑒𝑟𝑖𝑑𝑖𝑟 𝑖𝑛𝑠𝑎𝑛ı𝑛', 
'𝐻𝑒𝑟 ş𝑒𝑦𝑖 𝑏𝑖𝑙𝑒𝑛 𝑑𝑒ğ𝑖𝑙 𝑘ı𝑦𝑚𝑒𝑡 𝑏𝑖𝑙𝑒𝑛 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟 𝑜𝑙𝑠𝑢𝑛 ℎ𝑎𝑦𝑎𝑡ı𝑛ı𝑧𝑑𝑎', 
'𝑀𝑒𝑠𝑎𝑓𝑒 𝑖𝑦𝑖𝑑𝑖𝑟 𝑁𝑒 ℎ𝑎𝑑𝑑𝑖𝑛𝑖 𝑎ş𝑎𝑛 𝑜𝑙𝑢𝑟 𝑛𝑒 𝑑𝑒 𝑐𝑎𝑛ı𝑛ı 𝑠ı𝑘𝑎𝑛', 
'𝑌ü𝑟𝑒ğ𝑖𝑚𝑖𝑛 𝑡𝑎𝑚 𝑜𝑟𝑡𝑎𝑠ı𝑛𝑑𝑎 𝑏ü𝑦ü𝑘 𝑏𝑖𝑟 𝑦𝑜𝑟𝑔𝑢𝑛𝑙𝑢𝑘 𝑣𝑎𝑟', 
'𝑉𝑒𝑟𝑖𝑙𝑒𝑛 𝑑𝑒ğ𝑒𝑟𝑖𝑛 𝑛𝑎𝑛𝑘ö𝑟ü 𝑜𝑙𝑚𝑎𝑦ı𝑛 𝑔𝑒𝑟𝑖𝑠𝑖 ℎ𝑎𝑙𝑙𝑜𝑙𝑢𝑟', 
'𝐻𝑒𝑚 𝑔üç𝑙ü 𝑜𝑙𝑢𝑝 ℎ𝑒𝑚 ℎ𝑎𝑠𝑠𝑎𝑠 𝑘𝑎𝑙𝑝𝑙𝑖 𝑏𝑖𝑟𝑖 𝑜𝑙𝑚𝑎𝑘 ç𝑜𝑘 𝑧𝑜𝑟', 
'𝑀𝑢ℎ𝑡𝑎ç 𝑘𝑎𝑙ı𝑛 𝑦ü𝑟𝑒ğ𝑖 𝑔ü𝑧𝑒𝑙 𝑖𝑛𝑠𝑎𝑛𝑙𝑎𝑟𝑎', 
'İ𝑛𝑠𝑎𝑛 𝑎𝑛𝑙𝑎𝑑ığı 𝑣𝑒 𝑎𝑛𝑙𝑎şı𝑙𝑑ığı 𝑖𝑛𝑠𝑎𝑛𝑑𝑎 ç𝑖ç𝑒𝑘 𝑎ç𝑎𝑟', 
'İ𝑠𝑡𝑒𝑦𝑒𝑛 𝑑𝑎ğ𝑙𝑎𝑟ı 𝑎ş𝑎𝑟 𝑖𝑠𝑡𝑒𝑚𝑒𝑦𝑒𝑛 𝑡ü𝑚𝑠𝑒ğ𝑖 𝑏𝑖𝑙𝑒 𝑔𝑒ç𝑒𝑚𝑒𝑧', 
'İ𝑛ş𝑎𝑙𝑙𝑎ℎ 𝑠𝑎𝑏ı𝑟𝑙𝑎 𝑏𝑒𝑘𝑙𝑒𝑑𝑖ğ𝑖𝑛 ş𝑒𝑦 𝑖ç𝑖𝑛 ℎ𝑎𝑦ı𝑟𝑙ı 𝑏𝑖𝑟 ℎ𝑎𝑏𝑒𝑟 𝑎𝑙ı𝑟𝑠ı𝑛', 
'İ𝑦𝑖 𝑜𝑙𝑎𝑛 𝑘𝑎𝑦𝑏𝑒𝑡𝑠𝑒 𝑑𝑒 𝑘𝑎𝑧𝑎𝑛ı𝑟', 
'𝐺ö𝑛𝑙ü𝑛ü𝑧𝑒 𝑎𝑙𝑑ığı𝑛ı𝑧 𝑔ö𝑛𝑙ü𝑛ü𝑧ü 𝑎𝑙𝑚𝑎𝑦ı 𝑏𝑖𝑙𝑠𝑖𝑛', 
'𝑌𝑖𝑛𝑒 𝑦ı𝑟𝑡ı𝑘 𝑐𝑒𝑏𝑖𝑚𝑒 𝑘𝑜𝑦𝑚𝑢ş𝑢𝑚 𝑢𝑚𝑢𝑑𝑢', 
'Ö𝑙𝑚𝑒𝑘 𝐵𝑖 ş𝑒𝑦 𝑑𝑒ğ𝑖𝑙 𝑦𝑎ş𝑎𝑚𝑎𝑚𝑎𝑘 𝑘𝑜𝑟𝑘𝑢𝑛ç', 
'𝑁𝑒 𝑖ç𝑖𝑚𝑑𝑒𝑘𝑖 𝑠𝑜𝑘𝑎𝑘𝑙𝑎𝑟𝑎 𝑠ığ𝑎𝑏𝑖𝑙𝑑𝑖𝑚 𝑁𝑒 𝑑𝑒 𝑑ış𝑎𝑟ı𝑑𝑎𝑘𝑖 𝑑ü𝑛𝑦𝑎𝑦𝑎', 
'İ𝑛𝑠𝑎𝑛 𝑠𝑒𝑣𝑖𝑙𝑚𝑒𝑘𝑡𝑒𝑛 ç𝑜𝑘 𝑎𝑛𝑙𝑎şı𝑙m𝑎𝑦ı 𝑖𝑠𝑡𝑖𝑦𝑜𝑟𝑑𝑢 𝑏𝑒𝑙𝑘𝑖 𝑑𝑒', 
'𝐸𝑘𝑚𝑒𝑘 𝑝𝑎ℎ𝑎𝑙ı 𝑒𝑚𝑒𝑘 𝑢𝑐𝑢𝑧𝑑𝑢', 
'𝑆𝑎𝑣𝑎ş𝑚𝑎𝑦ı 𝑏ı𝑟𝑎𝑘ı𝑦𝑜𝑟𝑢𝑚 𝑏𝑢𝑛𝑢 𝑣𝑒𝑑𝑎 𝑠𝑎𝑦',
'Anca mezarda uslanırız x 🚬',
'Dertsiz dua soğuktur. ...',
'Edep aklın tercümanıdır. ...',
'Uzağımda ama her gece kalbimde uyuyor...',
'Her elini sıkanla dost, her canını sıkanla düşman olma...',
'Sabır vazgeçmek değil, umudu yarına ertelemektir...',
'Bir kum tanesiyim ama çölün derdini taşıyorum..',
'Çektiğini acı sanıyorsan, bir de anasız babasız büyümeye çalışan çocuklara bak. ...',
'Hava soğuk, umutlar uzak. ...',
'Sinir uçlarımı yok ettin sevgili. ...',
'Size sıradan biriymiş gibi davranan hiç kimseyi sevmeyin...',
'Ne yaptıysam seni unutamadım...',
'İnsanlar seninle konuşmayı bıraktığında, arkandan konuşmaya başlarlar...',
'Mükеmmеl kişiyi aramaktan vazgеç. Tеk ihtiyacın olan sana sahip olduğu için şanslı olduğunu düşünеn biridir...',
'Aşktan korkmak, yaşamdan korkmak demektir ve yaşamdan korkanlar şimdiden üç kez ölmüşlerdir...',
'Bazı insanlar yağmuru hissеdеr, bazıları isе sadеcе ıslanır...',
'Hayattaki en büyük zafer hiçbir zaman düşmemekte değil, her düştüğünde ayağa kalkmakta yatar...',
'Mutlu olmayı yarına bırakmak, karşıya geçmek için nehrin durmasını beklemeye benzer ve bilirsin, o nehir asla durmaz...',
'İnsanların, senin hakkında ne düşündüklerini önemsemeyerek, ömrünü uzatabilirsin mesela...',
'Unutma; Hеr gеlеn sеvmеz.. Vе hiçbir sеvеn gitmеz...',
'Üstada sorarlar sеvgi mi nеfrеt mi diyе, “nеfrеt” diyе cеvap vеrir vе еklеr; çünkü onun sahtеsi olmaz...',
'Yanlış bildiğin yolda; hеrkеslе yürüyеcеğinе, doğru bildiğin yolda; tеk başına yürü…',
'Aşk bir kadının yaşamının tüm öyküsü, erkeğin ise yalnızca bir serüvenidir...',
'Mutluluk elin erişebileceği çiçeklerden bir demet yapma sanatıdır...',
'Ne kadar hazin bir çağda yaşıyoruz, bir önyargıyı ortadan kaldırmak atomu parçalamaktan daha güç...',
'Ne kadar yaşadığımız değil, nasıl yaşadığımız önemlidir...',
'Gözü kesenin gözü önündeyiz...',
'Gözü kesenin gözü önündeyiz...',
'Gözü kesenin gözü önündeyiz...',
'Kendine yaslan dik yürü...',
'Kendine yaslan dik yürü...',
'Kendine yaslan dik yürü...',
'Ne kadar yükselirsen, uçmayı bilmeyenlere o kadar küçük görünürsün....',
'Ya başlamamalı, ya da bitirmeli...',
'Hayat bir öyküye benzer, önemli olan yanı eserin uzun olması değil, iyi olmasıdır...',
'Aşk kıyafeti her erkeğin üzerinde durmaz... Sadece adam olana yakışır...',
'Herkesin kral olmasına gerek yok. Birileri de adam olsun yeter...',
'Ne kadar adamsan o kadar çok düşmanın olur...',
'Diz üstü yaşayacağına ayaklarının üstünde ölmeyi tercih et...',
'Hiçbir zaman unutma! Vicdanın kadar adamsın...',
'Şarap gibi kadınlar içkiden anlamayan erkeklerin elinde heba oluyor...',
'Sevmek için yürek evlenmek için para lazım azizim!...',
'Dünyaları sığdırdığım gönlüme sen artık fazlalıksın...',
'Giderken kapıyı açık bırak yeni gelenler zorlanmasın...',
'Sessiz ve yorgun zamanlar bitti. Şimdi koşma zamanı!..',
'O bizi çoktan bitirdi de bizde bitmeyen şeyler var!..',
'Tekrar başla deseler koşarak gideceğim hatalar var...',




)


@client.on(events.NewMessage(pattern="^/mtag ?(.*)"))
async def mtag(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"{noqrup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski mesajları göremiyorum! (bu mesaj beni gruba eklemeden önce yazılmış)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Etiketleme mesajı yazmadın!__")
  else:
    return await event.respond("__Etiketleme için bir mesajı yanıtlayın veya bir mesaj yazın!__")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "❄️ Söz ile etiketleme başladı\n⏱️ İnterval - 2 saniye",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  ) 
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in gece_tag:
    
        await event.respond("⛔ Söz ile etiketleme işlemi durduruldu",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  )
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"**{usrtxt} {random.choice(mana)}**")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
    

#########################

# renk ile etiketleme modülü
renk = "🔴 🟠 🟡 🟢 🔵 🟣 🟤 ⚫ ⚪ " .split(" ") 
        

@client.on(events.NewMessage(pattern="^/rtag ?(.*)"))
async def rtag(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"{noqrup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski mesajları göremiyorum! (bu mesaj beni gruba eklemeden önce yazılmış)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Etiketleme mesajı yazmadın!__")
  else:
    return await event.respond("__Etiketleme için bir mesajı yanıtlayın veya bir mesaj yazın!__")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "❄️ Renk ile etiketleme başladı\n⏱️ İnterval - 2 saniye",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  ) 
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(renk)}](tg://user?id={usr.id}) "
      if event.chat_id not in gece_tag:
        await event.respond("⛔ Renk ile etiketleme işlemi durduruldu",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  )
        return
      if usrnum == 3:
        await client.send_message(event.chat_id, f"**{usrtxt} {msg}**")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

###############################

# renk ile etiketleme modülü
karakter = " ☮ ✈ ♋ 웃 유 ☠ ☯ ♥ ✌ ✖ ☢ ☣ ☤ ⚜ ❖ Σ ⊗ ♒ ♠ Ω ♤ ♣ ♧ ♡ ♦ ♢ ♔ ♕ ♚ ♛ ★ ☆ ✮ ✯ ☄ ☾ ☽ ☼  ۞ ۩ ✂ ✆ ✉ ✦ ✧ ∞ ♂ ♀ ☿ ❤ ❥ ❦ ❧ © ✘ ϟ ₪ ✔ ☥ ☦ ☧ ☨ ☩ ☪ ☫ ☬ ☭ ❤ ❥ ❣ ❦ ❧ ❡ ❢ " .split(" ") 
        

@client.on(events.NewMessage(pattern="^/ktag ?(.*)"))
async def ktag(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"{noqrup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski mesajları göremiyorum! (bu mesaj beni gruba eklemeden önce yazılmış)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Etiketleme mesajı yazmadın!__")
  else:
    return await event.respond("__Etiketleme için bir mesajı yanıtlayın veya bir mesaj yazın!__")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "❄️ Karakter ile etiketleme başladı\n⏱️ İnterval - 2 saniye",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  ) 
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(karakter)}](tg://user?id={usr.id}) "
      if event.chat_id not in gece_tag:
        await event.respond("⛔ Karakter ile etiketleme işlemi durduruldu",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  )
        return
      if usrnum == 3:
        await client.send_message(event.chat_id, f"**{usrtxt} {msg}**")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

###############################

# black etiketleme modülü
black =(
'bu gün yoktun 🙄',
'Nerdesin gözümüz yollarda kaldı 🤗',
'Nasılsın bu gün 🥰',
'Günün nasıl geçiyor 😋',
'Gelsene sohbet edelim 😉',
'Naber ya 😁',
'Yokluğun grupta çok belli ediyo be ☺️',
'Merhaba dostum 🤗',
'Gelsene 👀',
'Hayat yormuş gibi seni 🥲',
'Sen olmasan grup ne yapardı ya 🤗',
'İyi ki varsın 🥰',
'Sıkıcı bir gün sanırım 🙄',
'Nerelisin kanka ☺️',
'Nasılsın bakalım 👀😁',
'Görünmüyorsun hiç hasta mısın 🤧🤗',
'Havalar nasıl orda 🥶',
'Gelde iki muhabbet edelim 🙃',
'Yine yoksun 😪',
'İyi ki varsın 🥰',
'Sensiz tadı yok buranın 🥲',
'Naptın bu gün 🤗',
'Günün güzel geçti mi ☺️',
'Gelsene sıkıldık ya 🤗',
'Nasılsın bakalım 😉',
'Okul nasıl gidiyor 😁',
'Çay var içer misin 🙃',
'Bana yemek ısmarlasana 🥺',
'Sensiz olmuyor 🥺 gel artık 🥲',
'Kahve içer misin 🙃',
'Naber kankam 👻',
'Nasılsın bu gün 🥰',
'Bu gün keyfin yerin de mi 🤧',
'Seni tanıyalım mı 🤗',
'Kendini anlatsana biraz 😉',
'Seni tanıyalım artık 😉 başla hadi 😁',
'Orda havalar nasıl 🥶',
'Nasılsın 🙄',
'Nerdesin 🥲',
'Gruba gelmiyorsun hiç 🥲',
'Özlettin kendini gelsene 👀',
'Naber ya 🙃',
'Mutlu olmayı hak ediyorsun bence 😁',
'Herşey yolunda mı ☺️',
'Bir selam ver güneş doğsun 😁😁',
'Hayat yordu bizi 🥲',
'Sen nasıl bir insansın? 🙃',
'Grup sensiz olmaz ☺️',
'İyi ki burdasın 🥰',
'Muhabbetini özledik 🤗',
'Sohbet edelim mi 🙃',
'Kendini tanıtır mısın 👀',
'Hasta mısın yoksun 😪',
'Havalar nasıl orda 🥶',
'İyi ki varsın 🥰',
'Bana bi soru sor 🙃🙃',
'Günün nasıl geçiyor 😋',
'Akşam napıyosun ☺️',
'Bu gün ki planın ne 😋',
'Yemekte ne vardı 🙃',
'Çay olsa da içsek 🤧',
'Spor yapıyor musun 🏃',
'Yemek yapmayı biliyor musun 🙄',
'Hangi takımı tutuyorsun 😉',
'Nerelerdesin ya 👀',
'Çizgi film sever misin 👻',
'Bana bi film önersene 🙄',

)


@client.on(events.NewMessage(pattern="^/vtag ?(.*)"))
async def vtag(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"{noqrup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__özel mesajları göremiyorum ! (bu mesaj məni qrupa əlavə etməmişdən qabaq yazılıb)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Tag mesajı yazmadın!__")
  else:
    return await event.respond("__Etiket atmam için birşeyler yaz kanka!__")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "❄️ Etiket başladı\n⏱️ İnterval - 15 saniye",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  ) 
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in gece_tag:
        await event.respond("⛔ Etiket İşlemi Durduruldu",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  )
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"**{usrtxt}** {random.choice(black)}")
        await asyncio.sleep(15)
        usrnum = 0
        usrtxt = ""

    

#########################

# renk ile etiketleme modülü
karakter = " ☮ ✈ ♋ 웃 유 ☠ ☯ ♥ ✌ ✖ ☢ ☣ ☤ ⚜ ❖ Σ ⊗ ♒ ♠ Ω ♤ ♣ ♧ ♡ ♦ ♢ ♔ ♕ ♚ ♛ ★ ☆ ✮ ✯ ☄ ☾ ☽ ☼  ۞ ۩ ✂ ✆ ✉ ✦ ✧ ∞ ♂ ♀ ☿ ❤ ❥ ❦ ❧ © ✘ ϟ ₪ ✔ ☥ ☦ ☧ ☨ ☩ ☪ ☫ ☬ ☭ ❤ ❥ ❣ ❦ ❧ ❡ ❢ " .split(" ") 
        

@client.on(events.NewMessage(pattern="^/sor ?(.*)"))
async def doğruluk(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"{noqrup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski mesajları göremiyorum! (bu mesaj beni gruba eklemeden önce yazılmış)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond(f"**{random.choice(soz)}**")
  else:
    return await event.respond(f"**{random.choice(soz)}**")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "⏱️ İnterval - 2 saniye",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  ) 
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 0
      usrtxt += f"{random.choice(soz)}"
      if event.chat_id not in gece_tag:
        await event.respond("⛔ ",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  )
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"**{usrtxt} {msg}**")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

    
###############################


print(">> Bot çalışmaktadur merak etme 🚀 @memokra bilgi alabilirsin <<")
client.run_until_disconnected()
run_until_disconnected()
