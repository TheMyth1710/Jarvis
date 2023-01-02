bot_name = "Jarvis" #What would you want to name the bot? The bot will use this name to call itself! Just change the characters in between of ""
user_name = "Mudith" #You can set your own name here which the bot will use sometimes to help you! Just change the characters in between of ""
call_as = "sir".capitalize() #You can customize this value to whatever you want the bot to call you! Just change the characters in between of ""
choice_for_name = "3" #Enter either 1 (Where bot calls you as the variable `call_as`) | 2 (Where bot calls you as the variable `user_name`) | 3 (Where bot uses both variables when needed)
#Default for ^^^ is "3" | Note, if you leave it blank, or put any other value instead of 1,2,3 then it will be interpreted as 3!
music_dir = "C:\\Users\\dagam\\Music\\Fav Music" #Enter your specific song directory (downloaded songs in device)!
sleeping_hour = "" #Enter the usual hour you want to sleep! Note, the hour should be in 24 hour format
'''
Introducing customizable apps which you can open!.
And the second value should be, what you want to call it! Please don't add more than 2 values!
Please change the values of all the variables in this area with the name "app_(1-10)"!
Then, change their respective directories!

For example:

app_1 = ['Chrome', 'Engine'] 
Here, 'Chrome' is the name of the app and 'Engine' is what I name it! You can open this app by saying 'Open Chrome' or 'Open Engine'! I recommend not to add more than 3 names for a file, for errors.
dir_1 = ""
Note: Do not PUT in the location path of the file! That will open the folder where the file exists! For example:
To open Chrome, this is the directory of it: 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs'
Note, this directory would open the Programs folder! 
So, to open the app, simply edit the directory like this: 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Chrome'
Replace the single \ with \\ so that the code functions, this is because of python interpretation, and thus needs to be followed.
'''
app1 = ['visual studio code','code','vsc']
dir1 = "C:\\mudith\\Microsoft VS Code\\Code.exe" #Directory of `app_1`!

app2 = ['edge','browser'] #2nd Customizable App!
dir2 = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" #Directory of `app_2`!

app3 = ['minecraft','mc'] #3rd Customizable App!
dir3 = "C:\\Program Files (x86)\\Minecraft Launcher\\MinecraftLauncher.exe" #Directory of `app_3`!

app4 = []#4th Customizable App!
dir4 = "" #Directory of `app4`!

app5 = ['excel'] #5th Customizable App!
dir5 = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\EXCEL.EXE" #Directory of `app5`!

app6 = ['word'] #6th Customizable App!
dir6 = "C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE" #Directory of `app6`!

app7 = ['powerpoint'] #7th Customizable App!
dir7 = "" #Directory of `app7`!

app8 = [] #8th Customizable App!
dir8 = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\POWERPNT.EXE" #Directory of `app8`!

app9 = [] #9th Customizable App!
dir9 = "" #Directory of `app9`!

app10 = [] #10th Customizable App!
dir10 = "" #Directory of `app10`!
from PyDictionary import PyDictionary as dic