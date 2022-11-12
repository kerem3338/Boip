# V2.7


* changes.md dosyası eklendi.
* Çeşitli Hata düzeltmeleri.
* Yazım hataları düzeltildi.
* `export_scenes_dir` fonksiyonu artık çıktı işlemini onaylarken işlemi iptal ederseniz programı sonlandırmayacak. 
* `export_scenes` fonksiyonu ile artık animasyonlarınızı (asciimation)[https://github.com/octobanana/asciimation] animasyonu olarakta dışa aktarabilirsiniz!
* Animasyon yaratmayı kolaylaştıran Grafik sahne arayüz programı hazırlanıyor.


# V2.8 (Büyük Güncelleme)
* `LICENSE` dosyasındaki '2021' yazısı '2022' olarak değiştirildi.
* `log` fonksiyonu ile artık önceki sahnelere yeni eklemeler yapmak daha kolay.
* `logtype` fonksiyonu sayesinde sahneye kolayca yazı yazma efekti ekleyin.
* `logreset` fonksiyonu ile log'u kolayca temizleyin.
* `export_scenes` fonksiyonu `type="asciimation"` argümanı ile çağırldığında oluşan sahne eklememe hatası giderildi
* `cplay` fonksiyonu ile animasyonların curses modülü aracılığı ile oynatılabilmesine imkan tanındı.
* `scene_from_id` artık sadece sahne içeriğini döndürüyor veriyor.
* Artık animasyon oynatılırken komutlar okunup çalıştırılabilecek (animasyon oynatılırken hızı değiştirmek gibi).
* `commands` klasörü eklendi.
* `testcommandframe` `fonksiyonu ile komut yöneticisini test edebilirsiniz.
*  `commandframe` fonksiyonu ile komutları çalıştırabilirsiniz
* `new_command` fonksiyonu ile komut ekleyebilirsiniz
* Dökümantasyon Güncelleştirildi
* `lenght` fonksiyonu güncellendi.
* `README.md` güncellendi.
* `Animator(warning=True)` Animator sınıfına warning argümanı eklendi. İşlevi animasyon oynatılmadan önce nasıl çıkış yapılacağını göstermektir
* `Animator(add_empty=False)` Animator sınıfına add_empty argümanı eklendi. İşlevi animasyona boş kare eklemektir.
* Eğer kullanıcı `colored_traceback` modülünü kurmuş ise renklendirilmiş hata mesajları alacaktır

## Yeni Komutlar
 - `sleep` komutu ile animasyon hızını ayarlayabilirsiniz
 - `exec_from_file` komutu ile 'commands' klasöründeki bir komutu çalıştırabilirsiniz.
 - `commands/test` komutu eklendi (exec_from_file:test) 
