Name:		libmsn
Summary:	Reusable, open-source and fully documented library for MSN
Version:	4.2.1
Release:	2
License:	GPLv2+
Group:		Development/C++
Url:		http://sourceforge.net/projects/libmsn
Source0:	http://downloads.sourceforge.net/libmsn/%name-%version.tar.bz2
Patch0:		libmsn-4.2.1-unistd.patch
BuildRequires:	cmake
BuildRequires:	pkgconfig(openssl)

%description
Libmsn is a reusable, open-source, fully documented library for 
connecting to Microsoft's MSN Messenger service.

#-----------------------------------------------------------------------------

%define msn_major 0.3
%define libmsn %mklibname msn %{msn_major}

%package -n %{libmsn}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libmsn}
%{name} library.

%files -n %{libmsn}
%{_libdir}/libmsn.so.%{msn_major}*

#-----------------------------------------------------------------------------

%package test
Summary:	Connection test utility
Group:		Development/C++

%description test
Connection test utility.

%files test
%{_bindir}/*

#-----------------------------------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/C++
Requires:	%{libmsn} = %{version}-%{release}

%description devel
Files needed to build applications based on %{name}.

%files devel
%{_libdir}/pkgconfig/*
%{_includedir}/msn
%{_libdir}/libmsn.so

#-----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%cmake
%make

%install
%makeinstall_std -C build

%changelog
* Sun Nov 27 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 4.2.1-1
+ Revision: 734247
- new version

* Wed Nov 09 2011 Juan Luis Baptiste <juancho@mandriva.org> 4.1-7
+ Revision: 729284
- Added patch to fix MSN connection problem with kopete that started some days ago.

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 4.1-6
+ Revision: 661500
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 4.1-5mdv2011.0
+ Revision: 602580
- rebuild

* Tue Apr 06 2010 Funda Wang <fwang@mandriva.org> 4.1-4mdv2010.1
+ Revision: 532084
- rebuild
- add fedora patch to build with libmsn
- rebuild for new openssl

* Fri Feb 26 2010 Oden Eriksson <oeriksson@mandriva.com> 4.1-2mdv2010.1
+ Revision: 511587
- rebuilt against openssl-0.9.8m

* Fri Feb 12 2010 Funda Wang <fwang@mandriva.org> 4.1-1mdv2010.1
+ Revision: 504707
- New version 4.1

* Fri Jan 08 2010 Frederik Himpe <fhimpe@mandriva.org> 4.0-2mdv2010.1
+ Revision: 487719
- Use correct major

* Thu Jan 07 2010 Frederik Himpe <fhimpe@mandriva.org> 4.0-1mdv2010.1
+ Revision: 487345
- Update to new version 4.0

* Sun Aug 30 2009 Helio Chissini de Castro <helio@mandriva.com> 4.0-0.beta8.2mdv2010.0
+ Revision: 422359
- We're not ready for experimental features on wlm

* Fri Aug 28 2009 Helio Chissini de Castro <helio@mandriva.com> 4.0-0.beta8.1mdv2010.0
+ Revision: 422017
- New upstream version

* Wed Jul 29 2009 Helio Chissini de Castro <helio@mandriva.com> 4.0-0.beta7.1mdv2010.0
+ Revision: 404342
- New upstream release beta 7

* Thu Jun 25 2009 Frederik Himpe <fhimpe@mandriva.org> 4.0-0.beta6.1mdv2010.0
+ Revision: 389204
- Update to new version 4.0 beta 6

* Sat Jan 24 2009 Funda Wang <fwang@mandriva.org> 4.0-0.beta4.1mdv2009.1
+ Revision: 333168
- 4.0 beta 4

* Fri Jan 23 2009 Helio Chissini de Castro <helio@mandriva.com> 4.0-0.beta3.1mdv2009.1
+ Revision: 333083
- Update with beta 3 plus current fixes from svn

* Tue Jan 13 2009 Helio Chissini de Castro <helio@mandriva.com> 4.0-0.beta2.2mdv2009.1
+ Revision: 329027
- Update with current svn until beta3 is launched, with latest msn login fix

* Tue Dec 30 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0-0.beta2.1mdv2009.1
+ Revision: 321315
- Update to current beta2

* Wed Dec 03 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0-0.beta1.3mdv2009.1
+ Revision: 309741
- Compilae revision 75 of libmsn svn
- Required for new kde4 kopete.
- Fix bko http://bugs.kde.org/show_bug.cgi?id=176703

* Sun Nov 16 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.0-0.beta1.1mdv2009.1
+ Revision: 303850
- Fix lib install
- New version 4.0 beta 1

  + Funda Wang <fwang@mandriva.org>
    - fix url

* Wed Oct 29 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3.2-1mdv2009.1
+ Revision: 298574
- import libmsn


