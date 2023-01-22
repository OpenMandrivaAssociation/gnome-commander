%define _disable_ld_no_undefined 1

Summary:	A Gnome filemanager similar to the Norton Commander(TM) 
Name:		gnome-commander
Version:	1.16.0
Release:	1
License:	GPLv2+
Group:		File tools
Url:		http://www.freesoftware.fsf.org/gcmd/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	flex
BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	libxslt-proc
BuildRequires:	meson
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gnome-vfs-2.0)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	pkgconfig(libgsf-1)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(poppler)
BuildRequires:	pkgconfig(poppler-glib)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(smbclient)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(popt)
BuildRequires:	chmlib-devel
Requires:	gnome-vfs2

%description
Gnome Commander is a filemanager that just like the classical Norton
commander (TM) lets you do everything with the keyboard. It can
perform all standard file operations and some extra features like ftp
support.

%files -f %{name}.lang
%doc README TODO COPYING ChangeLog
%{_bindir}/gnome-commander
%{_bindir}/gcmd-block
%{_libdir}/gnome-commander/
%{_datadir}/pixmaps/*
%{_datadir}/applications/org.gnome.gnome-commander.desktop
%{_mandir}/man1/*
%{_datadir}/metainfo/org.gnome.gnome-commander.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-commander*
#{_datadir}/gnome-commander/mime/*

#----------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

rm -f %{buildroot}%{_libdir}/gnome-commander/*.a
rm -f %{buildroot}%{_libdir}/gnome-commander/plugins/*.a

desktop-file-install --vendor="" \
	--remove-category="Application" \
	--add-category="X-MandrivaLinux-System-FileTools" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

