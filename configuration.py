import data_values as data
app1 = data.app1
app2 = data.app2
app3 = data.app3
app4 = data.app4
app5 = data.app5
app6 = data.app6
app7 = data.app7
app8 = data.app8
app9 = data.app9
app10 = data.app10

#The 10 directories for the customizable apps!
dir1 = data.dir1
dir2 = data.dir2
dir3 = data.dir3
dir4 = data.dir4
dir5 = data.dir5
dir6 = data.dir6
dir7 = data.dir7
dir8 = data.dir8
dir9 = data.dir9
dir10 = data.dir10
bot_configuration = open("bot_configuration.txt","w")
bot_configuration.truncate()
bot_configuration.write("This is the bot configuration settings viewer for your bot! - Created by Mudith Daga")
bot_configuration.write("\n\nBot Name = "+data.bot_name+" (This is the name for your bot)\nUser Name = "+data.user_name+" (This is your actual name)\nUser Pronoun = "+data.call_as+" (This is the name you want the bot to call you with!)")
bot_configuration.write('\n\nThis is the part of customizable "open (app)" commmand. Herein, you can open the desired application you want (Max = 10)')
bot_configuration.write("\nThese are your current values for variables:\n(Note, app_int is the name of the app and dir_int is the directory for the app!")


#IF NO VALUE FOR DIR
if dir1 == "":
    dir1 = "No directory specified for App 1"
if dir2 == "":
    dir2 = "No directory specified for App 2"
if dir3 == "":
    dir3 = "No directory specified for App 3"
if dir4 == "":
    dir4 = "No directory specified for App 4"
if dir5 == "":
    dir5 = "No directory specified for App 5"
if dir6 == "":
    dir6 = "No directory specified for App 6"
if dir7 == "":
    dir7 = "No directory specified for App 7"
if dir8 == "":
    dir8 = "No directory specified for App 8"
if dir9 == "":
    dir9 = "No directory specified for App 9"
if dir10 == "":
    dir10 = "No directory specified for App 10"
#IF NO VALUE FOR APP
if app1 == "":
    app1 = "No specified app for App 1"
if app2 == "":
    app2 = "No specified app for App 2"
if app3 == "":
    app3 = "No specified app for App 3"
if app4 == "":
    app4 = "No specified app for App 4"
if app5 == "":
    app5 = "No specified app for App 5"
if app6 == "":
    app6 = "No specified app for App 6"
if app7 == "":
    app7 = "No specified app for App 7"
if app8 == "":
    app8 = "No specified app for App 8"
if app9 == "":
    app9 = "No specified app for App 9"
if app10 == "":
    app10 = "No specified app for App 10"

bot_configuration.write(f'''

App 1 = {app1.replace("open ","").capitalize()}
Directory for App 1 = {dir1}

App 2 = {app2.replace("open ","").capitalize()}
Directory for App 2 = {dir2}

App 3 = {app3.replace("open ","").capitalize()}
Directory for App 3 = {dir3}

App 4 = {app4.replace("open ","").capitalize()}
Directory for App 4 = {dir4}

App 5 = {app5.replace("open ","").capitalize()}
Directory for App 5 = {dir5}

App 6 = {app6.replace("open ","").capitalize()}
Directory for App 6 = {dir6}

App 7 = {app7.replace("open ","").capitalize()}
Directory for App 7 = {dir7}

App 8 = {app8.replace("open ","").capitalize()}
Directory for App 8 = {dir8}

App 9 = {app9.replace("open ","").capitalize()}
Directory for App 9 = {dir9}

App 10 = {app10.replace("open ","").capitalize()}
Directory for App 10 = {dir10}
''')
bot_configuration.write("\n\n\n\nTo change any of these variables go to data_values.py in the jarvis folder! For more help visit: ")
bot_configuration.close()