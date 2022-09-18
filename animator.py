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
import locale
import glob
import getpass
import threading

config = {
    "err-show": True
}

try:
    import cursor # Bu kütüphane konsolda imleci saklamak için gereklidir. | This library is required to store the cursor in the console.
except ModuleNotFoundError:
    if config["err-show"]:
        if locale.getdefaultlocale[0] == "tr_TR":
            print("'Cursor' Kütüphanesi bulunamadı lütfen kütüphaneyi indiriniz")
        else:
            print("'Cursor' Library not found please download the library")
    else:
        pass



class Frame:
    """Frame class for creating frames."""
    def __init__(self,content:str):
        self.content=content
        
    
    def change(self,content:str):
        self.content=content

    def __str__(self):
        return self.content

class Animator:
    def __init__(self, sleep_mode=True, sleep:int or float=1.0):
        self.sleep_mode=sleep_mode
        self.system_lang = locale.getdefaultlocale()[0]

        if self.system_lang == "tr_TR":
            self.sleep_error = "Hata: Uyku Modu aktif değil"
        else:
            self.sleep_error = "Error: Sleep mode not activated!"
            
        self.scenes_count = 0
        self.scenes = []
        
        self.sleep = sleep
        self.nmode_char="\n"
        self.version = "2.7"
        

        self.animation_info = {"author": getpass.getuser(), "usr_lang": self.system_lang, "sleep_mode": self.sleep_mode, "sleep": self.sleep, "scene_count": self.scenes_count, "boip_ver": self.version}
    
    def version(self):
        return self.version

    def lenght(self):
        if self.sleep_mode is True:
            if type(self.sleep) == int:
                return int(self.scenes_count)*int(self.sleep)
            elif type(self.sleep) == float:
                return float(self.scenes_count)*self.sleep
        else:
            print(self.sleep_error)

    def create_config(self, filename):
        with open(filename, "w") as file:
            file.write(self.animation_info)

    def scene_from_file(self, file, encoding="utf8"):
        """add new scene from file"""
        with open(file, "r", encoding=encoding) as file:
            self.scenes.append(file.read())
            self.scene_count += 1

    def scenes_from_file(self,filename,encoding="utf8"):
        """adds new scenes from file"""
        with open(filename,"r",encoding=encoding) as f:
            scenes_count=f.read().split(",")
            for i in range(len(scenes_count)-1):
                self.scenes.append(scenes_count[i])
                 
    def scenes_from_dir(self, dir, fileextension="txt"):
        """adds new scenes from dir
Example
test_directory/
0.txt
1.txt
"""
        for i in range(len(glob.glob(f"{dir}\\*.{fileextension}"))):
            with open(f"{dir}\\{i}.{fileextension}", "r") as file:
                self.scenes.append(file.read())
                self.scenes_count += 1

    def scene(self, scene):
        """add new scene"""
        
        self.scenes.append(scene)
        self.scenes_count += 1
    
    def shape(self, shape, position=None):
        """returns a shape"""
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
            self.scenes_count += 1
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


    def scene_from_id(self, id):
        print(self.scenes[id])

    def list_scenes(self):
        for i in range(len(self.scenes)):
            print(self.scenes[i])

    def scenes_count(self):
        """NOT:Sahne içinde kullanılırsa bulunduğu sahneyi eklemez örnek: eğer projenizde 6 sahne varsa 5 sahne gösterecektir eğer sahnenin içinde kullanmazsanız sahne sayınızı normal bir şekilde gösterecektir"""
        return self.scenes_count

    def set_sleep(self, sleep:int or float):
        if self.sleep_mode is True:
            self.sleep = sleep
        else:
            print(self.sleep_error)
        
    

    
    def clear(self,nmode=False,scenelenght=None,lastlenght=None):
        """clear screen"""
        if nmode == False:
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
        else:
            print(self.nmode_char*(scenelenght*os.get_terminal_size().columns))

    def play(self,nmode=False):
        """Starts Animation"""
        try:
            cursor.hide()
        except NameError:
            pass

        playing_scene=0
        if self.sleep_mode is True:
            for i in range(len(self.scenes)):
                try:
                    playing_scene=i
                    scene_lenght=len(self.scenes[i].splitlines())
                    last_lenght=len(self.scenes[i].splitlines())
                    self.clear(nmode=nmode,scenelenght=scene_lenght,lastlenght=last_lenght)
                    print(self.scenes[i])
                    time.sleep(self.sleep)
                    self.clear(nmode=nmode,scenelenght=scene_lenght,lastlenght=last_lenght)
                except KeyboardInterrupt:
                    self.clear()
                    print(f"Exited... Last scene: {playing_scene}")
                    cursor.show()
                    sys.exit()
            
        else:
            for i in range(len(self.scenes)):
                try:
                    scene_lenght=len(self.scenes[i].splitlines())
                    last_lenght=len(self.scenes[i].splitlines())
                    playing_scene=i
                    self.clear(nmode=nmode,scenelenght=scene_lenght,lastlenght=last_lenght)
                    print(self.scenes[i])
                    self.clear(nmode=nmode,scenelenght=scene_lenght,lastlenght=last_lenght)
                except KeyboardInterrupt:
                    self.clear()
                    print(f"Exited... Last scene: {playing_scene}")
                    cursor.show()
                    sys.exit()
        
                    





  
        


    def export_scenes_dir(self, dir, fileextension="txt"):
        """Exports All scenes to directory"""
        _ok=None
        if self.system_lang == "tr_TR":
            print("Yapmak istediğiniz işlem Kritik bir işlemdir\nEğer sahne sayısı fazla bir animasyonun çıktısını almak istiyorsanız bu yöntem önerilmez\nBilgisayarınızın hızını düşürebilir ayrıca diskte büyük miktarda yer kaplar")
            onayla = input("Onaylıyormusunuz (evet/hayır/hayir)")
            if onayla == "evet":
                _ok=True
            elif onayla == "hayır" or "hayir":
                pass
        else:
            print("The operation you want to do is a critical operation\nIf you want to output an animation with a large number of scenes, this method is not recommended\nIt may reduce the speed of your computer, and it also takes up a lot of space on the disk.")
            onayla = input("Do you confirm (yes/no)")
            if onayla == "yes":
                _ok=True
            elif onayla == "no":
                pass
        if _ok:
            if os.path.isdir(dir):
                for i in range(len(self.scenes)):
                    with open(f"{dir}\\{i}.{fileextension}", "w") as file:
                        file.write(self.scenes[i])
            else:
                if self.system_lang == "tr_TR":
                    print(f"{dir} Dosya yolu bulunamadı")
                else:
                    print("f{dir} File path not found")

    def export_scenes(self, exportfile, encoding="utf8",type="normal",x=30,y=30):
        """export all scenes"""
        with open(exportfile, "w", encoding=encoding) as exportfile:

            if type=="asciimation":
                exportfile.write(f"x:{x}\ny:{y}\nBEGIN\n")
                for i in range(len(self.scenes)):
                    if i==0:
                        pass
                    else:exportfile.write("\nEND\n")
                    scene=self.scenes[i]
                    scene=scene.replace("END","end")
                    exportfile.write(scene)

            if type=="normal":
                for i in range(len(self.scenes)):
                    exportfile.write(",")
                    exportfile.write(self.scenes[i])
