Name: libmsn
Summary: Reusable, open-source and fully documented library for MSN
Version: 4.0
Release: %mkrel 0.beta2.2
Url: http://sourceforge.net/projects/libmsn
License: GPLv2+
Group: Development/C++
BuildRoot: %{_tmppath}/%{name}-%{version}-build
Source0: %name-%version-beta2.tar.bz2
Patch0: libmsn-svn-before-beta3.patch
BuildRequires: cmake
BuildRequires: curl-devel
BuildRequires: pkgconfig

%description
Libmsn is a reusable, open-source, fully documented library for 
connecting to Microsoft's MSN Messenger service. 

#-----------------------------------------------------------------------------

%define msn_major 0
%define libmsn %mklibname msn %{msn_major}

%package -n %libmsn
Summary: %name library
Group: System/Libraries

%description -n %libmsn
%name library

%files -n %libmsn
%defattr(-,root,root)
%_libdir/libmsn.so.%{msn_major}*

#-----------------------------------------------------------------------------

%package test
Summary: Connection test utility
Group: Development/C++

%description test
Connection test utility.

%files test
%defattr(-,root,root)
%_bindir/*

#-----------------------------------------------------------------------------

%package devel
Summary: Devel stuff for %{name}
Group: Development/C++
Requires: %libmsn = %version

%description  devel
Files needed to build applications based on %{name}.

%files devel
%defattr(-,root,root)
%_libdir/pkgconfig/*
%_includedir/msn
%_libdir/libmsn.so

#-----------------------------------------------------------------------------

%prep
%setup -q -n libmsn-4.0-beta2
%patch0 -p1 -b .svn

%build
%cmake
%make

%install
%makeinstall_std -C build

%clean
rm -rf "%{buildroot}"
