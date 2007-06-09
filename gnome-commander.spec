Summary: A Gnome filemanager similar to the Norton Commander(TM) 
Name: gnome-commander
Version: 1.2.4
Release: %mkrel 1
URL: http://www.freesoftware.fsf.org/gcmd/
Source0: http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Source1: %{name}-48.png
Source2: %{name}-32.png
Source3: %{name}-16.png
License: GPL
Group: File tools
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: libgnomeui2-devel 
BuildRequires: gnome-vfs2-devel
BuildRequires: libxml2-devel
BuildRequires: libGConf2-devel
BuildRequires: libexif-devel
BuildRequires: python-devel
BuildRequires: libgsf-devel
BuildRequires: liblcms-devel
BuildRequires: libchm-devel
BuildRequires: libiptcdata-devel
BuildRequires: id3lib-devel
BuildRequires: perl-XML-Parser
BuildRequires: gnome-doc-utils libxslt-proc
BuildRequires: desktop-file-utils
#gw patched
BuildRequires: flex intltool gnome-common

%description

Gnome Commander is a filemanager that just like the classical Norton
commander (TM) lets you do everything with the keyboard. It can
perform all standard file operations and some extra features like ftp
support.

%prep
%setup -q

%build
%configure2_5x --disable-scrollkeeper
%make

%install
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{_localstatedir}/scrollkeeper

%makeinstall_std

%find_lang %name --with-gnome

rm -f %buildroot%_libdir/gnome-commander/*.a
rm -f %buildroot%_libdir/gnome-commander/plugins/*.a
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): \
command="%{_bindir}/gnome-commander" \
icon="%{name}.png" \
needs="X11" \
section="Applications/File tools" \
title="Gnome Commander" \
longtitle="Filemanager similar to the Norton Commander(TM)" xdg="true"
EOF
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-System-FileTools" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


install -d $RPM_BUILD_ROOT/%{_miconsdir}
install -d $RPM_BUILD_ROOT/%{_liconsdir}
install -d $RPM_BUILD_ROOT/%{_iconsdir}
cp %{SOURCE1} $RPM_BUILD_ROOT/%{_liconsdir}/%{name}.png
cp %{SOURCE2} $RPM_BUILD_ROOT/%{_iconsdir}/%{name}.png
cp %{SOURCE3} $RPM_BUILD_ROOT/%{_miconsdir}/%{name}.png

chmod 644 %buildroot%_libdir/%name/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_scrollkeeper
%{update_menus}

%postun
%clean_scrollkeeper
%{clean_menus}

%files -f %name.lang
%defattr(-,root,root)
%doc README TODO COPYING ChangeLog
%_bindir/gnome-commander
%_bindir/gcmd-block
%_libdir/gnome-commander/
%_datadir/pixmaps/*
%_datadir/applications/gnome-commander.desktop
%{_datadir}/gnome/help/gnome-commander/C/
%{_datadir}/man/man1/*
%{_datadir}/omf/gnome-commander/gnome-commander-C.omf
%{_menudir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png


