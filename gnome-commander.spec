%define _disable_ld_no_undefined 1

Summary:	A Gnome filemanager similar to the Norton Commander(TM) 
Name:		gnome-commander
Version:	1.18.2
Release:	1
License:	GPLv2+
Group:		File tools
Url:		https://www.freesoftware.fsf.org/gcmd/
Source0:	https://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	appstream-util
BuildRequires:	desktop-file-utils
BuildRequires:	flex
BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxslt-proc
BuildRequires:	meson
BuildRequires:	gtk-update-icon-cache
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gnome-vfs-2.0)
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
BuildRequires:	chmlib-devel
Requires:	gnome-vfs2

%description
Gnome Commander is a filemanager that just like the classical Norton
commander (TM) lets you do everything with the keyboard. It can
perform all standard file operations and some extra features like ftp
support.

%files -f %{name}.lang
%doc README* TODO COPYING
%{_bindir}/gnome-commander
%{_bindir}/gcmd-block
%{_libdir}/gnome-commander/
%{_datadir}/pixmaps/*
%{_datadir}/applications/org.gnome.gnome-commander.desktop
%{_mandir}/man1/*
%{_datadir}/metainfo/org.gnome.gnome-commander.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-commander*
#{_datadir}/gnome-commander/mime/*
%{_iconsdir}/hicolor/scalable/apps/gnome-commander-symbolic.svg
%{_iconsdir}/hicolor/scalable/apps/gnome-commander.svg
%{_iconsdir}/hicolor/scalable/apps/gnome-commander-internal-viewer.svg
%{_datadir}/gnome-commander/icons

%exclude %_datadir/%name/internal_viewer_hacking.txt
%exclude %_datadir/%name/keys.txt

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%meson -Dtests=disabled
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

