# Csound is really dumb about 64-bit
%ifarch	x86_64 ia64 ppc64 sparc64 s390x
%define	build64bit 1
%define	install64bit --word64
%define	useDouble 1
%else
%define	build64bit 0
%define	install64bit %{nil}
%define	useDouble 0
%endif

Summary:	A sound synthesis language and library
Name:		csound
Version:	5.18.02
Release:	5
License:	LGPLv2+
Group:		Sound

URL:		http://csound.sourceforge.net/
Source0:	http://downloads.sourceforge.net/csound/Csound%{version}.tar.gz
Source2:	http://downloads.sourceforge.net/csound/Csound5.18_manual_html.zip
Source100:	csound.rpmlintrc
Patch0:		csound-5.18.02-fixpython.patch
Patch1:		csound-5.18.02-no-usr-local.patch
Patch2:		csound-5.18.02-default-opcodedir.patch
Patch5:		csound-5.18.02-64-bit-plugin-path.patch
Patch6:		csound-5.18.02-fix-conflicts.patch
Patch7:		csound-5.18.02-fix-locale-install.patch
Patch9:		csound-5.18.02-default-pulse.patch
Patch10:	csound-5.18.02-compile-flag.patch
Patch13:	csound-5.18.02-fix-tcl-check.patch
Patch14:	csound-5.18.02-fix-link.patch

BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gcc-c++
BuildRequires:	gettext
BuildRequires:	python
BuildRequires:	scons
BuildRequires:	swig
BuildRequires:	jpackage-utils >= 1.5
BuildRequires:	texlive
BuildRequires:	texlive-latex
BuildRequires:	xsltproc

BuildRequires:	alsa-oss-devel
BuildRequires:	boost-devel
BuildRequires:	fltk-devel
BuildRequires:	java-1.6.0-openjdk-devel
BuildRequires:	java-1.5.0-gcj-devel
BuildRequires:	jpeg-devel
BuildRequires:	tcl-devel
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(dssi)
BuildRequires:	pkgconfig(fluidsynth)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(liblo)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(luajit)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(pixman-1)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(tk)
BuildRequires:	pkgconfig(vorbis)

%description
Csound is a sound and music synthesis system, providing facilities for
composition and performance over a wide range of platforms. It is not
restricted to any style of music, having been used for many years in
at least classical, pop, techno, ambient...

%package devel
Summary:	Csound development files and libraries
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description devel
Contains headers and libraries for developing applications that use Csound.

%package python
Summary:	Python Csound development files and libraries
Group:		Development/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python

%description python
Contains Python language bindings for developing Python applications that
use Csound.


#package python-devel
#Summary:		Csound python development files and libraries
#Group:		Development/Python
#Requires:	%{name}-python = %{version}-%{release}
#description python-devel
#Contains libraries for developing against csound-python.

%package java
Summary:	Java Csound support
Group:		Development/Java
Requires:	%{name} = %{version}-%{release}
Requires:	jpackage-utils >= 1.5
Requires:	java-1.5.0-gcj
Requires(post,postun):	gcj-tools

%description java
Contains Java language bindings for developing and running Java
applications that use Csound.


%package javadoc
Summary:	API documentation for Java Csound support
Group:		Development/Java

%description javadoc
API documentation for the %{name}-java package.

%package tk
Summary:	Tcl/Tk related Csound utilities
Group:		Sound
Requires:	%{name} = %{version}-%{release}
Requires:	tcl
Requires:	tk

%description tk
Contains Tcl/Tk related Csound utilities.


%package gui
Summary:	A FLTK-based GUI for Csound
Group:		Sound
Requires:	%{name} = %{version}-%{release}
Requires:	fltk
Requires:	xdg-utils

%description gui
Contains a FLTK-based GUI for Csound.


%package fltk
Summary:	FLTK plugins for Csound
Group:		Sound
Requires:	%{name} = %{version}-%{release}
Requires:	fltk

%description fltk
Contains FLTK plugins for csound.


%package jack
Summary:	Jack Audio plugins for Csound
Group:		Sound
Requires:	%{name} = %{version}-%{release}

%description jack
Contains Jack Audio plugins for Csound.


%package fluidsynth
Summary:	Fluidsyth soundfont plugin for Csound
Group:		Sound
Requires:	%{name} = %{version}-%{release}

%description fluidsynth
Contains Fluidsynth soundfont plugin for Csound.


%package dssi
Summary:	Disposable Soft Synth Interface (DSSI) plugin for Csound
Group:		Sound
Requires:	%{name} = %{version}-%{release}
Requires:	dssi

%description dssi
Disposable Soft Synth Interface (DSSI) plugin for Csound.


%package osc
Summary:	Open Sound Control (OSC) plugin for Csound
Group:		Sound
Requires:	%{name} = %{version}-%{release}

%description osc
Open Sound Control (OSC) plugin for Csound.


%package virtual-keyboard
Summary:	Virtual MIDI keyboard plugin for Csound
Group:		Sound
Requires:	%{name} = %{version}-%{release}
Requires:	fltk

%description virtual-keyboard
A virtual MIDI keyboard plugin for Csound.


%package manual
Summary:	Csound manual
Group:		Sound
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description manual
Canonical Reference Manual for Csound.


%prep
%setup -q -n Csound%{version}
%patch0 -p1 -b .fixpython
%patch1 -p1 -b .no-usr-local
%patch2 -p1 -b .default-opcodedir
%patch5 -p1 -b .64-bit-plugin-path
%patch6 -p1 -b .fix-conflicts
%patch7 -p1 -b .fix-local-install
%patch9 -p1 -b .default-pulse
%patch10 -p1 -b .compile-flag
%patch13 -p1 -b .tcl
%patch14 -p1 -b .link

# It needs a custom.py or scons will fail
cp custom-linux-jpff.py custom.py

#tar xf %{SOURCE1}
mkdir -p manual
(cd manual; unzip -q %{SOURCE2})

%build
%define Werror_cflags %{nil}

# TODO: (gvm) Try the cmake-based build

# Adjust location of the documentation for the GUI bits
sed -ie 's#\"firefox /usr/local/share/doc/csound/manual/#\"xdg-open file://%{_docdir}/%{name}-manual-%{version}/#' \
      frontends/fltk_gui/CsoundGlobalSettings.cpp

# Dirty hacks
sed -i s/"(LIBS = \['sndfile'\]"/"(LIBS = \['sndfile', 'python2.7'\]"/g SConstruct
sed -i s/"java-1.5.0"/"java-1.6.0"/g SConstruct
sed -i s/"java-1.5.0"/"java-1.6.0"/g custom.py

# -I %{py_platlibdir} -I %{_includedir} -I %{py_incdir}
scons \
      dynamicCsoundLibrary=1 \
      buildRelease=0 \
      noDebug=0 \
      disableGStabs=1 \
      buildInterfaces=1 \
      useGettext=1 \
      useALSA=1 \
      usePortAudio=0 \
      usePortMIDI=0 \
      useOSC=1 \
      useJack=1 \
      useFLTK=1 \
      buildVirtual=1 \
      useFluidsynth=1 \
      generatePdf=0 \
      buildCsound5GUI=1 \
      pythonVersion=%{python_version} \
      buildPythonOpcodes=1 \
      buildPythonWrapper=1 \
      buildLuaWrapper=1 \
      buildTclcsound=1 \
      buildJavaWrapper=1 \
      buildDSSI=1 \
      buildUtilities=1 \
      prefix=%{_prefix} \
      customCCFLAGS="%{optflags}" \
      customCXXFLAGS="%{optflags}" \
      customSHLINKFLAGS="%{ldflags}" \
      Word64=%{build64bit} \
      useDouble=%{useDouble}

# Generate javadoc
(cd interfaces; javadoc *.java)


%install
%{__rm} -rf %{buildroot}
%{__python} install.py --prefix=%{_prefix} --instdir=%{buildroot} %{install64bit}
%{__rm} -f %{buildroot}%{_docdir}/%{name}/COPYING
%{__rm} -f %{buildroot}%{_docdir}/%{name}/ChangeLog
%{__rm} -f %{buildroot}%{_docdir}/%{name}/INSTALL
%{__rm} -f %{buildroot}%{_docdir}/%{name}/readme-csound5.txt
%{__rm} -f %{buildroot}%{_bindir}/uninstall-csound5
%{__rm} -f %{buildroot}%{_prefix}/csound5-*.md5sums

install -dm 755 %{buildroot}%{_javadir}
(cd %{buildroot}%{_javadir}; ln -s %{_libdir}/%{name}/java/csnd.jar .)

install -dm 644 %{buildroot}%{_javadocdir}/%{name}-java
%{__chmod} -R 755 %{buildroot}%{_javadocdir}/%{name}-java
(cd interfaces; tar cf - *.html csnd/*.html) | (cd %{buildroot}%{_javadocdir}/%{name}-java; tar xvf -)

%{_bindir}/aot-compile-rpm

%find_lang %{name}5

%post java
if [ -x %{_bindir}/rebuild-gcj-db ]; then
  %{_bindir}/rebuild-gcj-db
fi

%postun java
if [ -x %{_bindir}/rebuild-gcj-db ]; then
  %{_bindir}/rebuild-gcj-db
fi

%files -f %{name}5.lang
%doc COPYING ChangeLog readme-csound5.txt
%{_bindir}/atsa
%{_bindir}/cs-launcher
%{_bindir}/csb64enc
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
%{_bindir}/scsort
%{_bindir}/cs-sndinfo
%{_bindir}/cs-srconv
%{_bindir}/pv_export
%{_bindir}/pv_import
%{_libdir}/lib%{name}.so.5.2
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/libampmidid.so
%{_libdir}/%{name}/plugins/libcellular.so
%{_libdir}/%{name}/plugins/libchua.so
%{_libdir}/%{name}/plugins/libcontrol.so
%{_libdir}/%{name}/plugins/libcs_date.so
%{_libdir}/%{name}/plugins/libcsladspa.so
%{_libdir}/%{name}/plugins/libdoppler.so
%{_libdir}/%{name}/plugins/libfareygen.so
%{_libdir}/%{name}/plugins/libfractalnoise.so
%{_libdir}/%{name}/plugins/libimage.so
%{_libdir}/%{name}/plugins/libjacko.so
%{_libdir}/%{name}/plugins/libjoystik.so
%{_libdir}/%{name}/plugins/libmixer.so
%{_libdir}/%{name}/plugins/libplaterev.so
%{_libdir}/%{name}/plugins/libpy.so
%{_libdir}/%{name}/plugins/librtalsa.so
%{_libdir}/%{name}/plugins/librtpulse.so
%{_libdir}/%{name}/plugins/libscansyn.so
%{_libdir}/%{name}/plugins/libserial.so
%{_libdir}/%{name}/plugins/libsignalflowgraph.so
%{_libdir}/%{name}/plugins/libstdutil.so
%{_libdir}/%{name}/plugins/libsystem_call.so
%{_libdir}/%{name}/plugins/libudprecv.so
%{_libdir}/%{name}/plugins/libudpsend.so
%{_libdir}/%{name}/plugins/liburandom.so

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/libcsnd.so


%files python
%{_libdir}/libcsnd.so.5.2
%{python_sitearch}/_csnd*
%{python_sitearch}/csnd*


#files python-devel
#{_libdir}/libcsnd.so


%files java
%{_libdir}/lib_jcsound.so
%{_libdir}/%{name}/java/
%{_javadir}/csnd.jar
%attr(-,root,root) %{_libdir}/gcj/%{name}


%files javadoc
%doc COPYING
%doc %{_javadocdir}/%{name}-java


%files tk
%{_libdir}/%{name}/tcl/
%{_bindir}/matrix.tk
%{_bindir}/brkpt
%{_bindir}/linseg
%{_bindir}/tabdes
%{_bindir}/cstclsh
%{_bindir}/cswish

%files gui
%{_bindir}/csound5gui


%files fltk
%{_libdir}/%{name}/plugins/libwidgets.so

%files jack
%{_libdir}/%{name}/plugins/librtjack.so
%{_libdir}/%{name}/plugins/libjackTransport.so


%files fluidsynth
%{_libdir}/%{name}/plugins/libfluidOpcodes.so


%files dssi
%{_libdir}/%{name}/plugins/libdssi4cs.so


%files osc
%{_libdir}/%{name}/plugins/libosc.so


%files virtual-keyboard
%{_libdir}/%{name}/plugins/libvirtual.so


%files manual
%doc manual/html

