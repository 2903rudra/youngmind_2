from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    User_choice = [
        ('SPOC','College_SPOC'),
        ('STUDENT','College_Student'),
    ]
    role = models.CharField(max_length = 20,choices = User_choice)

class College(models.Model):
    AISHE_CODE = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    address = models.TextField()
    pincode = models.CharField(max_length=10)
    faculty_first_name = models.CharField(max_length=100)
    faculty_last_name = models.CharField(max_length=100)
    faculty_designation = models.CharField(max_length=100)
    faculty_email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    spoc_consent_letter = models.FileField(upload_to='consent_letters/')
    college_logo = models.ImageField(upload_to='college_logos/')

class CollegeStudent(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    team_leader_first_name = models.CharField(max_length=100)
    team_leader_last_name = models.CharField(max_length=100)
    college_name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    faculty_name = models.CharField(max_length=100)
    faculty_designation = models.CharField(max_length=100)
    faculty_mobile_number = models.CharField(max_length=15)
    faculty_email_id = models.EmailField()
    photo = models.ImageField(upload_to='student_photos/')
    document = models.FileField(upload_to='student_documents/')

class TeamMember(models.Model):
    FULL_TIME = 'FT'
    PART_TIME = 'PT'
    STREAM_CHOICES = [
        (FULL_TIME, 'Full Time'),
        (PART_TIME, 'Part Time'),
    ]

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=100, unique=True)
    member_count = models.IntegerField(default=1)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    stream = models.CharField(max_length=2, choices=STREAM_CHOICES)
    academic_year = models.IntegerField()
    photo = models.ImageField(upload_to='team_member_photos/')
    document = models.FileField(upload_to='team_member_documents/')
