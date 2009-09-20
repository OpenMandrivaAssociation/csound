%define _default_patch_fuzz 1
%define Werror_cflags %nil

# Csound is really dumb about 64-bit
%ifarch x86_64 ia64 ppc64 sparc64
%define build64bit 1
%define install64bit --word64
%define useDouble 1
%else
%define build64bit 0
%define install64bit %{nil}
%define useDouble 0
%endif

#%{?!pyver: %define pyver %(python -c 'import sys;print(sys.version[0:3])')}

Summary:       A sound synthesis language and library
Name:          csound
Version:       5.10.1
Release:       %mkrel 1
URL:           http://csound.sourceforge.net/
License:       LGPLv2+
Group:         Sound

BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: swig scons 
BuildRequires: libsndfile-devel 
BuildRequires: png-devel 
BuildRequires: jpeg-devel
BuildRequires: python-devel
BuildRequires: alsa-lib-devel 
BuildRequires: libjack-devel
BuildRequires: pulseaudio-devel
BuildRequires: fluidsynth-devel 
BuildRequires: liblo-devel 
BuildRequires: dssi-devel 
BuildRequires: lua-devel
BuildRequires: fltk-devel 
BuildRequires: java-devel >= 1.4.0
BuildRequires: jpackage-utils >= 1.5
BuildRequires: java-gcj-compat-devel
BuildRequires: tk-devel 
BuildRequires: tcl-devel
BuildRequires: tetex 
BuildRequires: tetex-latex 
BuildRequires: libxslt-devel
BuildRequires: libvorbis-devel 
BuildRequires: libogg-devel
BuildRequires: gettext
BuildRequires: gcc-c++ 
BuildRequires: boost-devel

Obsoletes: csound-tutorial <= 5.08
Obsoletes: olpcsound <= 5.10.90

Source0: http://downloads.sourceforge.net/csound/Csound5.10.1.tar.gz
Source1: http://downloads.sourceforge.net/csound/Csound5.10_manual_src.tar.gz
Source2: http://downloads.sourceforge.net/csound/Csound5.10_manual_html.zip

Patch1: csound-5.10.1-no-usr-local.patch
Patch2: csound-5.10.1-default-opcodedir.patch
Patch3: csound-5.10.1-rtalsa-fix.patch
Patch4: csound-5.10.1-makebuild.patch
Patch5: csound-5.10.1-64-bit-plugin-path.patch
Patch6: csound-5.10.1-fix-conflicts.patch
Patch7: csound-5.10.1-fix-locale-install.patch
Patch8: csound-5.10.1-enable-oggplay.patch

Patch9: csound-2817271-soname.patch
Patch0: csound-fixpython.patch
Patch10: csound-default-pulse.patch

Patch11: Csound5.10-fix-tcl-check.patch
Patch12: Csound5.10-fix-includes.patch

%description
Csound is a sound and music synthesis system, providing facilities for
composition and performance over a wide range of platforms. It is not
restricted to any style of music, having been used for many years in
at least classical, pop, techno, ambient...


%package devel
Summary: Csound development files and libraries
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: olpcsound-devel <= 5.08.92

%description devel
Contains headers and libraries for developing applications that use Csound.

%package python
Summary: Python Csound development files and libraries
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: python

%description python
Contains Python language bindings for developing Python applications that
use Csound.

%package java
Summary: Java Csound support
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
Requires:         jpackage-utils >= 1.5
Requires:         java-1.5.0-gcj
Requires(post):   jpackage-utils >= 1.5
Requires(postun): jpackage-utils >= 1.5
Requires(post):   java-gcj-compat
Requires(postun): java-gcj-compat

%description java
Contains Java language bindings for developing and running Java
applications that use Csound.

%package javadoc
Summary: API documentation for Java Csound support
Group: Documentation

%description javadoc
API documentation for the %{name}-java package.

%package tk
Summary: Tcl/Tk related Csound utilities
Group: Applications/Multimedia
Requires: %{name} = %{version}-%{release}
Requires: tcl tk

%description tk
Contains Tcl/Tk related Csound utilities

%package gui
Summary: A FLTK-based GUI for Csound
Group: Applications/Multimedia
Requires: %{name} = %{version}-%{release}
Requires: fltk xdg-utils

%description gui
Contains a FLTK-based GUI for Csound

%package fltk
Summary: FLTK plugins for Csound
Group: Applications/Multimedia
Requires: %{name} = %{version}-%{release}
Requires: fltk

%description fltk
Contains FLTK plugins for csound

%package jack
Summary: Jack Audio plugins for Csound
Group: Applications/Multimedia
Requires: %{name} = %{version}-%{release}
Requires: jack-audio-connection-kit

%description jack
Contains Jack Audio plugins for Csound

%package fluidsynth
Summary: Fluidsyth soundfont plugin for Csound
Group: Applications/Multimedia
Requires: %{name} = %{version}-%{release}

%description fluidsynth
Contains Fluidsynth soundfont plugin for Csound.

%package dssi
Summary: Disposable Soft Synth Interface (DSSI) plugin for Csound
Group: Applications/Multimedia
Requires: %{name} = %{version}-%{release}
Requires: dssi

%description dssi
Disposable Soft Synth Interface (DSSI) plugin for Csound

%package osc
Summary: Open Sound Control (OSC) plugin for Csound
Group: Applications/Multimedia
Requires: %{name} = %{version}-%{release}

%description osc
Open Sound Control (OSC) plugin for Csound

%package virtual-keyboard
Summary: Virtual MIDI keyboard plugin for Csound
Group: Applications/Multimedia
Requires: %{name} = %{version}-%{release}
Requires: fltk

%description virtual-keyboard
A virtual MIDI keyboard plugin for Csound

%package manual
Summary: Csound manual
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description manual
Canonical Reference Manual for Csound.


%prep
%setup -q -n Csound5.10.1
%patch0 -p1 -b .fixpython
%patch1 -p1 -b .no-usr-local
%patch2 -p1 -b .default-opcodedir
%patch3 -p1 -b .rtalsa
%patch4 -p1 -b .makebuild
%patch5 -p1 -b .64-bit-plugin-path
%patch6 -p1 -b .fix-conflicts
%patch7 -p1 -b .fix-local-install
%patch8 -p1 -b .enable-oggplay
%patch9 -p1 -b .2817271-soname
%patch10 -p1 -b .default-pulse
%patch11 -p0 -b .fix_tcl_check
%patch12 -p1 -b .includes
tar xf %{SOURCE1}
(cd manual; unzip -q %{SOURCE2})

%build

# Adjust location of the documentation for the GUI bits
sed -ie 's#\"firefox /usr/local/share/doc/csound/manual/#\"xdg-open file://%{_docdir}/%{name}-manual-%{version}/#' \
      frontends/fltk_gui/CsoundGlobalSettings.cpp

scons dynamicCsoundLibrary=1 \
      buildRelease=0 \
      noDebug=0 \
      disableGStabs=1 \
      buildInterfaces=1 \
      useGettext=1 \
      useALSA=1 \
      usePortAudio=0 \
      usePortMIDI=0 \
      useOGG=1 \
      useOSC=1 \
      useJack=1 \
      useFLTK=1 \
      buildVirtual=1 \
      useFluidsynth=1 \
      generatePdf=0 \
      buildCsound5GUI=1 \
      pythonVersion=2.6 \
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

# This file is zero-lenth for some reason
%{__rm} -f manual/examples/ifthen.csd
# Remove the CVS dir in examples
%{__rm} -rf manual/examples/CVS

install -dm 755 %{buildroot}%{_javadir}
(cd %{buildroot}%{_javadir}; ln -s %{_libdir}/%{name}/java/csnd.jar .)

install -dm 644 %{buildroot}%{_javadocdir}/%{name}-java
%{__chmod} -R 755 %{buildroot}%{_javadocdir}/%{name}-java
(cd interfaces; tar cf - *.html csnd/*.html) | (cd %{buildroot}%{_javadocdir}/%{name}-java; tar xvf -)

%{_bindir}/aot-compile-rpm

%find_lang %{name}5

%clean
%{__rm} -rf %{buildroot}

%post java
if [ -x %{_bindir}/rebuild-gcj-db ]; then
  %{_bindir}/rebuild-gcj-db
fi

%postun java
if [ -x %{_bindir}/rebuild-gcj-db ]; then
  %{_bindir}/rebuild-gcj-db
fi

%files -f %{name}5.lang
%defattr(-,root,root,-)
%doc COPYING ChangeLog readme-csound5.txt
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
%{_libdir}/libcsnd.so.5.2
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/libambicode1.so
%{_libdir}/%{name}/plugins/libampmidid.so
%{_libdir}/%{name}/plugins/libbabo.so
%{_libdir}/%{name}/plugins/liblinear_algebra.so
%{_libdir}/%{name}/plugins/libbarmodel.so
%{_libdir}/%{name}/plugins/libcompress.so
%{_libdir}/%{name}/plugins/libcontrol.so
%{_libdir}/%{name}/plugins/libchua.so
%{_libdir}/%{name}/plugins/libcs_date.so
%{_libdir}/%{name}/plugins/libcs_pan2.so
%{_libdir}/%{name}/plugins/libcs_pvs_ops.so
%{_libdir}/%{name}/plugins/libeqfil.so
%{_libdir}/%{name}/plugins/libftest.so
%{_libdir}/%{name}/plugins/libgabnew.so
%{_libdir}/%{name}/plugins/libgrain4.so
%{_libdir}/%{name}/plugins/libhrtferX.so
%{_libdir}/%{name}/plugins/libhrtfnew.so
%{_libdir}/%{name}/plugins/libimage.so
%{_libdir}/%{name}/plugins/libloscilx.so
%{_libdir}/%{name}/plugins/libminmax.so
%{_libdir}/%{name}/plugins/libmixer.so
%{_libdir}/%{name}/plugins/libmodal4.so
%{_libdir}/%{name}/plugins/libmutexops.so
%{_libdir}/%{name}/plugins/liboggplay.so
%{_libdir}/%{name}/plugins/libpartikkel.so
%{_libdir}/%{name}/plugins/libphisem.so
%{_libdir}/%{name}/plugins/libphysmod.so
%{_libdir}/%{name}/plugins/libpitch.so
%{_libdir}/%{name}/plugins/libptrack.so
%{_libdir}/%{name}/plugins/libpvoc.so
%{_libdir}/%{name}/plugins/libpvsbuffer.so
%{_libdir}/%{name}/plugins/libpy.so
%{_libdir}/%{name}/plugins/librtalsa.so
%{_libdir}/%{name}/plugins/librtpulse.so
%{_libdir}/%{name}/plugins/libscansyn.so
%{_libdir}/%{name}/plugins/libscoreline.so
%{_libdir}/%{name}/plugins/libsfont.so
%{_libdir}/%{name}/plugins/libshape.so
%{_libdir}/%{name}/plugins/libstackops.so
%{_libdir}/%{name}/plugins/libstdopcod.so
%{_libdir}/%{name}/plugins/libstdutil.so
%{_libdir}/%{name}/plugins/libsystem_call.so
%{_libdir}/%{name}/plugins/libudprecv.so
%{_libdir}/%{name}/plugins/libudpsend.so
%{_libdir}/%{name}/plugins/libvbap.so
%{_libdir}/%{name}/plugins/libharmon.so
%{_libdir}/%{name}/plugins/libugakbari.so
%{_libdir}/%{name}/plugins/libvaops.so
%{_libdir}/%{name}/plugins/libvosim.so

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so

%files python
%defattr(-,root,root,-)
%{_libdir}/libcsnd.so
%{_libdir}/python%{pyver}/site-packages/*

%files java
%defattr(-,root,root,-)
%{_libdir}/lib_jcsound.so
%{_libdir}/%{name}/java/
%{_javadir}/csnd.jar
%attr(-,root,root) %{_libdir}/gcj/%{name}

%files javadoc
%defattr(-,root,root,-)
%doc %{_javadocdir}/%{name}-java

%files tk
%defattr(-,root,root,-)
%{_libdir}/%{name}/tcl/
%{_bindir}/matrix.tk
%{_bindir}/brkpt
%{_bindir}/linseg
%{_bindir}/tabdes
%{_bindir}/cstclsh
%{_bindir}/cswish

%files gui
%defattr(-,root,root,-)
%{_bindir}/csound5gui

%files fltk
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/libwidgets.so

%files jack
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/librtjack.so
%{_libdir}/%{name}/plugins/libjackTransport.so

%files fluidsynth
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/libfluidOpcodes.so

%files dssi
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/libdssi4cs.so

%files osc
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/libosc.so

%files virtual-keyboard
%defattr(-,root,root,-)
%{_libdir}/%{name}/plugins/libvirtual.so

%files manual
%defattr(-,root,root,-)
#%doc manual/copying.txt manual/credits.txt manual/readme.txt manual/news.txt
#%doc manual/html/*
#%doc manual/examples

