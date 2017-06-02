#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x249B39D24F25E3B6 (dshaw@jabberwocky.com)
#
Name     : npth
Version  : 1.5
Release  : 8
URL      : ftp://ftp.gnupg.org/gcrypt/npth/npth-1.5.tar.bz2
Source0  : ftp://ftp.gnupg.org/gcrypt/npth/npth-1.5.tar.bz2
Source99 : ftp://ftp.gnupg.org/gcrypt/npth/npth-1.5.tar.bz2.sig
Summary  : NPTH - the new GNU Portable Threads Library
Group    : Development/Tools
License  : LGPL-2.1
Requires: npth-bin
Requires: npth-lib

%description
NPTH is a cooperative thread library.

%package bin
Summary: bin components for the npth package.
Group: Binaries

%description bin
bin components for the npth package.


%package dev
Summary: dev components for the npth package.
Group: Development
Requires: npth-lib
Requires: npth-bin
Provides: npth-devel

%description dev
dev components for the npth package.


%package lib
Summary: lib components for the npth package.
Group: Libraries

%description lib
lib components for the npth package.


%prep
%setup -q -n npth-1.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1496413035
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1496413035
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/npth-config

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libnpth.so
/usr/share/aclocal/*.m4

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnpth.so.0
/usr/lib64/libnpth.so.0.1.1
