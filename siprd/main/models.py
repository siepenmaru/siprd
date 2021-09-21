from django.db import models

# Create your models here.

class User(models.Model):

    POSITION_CHOICES = (
        ('Asisten Ahli', 'Asisten_Ahli'),
        ('Lektor', 'Lektor'),
        ('Lektor Kepala', 'Lektor_Kepala'),
        ('Guru Besar/Professor', 'Guru_Besar_Professor')
    )

    ROLE_CHOICES = (
        ('Dosen', 'Dosen'),
        ('Reviewer', 'Reviewer'),
        ('SDM PT', 'SDM_PT'),
        ('Admin', 'Admin')
    )

    username = models.CharField(max_length=254, primary_key=True, unique=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=254)
    full_name = models.CharField(max_length=254)
    university = models.CharField(max_length=254, blank=True, null=True)
    NIP = models.IntegerField(blank=True, null=True)
    field_of_study = models.CharField(max_length=254)
    position = models.CharField(choices=POSITION_CHOICES)
    role = models.CharField(choices=ROLE_CHOICES)
    approved = models.BooleanField(default=False)

class KaryaIlmiah(models.Model):

    karil_id = models.AutoField(primary_key=True)
    pemilik = models.ForeignKey(User, on_delete=models.CASCADE)
    judul = models.CharField(max_length=None)
    journal_data = models.CharField(max_length=None)
    link_origin = models.CharField(max_length=None, blank=True, null=True)
    link_repo = models.CharField(max_length=None, blank=True, null=True)
    link_indexer = models.CharField(max_length=None, blank=True, null=True)
    link_simcheck = models.CharField(max_length=None, blank=True, null=True)
    link_correspondence = models.CharField(max_length=None, blank=True, null=True)
    indexer = models.CharField(max_length=None, blank=True, null=True)
    category = models.CharField(max_length=None)
    status = models.CharField(max_length=None)
    promotion = models.CharField(max_length=None)

class Review(models.Model):

    review_id = models.AutoField(primary_key=True)
    karil_id = models.ForeignKey(KaryaIlmiah, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    plagiarism_percentage = models.CharField(max_length=None)
    linearity = models.CharField(max_length=None)
    score_1 = models.IntegerField(max_length=3)
    score_2 = models.IntegerField(max_length=3)
    score_3 = models.IntegerField(max_length=3)
    score_4 = models.IntegerField(max_length=3)
    comment_1 = models.CharField(max_length=None)
    comment_2 = models.CharField(max_length=None)
    comment_3 = models.CharField(max_length=None)
    comment_4 = models.CharField(max_length=None)
    score_proposer = models.IntegerField(max_length=3)








