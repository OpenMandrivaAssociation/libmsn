Name:          libmsn
Summary:       Reusable, open-source and fully documented library for MSN
Version:       4.0
Release:       %mkrel 0.beta1.1
Url:           http://sourceforge.net/projects/libmsn
License:       GPLv2+
Group:         Development/C++
BuildRoot:     %{_tmppath}/%{name}-%{version}-build
Source0:       %name-%version-beta1.tar.bz2
Patch0:        libmsn-4.0-fix-lib-install.patch
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
%_kde_includedir/msn
%_kde_libdir/libmsn.so

#---------------------------------------------

%prep
%setup -q -n libmsn-4.0-beta1
%patch0 -p0
%build
%cmake_kde4
%make

%install
cd build
make DESTDIR=%buildroot install

%clean
rm -rf "%{buildroot}"
