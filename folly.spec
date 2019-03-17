Name:           folly
Version:        2019.03.04.00
Release:        1%{?dist}
Summary:        An open-source C++ library developed and used at Facebook.

License:        Apache2
URL:            https://github.com/facebook/folly
Source0:        https://github.com/facebook/folly/archive/v%{version}/folly-v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  double-conversion-devel
BuildRequires:  gcc-c++
BuildRequires:  gflags-devel
BuildRequires:  glog-devel
BuildRequires:  gtest-devel
BuildRequires:  jemalloc-devel
BuildRequires:  libaio-devel
BuildRequires:  libdwarf-devel
BuildRequires:  libsodium-devel
BuildRequires:  libunwind-devel
BuildRequires:  openssl-devel
BuildRequires:  snappy-devel
BuildRequires:  xz-devel

Requires:       double-conversion
Requires:       gflags
Requires:       glog
Requires:       jemalloc
Requires:       libaio
Requires:       libdwarf
Requires:       libsodium
Requires:       libunwind
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
%cmake -D CMAKE_LIBRARY_ARCHITECTURE=x86-64 .
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
%{_libdir}/*.so
%{_libdir}/pkgconfig/libfolly.pc

# FIXME: hardcoded libdir
%{_prefix}/lib/cmake/folly/

%files devel
%doc README.md
%{_includedir}/*


%changelog
* Sun Mar 17 2019 Evan Klitzke <evan@eklitzke.org>
- Initial package
