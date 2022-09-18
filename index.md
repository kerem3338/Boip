# Boip Ascii Animatör
> This page is currently not available for other languages

# Kurulum

[Python.org](https://python.org) adresinden python'u kurunuz.(3.8+)<br>
Boip'i kurmak için ilk önce [Github](https://github.com/kerem3338/Boip) Adresine gidin ve yeşil 'code' butonuna tıklayın ve ardından download zip seçeneğine tıklayın.<br>İndirilen dosyayı winrar veya başka bir program aracılığı ile bir klasöre çıkartın.

# Hadi Test Edelim
Boip kurduk artık sıra animasyon yapmakta.Bunun için boip'i indirdiğiniz klasörde yeni bir dosya oluşturun.
- Oluşturduğunuz dosyanın sonunun `.py` ile bittiğinen emin olun!

Oluşturduğunuz dosyayı herhangi bir metin düzenleyicisi ile açın.(Başlangıç aşaması için notepad++'ı tercih edebilirsiniz)<br>

## Animasyonu oluşturma
Animasyonumuz oluşturmak için öncelikle boip'i içe aktarmamız gerekiyor bunu yapmak için oluşturduğumuz dosyaya bir kod parçacığı ekleyeceğiz.<br>
```py
import animator #Boip'i içe aktardık
```
<br>

Güzel artık animasyonu yaratmak için `Animator`'ü çağırabiliriz.Bu sınıf bize animasyonumuzu oluşturmak için yardımcı olucak.<br>

```py
app=animator.Animator()
```

Şimdi ise animasyonumuza sahne eklemek için `scene` fonksiyonunu kullanalım.<br>

```py
app.scene("M")
```

Animasyonumuzu canlandırmak için birkaç sahne daha ekliyelim

```py
app.scene("ME")
app.scene("MER")
app.scene("MERH")
app.scene("MERHA")
app.scene("MERHAB")
app.scene("MERHABA")
```

Sonunda animasyonumuz tamamlandı artık onu izleyebiliriz! Bunun için `play` fonksiyonunu kullanacağız.<br>
```py
app.play()
```
- Eğer ekranın yanıp sönmesini istemiyorsanız `export_scenes(<dosya adı>,type='asciimation')` bu fonksiyonu kullanarak animasyonunuzu dışa aktarın sonra ise eğer windows kullanıyorsanız [replit](https://replit.com) adresinden  eğer bir linux dağıtımı kullanıyorsanız terminalinizden [asciimation](https://github.com/octobanana/asciimation)'u kurunuz 

### Tüm kod
```py
import animator #Boip'i içe aktardık
app=animator.Animator()
app.scene("M")
app.scene("ME")
app.scene("MER")
app.scene("MERH")
app.scene("MERHA")
app.scene("MERHAB")
app.scene("MERHABA")
app.play()
```