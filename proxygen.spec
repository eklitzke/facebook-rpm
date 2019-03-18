Name:           proxygen
Version:        2019.03.18.00
Release:        1%{?dist}
Summary:        A collection of C++ HTTP libraries including an easy to use HTTP server.

License:        Apache2
URL:            https://github.com/facebook/proxygen
Source0:        https://github.com/facebook/proxygen/archive/v%{version}/proxygen-%{version}.tar.gz

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


%build
%configure --disable-static
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license add-license-file-here
%doc add-main-docs-here
%{_libdir}/*.so.*

%files devel
%doc add-devel-docs-here
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Mon Mar 18 2019 Evan Klitzke <evan@eklitzke.org>
-
