from django.contrib import admin
from account.models import User, UserProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserModelAdmin
    # that reference specific fields on auth.User.
    list_display = (
        'id', 'email', 'name', 'password', 'is_admin',
        # 'user_type',
        # 'first_name',
        # 'last_name',
        # 'father_name',
        # 'gender',
        # 'marital_status',
        # 'DOB',
        # 'NIC',
        # 'passport_no',
        # 'passport_expiry',
        # 'blood_group',
        # 'cnic_img',
        # 'emp_photo',
        # 'job_title',
        # 'dnt',
        # 'joinig_department',
        # 'leaving_date',
        # 'hiring_comments',
        # 'email',
        # 'kav_email',
        # 'current_salary',
        # 'is_active',
        # 'leaving_reason',
        # 'starting_salary',
        # 'emp_agreement_image',
        # 'offer_letter_img',
        # 'NDA_letter_img',
        # 'username',
        # 'password',
        # 'last_modified_date',
        # 'last_login',
        # 'is_virtual',
        # 'residence_city',
    )
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'phone_number')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password', 'phone_number'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email', 'id')
    filter_horizontal = ()


# Now register the new UserModelAdmin...
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user_fk', 'first_name', 'last_name', 'experience', 'b_degree', 'b_institute',
                  'm_degree', 'm_institute', 'phd_degree', 'phd_institute', 'birth_date', 'sched_test'
    )
admin.site.register(User, UserModelAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
