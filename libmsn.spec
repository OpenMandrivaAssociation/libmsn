%define major	0.3
%define libname	%mklibname msn %{major}
%define devname	%mklibname msn -d

Summary:	Reusable, open-source and fully documented library for MSN
Name:		libmsn
Version:	4.2.1
Release:	13
License:	GPLv2+
Group:		Development/C++
Url:		http://sourceforge.net/projects/libmsn
Source0:	http://downloads.sourceforge.net/libmsn/%{name}-%{version}.tar.bz2
Patch0:		libmsn-4.2.1-unistd.patch
BuildRequires:	cmake
BuildRequires:	pkgconfig(openssl)

%description
Libmsn is a reusable, open-source, fully documented library for 
connecting to Microsoft's MSN Messenger service.

%package test
Summary:	Connection test utility
Group:		Development/C++

%description test
Connection test utility.

%package -n %{libname}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libname}
%{name} library.

%package -n %{devname}
Summary:	Devel stuff for %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name} = %{version}-%{release}
Obsoletes:	libmsn-devel < 4.2.1-3

%description -n %{devname}
Files needed to build applications based on %{name}.

%prep
%setup -q
%apply_patches

%build
%cmake
%make

%install
%makeinstall_std -C build

%files test
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libmsn.so.%{major}*

%files -n %{devname}
%{_libdir}/pkgconfig/*
%{_includedir}/msn
%{_libdir}/libmsn.so

