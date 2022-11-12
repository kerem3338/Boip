import sys,os
sys.path.insert(0,"../") #to be able to call boip from the examples folder

import animator
app=animator.Animator()
app.scene("->")
app.scene("-->")
app.scene(" -->")
app.scene("  -->")
app.scene("   -->")
app.play()
# For better and smooth experince play animation with cplay() 
#animator.curses.wrapper(app.cplay)
