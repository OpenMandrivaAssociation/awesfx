Name: 		awesfx
Version:	0.5.1c
Release:	5
Summary:	Utility programs for the AWE32 sound driver
Group:		System/Kernel and hardware
URL:		http://www.alsa-project.org/~iwai/awedrv.html#Utils
Source0:	http://www.alsa-project.org/~iwai/%{name}-%{version}.tar.bz2
Source2:	http://www.pvv.org/~thammer/localfiles/soundfonts_other/gu11-rom.zip
Patch0:		awesfx-0.5.1c-getline.patch
License:	GPL
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
%patch0 -p0
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
mkdir -p %{buildroot}/{%_mandir,%_bindir,%_libdir}
mkdir -p %{buildroot}/%{_sysconfdir}/midi
mkdir -p %{buildroot}/bin
%{makeinstall_std}
mkdir -p %{buildroot}%{_includedir}/awe
for i in include/*.h ; do
install -m 644 $i %{buildroot}%{_includedir}/awe
done
mv %{buildroot}%{_bindir}/sfxload %{buildroot}/bin/
cp gu11-rom/GU11-ROM.SF2 %{buildroot}%{_sysconfdir}/midi
#rm -rf %{buildroot}{%_libdir/sfbank,%_datadir/sounds/sf2}
rm -rf %{buildroot}%_libdir/sfbank
install -m 644 awelib/libawe.a %{buildroot}%_libdir

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



%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5.1c-4mdv2011.0
+ Revision: 662902
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.1c-3mdv2011.0
+ Revision: 603486
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.1c-2mdv2010.1
+ Revision: 522114
- rebuilt for 2010.1

* Mon Aug 10 2009 Funda Wang <fwang@mandriva.org> 0.5.1c-1mdv2010.0
+ Revision: 414152
- new version 0.5.1c

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.5.0d-9mdv2010.0
+ Revision: 413547
- fix build
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.5.0d-8mdv2009.1
+ Revision: 350139
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.5.0d-7mdv2009.0
+ Revision: 220476
- rebuild

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.5.0d-6mdv2008.1
+ Revision: 148904
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Jul 20 2007 Stéphane Téletchéa <steletch@mandriva.org> 0.5.0d-5mdv2008.0
+ Revision: 53847
- Remove the exclusive arch

* Thu Jun 07 2007 Anssi Hannula <anssi@mandriva.org> 0.5.0d-4mdv2008.0
+ Revision: 36129
- rebuild with correct optflags


* Mon Aug 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/14/06 09:21:36 (55890)
- mkrelisation

* Mon Aug 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/14/06 09:17:12 (55885)
Import awesfx

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.5.0d-2mdk
- Rebuild

* Wed Dec 22 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.5.0d-1mdk
- 0.5.0d
- update url
- fix summary-ended-with-dot
- cosmetics

* Wed Jan 28 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.5.0-1mdk
- new release
- kill patch 0 (now it's automake/autoconf aware)
- do not package samples as doc, let build system place it where needed

