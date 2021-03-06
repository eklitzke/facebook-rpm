Name:           fizz
Version:        2019.03.18.00
Release:        1%{?dist}
Summary:        C++14 implementation of the TLS-1.3 standard

License:        Apache2
URL:            https://github.com/facebookincubator/fizz
Source0:        https://github.com/facebookincubator/fizz/archive/v%{version}/fizz-v%{version}.tar.gz

BuildRequires:  cmake
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

Requires:       folly = %{version}

%description


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       folly-devel = %{version}
Requires:       openssl-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

%build
%cmake -DFOLLY_CMAKE_DIR=%{_libdir}/cmake/folly\
       -DCMAKE_INSTALL_DIR=%{_libdir}/cmake/fizz\
       fizz/
%make_build


%install
%make_install

%check
ctest -V %{?_smp_mflags}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc README.md
%license LICENSE
%{_libdir}/*.so
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/cmake/fizz/


%changelog
* Mon Mar 18 2019 Evan Klitzke <evan@eklitzke.org> - 2019.03.18.00-1
- new version

* Sun Mar 17 2019 Evan Klitzke <evan@eklitzke.org>
- Initial build.
