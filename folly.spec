Name:           folly
Version:        2019.03.18.00
Release:        1%{?dist}
Summary:        An open-source C++ library developed and used at Facebook.

License:        Apache2
URL:            https://github.com/facebook/folly
Source0:        https://github.com/facebook/folly/archive/v%{version}/folly-v%{version}.tar.gz

BuildRequires:  binutils-devel
BuildRequires:  boost-devel
BuildRequires:  bzip2-devel
BuildRequires:  cmake
BuildRequires:  double-conversion-devel
BuildRequires:  gcc-c++
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

Requires:       boost
Requires:       bzip2-libs
Requires:       double-conversion
Requires:       gflags
Requires:       glog
Requires:       jemalloc
Requires:       libaio
Requires:       libdwarf
Requires:       libevent
Requires:       libsodium
Requires:       libunwind
Requires:       libzstd
Requires:       lz4-libs
Requires:       openssl-libs
Requires:       snappy
Requires:       xz-libs

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
# FIXME: fix hard-coded arch
export CXXFLAGS="$CXXFLAGS -fPIC"
%cmake -DCMAKE_LIBRARY_ARCHITECTURE=x86-64\
       -DCMAKE_INSTALL_DIR=%{_libdir}/cmake/folly\
       -DFOLLY_CMAKE_DIR=%{_libdir}/cmake/folly\
       .
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

%files devel
%{_includedir}/*
%{_libdir}/cmake/folly/
%{_libdir}/pkgconfig/libfolly.pc


%changelog
* Mon Mar 18 2019 Evan Klitzke <evan@eklitzke.org> - 2019.03.18.00-1
- new version

* Sun Mar 17 2019 Evan Klitzke <evan@eklitzke.org>
- Initial package
