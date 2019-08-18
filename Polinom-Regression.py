import numpy as np #Numpy bir matematik kütüphanesi
import pandas as pd #Pandas düzgün veri çekebilmek için kullanılan kütüphane
import matplotlib.pyplot as plt #Matplotlib ise çizim yapabilmemiz için
from sklearn.preprocessing import PolynomialFeatures as pf
from sklearn import linear_model

data = pd.read_csv("linear.csv") #Veriyi alıyoruz.

x = data["metrekare"] #Metre kare sütununu x listesine alalım
y = data["fiyat"] #Aynı şeyi fiyat sütunu için yapalım.

x = np.array(x) #Listemizi bir diziye(matrise) dönüştürmüş oluyoruz.
y = np.array(y) #Aynı şekilde burda da yapıyoruz.


#Numpy'nin polinom fit özelliği var. Onu kullancağız ve polinomu oturatacak dataya.
a,b,c = np.polyfit(x,y,2)
#x ekseni,y ekseni, 2.dereceden olduğunu belirtiyoruz.
#ax^2+bx+c şeklinde denklem oluşturuyoruz aslında.
#burdan parametre sayısını arttırarak daha yüksek dereceli denklermler elde edebiliriz.
#a,b,c,d = np.polyfit(x,y,3) gibi.

z = np.arange(150) #0-150 arasında bir çizim alanı alıyoruz.

# plt.scatter(x,y)#verileri çizdiriyoruz
# plt.plot(z,a*z*z+b*z+c) #polinomu çizdiriyoruz


#nokta nokta gösterim için scatter, çizgi istiyorsak plot.




g = int(input("Kaç metrekare ? : "))
istenilen = a*g*g+b*g+c

plt.scatter(x,y)
plt.plot(z,a*z*z+b*z+c)

print(istenilen)
plt.scatter(g,istenilen,c="red",marker=">") #İstenilen noktayı belli ettik.
plt.show()




