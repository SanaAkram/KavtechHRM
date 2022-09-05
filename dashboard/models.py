from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from passlib.hash import pbkdf2_sha256


# Create your models here.
class UserType(models.Model):
    user = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.user


class Project(models.Model):
    # client = models.ForeignKey
    proj_name = models.CharField(max_length=50, null=True)
    domain = models.CharField(max_length=50, null=True)
    sub_domain = models.CharField(max_length=50, null=True)
    # tool_used = models.ForeignKey(max)-
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    comment = models.CharField(max_length=200, null=True)
    is_active = models.BooleanField(default=False, null=True)
    # proj_manager = models.ForeignKey
    scrum_master = models.ForeignKey('account.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.proj_name


class Sprint(models.Model):
    project_fk = models.ForeignKey('Project', on_delete=models.CASCADE)
    sprint_no = models.IntegerField(null=True)
    total_sprint = models.IntegerField(null=True)
    tasks_assigned = models.IntegerField(null=True)
    completed_tasks = models.IntegerField(null=True)
    pending_tasks = models.IntegerField(null=True)
    # tool_used = models.ForeignKey(max)
    QA_failed = models.IntegerField(null=True)
    story_points_completed = models.IntegerField(null=True)
    is_active = models.BooleanField(default=False, null=True)


class Clients(models.Model):
    project_fk = models.ForeignKey('Project', on_delete=models.CASCADE)
    client_name = models.CharField(max_length=20, null=True)
    company_name = models.CharField(max_length=20, null=True)
    company_website = models.CharField(max_length=20, null=True)
    company_bus_domain = models.CharField(max_length=20, null=True)
    company_address_line1 = models.CharField(max_length=20, null=True)
    company_address_line2 = models.CharField(max_length=20, null=True)
    company_city = models.CharField(max_length=20, null=True)
    company_country = models.CharField(max_length=20, null=True)
    company_person_1_name = models.CharField(max_length=20, null=True)
    company_person_1_email = models.CharField(max_length=20, null=True)
    company_person_1_role = models.CharField(max_length=20, null=True)
    company_person_1_im = models.CharField(max_length=20, null=True)
    company_person_2_name = models.CharField(max_length=20, null=True)
    company_person_2_email = models.CharField(max_length=20, null=True)
    company_person_2_role = models.CharField(max_length=20, null=True)
    company_person_2_im = models.CharField(max_length=20, null=True)
    company_person_3_name = models.CharField(max_length=20, null=True)
    company_person_3_email = models.CharField(max_length=20, null=True)
    company_person_3_role = models.CharField(max_length=20, null=True)
    company_person_3_im = models.CharField(max_length=20, null=True)
    referal_source = models.CharField(max_length=20, null=True)
    client_relation_start_date = models.CharField(max_length=20, null=True)
    client_relation_start_comment = models.CharField(max_length=20, null=True)
    comment = models.CharField(max_length=20, null=True)
    contact_person_1_phone = models.CharField(max_length=20, null=True)
    contact_person_2_phone = models.CharField(max_length=20, null=True)
    contact_person_3_phone = models.CharField(max_length=20, null=True)
    billing_currency = models.CharField(max_length=20, null=True)
    is_active = models.BooleanField(default=False, null=True)
    scrum_master_fk = models.ForeignKey('account.User', on_delete=models.CASCADE)


class ResourceProject(models.Model):
    project_fk = models.ForeignKey('Project', on_delete=models.CASCADE)
    resource_fk = models.ForeignKey('account.User', on_delete=models.CASCADE)
