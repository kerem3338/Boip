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
from playsound import playsound
#["foo", "bar", "baz"].index("bar")
class Animator:
    def __init__(self, sleep=1.0):
        self.scenes_count = 0
        self.scenes = []
        self.sleep = sleep
        self.version = "2.1"
        
    def version(self):
        return self.version

    def lenght(self):
        return self.scenes_count*self.sleep

    def scence_from_file(self, file, encoding="utf8"):
        """add new scene from file"""
        with open(file, "r", encoding=encoding) as file:
            self.scenes.append(file.read())
            self.scene_count += 1
            
    def scene(self, scene):
        """add new scene"""
        self.scenes.append(scene)
        self.scenes_count += 1
        
    def shape(self, shape, position=None):
        """return shape"""
        square = "##\n##"
        if shape == "square":
            return square
        else:
            print(f"InvalidShape: {shape}")
            
    def copy_last(self, copy_count=None):
        """copy last scene"""
        if copy_count is None:
            last_scene = len(self.scenes)-1
            self.scenes.append(self.scenes[last_scene])
            self.scenes_count +=1
        else:
            for i in range(copy_count):
                self.scenes_count += 1
                last_scene = len(self.scenes)-1
                self.scenes.append(self.scenes[last_scene])
                
    def copy_from_id(self, id, copy_count=None):
        if copy_count is None:
            scene = self.scenes[id]
            self.scenes.append(scene)
            self.scenes_count += 1
        else:
            for i in range(copy_count):
                self.scenes_count += 1
                self.scenes.append(self.scenes[id])
        
    
    def play_sound(self, soundfile, background:bool=True):
        if background is True:
            playsound(soundfile, False)
        elif background is False:
            playsound(soundfile)
        else:
            print(f"InvalidArgument: {backgound}")
            
    def scene_from_id(self, id):
        print(self.scenes[id])
        
    def list_scenes(self):
        for i in range(len(self.scenes)):
            print(self.scenes[i])
            
    def scenes_count(self):
        """NOT:Sahne içinde kullanılırsa bulunduğu sahneyi eklemez örnek: eğer projenizde 6 sahne varsa 5 sahne gösterecektir eğer sahnenin içinde kullanmazsanız sahne sayınızı normal bir şekilde gösterecektir""" 
        return self.scenes_count
    
    def set_sleep(self,sleep):
        self.sleep = sleep
    
    def clear(self):
        """clear screen"""
        if os.name == "nt":
            
            os.system("cls")
        else:
            os.system("clear")
            
    def play(self):
        """Play all scenes"""
        for i in range(len(self.scenes)):
            self.clear()
            print(self.scenes[i])
            time.sleep(self.sleep)
            self.clear()

    def export_scenes(self, exportfile, encoding="utf8"):
        """export all scenes"""
        with open(exportfile, "w", encoding=encoding) as exportfile:
            exportfile.write(f"Created using Boip Animator {self.version}")
            for i in range(len(self.scenes)):
                exportfile.write("\n")
                exportfile.write(self.scenes[i])
