%define gnome_pilot 2.32.0
Summary:	Gnome-pilot conduits
Name:		gnome-pilot-conduits
Version:	2.32.1
Release:	%mkrel 1
License:	GPL+
Group:		Office
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2

BuildRoot:	%{_tmppath}/%{name}-%{version}-root
URL:		http://www.gnome.org/gnome-pilot/

Requires:	gnome-pilot >= %gnome_pilot
BuildRequires:  gnome-pilot-devel >= %gnome_pilot
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

