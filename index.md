## Boip Ascii Animatör


Boip Konsol tabanlı animasyonlar oluşturmanızı sağlayan bir kütüphanedir.


### Kurulum

[Github](https://github.com/kerem3338/Boip) Adresine gidin ve Yeşil Code butonuna tıklayın açılan pencereden 'Download Zip' seçeneğine tıklayın ve inen zip dosyasını bir klasöre çıkartın


## Kullanmaya Başlama

Boip'i indirdiğiniz klasörde yeni bir dosya açın ve herhangi bir metin editöründe oluşturduğunuz dosyayı açın ve artık animasyonunuzu oluşturmaya hazırsınız!

**Boip'i İçeri Aktarma**<br>
`import animator` ile Boip'i içeri aktarıyoruz.<br>

**Animasayonu tanımlama**<br>
`animasyon=animator.Animator()` ile yeni bir sınıf oluşturuyoruz.<br>

### Komutlar
`scene(scene)` animasyona sahne ekler.<br>
`copy_last(copy_amount=None)` son sahneyi kopyalar (Eğer copy_amount değişkeni None değilse son sahneyi okadar kez kopyalar)<br>
`version` Boip'in versiyonunu döndürür.<br>
`copy_from_id(id,copy_amount=None)` Seçili sahneyi kopyalar.<br>
`scene_from_id(id)` Seçili sahneyi gösterir.<br>
`list_scenes` Bütün sahneleri gösterir.<br>
`scenes_count` Animasyondaki sahne sayısını gösterir.<br>
`play` Animasyonu oynatır.<br>

### Örnek

```py
import animator
animasyon=animator.Animator()
animasyon.scene("->")
animasyon.scene("-->")
animasyon.scene("--->")
animasyon.scene("---->")
animasyon.play()
```

### İletişim

Yaşadığınız Sorunları veya isteklerinizi [zoda@vuhuv.com](zoda@vuhuv.com) Adresine iletin.
