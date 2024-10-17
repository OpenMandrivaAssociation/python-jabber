%define version 0.4
%define release 11
%define pkgname jabberpy%{version}-0

Summary: Python jabber protocol module 
Name: python-jabber
Version: %{version} 
Release: %{release}
Source0: %{pkgname}.tar.bz2
License: LGPL
URL: https://jabberpy.sf.net/
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: python-devel
BuildArch: noarch

%description
Python module for jabber protocol support.
You can write client or services with it.

%prep
%setup -q -n %{pkgname}

%build
CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog CREDITS README docs/ examples/ util/ 
%py_puresitedir/*
