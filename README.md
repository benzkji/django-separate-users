# django-separate-users

Separate staff and non staff users with two proxy models (FrontendUser and Editor).
Nothing fancy, but as I ended up doing this again and again, this is a simple plug and forget
solution, that I'll probably use in many projects from now on.

- minimal requirement are the `is_staff` and `is_superuser` fields on your user model
- staff users can be given the right to edit non staff users (currently not possible, or everyone can make everyone a superuser)
- fieldsets for staff and non staff users can be defined via settings (not yet)
- better admin list views (filters, is_active, etc)

[//]: # (NOTE / WARNING: With django<1.11, it's not possible to run this app with as custom
`settings.AUTH_USER_MODEL`. See https://stackoverflow.com/questions/46935758/djangos-get-user-model-only-in-1-11-during-import-time
t)

NOTE: Custom user models are not supported (yet).

## Usage

In your settings, add to `INSTALLED_APPS`

    INSTALLED_APPS = [
        ...
        'separate_users',
        ...
    ]

Also, you NEED to define a `MIGRATION_MODULES` entry for `separate_users` (yes, a migration is created for proxy models!). As your UserModel might
be different, we cannot guess the needed migrations, so you'll need to create them yourself.

    MIGRATION_MODULES = {
        'separate_users': 'your_apps.separate_users_migrations',
    }

You'll need to create this folder, with an `__init__.py` in it, then you can run
`./manage.py makemigrations` (try --dry-run to see if it works as you would expect).

As of a django bug, you'll want to run `./manage.py fix_proxy_permissions`, otherwise your non
superusers (but staff) might not be able to edit frontend and/or editor users.