Summary: A Gnome filemanager similar to the Norton Commander(TM) 
Name: gnome-commander
Version: 1.2.8.7
Release: %mkrel 1
URL: http://www.freesoftware.fsf.org/gcmd/
Source0: http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0: gnome-commander-1.2.8.5-fix-str-fmt.patch
License: GPLv2+
Group: File tools
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: libgnomeui2-devel 
BuildRequires: gnome-vfs2-devel
BuildRequires: libxml2-devel
BuildRequires: libGConf2-devel
BuildRequires: libexiv-devel
BuildRequires: python-devel
BuildRequires: libgsf-devel
BuildRequires: lcms-devel
BuildRequires: libchm-devel
BuildRequires: libpoppler-devel
BuildRequires: taglib-devel
BuildRequires: intltool
BuildRequires: gnome-doc-utils libxslt-proc
BuildRequires: desktop-file-utils
#gw patched
BuildRequires: flex gnome-common

%description
Gnome Commander is a filemanager that just like the classical Norton
commander (TM) lets you do everything with the keyboard. It can
perform all standard file operations and some extra features like ftp
support.

%prep
%setup -q
%apply_patches

%build
%define _disable_ld_as_needed 1
%define _disable_ld_no_undefined 1
%configure2_5x --disable-scrollkeeper
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%find_lang %name --with-gnome
for omf in %buildroot%_datadir/omf/*/*[_-]??.omf;do 
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name.lang
done


rm -f %buildroot%_libdir/gnome-commander/*.a
rm -f %buildroot%_libdir/gnome-commander/plugins/*.a
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-System-FileTools" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


chmod 644 %buildroot%_libdir/%name/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_scrollkeeper
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%clean_scrollkeeper
%{clean_menus}
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc README TODO COPYING ChangeLog
%_bindir/gnome-commander
%_bindir/gcmd-block
%_libdir/gnome-commander/
%_datadir/pixmaps/*
%_datadir/applications/gnome-commander.desktop
%{_mandir}/man1/*
%{_datadir}/omf/gnome-commander/gnome-commander-C.omf
