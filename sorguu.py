# Apiler tsg yunusa aittir yarın ayni bu saate apiler kapanacaktır api satın almak için tsg yunusa yazabilirsiniz 

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests
from io import BytesIO
import asyncio
import aiohttp
import os
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
import aiohttp
from io import BytesIO
import json
import aiofiles
import random
import string
from functools import partial

sarki = 23480691
muzik = "519068128f1f5767dfeb224c15d23949"
wow = "bot token gir"

ramowlf = Client("insta_ramowlf", api_id=sarki, api_hash=muzik, bot_token=wow)

zenginpicler = "vip.txt"
ustyt = "keycik.txt"
yarrayemis = "yarrayemis.txt"

for file in [zenginpicler, ustyt, yarrayemis]:
    if not os.path.exists(file):
        open(file, "w").close()

async def vaygavat(client, user_id):
    try:
        member = await client.get_chat_member("@TurkUserBotKanali", user_id)
        if member.status == "left":
            return False
        return True
    except UserNotParticipant:
        return False
        
azginim = "buraya log grubunu gir"
vayoe = "sikisenler.txt"

ramazan_buba = [buraya kendi idni gir]

if not os.path.exists(vayoe):
    with open(vayoe, "w") as f:
        pass

async def sikisen(sikisme, yarram, amxik):
    async with aiofiles.open(vayoe, mode="r") as f:
        lines = await f.readlines()
        if any(str(sikisme) in line for line in lines):
            return  

    async with aiofiles.open(vayoe, mode="a") as f:
        await f.write(f"{sikisme} - {yarram} - {amxik}\n")

    await ramowlf.send_message(
        azginim,
        f"Bota start veren eleman\n\nNickName: {amxik}\n\nKullanıcı adı: @{yarram}\n\nID: {sikisme}"
    )

@ramowlf.on_message(filters.command("start"))
async def babapiro_ramo(client, message):
    sikisme = message.from_user.id
    yarram = message.from_user.username or "yok"
    amxik = message.from_user.first_name
    await sikisen(sikisme, yarram, amxik)

    try:
        member = await ramowlf.get_chat_member("TurkUserBotKanali", sikisme)
        if member.status == "left":
            return await message.reply(
                "Önce **❤️‍🔥 Kanalımıza** katıl: [Kanalımız](https://t.me/TurkUserBotKanali)\n\nKatıldıktan sonra tekrar /start yaz",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("❤️‍🔥 Kanalımıza Katıl", url="https://t.me/TurkUserBotKanali")]
                ])
            )
    except Exception:
        return await message.reply(
            "Önce **❤️‍🔥 Kanalımıza** katıl: [Kanalımız](https://t.me/TurkUserBotKanali)\n\nKatıldıktan sonra tekrar /start yaz",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("❤️‍🔥 Kanalımıza Katıl", url="https://t.me/TurkUserBotKanali")]
            ])
        )

    await message.reply(
        "**❤️‍🔥 Hoşgeldin Reis Botumuzu tercih ettiğin için teşekkür ederiz**",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📜 Sorgu Komutları", callback_data="gavatlar")],
            [InlineKeyboardButton("🫡 Admin Komutları", callback_data="babam")],
            [InlineKeyboardButton("❤️‍🩹 Kanalımız", url="https://t.me/TurkUserBotKanali")],
            [InlineKeyboardButton("😎 Vip Sorgular", callback_data="picler")],
            [InlineKeyboardButton("🩵 Geliştirici", url="https://t.me/ramowlf")]
        ])
    )

@ramowlf.on_callback_query(filters.regex("babam"))
async def babam(client, callback_query):
    babalar = (
        "🫡 **Babam yani Sahibimin Konutları** 🫡\n\n"
        "/key - Vip key oluşturur tek kişilik 🏆\n"
        "/vip - Oluşturulan vip key kullanımı için 🎁\n"
        "/cikar - Vip kullanıcının Vip üyeliğini kaldırır  🎀\n"
        "/toplam - Botunuzu kullanan toplam Üye sayısını gösterir 🎇\n\n"
        "[Vip Satın Almak için Tıkla 💎](https://t.me/ramowlf)"
    )
    
    await callback_query.message.edit_text(
        text=babalar,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Geri", callback_data="annehoplatan")]
        ])
    )
    
@ramowlf.on_callback_query(filters.regex("gavatlar"))
async def gavatlar(client, callback_query):
    fullsikis = (
        "📜 **Sorgu Komutları** 📜\n"
        "/aile - Aile sorgusu yapar 👪\n"
        "/gsmtc - GSM sorgusu yapar 📱\n"
        "/adres - Adres sorgusu yapar 🏠\n"
        "/tc - TC kimlik sorgusu yapar 🆔\n"
        "/adsoyad - Ad ve Soyad sorgusu yapar 👤\n"
        "/tcgsm - TC ve GSM sorgusu yapar 📲\n"
        "/apartman - Apartman sorgusu yapar 🏢\n\n"
        "🔗 **Biz Ait Olanlar** 🔗\n"
        "[Kanalımız](https://t.me/TurkUserBotKanali) 💬\n"
        "[Geliştirici](https://t.me/ramowlf) 👨‍💻"
    )

    await callback_query.message.edit_text(
        text=fullsikis,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Geri", callback_data="annehoplatan")]
        ])
    )

@ramowlf.on_callback_query(filters.regex("picler"))
async def picler(client, callback_query):
    picler = (
        "🔒 **VIP Sorgular** 🔒\n"
        "/isyeri - tc iş yeri sorgu 👪\n"
        "/polismodu - polis moduna geçer 📱\n"
        "/ehliyet - ehliyet sorgu 🏠\n"
        "/tapu - tapu sorgu 🆔\n"
        "/vesika - Vesika Sorgu\n\n"
        "🔗 **Biz Ait Olanlar** 🔗\n"
        "[Kanalımız](https://t.me/TurkUserBotKanali) 💬\n"
        "[Geliştirici](https://t.me/ramowlf) 👨‍💻"
    )

    await callback_query.message.edit_text(
        text=picler,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Geri", callback_data="annehoplatan")]
        ])
    )

@ramowlf.on_message(filters.command("toplam"))
async def sikisenpicler(client, message: Message):
    if message.from_user.id not in ramazan_buba:
        return await message.reply("🍑 Sadece Babam kullanabilir")
        
    try:
        async with aiofiles.open(vayoe, mode="r") as f:
            lines = await f.readlines()
        vayoee = len(lines)
        await message.reply(f"📊 Toplam Kullanıcı sayısı {vayoee}")
    except Exception as e:
        await message.reply("Botunda kullanıcı yok")

@ramowlf.on_callback_query(filters.regex("annehoplatan"))
async def annehoplatan(client, callback_query):
    await callback_query.message.edit_text(
        "**❤️‍🔥 Hoşgeldin Reis Botumuzu tercih ettiğin için teşekkür ederiz**",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📜 Sorgu Komutları", callback_data="gavatlar")],
            [InlineKeyboardButton("🫡 Admin Konutları", callback_data="babam")],
            [InlineKeyboardButton("❤️‍🩹 Kanalımız", url="https://t.me/TurkUserBotKanali")],
            [InlineKeyboardButton("😎 Vip Sorgular", callback_data="picler")],
            [InlineKeyboardButton("🩵 Geliştirici", url="https://t.me/ramowlf")]
        ])
    )

@ramowlf.on_message(filters.command("key"))
async def zenginlericin(client, message):
    if message.from_user.id not in ramazan_buba:
        return await message.reply("🍑 Babam Kullanabilir sadece")

    ramoss = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    async with aiofiles.open(ustyt, mode="a") as f:
        await f.write(f"{ramoss}\n")

    await message.reply(f"Tek Kişilik vip key:\n`{ramoss}`")

        
@ramowlf.on_message(filters.command("vip"))
async def zenginyavrusu(client, message):
    args = message.text.split()
    if len(args) != 2:
        return await message.reply("🤓 Kullanım: `/vip KEY`", quote=True)

    ramoss = args[1]

    async with aiofiles.open(ustyt, mode="r") as f:
        amon_ra = await f.readlines()
    amon_ra = [k.strip() for k in amon_ra]

    if ramoss not in amon_ra:
        return await message.reply("😆 Yanlış key veya kullanılmış")

    async with aiofiles.open(zenginpicler, mode="a") as f:
        await f.write(f"{message.from_user.id}\n")

    amon_ra.remove(ramoss)
    async with aiofiles.open(ustyt, mode="w") as f:
        await f.write("\n".join(amon_ra) + "\n")

    async with aiofiles.open(yarrayemis, mode="a") as f:
        await f.write(f"{ramoss}\n")

    await message.reply("😼 Vip Key alıp bize Destek olduğun için teşekkürler değerli vip kullanıcı")
            
@ramowlf.on_message(filters.command("cikar"))
async def vipten_cikar(client, message: Message):
    if message.from_user.id not in ramazan_buba:
        return await message.reply("🍑 Babam Kullanabilir Sadece")

    args = message.text.split()

    if len(args) != 2:
        return await message.reply("🤓 Kullanım: `/cikar 8119547604`")

    ramonun_yarra = args[1]

    try:
        async with aiofiles.open(zenginpicler, "r") as f:
            zenginler = await f.readlines()
    except FileNotFoundError:
        return await message.reply(" bulamadım vip.txt dosyasından")

    zenginler = [vip.strip() for vip in zenginler if vip.strip() != ramonun_yarra]

    async with aiofiles.open(zenginpicler, "w") as f:
        await f.writelines([vip + "\n" for vip in zenginler])

    await message.reply(f"😆 `{ramonun_yarra}` vip.txt dosyasından çıkardım")
    
@ramowlf.on_message(filters.command("adsoyad"))
async def ramazan_ozturk(client: Client, message: Message):
    
    if not await vaygavat(client, message.from_user.id):
        return await message.reply(
            "Önce **❤️‍🔥 Kanalımıza** katıl: [Kanalımız](https://t.me/TurkUserBotKanali)\n\nKatıldıktan sonra tekrar /start yaz",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("❤️‍🔥 Kanalımıza Katıl", url="https://t.me/TurkUserBotKanali")]
            ])
        )
    
    args = message.text.split(maxsplit=3)

    if len(args) < 3:
        await message.reply("🥰 bebiş Kullanım şu şekilde \n`/adsoyad ramazan öztürk istanbul` (il isteğe bağlı)]", quote=True)
        return

    ad = args[1]
    soyad = args[2]
    il = args[3] if len(args) > 3 else ""

    url = "https://apiv2.tsgonline.net/tsgapis/Botaltyapi/adpro.php"
    params = {
        "auth": "tsgxyunus",
        "ad": ad,
        "soyad": soyad,
        "il": il
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    data = await response.json()

                    if not data.get("success") or not data.get("data"):
                        await message.reply("😡 Öyle birisi Yok veya api yarra yemiş 😭")
                        return

                    ramazan = ""

                    for i, kisi in enumerate(data["data"], start=1):
                        ramazan += f"🧾 AdSoyad Sorgu {i}\n"
                        ramazan += f"👤 Ad Soyad     : {kisi.get('AD', 'yok')} {kisi.get('SOYAD', '')}\n"
                        ramazan += f"🆔 TC           : {kisi.get('TC', 'Yok')}\n"
                        ramazan += f"📞 GSM          : {kisi.get('GSM', 'Yok')}\n"
                        ramazan += f"👨 Baba Adı     : {kisi.get('BABAADI', 'Yok')}\n👨 Baba Tc        :({kisi.get('BABATC', 'yok')})\n"
                        ramazan += f"👩 Anne Adı     : {kisi.get('ANNEADI', 'Yok')}\n👩 Anne Tc        :({kisi.get('ANNETC', 'Yok')})\n"
                        ramazan += f"🎂 Doğum Tarihi : {kisi.get('DOGUMTARIHI', 'Yok')}\n"
                        ramazan += f"⚰️ Ölüm Tarihi  : {kisi.get('OLUMTARIHI', 'Yok')}\n"
                        ramazan += f"📍 Doğum Yeri   : {kisi.get('DOGUMYERI', 'Yok')}\n"
                        ramazan += f"🏡 Adres        : {kisi.get('ADRESIL', '')} / {kisi.get('ADRESILCE', '')}\n"
                        ramazan += f"🧬 Memleket     : {kisi.get('MEMLEKETIL', '')} / {kisi.get('MEMLEKETILCE', '')} / {kisi.get('MEMLEKETKOY', '')}\n"
                        ramazan += f"📄 Aile Sıra No : {kisi.get('AILESIRANO', 'Yok')}\n"
                        ramazan += f"📄 Birey Sıra No: {kisi.get('BIREYSIRANO', 'Yok')}\n"
                        ramazan += f"❤️ Medeni Hali : {kisi.get('MEDENIHAL', 'yok')}\n"
                        ramazan += f"🚻 Cinsiyet     : {kisi.get('CINSIYET', 'yok')}\n🩵 Geliştirici @ramowlf"
                        ramazan += "-" * 40 + "\n\n"

                    ramos = BytesIO()
                    ramos.write(ramazan.encode("utf-8"))
                    ramos.name = f"{ad}_{soyad}.txt"
                    ramos.seek(0)

                    await message.reply_document(document=ramos, caption="❤️‍🩹 Al kardeş @TuranMuzikBot")
                    ramos.close()

                else:
                    await message.reply("😔 api yarra yemiş", quote=True)

    except Exception:
        pass
  
@ramowlf.on_message(filters.command("tc"))
async def ramazann(client: Client, message: Message):
    
    if not await vaygavat(client, message.from_user.id):
        return await message.reply(
            "Önce **❤️‍🔥 Kanalımıza** katıl: [Kanalımız](https://t.me/TurkUserBotKanali)\n\nKatıldıktan sonra tekrar /start yaz",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("❤️‍🔥 Kanalımıza Katıl", url="https://t.me/TurkUserBotKanali")]
            ])
        )
        
    args = message.text.split(maxsplit=1)

    if len(args) != 2 or not args[1].isdigit() or len(args[1]) != 11:
        await message.reply("🧐 yanlış kullanma \n\n😘 Örnek: `/tc 11111111110`", quote=True)
        return

    tc = args[1]
    url = f"https://apiv2.tsgonline.net/tsgapis/Botaltyapi/adpro.php?auth=tsgxyunus&tc={tc}"

    await message.reply("🔍 Sorgulanıyor bekle", quote=True)

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data = await resp.json()

        if not data.get("success") or not data.get("data"):
            await message.reply("🙂‍↕️ Ya Api yarra yedi yada sen yanlış TC girdin", quote=True)
            return

        kisi = data["data"][0]

        ohh = (
            f"🧾 TC SORGU\n\n"
            f"👤 AD: {kisi.get('AD')}\n"
            f"👥 SOYAD: {kisi.get('SOYAD')}\n"
            f"📱 GSM: {kisi.get('GSM')}\n"
            f"👨 BABA ADI: {kisi.get('BABAADI')} - TC: {kisi.get('BABATC')}\n"
            f"👩 ANNE ADI: {kisi.get('ANNEADI')} - TC: {kisi.get('ANNETC')}\n"
            f"🎂 DOĞUM TARİHİ: {kisi.get('DOGUMTARIHI')}\n"
            f"⚰️ ÖLÜM TARİHİ: {kisi.get('OLUMTARIHI')}\n"
            f"📍 DOĞUM YERİ: {kisi.get('DOGUMYERI')}\n"
            f"🏡 MEMLEKET: {kisi.get('MEMLEKETIL')} / {kisi.get('MEMLEKETILCE')} - {kisi.get('MEMLEKETKOY')}\n"
            f"🏠 ADRES: {kisi.get('ADRESIL')} / {kisi.get('ADRESILCE')}\n"
            f"🆔 AİLE SIRA NO: {kisi.get('AILESIRANO')} | BİREY SIRA NO: {kisi.get('BIREYSIRANO')}\n"
            f"💍 MEDENİ HAL: {kisi.get('MEDENIHAL')}\n"
            f"🚻 CİNSİYET: {kisi.get('CINSIYET')}\n\n🩵 Geliştirici @ramowlf"
        )

        amcik = BytesIO()
        amcik.write(ohh.encode("utf-8"))
        amcik.name = f"{tc} TC.txt"
        amcik.seek(0)

        await message.reply_document(document=amcik, caption="❤️‍🔥 @TuranMuzikBot", quote=True)

    except Exception:
        pass  
        
@ramowlf.on_message(filters.command("adres"))
async def ramco(client: Client, message: Message):
    
    if not await vaygavat(client, message.from_user.id):
        return await message.reply(
            "Önce **❤️‍🔥 Kanalımıza** katıl: [Kanalımız](https://t.me/TurkUserBotKanali)\n\nKatıldıktan sonra tekrar /start yaz",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("❤️‍🔥 Kanalımıza Katıl", url="https://t.me/TurkUserBotKanali")]
            ])
        )
        
    args = message.text.split(maxsplit=1)

    if len(args) != 2 or not args[1].isdigit() or len(args[1]) != 11:
        await message.reply("🧐 Yanlış kullanım. \n\n😘 Örnek: `/adres 11111111110`", quote=True)
        return

    tc = args[1]
    url = f"https://apiv2.tsgonline.net/tsgapis/Botaltyapi/adres.php?tc={tc}"

    await message.reply("🔍 Sorgulanıyor bekle", quote=True)

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data = await resp.json()

        if not data.get("success") or not data.get("data"):
            await message.reply("🙂‍↕️ Ya API'den sorun oldu ya da yanlış TC girdin.", quote=True)
            return

        kisi = data["data"][0]

        azginlik = (
            f"🧾 ADRES SORGU\n\n"
            f"👤 Ad: {kisi.get('AdSoyad')}\n"
            f"📍 Doğum Yeri: {kisi.get('DogumYeri')}\n"
            f"🏠 İkametgah: {kisi.get('Ikametgah')}\n"
            f"💼 Vergi Numarası: {kisi.get('VergiNumarasi')}\n\n🩵 Geliştirici @ramowlf"
        )

        yarrakk = BytesIO()
        yarrakk.write(azginlik.encode("utf-8"))
        yarrakk.name = f"{tc}.txt"
        yarrakk.seek(0)

        await message.reply_document(document=yarrakk, caption="❤️‍🔥 @TuranMuzikBot", quote=True)

    except Exception:
        pass
     
@ramowlf.on_message(filters.command("apartman"))
async def ramazannnn(client: Client, message: Message):
    
    if not await vaygavat(client, message.from_user.id):
        return await message.reply(
            "Önce **❤️‍🔥 Kanalımıza** katıl: [Kanalımız](https://t.me/TurkUserBotKanali)\n\nKatıldıktan sonra tekrar /start yaz",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("❤️‍🔥 Kanalımıza Katıl", url="https://t.me/TurkUserBotKanali")]
            ])
        )
        
    args = message.text.split(maxsplit=1)

    if len(args) != 2 or not args[1].isdigit() or len(args[1]) != 11:
        await message.reply("🧐 Yanlış kullanım. \n\n😘 Örnek: `/apartman 11111111110`", quote=True)
        return

    tc = args[1]
    url = f"https://apiv2.tsgonline.net/tsgapis/Botaltyapi/apartman.php?tc={tc}"

    await message.reply("🔍 Sorgulanıyor bekle", quote=True)

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data = await resp.json()

        if not data.get("success") or not data.get("data"):
            await message.reply("🙂‍↕️ Ya API'den sorun oldu ya da yanlış TC girdin.", quote=True)
            return

        yarbeline = data["data"]

        Instagram_ramowlf = (
            f"🧾 APARTMAN SORGU\n\n"
            f"👤 Ad: {yarbeline.get('ADSOYAD')}\n"
            f"📍 Doğum Yeri: {yarbeline.get('DOGUMYERI')}\n"
            f"🏠 Adres: {yarbeline.get('ADRES')}\n"
            f"💼 Vergi Numarası: {yarbeline.get('VERGINO')}\n\n"
            f"👨‍👩‍👧‍👦 Apartmandaki Diğer Kişiler:\n"
        )

        for kisi in yarbeline.get("Apartmandakiler", []):
            Instagram_ramowlf += (
                f"\n👤 Ad: {kisi.get('ADSOYAD')}\n"
                f"📍 Doğum Yeri: {kisi.get('DOGUMYERI')}\n"
                f"🏠 Adres: {kisi.get('ADRES')}\n"
                f"💼 Vergi Numarası: {kisi.get('VERGINO')}\n"
            )

        ramowlf_Insta = BytesIO()
        ramowlf_Insta.write(Instagram_ramowlf.encode("utf-8"))
        ramowlf_Insta.name = f"{tc} apartman.txt"
        ramowlf_Insta.seek(0)

        await message.reply_document(document=ramowlf_Insta, caption="❤️‍🔥 @TuranMuzikBot", quote=True)

    except Exception:
        pass
        
@ramowlf.on_message(filters.command("tcgsm"))
async def github_ramowlf(client: Client, message: Message):
    
    if not await vaygavat(client, message.from_user.id):
        return await message.reply(
            "Önce **❤️‍🔥 Kanalımıza** katıl: [Kanalımız](https://t.me/TurkUserBotKanali)\n\nKatıldıktan sonra tekrar /start yaz",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("❤️‍🔥 Kanalımıza Katıl", url="https://t.me/TurkUserBotKanali")]
            ])
        )
        
    args = message.text.split(maxsplit=1)

    if len(args) != 2 or not args[1].isdigit() or len(args[1]) != 11:
        await message.reply("🧐 Yanlış kullanım. \n\n😘 Örnek: `/tcgsm 11111111110`", quote=True)
        return

    tc = args[1]
    url = f"https://apiv2.tsgonline.net/tsgapis/Botaltyapi/tcgsm.php?tc={tc}"

    await message.reply("🔍 Sorgulanıyor bekle", quote=True)

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data = await resp.json()

        if not data.get("success") or not data.get("data"):
            await message.reply("🙂‍↕️ Ya API'den sorun oldu ya da yanlış TC girdin.", quote=True)
            return

        sad_ramo = data["data"]

        gece_gunduz = (
            f"🩵 Geliştirici @ramowlf\n\n"
            f"🧾 TC GSM NUMARALAR\n\n"
            f"👤 TC: {tc}\n\n"
            f"📱 GSM Numaralar:\n"
        )

        for gsm in sad_ramo:
            gece_gunduz += f"- {gsm.get('GSM')}\n"

        gece = BytesIO()
        gece.write(gece_gunduz.encode("utf-8"))
        gece.name = f"{tc} tcgsm.txt"
        gece.seek(0)

        await message.reply_document(document=gece, caption="❤️‍🔥 @TuranMuzikBot", quote=True)

    except Exception:
        pass
        
@ramowlf.on_message(filters.command("gsmtc"))
async def telegram_ramowlf(client: Client, message: Message):
    
    if not await vaygavat(client, message.from_user.id):
        return await message.reply(
            "Önce **❤️‍🔥 Kanalımıza** katıl: [Kanalımız](https://t.me/TurkUserBotKanali)\n\nKatıldıktan sonra tekrar /start yaz",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("❤️‍🔥 Kanalımıza Katıl", url="https://t.me/TurkUserBotKanali")]
            ])
        )
        
    args = message.text.split(maxsplit=1)

    if len(args) != 2 or not args[1].isdigit():
        await message.reply("🧐 Yanlış kullanım. \n\n😘 Örnek: `/gsmtc 5326112849`", quote=True)
        return

    gsm = args[1]
    url = f"https://apiv2.tsgonline.net/tsgapis/Botaltyapi/gsmtc.php?gsm={gsm}"

    await message.reply("🔍 Sorgulanıyor bekle", quote=True)

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data = await resp.json()

        if not data.get("success") or not data.get("data"):
            await message.reply("🙂‍↕️ Ya API'den sorun oldu ya da yanlış GSM girdin.", quote=True)
            return

        pff = data["data"]

        ok = (
            f"🩵 Geliştirici \n\n"
            f"🧾 Gsmtc sorgu\n\n"
            f"📱 GSM: {gsm}\n\n"
            f"👤 TC:\n"
        )

        for ramo in pff:
            ok += f"- {ramo.get('TC')}\n"

        aynen = BytesIO()
        aynen.write(ok.encode("utf-8"))
        aynen.name = f"{gsm} gsmtc.txt"
        aynen.seek(0)

        await message.reply_document(document=aynen, caption="❤️‍🔥 @TuranMuzikBot", quote=True)

    except Exception as e:
        await message.reply(f"@ramowlf yaz", quote=True)
      
@ramowlf.on_message(filters.command("aile"))
async def Ig_ramowlf(client: Client, message: Message):
    
    if not await vaygavat(client, message.from_user.id):
        return await message.reply(
            "Önce **❤️‍🔥 Kanalımıza** katıl: [Kanalımız](https://t.me/TurkUserBotKanali)\n\nKatıldıktan sonra tekrar /start yaz",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("❤️‍🔥 Kanalımıza Katıl", url="https://t.me/TurkUserBotKanali")]
            ])
        )
        
    args = message.text.split(maxsplit=1)

    if len(args) != 2 or not args[1].isdigit():
        await message.reply("🫣 Yanlış kullanım \n\n🤓 Örnek: `/aile 11111111110`", quote=True)
        return

    tc = args[1]
    url = f"https://apiv2.tsgonline.net/tsgapis/Botaltyapi/aile.php?tc={tc}"

    await message.reply("🔍 Sorgulanıyor bekle", quote=True)

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data = await resp.json()

        if not data.get("success") or not data.get("data"):
            await message.reply("🙂‍↕️ API'den veri alınamadı veya yanlış TC girdiniz", quote=True)
            return

        aboo = data["data"]
        ramoss = f"👨‍👩‍👧‍👦 AİLE SORGUSU - TC: {tc}\n\n"

        for kisi in aboo:
            ramoss += (
                f"👤 ADI: {kisi.get('AD', '')} {kisi.get('SOYAD', '')}\n"
                f"📱 GSM: {kisi.get('GSM', 'YOK')}\n"
                f"🧬 BABA: {kisi.get('BABAADI', '')} - {kisi.get('BABATC', '')}\n"
                f"👩 ANNE: {kisi.get('ANNEADI', '')} - {kisi.get('ANNETC', '')}\n"
                f"🎂 D.TARİHİ: {kisi.get('DOGUMTARIHI', '')}\n"
                f"⚰️ Ö.TARİHİ: {kisi.get('OLUMTARIHI', 'YOK')}\n"
                f"🌍 D.YERİ: {kisi.get('DOGUMYERI', '')}\n"
                f"🏡 MEMLEKET: {kisi.get('MEMLEKETIL', '')} / {kisi.get('MEMLEKETILCE', '')} / {kisi.get('MEMLEKETKOY', '')}\n"
                f"📍 ADRES: {kisi.get('ADRESIL', '')} / {kisi.get('ADRESILCE', '')}\n"
                f"📄 AİLE SIRA NO: {kisi.get('AILESIRANO', '')} - BİREY SIRA NO: {kisi.get('BIREYSIRANO', '')}\n"
                f"💍 MEDENİ HAL: {kisi.get('MEDENIHAL', '')}\n"
                f"🚻 CİNSİYET: {kisi.get('CINSIYET', '')}\n"
                f"🧿 YAKINLIK: {kisi.get('Yakinlik', '')}\n\n"
                f"🩵 Geliştirici @ramowlf\n"
                                f"───────────────────────\n"
            )

        from io import BytesIO
        yarin = BytesIO(ramoss.encode("utf-8"))
        yarin.name = f"{tc} Aile.txt"

        await message.reply_document(document=yarin, caption="❤️‍🔥 @TuranMuzikBot", quote=True)

    except Exception as e:
        await message.reply(f"@ramowlf yaz", quote=True)
        
        
print("bot aktif")
ramowlf.run()