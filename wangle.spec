Name:           wangle
Version:        2019.03.18.00
Release:        1%{?dist}
Summary:        Wangle is a framework providing a set of common client/server abstractions for building services in a consistent, modular, and composable way.

License:        Apache2
URL:            https://github.com/facebook/wangle
Source0:        https://github.com/facebook/wangle/archive/v%{version}/wangle-v%{version}.tar.gz

BuildRequires: cmake
BuildRequires: fizz-devel
BuildRequires: folly-devel
BuildRequires: gflags-devel >= 2.2.0

Requires:      fizz
Requires:      folly

%description


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup


%build
%cmake -DCMAKE_INSTALL_DIR=%{_libdir}/cmake/wangle\
       wangle
%make_build


%install
%make_install

%check
ctest -V %{?_smp_mflags}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license LICENSE
%doc README.md
%{_libdir}/*.so.*

%files devel
%doc README.md
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/wangle/

%changelog
* Mon Mar 18 2019 Evan Klitzke <evan@eklitzke.org> - 2019.03.18.00-1
- new version

* Mon Mar 18 2019 Evan Klitzke <evan@eklitzke.org>
- Initial package