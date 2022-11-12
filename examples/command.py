import sys
sys.path.insert(0,"../") #to be able to call boip from the examples folder


import animator #Importing animator

app=animator.Animator(add_empty=True) #add_empty: Adds empty frame
app.new_command(40,"<COMMAND BEGIN>exec_from_file:test<COMMAND END>",True) #This command is for executing the test file in the commands folder.
animator.curses.wrapper(app.cplay)
