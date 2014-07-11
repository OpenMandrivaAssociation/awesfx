Summary:	Utility programs for the AWE32 sound driver
Name: 		awesfx
Version:	0.5.1d
Release:	11
Group:		System/Kernel and hardware
License:	GPLv2
Url:		http://www.alsa-project.org/~iwai/awedrv.html#Utils
Source0:	ftp://ftp.suse.com/pub/people/tiwai/awesfx/%{name}-%{version}.tar.gz
Source2:	http://www.pvv.org/~thammer/localfiles/soundfonts_other/gu11-rom.zip
#ExclusiveArch:	%{ix86} alpha
BuildRequires:	unzip
BuildRequires:	pkgconfig(alsa)

%description
The awesfx package contains necessary utilities for the AWE32
sound driver.

If you must use an AWE32 sound driver, you should install
this package.

%package	devel
Group:		Development/C
Requires:	%{name} = %{version}
Summary:	Development files for awesfx

%description	devel
Development files needed for awesfx.

%prep
%setup -q
mkdir gu11-rom
cd gu11-rom
unzip %{SOURCE2}
cd ..

#install -m644 %{SOURCE3} -D include/linux/awe_voice.h

#perl -pi -e "s|getline|awesfx_getline|g" *.c

%build
%configure2_5x
%make

%install
mkdir -p %{buildroot}/{%_mandir,%_bindir,%{_libdir}}
mkdir -p %{buildroot}/%{_sysconfdir}/midi
mkdir -p %{buildroot}/bin
%makeinstall_std
mkdir -p %{buildroot}%{_includedir}/awe
for i in include/*.h ; do
install -m 644 $i %{buildroot}%{_includedir}/awe
done
mv %{buildroot}%{_bindir}/sfxload %{buildroot}/bin/
cp gu11-rom/GU11-ROM.SF2 %{buildroot}%{_sysconfdir}/midi
#rm -rf %{buildroot}{%{_libdir}/sfbank,%_datadir/sounds/sf2}
rm -rf %{buildroot}%{_libdir}/sfbank
install -m 644 awelib/libawe.a %{buildroot}%{_libdir}

%files
%doc gu11-rom
%config(noreplace) %{_sysconfdir}/midi/GU11-ROM.SF2
/bin/*
%{_bindir}/*
%{_mandir}/man1/*.1*
%_datadir/sounds/sf2

%files devel
%dir %{_includedir}/awe
%{_includedir}/awe/*
%{_libdir}/*.a

