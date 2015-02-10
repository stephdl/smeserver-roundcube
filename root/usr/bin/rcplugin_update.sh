#!/bin/bash
/sbin/e-smith/db configuration setprop php AllowUrlFopen On
/sbin/e-smith/expand-template /etc/php.ini
/etc/init.d/httpd-e-smith restart >/dev/null 2>&1
pathroundcube=$(pwd)
cd /usr/share/roundcubemail
php /usr/share/roundcubemail/composer.phar self-update
php /usr/share/roundcubemail/composer.phar update
/sbin/e-smith/db configuration setprop php AllowUrlFopen off
/sbin/e-smith/expand-template /etc/php.ini
/etc/init.d/httpd-e-smith restart >/dev/null 2>&1
cd $pathroundcube

