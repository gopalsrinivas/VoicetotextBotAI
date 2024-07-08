from django.contrib import admin
from .models import DrDepartment, DoctorDetails


@admin.register(DrDepartment)
class DrDepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'is_active', 'created_at', 'updated_at')
    search_fields = ('department_name',)
    list_filter = ('is_active',)


@admin.register(DoctorDetails)
class DoctorDetailsAdmin(admin.ModelAdmin):
    list_display = ('doctor_id', 'first_name', 'last_name', 'department', 'is_active', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'doctor_id')
    list_filter = ('is_active', 'department')
    exclude = ('doctor_id',)

    def save_model(self, request, obj, form, change):
        if not obj.doctor_id:
            last_doctor = DoctorDetails.objects.all().order_by('id').last()
            if not last_doctor or not last_doctor.doctor_id:
                obj.doctor_id = 'Dr_0001'
            else:
                try:
                    last_doctor_id = last_doctor.doctor_id
                    last_doctor_num = int(last_doctor_id.split('_')[1])
                    new_doctor_num = last_doctor_num + 1
                    obj.doctor_id = f'Dr_{new_doctor_num:04d}'
                except (IndexError, ValueError) as e:
                    obj.doctor_id = 'Dr_0001'
        super().save_model(request, obj, form, change)
