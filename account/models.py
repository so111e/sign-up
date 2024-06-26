from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings

class Post(models.Model):
    title=models.CharField(max_length=60)
    text=models.TextField()

class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):

        if not username:
            raise ValueError('아이디:')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

#슈퍼유저 만드는거
    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    user_number = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15, unique=True, null=False, blank=False)
    email = models.EmailField(default='', max_length=100, null=False, blank=False, unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    #필수로 작성해야하는 필드 명시
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

#admin페이지에서 오류 잡는 용도입니다
    @property
    def is_staff(self):
        return self.is_admin
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    
    def __str__(self):
        return self.user.username
