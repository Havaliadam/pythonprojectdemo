import sqlite3

with sqlite3.connect("ayhancelik.db") as baglanti:

    imlec=baglanti.cursor()

#imlec.execute("CREATE TABLE IF NOT EXISTS ekip(isim TEXT,yas INT,cinsiyet TEXT)")
#imlec.execute("SELECT yas ,isim from ekip ")
#imlec.execute("Select*from ekip WHERE yas==22 AND cinsiyet=='Erkek'")

#for veri in imlec.fetchall():
 #print(veri)
#imlec.execute("INSERT INTO ekip Values('ayhan',21,'Erkek')")
#imlec.execute("INSERT INTO ekip Values('ela',18,'kadın')")
#imlec.execute("INSERT INTO ekip Values('mert',25,'Erkek')")
#imlec.execute("UPDATE ekip SET yas=25 WHERE isim = 'ela'")
imlec.execute("DELETE FROM ekip WHERE  isim='mert'")
baglanti.commit()


