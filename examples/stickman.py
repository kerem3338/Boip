from animator import Animator
app=Animator(0.5)
app.scene("""
    ---
   |   |
    ---
     |
  \\--|--/
     |
    / \\
    | |
    | |
""")
app.copy_last(1)
app.scene("""
    ---
   |   |
    ---
     |  |
  \\--|-/
     |
    / \\
    | |
    | |
""")
app.copy_last(1)
app.scene("""
    ---
   |   |
    ---
     |  /
  \\--|-/
     |
    / \\
    | |
    | |
""")
app.copy_last(1)
app.scene("""
    ---
   |   |
    ---
     |  |
  \\--|-/
     |
    / \\
    | |
    | |
""")
app.copy_last(1)
app.scene("""
    ---
   |   |
    ---
     | \\
  \\--|-/
     |
    / \\
    | |
    | |
""")
app.play()
