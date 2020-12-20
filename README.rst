Networky
########

Runs speedtest-db periodically and saves the results in a SQL DB.

You can make it run periodically by using the systemd files in the
scripts folder.

This uses SQLAlchemy, so you can use any DB supported by
SQLAlchemy.

Installing
**********

The tutorial creates a postgres database called ``neteworky`` with
a user call ``networky`` with password ``1234``. You can change this
by setting an environment variable ``NETWORKY_DATABASE_URI``, following
`SQLAlchemy Database URI patterns <https://docs.sqlalchemy.org/en/13/core/engines.html#database-urls>`_.

1. Clone this project
2. Go to the ``src`` folder and run ``pip install .``.
3. Install postgres. In Ubuntu / debian this is ``sudo apt install postgresql``.
3. Run in your terminal: ``./scripts/create-db.sh`` to create the
   database and user. You want to execute this with a user with access
   to the database. In Ubuntu / Debian this would be like
   ``sudo -u postgres bash scripts/create-db.sh``
3. Run the command ``networky setup`` to create the database tables.
4. Run ``networky compute`` to perform the test and save it to the DB.

Executing periodically through systemd
======================================
If you have ``systemd`` in your system, you can execute networky
periodically.

Checkout the files in the scripts folder and modify them to your taste.
In a minimal configuration, you only have to correct the path in ``networky.service``
to the path where you cloned this repository, and then
execute ``install-system.sh``.

If you changed your database configuration, you can add the environment
variable in the file ``systemd.run.sh``, before executing ``networky compute``.
