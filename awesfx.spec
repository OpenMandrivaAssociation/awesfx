Name: 		awesfx
Version:	0.5.0d
Release:	%mkrel 5
Summary:	Utility programs for the AWE32 sound driver
Group:		System/Kernel and hardware
URL:		http://www.alsa-project.org/~iwai/awedrv.html#Utils
Source0:	http://www.alsa-project.org/~iwai/%{name}-%{version}.tar.bz2
Source2:	http://www.pvv.org/~thammer/localfiles/soundfonts_other/gu11-rom.zip
Source3:	awe_voice.h
License:	GPL
#ExclusiveArch:	%{ix86} alpha
BuildRequires:	unzip
BuildRequires:	alsa-lib-devel >= 1.0.2-2mdk

%description
The awesfx package contains necessary utilities for the AWE32
sound driver.

If you must use an AWE32 sound driver, you should install
this package.

%package	devel
Group:		Development/C
Requires:	%{name} = %{version}-%{release}
Summary:	Development files for awesfx

%description	devel
Development files needed for awesfx.

%prep
%setup -q
mkdir gu11-rom
cd gu11-rom
unzip %{SOURCE2}
cd ..

install -m644 %{SOURCE3} -D include/linux/awe_voice.h

%build
export PATH=$PATH:/usr/X11R6/bin
%configure2_5x
make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/{%_mandir,%_bindir,%_libdir}
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/midi
mkdir -p $RPM_BUILD_ROOT/bin
%{makeinstall_std}
mkdir -p $RPM_BUILD_ROOT%{_includedir}/awe
for i in include/*.h ; do
install -m 644 $i $RPM_BUILD_ROOT%{_includedir}/awe
done
mv $RPM_BUILD_ROOT%{_bindir}/sfxload $RPM_BUILD_ROOT/bin/
cp gu11-rom/GU11-ROM.SF2 $RPM_BUILD_ROOT%{_sysconfdir}/midi
#rm -rf $RPM_BUILD_ROOT{%_libdir/sfbank,%_datadir/sounds/sf2}
rm -rf $RPM_BUILD_ROOT%_libdir/sfbank
install -m 644 awelib/libawe.a $RPM_BUILD_ROOT%_libdir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc gu11-rom
%config(noreplace) %{_sysconfdir}/midi/GU11-ROM.SF2
/bin/*
%{_bindir}/*
%{_mandir}/man1/*.1*
%_datadir/sounds/sf2

%files devel
%defattr(-,root,root)
%dir %{_includedir}/awe
%{_includedir}/awe/*
%{_libdir}/*.a

