#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : p11-kit
Version  : 0.23.22
Release  : 71
URL      : file:///insilications/build/clearlinux/packages/p11-kit/p11-kit-0.23.22.tar.gz
Source0  : file:///insilications/build/clearlinux/packages/p11-kit/p11-kit-0.23.22.tar.gz
Summary  : Library and proxy module for properly loading and sharing PKCS#11 modules.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: p11-kit-bin = %{version}-%{release}
Requires: p11-kit-data = %{version}-%{release}
Requires: p11-kit-lib = %{version}-%{release}
Requires: p11-kit-libexec = %{version}-%{release}
Requires: p11-kit-locales = %{version}-%{release}
Requires: p11-kit-services = %{version}-%{release}
Requires: ca-certs
Requires: ca-certs-static
BuildRequires : bash-completion-dev
BuildRequires : buildreq-meson
BuildRequires : ca-certs
BuildRequires : ca-certs-static
BuildRequires : ccache
BuildRequires : findutils
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gtk-doc
BuildRequires : intltool-dev
BuildRequires : libffi-dev
BuildRequires : libffi-dev32
BuildRequires : libffi-staticdev
BuildRequires : libffi-staticdev32
BuildRequires : libtasn1-dev
BuildRequires : libtasn1-dev32
BuildRequires : libtasn1-staticdev
BuildRequires : libtasn1-staticdev32
BuildRequires : libxslt-bin
BuildRequires : openssl
BuildRequires : openssl-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(32libffi)
BuildRequires : pkgconfig(32libsystemd)
BuildRequires : pkgconfig(32libtasn1)
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(libffi)
BuildRequires : pkgconfig(libssl)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libtasn1)
BuildRequires : pkgconfig(openssl)
BuildRequires : util-linux-bin
BuildRequires : util-linux-dev
BuildRequires : util-linux-extras
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
# Disable automatic requeriments processing
AutoReq: no
Patch1: 0001-Added-P11_TRUST_PATHS-to-override-via-env.patch
Patch2: 0002-Use-p11-trust-instead-of-trust.patch

%description
# p11-kit
[![Build Status](https://travis-ci.org/p11-glue/p11-kit.svg?branch=master)](https://travis-ci.org/p11-glue/p11-kit) [![Coverage Status](https://img.shields.io/coveralls/p11-glue/p11-kit.svg)](https://coveralls.io/r/p11-glue/p11-kit) [![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/1627/badge)](https://bestpractices.coreinfrastructure.org/en/projects/1627) [![Total alerts](https://img.shields.io/lgtm/alerts/g/p11-glue/p11-kit.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/p11-glue/p11-kit/alerts/) [![Language grade: C/C++](https://img.shields.io/lgtm/grade/cpp/g/p11-glue/p11-kit.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/p11-glue/p11-kit/context:cpp)

%package bin
Summary: bin components for the p11-kit package.
Group: Binaries
Requires: p11-kit-data = %{version}-%{release}
Requires: p11-kit-libexec = %{version}-%{release}
Requires: p11-kit-services = %{version}-%{release}
# Disable automatic requeriments processing
AutoReq: no

%description bin
bin components for the p11-kit package.


%package data
Summary: data components for the p11-kit package.
Group: Data
# Disable automatic requeriments processing
AutoReq: no

%description data
data components for the p11-kit package.


%package dev
Summary: dev components for the p11-kit package.
Group: Development
Requires: p11-kit-lib = %{version}-%{release}
Requires: p11-kit-bin = %{version}-%{release}
Requires: p11-kit-data = %{version}-%{release}
Provides: p11-kit-devel = %{version}-%{release}
Requires: p11-kit = %{version}-%{release}
# Disable automatic requeriments processing
AutoReq: no

%description dev
dev components for the p11-kit package.


%package dev32
Summary: dev32 components for the p11-kit package.
Group: Default
Requires: p11-kit-lib32 = %{version}-%{release}
Requires: p11-kit-bin = %{version}-%{release}
Requires: p11-kit-data = %{version}-%{release}
Requires: p11-kit-dev = %{version}-%{release}
# Disable automatic requeriments processing
AutoReq: no

%description dev32
dev32 components for the p11-kit package.


%package lib
Summary: lib components for the p11-kit package.
Group: Libraries
Requires: p11-kit-data = %{version}-%{release}
Requires: p11-kit-libexec = %{version}-%{release}
# Disable automatic requeriments processing
AutoReq: no

%description lib
lib components for the p11-kit package.


%package lib32
Summary: lib32 components for the p11-kit package.
Group: Default
Requires: p11-kit-data = %{version}-%{release}
# Disable automatic requeriments processing
AutoReq: no

%description lib32
lib32 components for the p11-kit package.


%package libexec
Summary: libexec components for the p11-kit package.
Group: Default
# Disable automatic requeriments processing
AutoReq: no

%description libexec
libexec components for the p11-kit package.


%package locales
Summary: locales components for the p11-kit package.
Group: Default
# Disable automatic requeriments processing
AutoReq: no

%description locales
locales components for the p11-kit package.


%package services
Summary: services components for the p11-kit package.
Group: Systemd services
# Disable automatic requeriments processing
AutoReq: no

%description services
services components for the p11-kit package.


%prep
%setup -q -n p11-kit
cd %{_builddir}/p11-kit
%patch1 -p1
%patch2 -p1
pushd ..
cp -a p11-kit build32
popd

%build
## build_prepend content
find . -type f -name '*.txt' -exec sed -i 's:libffi\.so\b:libffi.a:g' {} \;
find . -type f -name '*.ninja' -exec sed -i 's:libffi\.so\b:libffi.a:g' {} \;
find . -type f -name '*.json' -exec sed -i 's:libffi\.so\b:libffi.a:g' {} \;
find . -type f -name '*.txt' -exec sed -i 's:libtasn1\.so\b:libtasn1.a:g' {} \;
find . -type f -name '*.ninja' -exec sed -i 's:libtasn1\.so\b:libtasn1.a:g' {} \;
find . -type f -name '*.json' -exec sed -i 's:libtasn1\.so\b:libtasn1.a:g' {} \;
## build_prepend end
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610853065
export GCC_IGNORE_WERROR=1
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fuse-ld=bfd -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe  -fPIC -fdata-sections -ffunction-sections -flto=16 -fno-plt -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -Wl,-O2 -Wl,-z,now -Wl,-z,relro -ffat-lto-objects -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_GEN"
export FCFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fuse-ld=bfd -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe  -fPIC -fdata-sections -ffunction-sections -flto=16 -fno-plt -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -Wl,-O2 -Wl,-z,now -Wl,-z,relro -ffat-lto-objects -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_GEN"
export FFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fuse-ld=bfd -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe  -fPIC -fdata-sections -ffunction-sections -flto=16 -fno-plt -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -Wl,-O2 -Wl,-z,now -Wl,-z,relro -ffat-lto-objects -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_GEN"
export CXXFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fuse-ld=bfd -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe  -fPIC -fdata-sections -ffunction-sections -flto=16 -fno-plt -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -Wl,-O2 -Wl,-z,now -Wl,-z,relro -ffat-lto-objects -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_GEN"
export LDFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fno-semantic-interposition -fuse-ld=bfd -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe  -fPIC -fdata-sections -ffunction-sections -flto=16 -fno-plt -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -Wl,-O2 -Wl,-z,now -Wl,-z,relro -ffat-lto-objects -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_GEN"
#  -fipa-pta
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -malign-data=cacheline -feliminate-unused-debug-types -fno-lto -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -pipe  -fPIC -fdata-sections -ffunction-sections -flto=16 -fno-plt -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -Wl,-O2 -Wl,-z,now -Wl,-z,relro -ffat-lto-objects -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_USE"
export FCFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -malign-data=cacheline -feliminate-unused-debug-types -fno-lto -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -pipe  -fPIC -fdata-sections -ffunction-sections -flto=16 -fno-plt -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -Wl,-O2 -Wl,-z,now -Wl,-z,relro -ffat-lto-objects -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_USE"
export FFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -malign-data=cacheline -feliminate-unused-debug-types -fno-lto -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -pipe  -fPIC -fdata-sections -ffunction-sections -flto=16 -fno-plt -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -Wl,-O2 -Wl,-z,now -Wl,-z,relro -ffat-lto-objects -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_USE"
export CXXFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -malign-data=cacheline -feliminate-unused-debug-types -fno-lto -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -fvisibility-inlines-hidden -pipe  -fPIC -fdata-sections -ffunction-sections -flto=16 -fno-plt -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -Wl,-O2 -Wl,-z,now -Wl,-z,relro -ffat-lto-objects -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_USE"
export LDFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -malign-data=cacheline -feliminate-unused-debug-types -fno-lto -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -pipe  -fPIC -fdata-sections -ffunction-sections -flto=16 -fno-plt -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -Wl,-O2 -Wl,-z,now -Wl,-z,relro -ffat-lto-objects -fomit-frame-pointer -ffast-math -fstrict-aliasing -fexceptions $PGO_USE"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#
%global _lto_cflags 1
unset CCACHE_DISABLE
export PATH="/usr/lib64/ccache/bin:$PATH"
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
## altflags_pgo end
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddefault_library=both -Dgtk_doc=false -Dman=false -Dtrust_paths=/var/cache/ca-certs -Dhash_impl=internal -Dtest=true -Dlibffi=enabled  builddir
## make_prepend content
find . -type f -name '*.txt' -exec sed -i 's:libffi\.so\b:libffi.a:g' {} \;
find . -type f -name '*.ninja' -exec sed -i 's:libffi\.so\b:libffi.a:g' {} \;
find . -type f -name '*.json' -exec sed -i 's:libffi\.so\b:libffi.a:g' {} \;
find . -type f -name '*.txt' -exec sed -i 's:libtasn1\.so\b:libtasn1.a:g' {} \;
find . -type f -name '*.ninja' -exec sed -i 's:libtasn1\.so\b:libtasn1.a:g' {} \;
find . -type f -name '*.json' -exec sed -i 's:libtasn1\.so\b:libtasn1.a:g' {} \;
## make_prepend end
ninja %{?_smp_mflags} -v -C builddir

meson test -C builddir || :
find builddir/ -type f,l -not -name '*.gcno' -delete -print
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddefault_library=both -Dgtk_doc=false -Dman=false -Dtrust_paths=/var/cache/ca-certs -Dhash_impl=internal -Dtest=true -Dlibffi=enabled  builddir
## make_prepend content
find . -type f -name '*.txt' -exec sed -i 's:libffi\.so\b:libffi.a:g' {} \;
find . -type f -name '*.ninja' -exec sed -i 's:libffi\.so\b:libffi.a:g' {} \;
find . -type f -name '*.json' -exec sed -i 's:libffi\.so\b:libffi.a:g' {} \;
find . -type f -name '*.txt' -exec sed -i 's:libtasn1\.so\b:libtasn1.a:g' {} \;
find . -type f -name '*.ninja' -exec sed -i 's:libtasn1\.so\b:libtasn1.a:g' {} \;
find . -type f -name '*.json' -exec sed -i 's:libtasn1\.so\b:libtasn1.a:g' {} \;
## make_prepend end
ninja %{?_smp_mflags} -v -C builddir
pushd ../build32/
export CFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export CXXFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export LDFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
unset LD_LIBRARY_PATH
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
meson --libdir=lib32 --prefix=/usr --buildtype=plain -Ddefault_library=both -Dgtk_doc=false -Dman=false -Dtrust_paths=/var/cache/ca-certs -Dhash_impl=internal -Dtest=true -Dlibffi=enabled  builddir
ninja %{?_smp_mflags} -v -C builddir
popd

%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
meson test -C builddir || :
cd ../build32;
meson test -C builddir || : || :

%install
pushd ../build32/
DESTDIR=%{buildroot} ninja -C builddir install
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang p11-kit
## Remove excluded files
rm -f %{buildroot}/etc/pkcs11/pkcs11.conf.example
rm -f %{buildroot}%{_libdir}/p11-kit/trust-extract-compat
## install_append content
mv %{buildroot}/usr/bin/trust %{buildroot}/usr/bin/p11-trust
install -m 0755 trust-stub %{buildroot}/usr/bin/trust
ln -s %{_libdir}/pkcs11/p11-kit-trust.so %{buildroot}/%{_libdir}/libnssckbi.so
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/p11-kit
/usr/bin/p11-trust
/usr/bin/trust

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/p11-kit
/usr/share/bash-completion/completions/trust
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
/usr/lib32/pkgconfig/32p11-kit-1.pc
/usr/lib32/pkgconfig/p11-kit-1.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnssckbi.so
/usr/lib64/libp11-kit.so
/usr/lib64/libp11-kit.so.0
/usr/lib64/libp11-kit.so.0.3.0
/usr/lib64/p11-kit-proxy.so
/usr/lib64/pkcs11/p11-kit-client.so
/usr/lib64/pkcs11/p11-kit-trust.so

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libp11-kit.so
/usr/lib32/libp11-kit.so.0
/usr/lib32/libp11-kit.so.0.3.0
/usr/lib32/p11-kit-proxy.so
/usr/lib32/pkcs11/p11-kit-client.so
/usr/lib32/pkcs11/p11-kit-trust.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/p11-kit/p11-kit-remote
/usr/libexec/p11-kit/p11-kit-server
/usr/libexec/p11-kit/trust-extract-compat

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/p11-kit-server.service
/usr/lib/systemd/user/p11-kit-server.socket

%files locales -f p11-kit.lang
%defattr(-,root,root,-)

