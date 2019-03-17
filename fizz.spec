Name:           fizz
Version:        2019.03.04.00
Release:        1%{?dist}
Summary:        C++14 implementation of the TLS-1.3 standard

License:        Apache2
URL:            https://github.com/facebookincubator/fizz
Source0:        https://github.com/facebookincubator/fizz/archive/v%{version}/fizz-v%{version}.tar.gz

Patch1:         0001-gflags.patch

BuildRequires:  cmake
BuildRequires:  folly-devel = %{version}
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel

Requires:       folly = %{version}

%description


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch1 -p1

%build
%cmake -DFOLLY_CMAKE_DIR=/usr/lib64/cmake/folly\
       -DCMAKE_INSTALL_DIR=%{_libdir}/cmake/fizz\
       fizz/
%make_build


%install
%make_install


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license LICENSE
%doc README.md
%{_libdir}/*.so
%{_libdir}/*.so.*

%files devel
%doc README.md
%{_includedir}/*
%{_libdir}/cmake/fizz/


%changelog
* Sun Mar 17 2019 Evan Klitzke <evan@eklitzke.org>
- Initial build.
