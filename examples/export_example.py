#Asciimation (https://github.com/octobanana/asciimation) by octobanana
import sys,os
sys.path.insert(0,"../") #to be able to call boip from the examples folder


#Importing animator
import animator

app=animator.Animator()
app.new_command(40,"<COMMAND BEGIN>exec_from_file:test<COMMAND END>",True)

app.export_scenes("export",type="asciimation") #Exports all scenes to one file


#Play the Animation
os.system("asciimation -f export")

"""
If you get a error message do this steps

-------------------------------------------------

LINUX

$alias asciimation="build/location/asciimation"

-------------------------------------------------

WINDOWS

Add asciimation build directory to environment variables

-------------------------------------------------
"""
