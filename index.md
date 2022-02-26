## Boip Ascii Animatör


Boip Konsol tabanlı animasyonlar oluşturmanızı sağlayan bir kütüphanedir.


### Kurulum

[Github](https://github.com/kerem3338/Boip) Adresine gidin ve Yeşil Code butonuna tıklayın açılan pencereden 'Download Zip' seçeneğine tıklayın ve inen zip dosyasını bir klasöre çıkartın


## Kullanmaya Başlama

Boip'i indirdiğiniz klasörde yeni bir dosya açın ve herhangi bir metin editöründe oluşturduğunuz dosyayı açın ve artık animasyonunuzu oluşturmaya hazırsınız!

**Boip'i İçeri Aktarma**
`import animator` ile Boip'i içeri aktarıyoruz.

**Animasayonu tanımlama**
`animasyon=animator.Animator()` ile yeni bir sınıf oluşturuyoruz.

### Komutlar
`scene(scene)` animasyona sahne ekler.
`copy_last(copy_amount=None)` son sahneyi kopyalar (Eğer copy_amount değişkeni None değilse son sahneyi okadar kez kopyalar)
`version` Boip'in versiyonunu döndürür.
`copy_from_id(id,copy_amount=None)` Seçili sahneyi kopyalar.
`scene_from_id(id)` Seçili sahneyi gösterir.
`list_scenes` Bütün sahneleri gösterir.
`scenes_count` Animasyondaki sahne sayısını gösterir.
`play` Animasyonu oynatır.

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
