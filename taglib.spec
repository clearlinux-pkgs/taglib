#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : taglib
Version  : 1.13
Release  : 12
URL      : https://taglib.org/releases/taglib-1.13.tar.gz
Source0  : https://taglib.org/releases/taglib-1.13.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1 MPL-1.1
Requires: taglib-bin = %{version}-%{release}
Requires: taglib-lib = %{version}-%{release}
Requires: taglib-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : zlib-dev

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
%setup -q -n taglib-1.13
cd %{_builddir}/taglib-1.13

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666970250
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1666970250
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/taglib
cp %{_builddir}/taglib-%{version}/COPYING.LGPL %{buildroot}/usr/share/package-licenses/taglib/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
cp %{_builddir}/taglib-%{version}/COPYING.MPL %{buildroot}/usr/share/package-licenses/taglib/aba8d76d0af67d57da3c3c321caa59f3d242386b || :
pushd clr-build
%make_install
popd

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
/usr/include/taglib/tpropertymap.h
/usr/include/taglib/trefcounter.h
/usr/include/taglib/trueaudiofile.h
/usr/include/taglib/trueaudioproperties.h
/usr/include/taglib/tstring.h
/usr/include/taglib/tstringlist.h
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
/usr/lib64/libtag.so
/usr/lib64/libtag_c.so
/usr/lib64/pkgconfig/taglib.pc
/usr/lib64/pkgconfig/taglib_c.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtag.so.1
/usr/lib64/libtag.so.1.19.0
/usr/lib64/libtag_c.so.0
/usr/lib64/libtag_c.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/taglib/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/taglib/aba8d76d0af67d57da3c3c321caa59f3d242386b
