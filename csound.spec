%global	debug_package	%{nil}

%define	api		7.0
%define	major		7
%define	libname		%mklibname %{name} %{major}
%define	develname	%mklibname -d %{name}

%define		gitdate	20251118

%bcond_without	manual
# As with 7.0.0beta1 java build is disabled in the sources
%bcond_with	java

# Avoid providing private libraries
%global		__provides_exclude	_CsoundAC.so | _csnd7.so

Summary:		A sound synthesis language and library
Name:		csound
# Beta release
Version:		7.0.0
Release:		0.beta10
License:		LGPLv2+
Group:		Sound
Url:		https://csound.com
# Sub-modules are a pain...
#Source0:	https://github.com/csound/csound/archive/%%{name}-%%{version}.tar.gz
Source0:	%{name}-%{gitdate}.tar.xz
%if %{with manual}
Source1:	https://github.com/csound/csound/releases/download/%{version}/Csound6.18.0_manual_html.zip
%endif
Source100:	csound.rpmlintrc
Patch0:		csound-7.0.0beta1-64bit-plugin-path.patch
Patch1:		csound-7.0.0beta1-default-to-pulse.patch
Patch2:		csound-7.0.0beta1-sse2.patch
Patch3:		csound-7.0.0beta1-xdg-open.patch
Patch4:		csound-7.0.0beta10-fix-cmake-files-path.patch
BuildRequires:		cmake >= 3.13.4
BuildRequires:		bison
BuildRequires:		doxygen
BuildRequires:		faust >= 2.0.0
BuildRequires:		flex
BuildRequires:		git
BuildRequires:		getfem
BuildRequires:		gettext
%if %{with java}
BuildRequires:		java-21-openjdk-module-jdk.jpackage
BuildRequires:		java-21-openjdk-devel
%endif
BuildRequires:		python
BuildRequires:		swig >= 2.0
BuildRequires:		xsltproc
BuildRequires:		boost-devel
BuildRequires:		gomp-devel
BuildRequires:		ladspa-devel
BuildRequires:		libmusicxml-devel
BuildRequires:		llvm-devel
BuildRequires:		pkgconfig(alsa)
BuildRequires:		pkgconfig(cunit)
BuildRequires:		pkgconfig(dssi)
BuildRequires:		pkgconfig(eigen3)
BuildRequires:		pkgconfig(flac)
BuildRequires:		pkgconfig(jack)
BuildRequires:		pkgconfig(libcurl)
BuildRequires:		pkgconfig(libjpeg)
BuildRequires:		pkgconfig(liblo)
BuildRequires:		pkgconfig(libpng)
BuildRequires:		pkgconfig(libpipewire-0.3)
BuildRequires:		pkgconfig(libpulse)
BuildRequires:		pkgconfig(lua)
BuildRequires:		pkgconfig(luajit)
BuildRequires:		pkgconfig(ogg)
BuildRequires:		pkgconfig(openssl)
BuildRequires:		pkgconfig(opus)
BuildRequires:		pkgconfig(portaudio-2.0)
BuildRequires:		pkgconfig(portmidi)
BuildRequires:		pkgconfig(python3)
BuildRequires:		pkgconfig(samplerate)
BuildRequires:		pkgconfig(sndfile) >= 1.1.0
BuildRequires:		pkgconfig(speex)
BuildRequires:		pkgconfig(vorbis)
BuildRequires:		pkgconfig(vorbisenc)
BuildRequires:		pkgconfig(x11)

%description
Csound is a sound and music synthesis system, providing facilities for
composition and performance over a wide range of platforms. It is not
restricted to any style of music, having been used for many years in at least
classical, pop, techno, ambient...

%files -f csound7.lang
%doc COPYING README.md Release_Notes/*
%{_bindir}/atsa
%{_bindir}/cs
%{_bindir}/cs-srconv
%{_bindir}/csanalyze
%{_bindir}/csb64enc
%{_bindir}/csbeats
%{_bindir}/csdebugger
%{_bindir}/%{name}
%{_bindir}/cvanal
%{_bindir}/dnoise
%{_bindir}/envext
%{_bindir}/extract
%{_bindir}/extractor
%{_bindir}/het_export
%{_bindir}/het_import
%{_bindir}/hetro
%{_bindir}/lpanal
%{_bindir}/lpc_export
%{_bindir}/lpc_import
%{_bindir}/makecsd
%{_bindir}/mixer
%{_bindir}/pv_export
%{_bindir}/pv_import
%{_bindir}/pvanal
%{_bindir}/pvlook
%{_bindir}/scale
%{_bindir}/scot
%{_bindir}/scsort
%{_bindir}/sdif2ad
%{_bindir}/smf_conv
%{_bindir}/sndinfo
%{_bindir}/src_conv
%{_datadir}/samples/*

#-------------------------------------------------------------------------------

%package -n %{libname}
Summary:	Csound main library and plug-ins
Group:		System/Libraries
# Dropped plugins packages
%rename	%{name}-fltk
%rename	%{name}-fluidsynth
%rename	%{name}-stk
%rename	%{name}-virtual-keyboard

%description -n %{libname}
Contains the libraries and the main plug-ins for using Csound.

%files -n %{libname}
%doc COPYING
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins-%{api}
%{_libdir}/lib%{name}64.so.%{major}*
#{_libdir}/libcsnd7.so.%%{major}*
#{_libdir}/luaCsnd7.so
#{_libdir}/%%{name}/plugins-%%{api}/libarrayops.so
#{_libdir}/%%{name}/plugins-%%{api}/libampmidid.so
#{_libdir}/%%{name}/plugins-%%{api}/libcontrol.so
%{_libdir}/%{name}/plugins-%{api}/libdeprecated.so
#{_libdir}/%%{name}/plugins-%%{api}/libdoppler.so
#{_libdir}/%%{name}/plugins-%%{api}/libbformdec2.so
#{_libdir}/%%{name}/plugins-%%{api}/libfractalnoise.so
#{_libdir}/%%{name}/plugins-%%{api}/libftsamplebank.so
%{_libdir}/%{name}/plugins-%{api}/libipmidi.so
%{_libdir}/%{name}/plugins-%{api}/libjoystick.so
#{_libdir}/%%{name}/plugins-%%{api}/liblfsr.so
#{_libdir}/%%{name}/plugins-%%{api}/libmixer.so
#{_libdir}/%%{name}/plugins-%%{api}/libpadsynth.so
%{_libdir}/%{name}/plugins-%{api}/libpmidi.so
#{_libdir}/%%{name}/plugins-%%{api}/libpvsops.so
%{_libdir}/%{name}/plugins-%{api}/librtalsa.so
%{_libdir}/%{name}/plugins-%{api}/librtpa.so
%{_libdir}/%{name}/plugins-%{api}/librtpulse.so
%{_libdir}/%{name}/plugins-%{api}/librtpw.so
#{_libdir}/%%{name}/plugins-%%{api}/libscansyn.so
#{_libdir}/%%{name}/plugins-%%{api}/libsignalflowgraph.so
%{_libdir}/%{name}/plugins-%{api}/libstdutil.so
#{_libdir}/%%{name}/plugins-%%{api}/libtrigenvsegs.so
#{_libdir}/%%{name}/plugins-%%{api}/liburandom.so

#-------------------------------------------------------------------------------

%package -n %{develname}
Summary:	Csound development files and libraries
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{name}-devel < %{EVRD}

%description -n %{develname}
Contains headers and libraries for developing applications that use Csound.

%files -n %{develname}
%doc COPYING
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/*
%{_libdir}/lib%{name}64.so
#{_libdir}/libcsnd7.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/cmake/csound/CsoundConfig.cmake
%{_datadir}/cmake/csound/CsoundConfig-relwithdebinfo.cmake

#-------------------------------------------------------------------------------

%package python
Summary:	Python Csound files
Group:		Development/Python
Requires:	%{libname} = %{EVRD}
Requires:	python
Requires:	python-numpy

%description python
Contains Python files for using Csound.

%files python
%doc COPYING
%{py_sitedir}/ctcsound.py

#-------------------------------------------------------------------------------

%if %{with java}
%package java
Summary:	Java Csound support
Group:		Development/Java
Requires:	%{libname} = %{EVRD}
Requires:	jpackage-utils >= 1.5

%description java
Contains Java language bindings for developing and running Java applications
that use Csound.

%files java
%doc COPYING
%{_libdir}/lib_jcsound7.so
%{_libdir}/lib_jcsound.so.1
%{_libdir}/csnd7.jar
%{_javadir}/csnd7.jar

#-------------------------------------------------------------------------------

%package javadoc
Summary:	API documentation for Java Csound support
Group:		Development/Java
Requires:	%{name}-java = %{EVRD}

%description javadoc
API documentation for the %{name}-java package.

%files javadoc
%doc COPYING
%doc %{_javadocdir}/%{name}-java
%endif

#-------------------------------------------------------------------------------

%package jack
Summary:	Jack Audio plug-ins for Csound
Group:		Sound
Requires:	%{libname} = %{EVRD}
Requires:	jackit

%description jack
Contains Jack Audio plugins for Csound.

%files jack
%doc COPYING
%{_libdir}/%{name}/plugins-%{api}/librtjack.so
#{_libdir}/%%{name}/plugins-%%{api}/libjackTransport.so

#-------------------------------------------------------------------------------

%package dssi
Summary:	Disposable Soft Synth Interface (DSSI) plug-in for Csound
Group:		Sound
Requires:	%{libname} = %{EVRD}
Requires:	dssi

%description dssi
Disposable Soft Synth Interface (DSSI) plug-in for Csound.

%files dssi
%doc COPYING
%{_libdir}/%{name}/plugins-%{api}/libdssi4cs.so

#-------------------------------------------------------------------------------

%package osc
Summary:	Open Sound Control (OSC) plug-in for Csound
Group:		Sound
Requires:	%{libname} = %{EVRD}

%description osc
Open Sound Control (OSC) plug-in for Csound.

%files osc
%doc COPYING
%{_libdir}/%{name}/plugins-%{api}/libosc.so

#-------------------------------------------------------------------------------

%if %{with_manual}
%package manual
Summary:	The Csound manual
Group:		Sound
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description manual
Canonical Reference Manual for Csound.

%files manual
%doc manual/html
%endif

#-------------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{gitdate}

%if %{with_manual}
# Extract manual files and fix perms
mkdir -p manual
pushd manual
	unzip -q %{SOURCE1}
	chmod 0755 html
	cd html
	chmod 0644 *.html *.css
	chmod 0755 images examples
	cd images/callouts
	chmod 0644 *
	cd ..
	chmod 0755 callouts
	chmod 0644 *.png *.jpg *.gif
	cd ..
	cd examples
	chmod 0644 *
	chmod 0755 musical
	cd ../..
popd
%endif

# Fix source perms
find Opcodes/emugens/ -name "*.c" -o -name "*.h" | xargs chmod 0644
find util/ -name "*.c" -o -name "*.h" | xargs chmod 0644
find util1/sortex/ -name "*.c" -o -name "*.h" | xargs chmod 0644


%build
#-DLUA_LIBRARY="%%{_libdir}/libluajit-5.1.so" \
#-DLUA_MODULE_INSTALL_DIR="%%{_libdir}" \
%cmake \
	-DBUILD_RELEASE=1 \
	-DBUILD_UTILITIES=1 \
	-DBUILD_DSSI_OPCODES=1 \
	-DBUILD_PLUGINS=0 \
	-DBUILD_TESTS=0 \
	-DBUILD_LTO=1 \
	-DFAIL_MISSING=0 \
	-DUSE_DOUBLE=1 \
	-DUSE_LIB64=1 \
	-DUSE_CURL=1 \
	-DUSE_GETTEXT=1 \
	-DLIBRARY_INSTALL_DIR="%{_libdir}"

%make_build

%if %{with java}
# Generate javadoc...
pushd interfaces
	javadoc *.java
popd
%endif


%install
%make_install -C build

# Fix filename conflict
mv %{buildroot}%{_bindir}/srconv %{buildroot}%{_bindir}/cs-srconv

%if %{with java}
# Put the java package where it should be and make sure csound can find it
install -dm 755 %{buildroot}%{_javadir}
(cd %{buildroot}%{_javadir}; ln -s %{_libdir}/csnd7.jar .)
# Create index for it
jar -i %{buildroot}%{_libdir}/csnd7.jar

# Package the docs for java
install -dm 644 %{buildroot}%{_javadocdir}/%{name}-java
%{__chmod} -R 755 %{buildroot}%{_javadocdir}/%{name}-java
pushd build/interfaces
	(tar cf - *.html csnd7/*.html) | (cd %{buildroot}%{_javadocdir}/%{name}-java; tar xvf -)
popd
%endif

%find_lang csound7
