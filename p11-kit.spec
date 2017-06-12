#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD605848ED7E69871 (ueno@gnu.org)
#
Name     : p11-kit
Version  : 0.23.7
Release  : 44
URL      : http://p11-glue.freedesktop.org/p11-kit.html
Source0  : https://github.com/p11-glue/p11-kit/releases/download/%{version}/p11-kit-%{version}.tar.gz
Source1  : p11-kit-trigger.service
Source2  : p11-kit.tmpfiles
Source99 : https://github.com/p11-glue/p11-kit/releases/download/%{version}/p11-kit-%{version}.tar.gz.sig
Summary  : Library and proxy module for properly loading and sharing PKCS#11 modules.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: p11-kit-bin
Requires: p11-kit-config
Requires: p11-kit-lib
Requires: p11-kit-doc
Requires: p11-kit-data
Requires: findutils
BuildRequires : ca-certs
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkgconfig(32libffi)
BuildRequires : pkgconfig(32libtasn1)
BuildRequires : pkgconfig(libffi)
BuildRequires : pkgconfig(libtasn1)
Patch1: 0001-Fix-test-case.patch
Patch2: 0002-steal-update-ca-trust-from-fedora.patch
Patch3: 0003-Add-shell-script-to-call-post-update.patch
Patch4: 0004-Added-P11_TRUST_PATHS-to-override-via-env.patch

%define trust_path /var/cache/ca-certs:/etc/ssl/certs:/usr/share/ca-certs

%description
P11-KIT
Provides a way to load and enumerate PKCS#11 modules. Provides a standard
configuration setup for installing PKCS#11 modules in such a way that they're
discoverable.

%package bin
Summary: bin components for the p11-kit package.
Group: Binaries
Requires: p11-kit-data
Requires: p11-kit-config

%description bin
bin components for the p11-kit package.


%package config
Summary: config components for the p11-kit package.
Group: Default

%description config
config components for the p11-kit package.


%package data
Summary: data components for the p11-kit package.
Group: Data

%description data
data components for the p11-kit package.


%package dev
Summary: dev components for the p11-kit package.
Group: Development
Requires: p11-kit-lib
Requires: p11-kit-bin
Requires: p11-kit-data
Provides: p11-kit-devel

%description dev
dev components for the p11-kit package.


%package dev32
Summary: dev32 components for the p11-kit package.
Group: Default
Requires: p11-kit-lib32
Requires: p11-kit-bin
Requires: p11-kit-data
Requires: p11-kit-dev

%description dev32
dev32 components for the p11-kit package.


%package doc
Summary: doc components for the p11-kit package.
Group: Documentation

%description doc
doc components for the p11-kit package.


%package lib
Summary: lib components for the p11-kit package.
Group: Libraries
Requires: p11-kit-data
Requires: p11-kit-config

%description lib
lib components for the p11-kit package.


%package lib32
Summary: lib32 components for the p11-kit package.
Group: Default
Requires: p11-kit-data
Requires: p11-kit-config

%description lib32
lib32 components for the p11-kit package.

%prep
%setup -q -n p11-kit-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
pushd ..
cp -a p11-kit-%{version} build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1492696678
%configure --disable-static --with-trust-paths=%{trust_path} --with-hash-impl=internal
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static --with-trust-paths=%{trust_path} --with-hash-impl=internal   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1492696678
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/p11-kit-trigger.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/tmpfiles.d/p11-kit.conf
## make_install_append content
rm %{buildroot}/%{_libexecdir}/p11-kit/trust-extract-compat
install -m 0755 %{_builddir}/p11-kit-%{version}/update-ca-trust  %{buildroot}/%{_bindir}/update-ca-trust
install -m 0755 %{_builddir}/p11-kit-%{version}/trust-certs %{buildroot}/%{_bindir}/trust-certs
ln -s %{_bindir}/update-ca-trust  %{buildroot}/%{_libexecdir}/p11-kit/trust-extract-compat
ln -s %{_libdir}/pkcs11/p11-kit-trust.so %{buildroot}/%{_libdir}/libnssckbi.so
## make_install_append end

%files
%defattr(-,root,root,-)
/usr/libexec/p11-kit/p11-kit-remote
/usr/libexec/p11-kit/p11-kit-server
/usr/libexec/p11-kit/trust-extract-compat

%files bin
%defattr(-,root,root,-)
/usr/bin/p11-kit
/usr/bin/trust
/usr/bin/trust-certs
/usr/bin/update-ca-trust

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/p11-kit-trigger.service
/usr/lib/tmpfiles.d/p11-kit.conf

%files data
%defattr(-,root,root,-)
/usr/share/p11-kit/modules/p11-kit-trust.module

%files dev
%defattr(-,root,root,-)
/usr/include/p11-kit-1/p11-kit/deprecated.h
/usr/include/p11-kit-1/p11-kit/iter.h
/usr/include/p11-kit-1/p11-kit/p11-kit.h
/usr/include/p11-kit-1/p11-kit/pin.h
/usr/include/p11-kit-1/p11-kit/pkcs11.h
/usr/include/p11-kit-1/p11-kit/pkcs11x.h
/usr/include/p11-kit-1/p11-kit/remote.h
/usr/include/p11-kit-1/p11-kit/uri.h
/usr/lib64/pkgconfig/p11-kit-1.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libp11-kit.so
/usr/lib32/p11-kit-proxy.so
/usr/lib32/pkgconfig/32p11-kit-1.pc
/usr/lib32/pkgconfig/p11-kit-1.pc

%files doc
%defattr(-,root,root,-)
/usr/share/gtk-doc/html/p11-kit/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libp11-kit.so.0
/usr/lib64/libp11-kit.so.0.3.0
/usr/lib64/pkcs11/p11-kit-trust.so
/usr/lib64/pkcs11/p11-kit-client.so
/usr/lib64/libnssckbi.so
/usr/lib64/libp11-kit.so
/usr/lib64/p11-kit-proxy.so

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libp11-kit.so.0
/usr/lib32/libp11-kit.so.0.3.0
/usr/lib32/pkcs11/p11-kit-trust.so
/usr/lib32/pkcs11/p11-kit-client.so
