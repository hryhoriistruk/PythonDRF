from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_kwargs):
        if not email:
            raise ValueError('email is unset')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_kwargs):
        extra_kwargs.setdefault('is_active', True)
        extra_kwargs.setdefault('is_staff', True)
        extra_kwargs.setdefault('is_superuser', True)

        if not extra_kwargs.get('is_staff'):
            raise ValueError('is_staff must be True')

        if not extra_kwargs.get('is_active'):
            raise ValueError('is_active must be True')

        if not extra_kwargs.get('is_superuser'):
            raise ValueError('is_superuser must be True')

        user = self.create_user(email, password, **extra_kwargs)
        return user

    def all_with_profiles(self):
        return self.select_related('profile')

    def all_with_roles_seller(self):
        return self.prefetch_related('sellers').all()

    def filter_by_roles(self, roles):
        return self.filter(roles=roles)
