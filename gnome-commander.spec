%define _disable_ld_no_undefined 1

Summary:	A Gnome filemanager similar to the Norton Commander(TM) 
Name:		gnome-commander
Version:	2.0.3
Release:	1
License:	GPLv2+
Group:		File tools
Url:		https://www.freesoftware.fsf.org/gcmd/
Source0:	https://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
Source1:        vendor.tar.xz

BuildRequires:	appstream-util
BuildRequires:	desktop-file-utils
BuildRequires:	flex
BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxslt-proc
BuildRequires:	meson
BuildRequires:	rust-packaging
BuildRequires:	gtk-update-icon-cache
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.0.0
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(harfbuzz-gobject)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libgsf-1)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(poppler)
BuildRequires:	pkgconfig(poppler-glib)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(smbclient)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(unique-1.0)
BuildRequires:	pkgconfig(popt)
BuildRequires:	pkgconfig(vte-2.91-gtk4)
BuildRequires:	chmlib-devel

%description
Gnome Commander is a filemanager that just like the classical Norton
commander (TM) lets you do everything with the keyboard. It can
perform all standard file operations and some extra features like ftp
support.

%files -f %{name}.lang
%doc README* COPYING
%doc %{_datadir}/doc/libgcmd-1.0/
%{_bindir}/gnome-commander
%{_libdir}/gnome-commander/
%{_libdir}/libgcmd.so
%{_libdir}/girepository-1.0/GnomeCmd-1.0.typelib
%{_datadir}/pixmaps/*
%{_datadir}/applications/org.gnome.gnome-commander.desktop
%{_mandir}/man1/*
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-commander*
%{_datadir}/gir-1.0/GnomeCmd-1.0.gir
%{_datadir}/metainfo/org.gnome.gnome-commander.metainfo.xml
%{_datadir}/gnome-commander/icons
%{_iconsdir}/hicolor/scalable/apps/gnome-commander-symbolic.svg
%{_iconsdir}/hicolor/scalable/apps/gnome-commander.svg
%{_iconsdir}/hicolor/scalable/apps/gnome-commander-internal-viewer.svg

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -a1
%cargo_prep -v vendor

%build
%meson
%meson_build

%install
%meson_install

rm -f %buildroot%_libdir/libgcmd.a

%find_lang %{name} --with-gnome

rm -f %{buildroot}%{_libdir}/gnome-commander/*.a
rm -f %{buildroot}%{_libdir}/gnome-commander/plugins/*.a

desktop-file-install --vendor="" \
	--remove-category="Application" \
	--add-category="X-MandrivaLinux-System-FileTools" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

