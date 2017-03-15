# django-separate-users
separate staff and non staff users with two proxy models. nothing fancy, but as I ended up doing this again and again, this is a simple plug and forget solution, that I'll probably use in many projects from now on.

- staff users can be given the right to edit non staff users (currently not possible, or everyone can make everyone a superuser)
- fieldsets for staff and non staff users can be defined via settings
- less clutter
