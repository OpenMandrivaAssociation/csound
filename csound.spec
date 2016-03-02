%ifarch %{arm} %{ix86} x86_64
%global has_luajit 1
%endif

%define _default_patch_fuzz 1
%define Werror_cflags %nil

%global __requires_exclude_from  %{_docdir}/%{name}

# Csound is really dumb about 64-bit
%ifarch x86_64 ia64
%define build64bit 1
%define install64bit --word64
%define useDouble 1
%else
%define build64bit 0
%define install64bit %{nil}
%define useDouble 0
%endif

%define build_java 0
%{?_with_java: %{expand: %%global build_java 1}}

Summary:	A sound synthesis language and library
Name:		csound
Version:	6.06
Release:	1
License:	LGPLv2+
Group:		Sound
URL:		http://csound.sourceforge.net/

Source0:	http://downloads.sourceforge.net/csound/Csound%{version}.tar.gz
Source2:	http://downloads.sourceforge.net/csound/manual_src.tar.gz

# Some patches taken from the Fedora .spec - thanks!
# Put plugins in _libdir/csound/plugins on all platforms
Patch0:  %{name}-6.03-64-bit-plugin-path.patch
# Rename some binaries to avoid name conflicts
Patch1:  %{name}-6.03-fix-conflicts.patch
# Default to using pulseaudio instead of portaudio
Patch2:  %{name}-6.03-default-pulse.patch
# Do not use SSE2 on non-x86_64 platforms
Patch3:  %{name}-6.03-sse2.patch
# Adapt to the way portmidi/porttime is packaged in Fedora
Patch4:  %{name}-6.03-porttime.patch
# Use xdg-open to open a browser to view the manual
Patch5:  %{name}-6.03-xdg-open.patch

BuildRequires:	cmake
BuildRequires:	swig
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	png-devel
BuildRequires:	jpeg-devel
BuildRequires:	python2-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
BuildRequires:	pulseaudio-devel
BuildRequires:	fluidsynth-devel
BuildRequires:	pkgconfig(liblo)
BuildRequires:	dssi-devel
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(luajit)
BuildRequires:	portaudio-devel
BuildRequires:	fltk-devel
%if %{build_java}
BuildRequires:	java-devel
BuildRequires:	jpackage-utils
%endif
BuildRequires:	ladspa-devel
BuildRequires:	libxslt-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libogg-devel
BuildRequires:	gettext
BuildRequires:	gcc-c++
BuildRequires:	boost-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-dtd45-xml
BuildRequires:	docbook-dtd42-xml
BuildRequires:	xsltproc

Obsoletes:	csound-tutorial <= 5.08
Obsoletes:	olpcsound <= 5.10.90
Obsoletes:	csound-java < 5.19.01-10
Obsoletes:	csound-javadoc < 5.19.01-10

# The fltk and tcl/tk frontends were removed in version 6 of csound.  These
# obsoletes can be removed in Mageia 7.
Obsoletes: %{name}-gui < 6.0-1
Provides:  %{name}-gui = 6.0-1
Obsoletes: %{name}-tk  < 6.0-1
Provides:  %{name}-tk  = 6.0-1

%global luaver %(lua -v | sed -r 's/Lua ([[:digit:]]+\\.[[:digit:]]+).*/\\1/')

%description
Csound is a sound and music synthesis system, providing facilities for
composition and performance over a wide range of platforms. It is not
restricted to any style of music, having been used for many years in
at least classical, pop, techno, ambient...

%package	devel
Summary:	Csound development files and libraries
Group:		Development/C
Requires:	%{name} = %{version}-%{release}
Obsoletes:	olpcsound-devel <= 5.10.90
Conflicts:	%{name}-python < 5.13.0-3

%description	devel
Contains headers and libraries for developing applications that use Csound.

%package	python
Summary:	Python Csound development files and libraries
Group:		Development/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python2

%description	python
Contains Python language bindings for developing Python applications that
use Csound.

%if %{build_java}
%package	java
Summary:	Java Csound support
Group:		Development/Java
Requires:	%{name} = %{version}-%{release}
Requires:	java-headless
Requires:	jpackage-utils

%description	java
Contains Java language bindings for developing and running Java
applications that use Csound.

%package	javadoc
Summary:	API documentation for Java Csound support
Group:		Development/Java

%description	javadoc
API documentation for the %{name}-java package.
%endif

%if 0%{?has_luajit}
%package lua
Summary: Lua Csound support
Requires: %{name} = %{version}-%{release}

%description lua
Contains Lua language bindings for developing and running Lua
applications that use Csound.
%endif

%package	fltk
Summary:	FLTK plugins for Csound
Group:		Sound
Requires:	%{name} = %{version}-%{release}
Requires:	fltk

%description	fltk
Contains FLTK plugins for csound

%package	jack
Summary:	Jack Audio plugins for Csound
Group:		Sound
Requires:	%{name} = %{version}-%{release}
Requires:	jackit

%description	jack
Contains Jack Audio plugins for Csound

%package	fluidsynth
Summary:	Fluidsyth soundfont plugin for Csound
Group:		Sound
Requires:	%{name} = %{version}-%{release}

%description	fluidsynth
Contains Fluidsynth soundfont plugin for Csound.

%package	dssi
Summary:	Disposable Soft Synth Interface (DSSI) plugin for Csound
Group:		Sound
Requires:	%{name} = %{version}-%{release}
Requires:	dssi

%description	dssi
Disposable Soft Synth Interface (DSSI) plugin for Csound

%package	osc
Summary:	Open Sound Control (OSC) plugin for Csound
Group:		Sound
Requires:	%{name} = %{version}-%{release}

%description	osc
Open Sound Control (OSC) plugin for Csound

%package portaudio
Summary: PortAudio plugin for Csound
Requires: %{name} = %{version}-%{release}

%description portaudio
PortAudio plugin for Csound

%package	virtual-keyboard
Summary:	Virtual MIDI keyboard plugin for Csound
Group:		Sound
Requires:	%{name} = %{version}-%{release}
Requires:	fltk

%description	virtual-keyboard
A virtual MIDI keyboard plugin for Csound

%package	doc
Summary:	Csound manual
Group:		Sound
Obsoletes:	%{name}-manual
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	doc
Canonical Reference Manual for Csound.


%prep
%setup -q -n Csound%{version}
%setup -q -n Csound%{version} -T -D -a 2

%patch0 -p1 -b .64-bit-plugin-path
%patch1 -p1 -b .fix-conflicts
%patch2 -p0 -b .default-pulse
%ifnarch x86_64
%patch3 -p1 -b .sse2
%endif
%patch4 -p1 -b .porttime
%patch5 -p0 -b .xdg-open

# Fix python, lua, and java install paths
sed -e 's,\(set(PYTHON_MODULE_INSTALL_DIR \).*,\1"%{python2_sitearch}"),' \
    -e 's,\(set(JAVA_MODULE_INSTALL_DIR.*\)),\1/csound/java),' \
    -e 's,\(set(LUA_MODULE_INSTALL_DIR.*\)),\1/lua/%{luaver}),' \
    -i CMakeLists.txt

# PYTHON_MODULE_INSTALL_DIR was changed to execute_process.
perl -p -0777 -i -e 's#execute_process\s*\(.*?OUTPUT_VARIABLE (PYTHON_MODULE_INSTALL_DIR)\s*?\)\s*\n#set($1 "%{python2_sitearch}")\n#ms' CMakeLists.txt

# Fix end of line encodings
%define fix_line_encoding() \
  sed -i.orig 's/\\r\\n/\\n/;s/\\r/\\n/g' %1; \
  touch -r %1.orig %1; \
  rm -f %1.orig;

for csd in $(find manual6/examples -name \*.csd); do
  %fix_line_encoding $csd
done
%fix_line_encoding examples/c/pvsbus.csd
%fix_line_encoding examples/cplusplus/fl_controller.dev
%fix_line_encoding examples/csoundapi_tilde/csoundapi-osx.pd
%fix_line_encoding examples/lua/csound_ffi.lua
%fix_line_encoding examples/opcode_demos/band.csd
%fix_line_encoding examples/opcode_demos/sdft.csd
%fix_line_encoding manual6/examples/128,8-torus
%fix_line_encoding manual6/examples/128-spiral-8,16,128,2,1over2
%fix_line_encoding manual6/examples/128-stringcircular
%fix_line_encoding manual6/examples/string-128.matrix

# Fix spurious executable bits
chmod a-x examples/csoundapi_tilde/csoundapi-osx.pd \
          examples/csoundapi_tilde/csoundapi.pd \
          examples/lua/lua_example.lua \
          manual6/examples/128*
%build
if [ "%{_libdir}" = "%{_prefix}/lib64" ]; then
  %cmake -DUSE_LIB64:BOOL=ON
else
  %cmake -DUSE_LIB64:BOOL=OFF
fi

make %{?_smp_mflags} V=1

%if %{build_java}
# Generate javadoc
(cd interfaces; mkdir apidocs; javadoc -d apidocs *.java)
%endif

# Make the manual
(
    cd ../
    make -C manual6 html-dist \
      XSL_BASE_PATH=%{_datadir}/sgml/docbook/xsl-stylesheets
)

%install
pushd build
%make_install

%if %{build_java}

# Fix the Java installation
install -dm 755 %{buildroot}%{_javadir}
(cd %{buildroot}%{_javadir}; ln -s %{_libdir}/%{name}/java/csnd.jar .)
mv %{buildroot}%{_libdir}/%{name}/java/lib_jcsound6.so %{buildroot}%{_libdir}

# Install Javadocs
install -dm 755 %{buildroot}%{_javadocdir}
cp -a interfaces/apidocs %{buildroot}%{_javadocdir}/%{name}-java

%endif

popd

%find_lang %{name}6

%files -f %{name}6.lang
%doc COPYING ChangeLog README.md
%{_bindir}/atsa
%{_bindir}/cs
%{_bindir}/csanalyze
%{_bindir}/csb64enc
%{_bindir}/csbeats
%{_bindir}/csdebugger
%{_bindir}/csound
%{_bindir}/cvanal
%{_bindir}/dnoise
%{_bindir}/cs-envext
%{_bindir}/cs-extract
%{_bindir}/cs-extractor
%{_bindir}/het_export
%{_bindir}/het_import
%{_bindir}/hetro
%{_bindir}/lpanal
%{_bindir}/lpc_export
%{_bindir}/lpc_import
%{_bindir}/makecsd
%{_bindir}/cs-mixer
%{_bindir}/pvanal
%{_bindir}/pvlook
%{_bindir}/cs-scale
%{_bindir}/cs-scot
%{_bindir}/cs-src_conv
%{_bindir}/scsort
%{_bindir}/sdif2ad
%{_bindir}/cs-sndinfo
%{_bindir}/cs-srconv
%{_bindir}/pv_export
%{_bindir}/pv_import
%{_libdir}/lib%{name}64.so.6.0
%{_libdir}/libcsnd6.so.6.0
%dir %{_libdir}/%{name}/plugins-6.0
%{_libdir}/%{name}/plugins-6.0/csladspa.so
%{_libdir}/%{name}/plugins-6.0/libampmidid.so
%{_libdir}/%{name}/plugins-6.0/libbuchla.so
%{_libdir}/%{name}/plugins-6.0/libcellular.so
%{_libdir}/%{name}/plugins-6.0/libcontrol.so
%{_libdir}/%{name}/plugins-6.0/libchua.so
%{_libdir}/%{name}/plugins-6.0/libcs_date.so
%{_libdir}/%{name}/plugins-6.0/libdoppler.so
%{_libdir}/%{name}/plugins-6.0/libexciter.so
%{_libdir}/%{name}/plugins-6.0/libframebuffer.so
%{_libdir}/%{name}/plugins-6.0/libfareygen.so
%{_libdir}/%{name}/plugins-6.0/libfractalnoise.so
%{_libdir}/%{name}/plugins-6.0/libimage.so
%{_libdir}/%{name}/plugins-6.0/libipmidi.so
%{_libdir}/%{name}/plugins-6.0/libjacko.so
%{_libdir}/%{name}/plugins-6.0/libjoystick.so
%{_libdir}/%{name}/plugins-6.0/libmixer.so
#%%{_libdir}/%%{name}/plugins/liboggplay.so
%{_libdir}/%{name}/plugins-6.0/libpadsynth.so
%{_libdir}/%{name}/plugins-6.0/libplaterev.so
%{_libdir}/%{name}/plugins-6.0/libpy.so
%{_libdir}/%{name}/plugins-6.0/librtalsa.so
%{_libdir}/%{name}/plugins-6.0/librtpulse.so
%{_libdir}/%{name}/plugins-6.0/libscansyn.so
%{_libdir}/%{name}/plugins-6.0/libserial.so
%{_libdir}/%{name}/plugins-6.0/libsignalflowgraph.so
%{_libdir}/%{name}/plugins-6.0/libstdutil.so
%{_libdir}/%{name}/plugins-6.0/libsystem_call.so
%{_libdir}/%{name}/plugins-6.0/liburandom.so

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}64.so
%{_libdir}/libcsnd6.so

%files python
%{python2_sitearch}/*

%if %{build_java}
%files java
%{_libdir}/lib_jcsound.so
%{_libdir}/%{name}/java/
%{_javadir}/csnd.jar

%files javadoc
%{_javadocdir}/%{name}-java
%endif

%if 0%{?has_luajit}
%files lua
%{_libdir}/%{name}/plugins-6.0/libLuaCsound.so
%{_libdir}/lua/%{luaver}/*
%endif

%files fltk
%{_libdir}/%{name}/plugins-6.0/libwidgets.so

%files jack
%{_libdir}/%{name}/plugins-6.0/librtjack.so
%{_libdir}/%{name}/plugins-6.0/libjackTransport.so

%files fluidsynth
%{_libdir}/%{name}/plugins-6.0/libfluidOpcodes.so

%files dssi
%{_libdir}/%{name}/plugins-6.0/libdssi4cs.so

%files osc
%{_libdir}/%{name}/plugins-6.0/libosc.so

%files portaudio
%{_libdir}/%{name}/plugins-6.0/librtpa.so

%files virtual-keyboard
%{_libdir}/%{name}/plugins-6.0/libvirtual.so

%files doc
%doc manual6/copying.txt
%doc manual6/html/*
%doc examples/*
