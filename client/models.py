# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Client(models.Model):
    idclient = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=30, blank=True, null=True)
    prenom = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=False)
    password = models.CharField(max_length=250, blank=True, null=True)
    profile = models.IntegerField( blank=True, null=False)
    contact = models.CharField(max_length=8, blank=True, null=True)

    def __str__(self):
        return self

    class Meta:
        managed = False
        db_table = 'client'


class Compte(models.Model):
    idcompte = models.AutoField(primary_key=True)
    client_idclient = models.PositiveIntegerField(db_column='Client_idclient')  # Field name made lowercase.
    solde = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self

    class Meta:
        managed = False
        db_table = 'compte'


class Equipe(models.Model):
    idequipe = models.AutoField(db_column='idEquipe', primary_key=True)  # Field name made lowercase.
    libelle = models.CharField(max_length=50, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    initiale = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.libelle

    class Meta:
        managed = False
        db_table = 'equipe'


class Pari(models.Model):
    idpari = models.AutoField(db_column='idPari', primary_key=True)  # Field name made lowercase.
    rencontre_idrencontre = models.PositiveIntegerField(db_column='Rencontre_idRencontre')  # Field name made lowercase.
    client_idclient = models.PositiveIntegerField(db_column='Client_idclient')  # Field name made lowercase.
    montant = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    gain = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self

    class Meta:
        managed = False
        db_table = 'pari'


class Rencontre(models.Model):
    idrencontre = models.AutoField(db_column='idRencontre', primary_key=True)  # Field name made lowercase.
    sport_idsport = models.PositiveIntegerField(db_column='Sport_idSport')  # Field name made lowercase.
    equipe1 = models.PositiveIntegerField(blank=True, null=True)
    cote1 = models.PositiveIntegerField(blank=True, null=True)
    equipe2 = models.PositiveIntegerField(blank=True, null=True)
    cote2 = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
            return self

    class Meta:
        managed = False
        db_table = 'rencontre'


class Resultat(models.Model):
    idresultat = models.AutoField(db_column='idResultat', primary_key=True)  # Field name made lowercase.
    rencontre_idrencontre = models.PositiveIntegerField(db_column='Rencontre_idRencontre')  # Field name made lowercase.
    equi1 = models.PositiveIntegerField(blank=True, null=True)
    equi2 = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
            return self

    class Meta:
        managed = False
        db_table = 'resultat'


class Scorepari(models.Model):
    idscorepari = models.AutoField(db_column='idScorePari', primary_key=True)  # Field name made lowercase.
    pari_idpari = models.PositiveIntegerField(db_column='Pari_idPari')  # Field name made lowercase.
    score1 = models.PositiveIntegerField(blank=True, null=True)
    score2 = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
            return self

    class Meta:
        managed = False
        db_table = 'scorepari'


class Sport(models.Model):
    idsport = models.AutoField(db_column='idSport', primary_key=True)  # Field name made lowercase.
    libelles = models.CharField(db_column='libelleS', max_length=250, blank=True, null=True)  # Field name made lowercase.
    icone = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
            return self.libelles

    class Meta:
        managed = False
        db_table = 'sport'
