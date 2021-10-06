# CicekSepeti Product Sorting
Proje Web Sitesi: https://sortciceksepeti.herokuapp.com/

Sitelere girdiğimiz zaman ürünleri puana göre sıraladığımız da bu sıralamanın nasıl yapıldığını merak ettiniz mi?

100 yorum alıp 4.5 puan alan ürün mü üst sırada olmalı yoksa 1000 yorum alıp 4.2 puan alan ürün mü üst sırada olmalı?

Ürünlerde ki puan ağırlıklarının farklı olmasının sıralamaya etkisi var mı? Bir üründe ki 5 yıldız sayısı ile 1 yıldız alma sayısının sıralamaya etkisi olmalı mı?


Web sitelerinde ürünleri puan/yorum sayısına göre sıralamak önemlidir. <a target="_blank" href="https://bootcamp.veribilimiokulu.com/egitim/veri-bilimci-yetistirme-programi/">Veribilimi Okulu</a> kapsamında öğrendiğim sıralama yöntemlerinden bayes yöntemini kullanarak ürünleri sıralamayı öğreneceğiz ve örnekle de beraber tecrübe edeceğiz.

Not: Herhangi bir sorun yaşamamak amacıyla scrape kodlarını paylaşmayacağım. Sunucuda çalıştırdığım için sitede ki ilk sayfanın ilk 20 ürünün bilgisini alıp sıralama yapacaktır.

# Not
Program çalışırken gidilen sayfada ki bilgileri scrape edip sıralama yapacağı için çiçeksepetinde ki sayfanın puana göre sıralanmış olması gerekiyor ve link sonunda sayfa numarası yazmamalıdır.

Örnek sayfa linki: https://www.ciceksepeti.com/kozmetik-varvar?orderby=7&page=

## Çıktıların Anlamı
<strong>This text is important!</strong>

<strong>Site ranking:</strong> Ürünün çiçeksepetinde ki sırası

<strong>Product Rating:</strong> Ürün puanı

<strong>Bayesian Rating Score:</strong> Ürünün bayes skoru

<strong>Weighted Rating Score:</strong> Ürünün weighted skoru

<strong>Comment number:</strong> Ürünün toplam yorum sayısı

