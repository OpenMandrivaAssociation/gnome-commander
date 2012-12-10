Summary:	A Gnome filemanager similar to the Norton Commander(TM) 
Name:		gnome-commander
Version:	1.2.8.15
Release:	2
License:	GPLv2+
Group:		File tools
URL:		http://www.freesoftware.fsf.org/gcmd/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
Patch0:		gnome-commander-1.2.8.5-fix-str-fmt.patch
Patch1:		gnome-commander-1.2.8.15-gcc47.patch
Patch2:		gnome-commander-1.2.8.15-poppler020.patch
BuildRequires:	libchm-devel
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gnome-vfs-2.0)
BuildRequires:	pkgconfig(lcms)
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	pkgconfig(libgsf-1)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(poppler)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	libxslt-proc
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	flex
BuildRequires:	gnome-common

%description
Gnome Commander is a filemanager that just like the classical Norton
commander (TM) lets you do everything with the keyboard. It can
perform all standard file operations and some extra features like ftp
support.

%prep
%setup -q
%apply_patches

%build
autoreconf
%define _disable_ld_no_undefined 1
%configure2_5x --disable-scrollkeeper
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

rm -f %{buildroot}%{_libdir}/gnome-commander/*.a
rm -f %{buildroot}%{_libdir}/gnome-commander/plugins/*.a

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-System-FileTools" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*


%files -f %{name}.lang
%doc README TODO COPYING ChangeLog
%{_bindir}/gnome-commander
%{_bindir}/gcmd-block
%{_libdir}/gnome-commander/
%{_datadir}/pixmaps/*
%{_datadir}/applications/gnome-commander.desktop
%{_mandir}/man1/*

