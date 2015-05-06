%define major		0
%define libname		%mklibname %{name} %{major}
%define devname		%mklibname %{name} -d
%define libnameui	%mklibname qmmpui %{major}
%define devnameui	%mklibname qmmpui -d

######################
# Hardcode PLF build
%define build_plf 0
######################

%if %{build_plf}
%define distsuffix plf
%define extrarelsuffix plf
%endif

Summary:	Qt-based Multimedia Player
Name:		qmmp
Version:	0.8.3
Release:	2%{?extrarelsuffix}
License:	GPLv2+
Group:		Sound
Url:		http://qmmp.ylsoftware.com/index_en.php
Source:		http://qmmp.ylsoftware.com/files/%{name}-%{version}.tar.bz2

BuildRequires:	cmake
BuildRequires:	ffmpeg-devel
BuildRequires:	libgme-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	qt4-devel
BuildRequires:	qt4-linguist
BuildRequires:	sidplay-devel
BuildRequires:	wildmidi-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(enca)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(libbs2b)
BuildRequires:	pkgconfig(libcddb)
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libmms)
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(libprojectM)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libsidplay2)
BuildRequires:	pkgconfig(libsidplayfp)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(opus)
BuildRequires:	pkgconfig(opusfile)
BuildRequires:	pkgconfig(samplerate)
# do not remove sdl-headers needed by sid-ogg.Sflo
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(udisks)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(wavpack)

%if %{build_plf}
BuildRequires:	libfaad2-devel
%else
BuildConflicts:	libfaad2-devel
%endif
Requires:	%{libname} = %{EVRD}
Requires:	%{libnameui} = %{EVRD}
Requires:	%{name}-plugins = %{EVRD}
Suggests:	%{name}-aac = %{EVRD}
%if %{mdvver} >= 201210
Suggests:	%{name}-ffmpeg = %{EVRD}
%else
Suggests:	%{name}-ffmpeg-legacy = %{EVRD}
%endif
Suggests:	%{name}-jack = %{EVRD}
Suggests:	%{name}-modplug = %{EVRD}
Suggests:	%{name}-musepack = %{EVRD}
Suggests:	%{name}-oss = %{EVRD}
Suggests:	%{name}-wavpack = %{EVRD}
Suggests:	%{name}-plugin-pack
Requires:	unzip
Requires:	wildmidi

%description
This program is an audio-player, written with help of Qt library. The user
interface is similar to winamp or xmms.

Main opportunities:
* winamp and xmms skins support;
* plugins support;
* MPEG1 layer 1/2/3 support;
* Ogg Vorbis support;
* native FLAC support;
* Musepack support;
* WavePack support;
* ModPlug support;
* WMA support;
* PCM WAVE support;
* AlSA sound output;
* JACK sound output;
* OSS sound output;
* PulseAudio output;
* Last.fm scrobbler;
* D-Bus support;
* Spectrum Analyzer;
* sample rate conversion;
* streaming support (MP3, Vorbis via IceCast/ShoutCast).

%files
%doc AUTHORS ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_datadir}/%{name}

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library for %{name}
Group:		System/Libraries

%description -n %{libname}
Qmmp is an audio-player, written with help of Qt library.
This package contains the library needed by %{name}.

%files -n %{libname}
%doc AUTHORS ChangeLog
%{_libdir}/libqmmp.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libnameui}
Summary:	Library for %{name}
Group:		System/Libraries

%description -n %{libnameui}
Qmmp is an audio-player, written with help of Qt library.
This package contains the library needed by %{name}.

%files -n %{libnameui}
%doc AUTHORS ChangeLog
%{_libdir}/libqmmpui.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Qmmp is an audio-player, written with help of Qt library.
This package contains the files needed for developing applications
which use %{name}.

%files -n %{devname}
%doc AUTHORS ChangeLog
%{_includedir}/%{name}
%{_libdir}/libqmmp.so
%{_libdir}/pkgconfig/qmmp.pc

#----------------------------------------------------------------------------

%package -n %{devnameui}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libnameui} = %{EVRD}
Provides:	%{name}ui-devel = %{EVRD}
Conflicts:	%{_lib}qmmp-devel < 0.7.2

%description -n %{devnameui}
Qmmp is an audio-player, written with help of Qt library.
This package contains the files needed for developing applications
which use %{name}.

%files -n %{devnameui}
%doc AUTHORS ChangeLog
%{_includedir}/qmmpui
%{_libdir}/libqmmpui.so
%{_libdir}/pkgconfig/qmmpui.pc

#----------------------------------------------------------------------------

%if %{build_plf}
%package aac
Summary:	Qmmp AAC Input Plugin
Group:		Sound

%description aac
This is the AAC Input plug-in for Qmmp.

This package is in restricted repository because AAC codec is patent-protected.

%files aac
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Input/libaac.so
%endif

#----------------------------------------------------------------------------

#  ffmpeg-legacy in LTS
%if %{mdvver} >= 201210
%package ffmpeg
Summary:	Qmmp FFMPEG Input Plugin
Group:		Sound

%description ffmpeg
This is the FFMPEG Input Plugin for Qmmp.

%files ffmpeg
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Input/libffmpeg.so

%else

%package ffmpeg-legacy
Summary:	Qmmp FFMPEG Input Plugin
Group:		Sound

%description ffmpeg-legacy
This is the FFMPEG Input Plugin for Qmmp.

%files ffmpeg-legacy
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Input/libffmpeg_legacy.so
%endif

#----------------------------------------------------------------------------

%package jack
Summary:	Qmmp Jack Output Plugin
Group:		Sound

%description jack
This is the Jack Output Plugin for Qmmp.

%files jack
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Output/libjack.so

#----------------------------------------------------------------------------

%package modplug
Summary:	Qmmp Modplug Input Plugin
Group:		Sound

%description modplug
This is the Modplug Input Plugin for Qmmp.

%files modplug
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Input/libmodplug.so

#----------------------------------------------------------------------------

%package musepack
Summary:	Qmmp MusePack Output Plugin
Group:		Sound

%description musepack
This is the Musepack Input Plugin for Qmmp.

%files musepack
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Input/libmpc.so

#----------------------------------------------------------------------------
%package opus
Summary:	Qmmp Opus Input Plugin
Group:		Sound

%description opus
This is the Opus Input Plugin for Qmmp.

%files opus
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Input/libopus.so

#----------------------------------------------------------------------------

%package oss
Summary:	Qmmp OSS Output Plugin
Group:		Sound

%description oss
This is the Jack OSS Plugin for Qmmp.

%files oss
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Output/liboss.so


#----------------------------------------------------------------------------

%package plugins
Summary:	Qmmp Plugins
Group:		Sound

%description plugins
Qmmp is an audio-player, written with help of Qt library.
This contains basic plug-in distribution.

%files plugins
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Input/libflac.so
%{_libdir}/%{name}/Input/libmad.so
%{_libdir}/%{name}/Input/libsndfile.so
%{_libdir}/%{name}/Input/libvorbis.so
%{_libdir}/%{name}/Input/libcdaudio.so
%{_libdir}/%{name}/Input/libcue.so
%{_libdir}/%{name}/Input/libgme.so
%{_libdir}/%{name}/Input/libwildmidi.so
%{_libdir}/%{name}/Output/libalsa.so
%{_libdir}/%{name}/Output/libpulseaudio.so
%{_libdir}/%{name}/Output/libnull.so
%{_libdir}/%{name}/General/libnotifier.so
%{_libdir}/%{name}/General/libscrobbler.so
%{_libdir}/%{name}/General/libstatusicon.so
%{_libdir}/%{name}/General/libfileops.so
%{_libdir}/%{name}/General/libhotkey.so
%{_libdir}/%{name}/General/liblyrics.so
%{_libdir}/%{name}/General/libmpris.so
%{_libdir}/%{name}/General/libcovermanager.so
%{_libdir}/%{name}/General/libkdenotify.so
%{_libdir}/%{name}/General/libstreambrowser.so
%{_libdir}/%{name}/General/libconverter.so
%{_libdir}/%{name}/General/libcopypaste.so
%{_libdir}/%{name}/General/libtrackchange.so
%{_libdir}/%{name}/General/libudisks2.so
%{_libdir}/%{name}/General/libgnomehotkey.so
%{_libdir}/%{name}/General/librgscan.so
%{_libdir}/%{name}/PlayListFormats/*
%{_libdir}/%{name}/CommandLineOptions/libincdecvolumeoption.so
%{_libdir}/%{name}/CommandLineOptions/libseekoption.so
%{_libdir}/%{name}/CommandLineOptions/libstatusoption.so
%{_libdir}/%{name}/CommandLineOptions/libplaylistoption.so
%{_libdir}/%{name}/Effect/libsrconverter.so
%{_libdir}/%{name}/Effect/libbs2b.so
%{_libdir}/%{name}/Effect/libladspa.so
%{_libdir}/%{name}/Effect/libcrossfade.so
%{_libdir}/%{name}/Effect/libstereo.so
%{_libdir}/%{name}/Engines/libmplayer.so
%{_libdir}/%{name}/FileDialogs/libqmmpfiledialog.so
%{_libdir}/%{name}/Transports/libhttp.so
%{_libdir}/%{name}/Transports/libmms.so
%{_libdir}/%{name}/Visual/libanalyzer.so
%{_libdir}/%{name}/Visual/libprojectm.so
%{_libdir}/%{name}/Ui/libskinned.so

#----------------------------------------------------------------------------
%package sid
Summary:	Qmmp SID Input Plugin
Group:		Sound

%description sid
This is the SID Input Plugin for Qmmp.

%files sid
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Input/libsid.so

#----------------------------------------------------------------------------

%package wavpack
Summary:	Qmmp WavPack Input Plugin
Group:		Sound

%description wavpack
This is the WavPack Input Plugin for Qmmp.

%files wavpack
%doc AUTHORS ChangeLog
%{_libdir}/%{name}/Input/libwavpack.so

#----------------------------------------------------------------------------

%prep
%setup -q

%build
#oss3 support is deprecated upstream for now I'll enable it ...
%cmake_qt4 -DUSE_HAL:BOOL=FALSE \
	-DUSE_OSS:BOOL=TRUE \
	-DUSE_OSS:UDISKS2=TRUE \
	-DUSE_RPATH=TRUE \
	-DCMAKE_INSTALL_PREFIX=/usr

%make

%install
%makeinstall_std -C build

