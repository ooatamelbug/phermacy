from django.db import models

# Create your models here.
class Classes(models.Model):
    id= models.UUIDField(primary_key=True)
    class_name= models.CharField(max_length=20)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.class_name


class Drug(models.Model):
    id= models.UUIDField(primary_key=True)
    en_brand_name= models.CharField(max_length=25)
    ar_brand_name= models.CharField(max_length=25)
    chemical_name= models.CharField(max_length=25)
    national_code= models.CharField(max_length=25)
    manufacture= models.CharField(max_length=25)
    drug_dose= models.CharField(max_length=25)
    drug_usage= models.CharField(max_length=25)
    main_uom= models.CharField(max_length=25)
    small_uom= models.CharField(max_length=25)
    drug_status= models.BooleanField(default=True)
    class_id= models.ForeignKey(Classes, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.class_name
