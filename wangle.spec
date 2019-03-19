Name:           wangle
Version:        2019.03.18.00
Release:        1%{?dist}
Summary:        Wangle is a framework providing a set of common client/server abstractions for building services in a consistent, modular, and composable way.

License:        Apache2
URL:            https://github.com/facebook/wangle
Source0:        https://github.com/facebook/wangle/archive/v%{version}/wangle-v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  fizz-devel = %{version}
BuildRequires:  folly-devel = %{version}
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  openssl-devel
BuildRequires:  binutils-devel
BuildRequires:  boost-devel
BuildRequires:  bzip2-devel
BuildRequires:  double-conversion-devel
BuildRequires:  gflags-devel >= 2.2.0
BuildRequires:  glog-devel
BuildRequires:  gtest-devel
BuildRequires:  jemalloc-devel
BuildRequires:  libaio-devel
BuildRequires:  libdwarf-devel
BuildRequires:  libevent-devel
BuildRequires:  libsodium-devel
BuildRequires:  libunwind-devel
BuildRequires:  libzstd-devel
BuildRequires:  lz4-devel
BuildRequires:  openssl-devel
BuildRequires:  snappy-devel
BuildRequires:  xz-devel
BuildRequires:  cmake

Requires:       fizz
Requires:       folly

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

# XXX: this is broken
#%check
#ctest -V %{?_smp_mflags}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc README.md
%license LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/wangle/

%changelog
* Mon Mar 18 2019 Evan Klitzke <evan@eklitzke.org> - 2019.03.18.00-1
- new version

* Mon Mar 18 2019 Evan Klitzke <evan@eklitzke.org>
- Initial package
