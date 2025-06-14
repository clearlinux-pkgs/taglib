#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v27
# autospec commit: 65cf152
#
Name     : taglib
Version  : 2.1
Release  : 17
URL      : https://taglib.org/releases/taglib-2.1.tar.gz
Source0  : https://taglib.org/releases/taglib-2.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1 MPL-1.1
Requires: taglib-bin = %{version}-%{release}
Requires: taglib-lib = %{version}-%{release}
Requires: taglib-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : utf8cpp-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Run "make docs" in the parent directory to generate the TagLib API documentation.

%package bin
Summary: bin components for the taglib package.
Group: Binaries
Requires: taglib-license = %{version}-%{release}

%description bin
bin components for the taglib package.


%package dev
Summary: dev components for the taglib package.
Group: Development
Requires: taglib-lib = %{version}-%{release}
Requires: taglib-bin = %{version}-%{release}
Provides: taglib-devel = %{version}-%{release}
Requires: taglib = %{version}-%{release}

%description dev
dev components for the taglib package.


%package lib
Summary: lib components for the taglib package.
Group: Libraries
Requires: taglib-license = %{version}-%{release}

%description lib
lib components for the taglib package.


%package license
Summary: license components for the taglib package.
Group: Default

%description license
license components for the taglib package.


%prep
%setup -q -n taglib-2.1
cd %{_builddir}/taglib-2.1
pushd ..
cp -a taglib-2.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1748884952
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1748884952
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/taglib
cp %{_builddir}/taglib-%{version}/COPYING.LGPL %{buildroot}/usr/share/package-licenses/taglib/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
cp %{_builddir}/taglib-%{version}/COPYING.MPL %{buildroot}/usr/share/package-licenses/taglib/aba8d76d0af67d57da3c3c321caa59f3d242386b || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/taglib-config

%files dev
%defattr(-,root,root,-)
/usr/include/taglib/aifffile.h
/usr/include/taglib/aiffproperties.h
/usr/include/taglib/apefile.h
/usr/include/taglib/apefooter.h
/usr/include/taglib/apeitem.h
/usr/include/taglib/apeproperties.h
/usr/include/taglib/apetag.h
/usr/include/taglib/asfattribute.h
/usr/include/taglib/asffile.h
/usr/include/taglib/asfpicture.h
/usr/include/taglib/asfproperties.h
/usr/include/taglib/asftag.h
/usr/include/taglib/attachedpictureframe.h
/usr/include/taglib/audioproperties.h
/usr/include/taglib/chapterframe.h
/usr/include/taglib/commentsframe.h
/usr/include/taglib/dsdiffdiintag.h
/usr/include/taglib/dsdifffile.h
/usr/include/taglib/dsdiffproperties.h
/usr/include/taglib/dsffile.h
/usr/include/taglib/dsfproperties.h
/usr/include/taglib/eventtimingcodesframe.h
/usr/include/taglib/fileref.h
/usr/include/taglib/flacfile.h
/usr/include/taglib/flacmetadatablock.h
/usr/include/taglib/flacpicture.h
/usr/include/taglib/flacproperties.h
/usr/include/taglib/generalencapsulatedobjectframe.h
/usr/include/taglib/id3v1genres.h
/usr/include/taglib/id3v1tag.h
/usr/include/taglib/id3v2.h
/usr/include/taglib/id3v2extendedheader.h
/usr/include/taglib/id3v2footer.h
/usr/include/taglib/id3v2frame.h
/usr/include/taglib/id3v2framefactory.h
/usr/include/taglib/id3v2header.h
/usr/include/taglib/id3v2synchdata.h
/usr/include/taglib/id3v2tag.h
/usr/include/taglib/infotag.h
/usr/include/taglib/itfile.h
/usr/include/taglib/itproperties.h
/usr/include/taglib/modfile.h
/usr/include/taglib/modfilebase.h
/usr/include/taglib/modproperties.h
/usr/include/taglib/modtag.h
/usr/include/taglib/mp4atom.h
/usr/include/taglib/mp4coverart.h
/usr/include/taglib/mp4file.h
/usr/include/taglib/mp4item.h
/usr/include/taglib/mp4itemfactory.h
/usr/include/taglib/mp4properties.h
/usr/include/taglib/mp4tag.h
/usr/include/taglib/mpcfile.h
/usr/include/taglib/mpcproperties.h
/usr/include/taglib/mpegfile.h
/usr/include/taglib/mpegheader.h
/usr/include/taglib/mpegproperties.h
/usr/include/taglib/oggfile.h
/usr/include/taglib/oggflacfile.h
/usr/include/taglib/oggpage.h
/usr/include/taglib/oggpageheader.h
/usr/include/taglib/opusfile.h
/usr/include/taglib/opusproperties.h
/usr/include/taglib/ownershipframe.h
/usr/include/taglib/podcastframe.h
/usr/include/taglib/popularimeterframe.h
/usr/include/taglib/privateframe.h
/usr/include/taglib/relativevolumeframe.h
/usr/include/taglib/rifffile.h
/usr/include/taglib/s3mfile.h
/usr/include/taglib/s3mproperties.h
/usr/include/taglib/shortenfile.h
/usr/include/taglib/shortenproperties.h
/usr/include/taglib/shortentag.h
/usr/include/taglib/speexfile.h
/usr/include/taglib/speexproperties.h
/usr/include/taglib/synchronizedlyricsframe.h
/usr/include/taglib/tableofcontentsframe.h
/usr/include/taglib/tag.h
/usr/include/taglib/tag_c.h
/usr/include/taglib/taglib.h
/usr/include/taglib/taglib_config.h
/usr/include/taglib/taglib_export.h
/usr/include/taglib/tbytevector.h
/usr/include/taglib/tbytevectorlist.h
/usr/include/taglib/tbytevectorstream.h
/usr/include/taglib/tdebuglistener.h
/usr/include/taglib/textidentificationframe.h
/usr/include/taglib/tfile.h
/usr/include/taglib/tfilestream.h
/usr/include/taglib/tiostream.h
/usr/include/taglib/tlist.h
/usr/include/taglib/tlist.tcc
/usr/include/taglib/tmap.h
/usr/include/taglib/tmap.tcc
/usr/include/taglib/tpicturetype.h
/usr/include/taglib/tpropertymap.h
/usr/include/taglib/trueaudiofile.h
/usr/include/taglib/trueaudioproperties.h
/usr/include/taglib/tstring.h
/usr/include/taglib/tstringlist.h
/usr/include/taglib/tvariant.h
/usr/include/taglib/tversionnumber.h
/usr/include/taglib/uniquefileidentifierframe.h
/usr/include/taglib/unknownframe.h
/usr/include/taglib/unsynchronizedlyricsframe.h
/usr/include/taglib/urllinkframe.h
/usr/include/taglib/vorbisfile.h
/usr/include/taglib/vorbisproperties.h
/usr/include/taglib/wavfile.h
/usr/include/taglib/wavpackfile.h
/usr/include/taglib/wavpackproperties.h
/usr/include/taglib/wavproperties.h
/usr/include/taglib/xingheader.h
/usr/include/taglib/xiphcomment.h
/usr/include/taglib/xmfile.h
/usr/include/taglib/xmproperties.h
/usr/lib64/cmake/taglib/taglib-config-version.cmake
/usr/lib64/cmake/taglib/taglib-config.cmake
/usr/lib64/cmake/taglib/taglib-targets-relwithdebinfo.cmake
/usr/lib64/cmake/taglib/taglib-targets.cmake
/usr/lib64/libtag.so
/usr/lib64/libtag_c.so
/usr/lib64/pkgconfig/taglib.pc
/usr/lib64/pkgconfig/taglib_c.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libtag.so.2.1.0
/V3/usr/lib64/libtag_c.so.2.1.0
/usr/lib64/libtag.so.2
/usr/lib64/libtag.so.2.1.0
/usr/lib64/libtag_c.so.2
/usr/lib64/libtag_c.so.2.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/taglib/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/taglib/aba8d76d0af67d57da3c3c321caa59f3d242386b
