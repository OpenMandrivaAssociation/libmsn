Name:          libmsn
Summary:       Reusable, open-source and fully documented library for MSN
Version:       3.2
Release:       %mkrel 1
Url:           http://indi.sourceforge.net/index.php/Main_Page
License:       GPLv2+
Group:         Development/C++
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
Source0:       %{name}-%{version}.tar.gz
Patch0:        libmsn-3.2-fix-build.patch
BuildRequires: kde4-macros
BuildRequires: curl-devel

%description
Libmsn is a reusable, open-source, fully documented library for 
connecting to Microsoft's MSN Messenger service. 

#---------------------------------------------

%define msn_major 0
%define libmsn %mklibname msn %{msn_major}

%package -n %libmsn
Summary: %name library
Group: System/Libraries

%description -n %libmsn
%name library

%files -n %libmsn
%defattr(-,root,root)
%_kde_libdir/libmsn.so.%{msn_major}*

#-----------------------------------------------------------------------------

%package devel
Summary: Devel stuff for %{name}
Group: Development/C++
Requires: %libmsn = %version
%description  devel
Files needed to build applications based on %{name}.

%files devel
%defattr(-,root,root)
%_kde_bindir/msntest
%_kde_includedir/msn
%exclude %_kde_libdir/libmsn.a
%exclude %_kde_libdir/libmsn.la
%_kde_libdir/libmsn.so

#---------------------------------------------

%prep
%setup -q 
%patch0 -p1

%build
%define _disable_ld_no_undefined 1
%configure2_5x
%make

%install
make DESTDIR=%buildroot install

%clean
rm -rf "%{buildroot}"
