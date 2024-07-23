from django_filters import rest_framework as filters


class UserFilter(filters.FilterSet):
    roles_starts_with = filters.CharFilter('roles', 'istartswith')
    email_starts_with = filters.CharFilter('email', 'istartswith')
    name_starts_with = filters.CharFilter('profile', 'name__istartswith')
    surname_starts_with = filters.CharFilter('profile', 'surname__istartswith')
    company_name_starts_with = filters.CharFilter('profile', 'company_name__istartswith')
    position_starts_with = filters.CharFilter('profile', 'position__istartswith')
    phone_number_starts_with = filters.CharFilter('profile', 'phone_number__starts_with')

    roles_contains = filters.CharFilter('roles', 'icontains')
    email_contains = filters.CharFilter('email', 'icontains')
    name_contains = filters.CharFilter('profile', 'name__icontains')
    surname_contains = filters.CharFilter('profile', 'surname__icontains')
    company_name_contains = filters.CharFilter('profile', 'company_name__icontains')
    position_contains = filters.CharFilter('profile', 'position__icontains')
    phone_number_contains = filters.CharFilter('profile', 'phone_number__contains')

    order = filters.OrderingFilter(
        fields=(
            'id',
            'email',
            'roles',
            ('profile__name', 'name'),
            ('profile__surname', 'surname'),
            ('profile__company_name', 'company_name'),
            ('profile__position', 'position'),
            ('profile__phone_number', 'phone_number')
        )
    )
