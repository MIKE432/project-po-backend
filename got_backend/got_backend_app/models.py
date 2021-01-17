from django.db import models

# Create your models here.
class GrupaGorska(models.Model):
    kodgrupy = models.CharField(db_column='KodGrupy', max_length=4, primary_key=True)  # Field name made lowercase.
    nazwa = models.CharField(db_column='Nazwa', max_length=255)  # Field name made lowercase.
    idreg = models.ForeignKey('Region', db_column='IdReg', on_delete=models.DO_NOTHING)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GrupaGorska'


class Ksiazeczka(models.Model):
    idksiazki = models.AutoField(db_column='IdKsiazki', primary_key=True)  # Field name made lowercase.
    idturysty = models.ForeignKey('Osoba', models.DO_NOTHING, db_column='IdTurysty')  # Field name made lowercase.
    punktacja = models.IntegerField(db_column='Punktacja')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ksiazeczka'


class Legitymacja(models.Model):
    nrlegi = models.AutoField(db_column='NrLegi', primary_key=True)  # Field name made lowercase.
    idprzod = models.ForeignKey('Osoba', models.DO_NOTHING, db_column='IdPrzod')  # Field name made lowercase.
    terminwazn = models.DateField(db_column='TerminWazn')  # Field name made lowercase.
    dataprzyznania = models.DateField(db_column='DataPrzyznania')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Legitymacja'


class Odcinek(models.Model):
    idodc = models.AutoField(db_column='IdOdc', primary_key=True)  # Field name made lowercase.
    idpoczatek = models.ForeignKey('Punkt', models.DO_NOTHING, db_column='IdPoczatek')  # Field name made lowercase.
    idkoniec = models.ForeignKey('Punkt', models.DO_NOTHING, db_column='IdKoniec')  # Field name made lowercase.
    nazwa = models.CharField(db_column='Nazwa', max_length=255)  # Field name made lowercase.
    przewyzszenie = models.FloatField(db_column='Przewyzszenie')  # Field name made lowercase.
    dlugosc = models.FloatField(db_column='Dlugosc')  # Field name made lowercase.
    czyaktywny = models.BooleanField(db_column='CzyAktywny')  # Field name made lowercase.
    dataponotw = models.DateField(db_column='DataPonOtw', blank=True, null=True)  # Field name made lowercase.
    punktacja = models.IntegerField(db_column='Punktacja', blank=True, null=True)  # Field name made lowercase.
    rokakt = models.IntegerField(db_column='RokAkt', blank=True, null=True)  # Field name made lowercase.
    discriminator = models.CharField(db_column='Discriminator', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Odcinek'


class Odcinekweryfikowany(models.Model):
    idodcwer = models.AutoField(db_column='IdOdcWer', primary_key=True)  # Field name made lowercase.
    idodc = models.ForeignKey(Odcinek, models.DO_NOTHING, db_column='IdOdc')  # Field name made lowercase.
    datawer = models.DateField(db_column='DataWer', blank=True, null=True)  # Field name made lowercase.
    czyzwer = models.BooleanField(db_column='CzyZwer', blank=True, null=True)  # Field name made lowercase.
    nrporz = models.IntegerField(db_column='NrPorz')  # Field name made lowercase.
    idtrasy = models.ForeignKey('Trasa', models.DO_NOTHING, db_column='IdTrasy')  # Field name made lowercase.
    idprzod = models.ForeignKey('Osoba', models.DO_NOTHING, db_column='IdPrzod', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OdcinekWeryfikowany'


class Osoba(models.Model):
    idosoby = models.AutoField(db_column='IdOsoby', primary_key=True)  # Field name made lowercase.
    imie = models.CharField(db_column='Imie', max_length=40)  # Field name made lowercase.
    nazwisko = models.CharField(db_column='Nazwisko', max_length=40)  # Field name made lowercase.
    plec = models.CharField(db_column='Plec', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dataur = models.DateField(db_column='DataUr')  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=255)  # Field name made lowercase.
    haslo = models.CharField(db_column='Haslo', max_length=64)  # Field name made lowercase.
    czyakt = models.BooleanField(db_column='CzyAkt')  # Field name made lowercase.
    czyniepeln = models.BooleanField(db_column='CzyNiepeln')  # Field name made lowercase.
    miasto = models.CharField(db_column='Miasto', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ulica = models.CharField(db_column='Ulica', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nrdomu = models.IntegerField(db_column='NrDomu', blank=True, null=True)  # Field name made lowercase.
    nrmieszk = models.IntegerField(db_column='NrMieszk', blank=True, null=True)  # Field name made lowercase.
    kodpoczt = models.CharField(db_column='KodPoczt', max_length=6, blank=True, null=True)  # Field name made lowercase.
    nrtel = models.CharField(db_column='NrTel', max_length=12, blank=True, null=True)  # Field name made lowercase.
    discriminator = models.CharField(db_column='Discriminator', max_length=15)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Osoba'


class Punkt(models.Model):
    idpunktu = models.AutoField(db_column='IdPunktu', primary_key=True)  # Field name made lowercase.
    nazwa = models.CharField(db_column='Nazwa', max_length=255)  # Field name made lowercase.
    wysokosc = models.FloatField(db_column='Wysokosc')  # Field name made lowercase.
    szerokoscgeo = models.FloatField(db_column='SzerokoscGeo')  # Field name made lowercase.
    dlugoscgeo = models.FloatField(db_column='DlugoscGeo')  # Field name made lowercase.
    kodgrupy = models.ForeignKey(GrupaGorska, models.DO_NOTHING, db_column='KodGrupy')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Punkt'


class Region(models.Model):
    idreg = models.AutoField(db_column='IdReg', primary_key=True)  # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Region'


class Trasa(models.Model):
    idtrasy = models.AutoField(db_column='IdTrasy', primary_key=True)  # Field name made lowercase.
    nazwa = models.CharField(db_column='Nazwa', max_length=40)  # Field name made lowercase.
    sumapunkt = models.IntegerField(db_column='SumaPunkt')  # Field name made lowercase.
    datapocz = models.DateField(db_column='DataPocz')  # Field name made lowercase.
    datakonc = models.DateField(db_column='DataKonc')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Trasa'


class Trasaskladowa(models.Model):
    idwycieczki = models.ForeignKey('Wycieczka', models.DO_NOTHING, db_column='IdWycieczki')  # Field name made lowercase.
    idtrasy = models.ForeignKey(Trasa, models.DO_NOTHING, db_column='IdTrasy')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TrasaSkladowa'


class Uczestnictwo(models.Model):
    idturysty = models.ForeignKey(Osoba, models.DO_NOTHING, db_column='IdTurysty')  # Field name made lowercase.
    idwycieczki = models.ForeignKey('Wycieczka', models.DO_NOTHING, db_column='IdWycieczki')  # Field name made lowercase.
    opis = models.CharField(db_column='Opis', max_length=2000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Uczestnictwo'


class Uprawnienie(models.Model):
    nrlegitimacji = models.ForeignKey(Legitymacja, models.DO_NOTHING, db_column='NrLegitimacji')  # Field name made lowercase.
    kodgrupy = models.ForeignKey(GrupaGorska, models.DO_NOTHING, db_column='KodGrupy')  # Field name made lowercase.
    dataprzyznania = models.DateField(db_column='DataPrzyznania')  # Field name made lowercase.
    datawaznosci = models.DateField(db_column='DataWaznosci')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Uprawnienie'


class Wycieczka(models.Model):
    idwycieczki = models.AutoField(db_column='IdWycieczki', primary_key=True)  # Field name made lowercase.
    nazwa = models.CharField(db_column='Nazwa', max_length=40)  # Field name made lowercase.
    datapocz = models.DateField(db_column='DataPocz')  # Field name made lowercase.
    datakonc = models.DateField(db_column='DataKonc')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Wycieczka'
