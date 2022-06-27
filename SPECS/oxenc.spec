Name:           oxenc
Version:        1.0.3
Release:        1%{?dist}
Summary:        oxen-encoding header only library

License:        BSD
URL:            https://github.com/oxen-io/oxen-encoding
Source0:        %{name}-%{version}.src.tar.gz

%global sonamever %{version}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  git

#Patch1:

%description
Base 16/32/64 and Bittorrent Encoding/Decoding Header Only Library

%package
Summary: oxen-encoding

%description
This package contains the the header library file needed by to build oxen-mq.

%prep

%autosetup

%build

%undefine __cmake_in_source_build

%cmake -DCMAKE_BUILD_TYPE=Release

%cmake_build

%install

%cmake_install

%files

%license LICENSE
%doc README.md
#%{_libdir}/liboxenmq.so.%{version}



%changelog
* Mon Jun 27 2022 Techincal Tumbleweed <necro_nemesis@hotmail.com> -1.0.3~1
- Initial fork from dev
