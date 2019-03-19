Name:           proxygen
Version:        2019.03.18.00
Release:        1%{?dist}
Summary:        A collection of C++ HTTP libraries including an easy to use HTTP server.

License:        Apache2
URL:            https://github.com/facebook/proxygen
Source0:        https://github.com/facebook/proxygen/archive/v%{version}/proxygen-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  folly-devel  = %{version}
BuildRequires:  fizz-devel   = %{version}
BuildRequires:  wangle-devel = %{version}

Requires:  folly  = %{version}
Requires:  fizz   = %{version}
Requires:  wangle = %{version}


%description


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
cd proxygen
autoreconf -ivf


%build
%configure --disable-static
%make_build


%install
%make_install


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license LICENSE
%{_libdir}/*.so.*

%files devel
%doc README.md
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Mon Mar 18 2019 Evan Klitzke <evan@eklitzke.org>
-
