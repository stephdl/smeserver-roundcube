%define name smeserver-roundcube
%define version 1.0
%define release 7

Summary: smserver rpm to setup roundcube, an IMAP mail client
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
Source: %{name}-%{version}.tar.gz
License: GNU GPL version 2
URL: http://www.contribs.org
Group: SMEserver/addon
BuildRoot: %{_tmppath}/%{name}-buildroot
Prefix: %{_prefix}
BuildArchitectures: noarch
BuildRequires: e-smith-devtools
Requires: e-smith-release >= 8.0
Requires: roundcube >= 1.0
Requires: git
AutoReqProv: no

%description
smserver rpm to setup the roundcube IMAP mail client.

%changelog
* Wed Apr 14 2014 stephane de labrusse <stephdl@de-labrusse.fr> 1.0-7
- removed the copymessage plugin activated

* Wed Apr 02 2014 stephane de labrusse <stephdl@de-labrusse.fr> 1.0-6
- corrected issue with the tasklists  db issue
- added auto-update for composer in the script rcplugin_update.sh 

* Sat Feb 15 2014 stephane de labrusse <stephdl@de-labrusse.fr> 1.0-5
- adapted to the upstream update eg roundcube 1.0

* Sun Nov 10 2013 JP Pialasse <tests@pialasse.com> 0.9-18.sme
- cleaning build section [SME: 7981]

* Wed Nov 6 2013 JP Pialasse <tests@pialasse.com> 0.9-17.sme
- corrected bug: typo in patch1 [SME: 7981]

* Thu Nov 5 2013 JP Pialasse <tests@pialasse.com> 0.9-16.sme
- corrected bug [SME: 7981]
- moved out spec file sql init and other event and actions

* Sat Oct 26 2013 stephane de labrusse <stephdl@de-labrusse.fr> 0.9.15
- Change the version of roundcubemail-plugins-kolab to 3.02 : http://git.kolab.org/roundcubemail-plugins-kolab/

* Sun Oct 20 2013 stephane de labrusse <stephdl@de-labrusse.fr> 0.9.14
- Change the original https_only

* Sat Oct 13 2013 stephane de labrusse <stephdl@de-labrusse.fr> 0.9.13
- Add the Kolab calendar plugin 		    : http://git.kolab.org/roundcubemail-plugins-kolab/tree/plugins/calendar
- Add the context menu for right click, very useful : http://www.tehinterweb.co.uk/roundcube/#picontextmenu
- Add the "Mark as Junk 2" to kick spam to junkmail : http://www.tehinterweb.co.uk/roundcube/#pimarkasjunk2

* Sat Oct 5 2013 stephane de Labrusse <stephdl@de-labrusse.fr> 0.9.12
- Add the SME Server internal LDAP addressbooks in roundcube

* Sat Sep 21 2013 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.9.11
- Add carddav functionnality http://www.crash-override.net/carddav.html

* Wed Jun 05 2013 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.9.9
- add a tmp folder in httpd.conf
* Mon Jun 03 2013 Stephane de Labrusse <stephdl@de-labrusse.fr>
- requires sme8 0.9-8

* Thu Jun 28 2007 Stephen Noble <stephen@dungog.net> 
- add domain property to use existing host or domain 0.9-7

* Thu Jun 21 2007 Stephen Noble <stephen@dungog.net> 
- update .spec file 0.9-6

* Thu Jun 21 2007 Stephen Noble <stephen@dungog.net> 
- automate config file creation
- proxypass to fix https redirect bug
- [0.9-5]

* Fri Apr 6 2007 Stephen Noble <stephen@dungog.net> 
- revert mysql password creation
- [0.9-4]

* Wed Feb 14 2007 Stephen Noble <stephen@dungog.net> 
- remove phpinfo
- simplify mysql password creation
- don't alias / in httpd for nul values in URL
- [0.9-3]

* Thu Dec 14 2006 Stephen Noble <support@dungog.net>
- php_admin_value eaccelerator enabled
- [0.9-2]

* Tue Dec 12 2006 Stephen Noble <support@dungog.net>
- initial release
- [0.9-1]

%prep
%setup
#%patch0 -p1


%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING"  >> %{name}-%{version}-filelist

%clean
cd ..
rm -rf %{name}-%{version}

%pre
%preun

%post

%postun
#uninstall
if [ $1 = 0 ] ; then
 /sbin/e-smith/expand-template /etc/httpd/conf/httpd.conf
 /usr/local/bin/svc -h /service/httpd-e-smith
fi

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%attr(755,root,root) /usr/bin/rcplugin_update.sh
