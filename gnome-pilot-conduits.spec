%define gnome_pilot 2.91.93
Summary:	Gnome-pilot conduits
Name:		gnome-pilot-conduits
Version:	2.91.93
Release:	1
License:	GPL+
Group:		Office
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2

BuildRoot:	%{_tmppath}/%{name}-%{version}-root
URL:		https://www.gnome.org/gnome-pilot/

Requires:	gnome-pilot >= %gnome_pilot
BuildRequires:  pkgconfig(gnome-pilot-3.0) >= %gnome_pilot
BuildRequires:  intltool

%description
gnome-pilot is a collection of programs and daemon for integrating
GNOME and Palm devices.

This is a collection of additional conduits for gnome-pilot, it
currently features:
 - MAL conduit
 - email conduit
 - expense conduit
 - memo file conduit
 - time conduit

%prep
%setup -q 

%build
%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %{name}

# remove unpackaged files 
rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-pilot/conduits/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/gnome-pilot/conduits/*.so*
%{_datadir}/gnome-pilot/conduits/*



%changelog
* Fri Aug 31 2012 Vladimir Testov <vladimir.testov@rosalab.ru> 2.91.93-1
- update to 2.91.93

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.32.1-2mdv2011.0
+ Revision: 664880
- mass rebuild

* Thu Oct 21 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.32.1-1mdv2011.0
+ Revision: 587091
- update build deps
- update to new version 2.32.1

* Wed Oct 13 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.32.0-1mdv2011.0
+ Revision: 585320
- new version
- bump gnome-pilot dep
- update file list

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.17-2mdv2010.1
+ Revision: 521488
- rebuilt for 2010.1

* Thu Jan 08 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.0.17-1mdv2009.1
+ Revision: 327026
- update to new version 2.0.17

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.0.16-2mdv2009.0
+ Revision: 221089
- rebuild

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - new version
    - update deps

* Mon Feb 11 2008 Frederic Crozat <fcrozat@mandriva.com> 2.0.15-4mdv2008.1
+ Revision: 165281
- Rebuild against latest pilot-link

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Sep 20 2007 Adam Williamson <awilliamson@mandriva.org> 2.0.15-2mdv2008.0
+ Revision: 91286
- rebuild for 2008
- minor cleanups


* Thu Dec 28 2006 Frederic Crozat <fcrozat@mandriva.com> 2.0.15-1mdv2007.0
+ Revision: 102267
- Release 2.0.15
- Import gnome-pilot-conduits

* Fri Sep 08 2006 Frederic Crozat <fcrozat@mandriva.com> 2.0.14-1mdv2007.0
- Release 2.0.14 final

* Thu Aug 31 2006 Frederic Crozat <fcrozat@mandriva.com> 2.0.14-0.pre5.1mdv2007.0
- Release 2.0.14pre5

* Tue Jun 20 2006 Frederic Crozat <fcrozat@mandriva.com> 2.0.13-5mdv2007.0
- Rebuild and upload correctly

* Mon Jun 19 2006 Stefan van der Eijk <stefan@eijk.nu.lurtspam> 2.0.13-4
- rebuild for png
- %%mkrel

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.0.13-3mdk
- Rebuild

* Sat Aug 13 2005 Frederic Crozat <fcrozat@mandriva.com> 2.0.13-2mdk 
- Patch0: fix conduits location for x86-64

* Fri Jun 17 2005 Götz Waschk <waschk@mandriva.org> 2.0.13-1mdk
- bump deps
- New release 2.0.13

* Fri Dec 10 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0.12-1mdk
- New release 2.0.12

* Sat Aug 28 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0.11-1mdk
- Release 2.0.11
- Drop patch 0 (shoudn't be needed anymore)

