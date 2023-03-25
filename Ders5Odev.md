# Pytest Decorators:

-		@pytest.mark.parametrize("x,y",[(1,2),(a,b)]
Fonksiyonda x ve y parametrelerine verilen değerlerin sırayla test edilmesini sağlar.


  -   	@pytest.mark.skip(reason=".....") 
  Bir altında bulunan fonksiyonun test edilmeden geçilmesini sağlar. İçerisine "reason=" kısmı girilmediği zaman da çalışır.
   
   
  -     @pytest.mark.skipif(conditions,reason=".....") 
  Belli bir koşul sağlandığında fonksiyonun geçilmesini sağlar. Kedni denediğim testlerde "reason=" kısmını yazmadığım durumlarda hata aldığım için bu kısmı eklemenin zorunlu olduğunu anladım.
  
  
  -     @pytest.mark.filterwarnings("error") 
   Testlerde ortaya çıkan belirli bir uyarı mesajını filtrelemek için kullanılır. Bu dekoratör, testlerin daha temiz bir çıktı üretmesine ve test raporlarının daha kolay okunmasına yardımcı olabilir.
  
  
  -     @pytest.mark.xfail()
  Testin sonucunun yanlış olduğunu bildiğimiz ve sonucu etkilememesini istediğimiz durumlarda kullanılır.
  
  
  -     @pytest.fixture()
  Anladığım kadarıyla testlerde kullanılacak parametreleri işaretlemek için kullanılır. Kullanmak için bir hazırlık fonksiyonu oluşturulur ve bu decorator ile işaretlendikten sonra testlerde çağrılma durumunda parametre olarak kullanılır.
  
  
  -     @pytest.mark.usefixtures()
  Fixture olarak belirlediğimiz denklemlerdeki sonuçları alır ve belirtilen fonsiyonda parametre olarak kullanır.
  
  
  ###  Örnekler:
  
  
  
  @pytest.mark.usefixtures() , @pytest.fixture() : Bu iki decorator karışık geldiği için bulduğum güzel örneklerle desteklemek istedim.
 ```py
 import pytest
 @pytest.fixture
def my_fixture():
    return "Hello, World!"

@pytest.fixture
def my_other_fixture():
    return 42

@pytest.mark.usefixtures("my_fixture", "my_other_fixture")
def test_mytest():
    assert my_fixture == "Hello, World!"
    assert my_other_fixture == 42
  ```
 
 
      
