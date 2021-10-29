"""
Boip Animator is a python library for creating text-based animations.

sample
import animator
app = animator.Animator()
app.scene("<")
app.scene("<<")
app.scene("<<<")
app.scene("<<<")
app.scene("<<<<")
app.play()
"""
import os
import sys
import time

version = "1.0"
class Animator:
    def __init__(self, sleep=1.0):
        self.scene_count = 0
        self.scenes = []
        self.sleep = sleep
    def version(self):
        return "1.0"
    def scene(self, scene):
        """add new scene"""
        self.scenes.append(scene)
        self.scene_count += 1
    def list_scenes(self):
        for i in range(len(self.scenes)):
            print(self.scenes[i])
    def scenes_count(self):
        return scene_count
    def set_sleep(self,sleep):
        self.sleep = sleep

    def clear(self):
        """clear screen"""
        if os.name == "nt":
            
            os.system("cls")
        else:
            os.system("clear")
    def play(self):
        for i in range(len(self.scenes)):
            self.clear()
            print(self.scenes[i])
            time.sleep(self.sleep)
            self.clear()
    def export(self, exportfile):
        print("Yakında...")
        
