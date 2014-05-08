alo-hacklab
===========

RGB led која дига паника кога некој ќе и даде команда од ирц/твитер за да им обрати внимание на тие што се во Хаклаб а не се при компјутер


Инсталација
-----------

1. Треба https://github.com/mvitousek/pi-blaster да биде инсталирано и стартувано на RPI-то.
2. На машината каде што е веб сервисот треба да се инсталираат flask и requests:

   PYTHONUSERBASE=$PWD/py-env pip2 install --user -r requirements.txt


ps.

Uses a pi-blaster without the `daemon` function.
