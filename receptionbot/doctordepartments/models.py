from django.db import models

class DrDepartment(models.Model):
    department_name = models.CharField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "1. Dr Department"
        verbose_name_plural = "1. Dr Departments"

    def __str__(self):
        return self.department_name

class DoctorDetails(models.Model):
    doctor_id = models.CharField(max_length=100, unique=True, blank=True, editable=False)
    department = models.ForeignKey(DrDepartment, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    age = models.CharField(max_length=3)
    address = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "2. Doctor Details"
        verbose_name_plural = "2. Doctor Details"

    def __str__(self):
        return f"{self.department} - {self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self.doctor_id:
            last_doctor = DoctorDetails.objects.all().order_by('id').last()
            if not last_doctor:
                self.doctor_id = 'Dr_0001'
            else:
                doctor_id = last_doctor.doctor_id
                doctor_int = int(doctor_id.split('_')[1])
                new_doctor_int = doctor_int + 1
                self.doctor_id = f'Dr_{new_doctor_int:04d}'
        super().save(*args, **kwargs)
