# Management Commands

These are the available management commands available to this application, a description, and how to use them.
These descriptions also live in the management command Python file as well.

Generally if there is an `x` in the usage description, `x` means the number of times the script will loop.

## licenses

All management commands associated with the licenses Django application.

### create_software_license_pairs

Creates a Software entry with a
randomly generated license key. By using this script
you will generate a software title and license key pair.
All pairs created with this script will show in the web
apps front-end and in the admin console.

The random word is generated from the system's
dictionary, assuming you're using a unix based system.

**Usage:** `python manage.py create_software_title x`

### create_software_title

Creates a Software entry **without**
a license key. Since there is not an associated license
key the software titles generated with this script
will not appear in the web apps front-end but will show
under Software in the admin console.

If you need generate a Software and License pair
refer to create_software_license_pairs.py in the
same directory as this script.

**Usage:** `python manage.py create_software_title x`

### create_users

This was a simple management command to get familiar
with Django management commands again, it's be a while.

Only creates standard users, does not create superusers.

**Usage:** `python manage.py create_users x`
