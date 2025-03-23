#
# Conditional build:
%bcond_without	images	# images package
#
%define		sndver	1.71.0
%define		imgver	1.71.0
Summary:	Crossfire client
Summary(pl.UTF-8):	Klient Crossfire
Name:		crossfire-client
Version:	1.71.0
Release:	1
License:	GPL v2+
Group:		Applications/Games
Source0:	https://downloads.sourceforge.net/crossfire/%{name}-%{version}.tar.bz2
# Source0-md5:	a32b9a3cb42f65820c5a9193dcfa56d5
Source1:	https://downloads.sourceforge.net/crossfire/%{name}-sounds-%{sndver}.tar.bz2
# Source1-md5:	3c9b8045231d4f861986b76b1bfde328
Source2:	https://downloads.sourceforge.net/crossfire/%{name}-images-%{imgver}.tar.bz2
# Source2-md5:	91e9ad93276be1565d190fccdcfb810d
Patch1:		%{name}-link.patch
URL:		http://crossfire.real-time.com/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libglade2-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	lua-devel >= 5.1.0
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
Suggests:	crossfire-client-images
Suggests:	crossfire-client-sounds
Obsoletes:	crossfire-client-common < 1.60
Obsoletes:	crossfire-client-gtk < 1.60
Obsoletes:	crossfire-client-gtk2 < 1.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK+2 client to crossfire.

Crossfire is a multiplayer graphical arcade and adventure game made
for the X-Window environment. There are also Windows and Java clients
available.

It has certain flavours from other games, especially Gauntlet (TM) and
Nethack/Moria.

Any number of players can move around in their own window, finding and
sing items and battle monsters. They can choose to cooperate or
compete in the same "world".

%description -l pl.UTF-8
Klient Crossfire pod GTK+2.

Crossfire to graficzna gra przygodowa dla środowiska X-Window. Są
także dostępni klienci pod Windows i w Javie. Łączy cechy z kilku
gier, głównie Gauntleta i Nethacka/Morii.

Dowolna liczba graczy może się poruszać w swoich oknach, szukając
przedmiotów i walcząc z potworami. Mogą grać w kooperacji lub
przeciwko sobie w tym samym "świecie".

%package sounds
Summary:	Crossfire sounds
Summary(pl.UTF-8):	Dźwięki do Crossfire
Group:		Applications/Games

%description sounds
Some sound files and the sound server for crossfire.

%description sounds -l pl.UTF-8
Pliki dźwiękowe i serwer dźwięku dla Crossfire.

%package images
Summary:	Crossfire images
Summary(pl.UTF-8):	Obrazki do Crossfire
Group:		Applications/Games

%description images
Some images extracted from server for Crossfire.

%description images -l pl.UTF-8
Trochę obrazków wyciągniętych z serwera do Crossfire.

%prep
%setup -q -a1
%patch -P1 -p1
%{__mv} sounds cfsounds
%if %{with images}
install -d images
cd images
tar xf %{SOURCE2}
cd ..
%endif

%build
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?debug:--enable-debug} \
	--disable-alsa \
	--enable-sdl_mixer \
	--with-sound-dir=%{_datadir}/%{name}/sounds
%{__perl} -i -p -e 's/\#define HAVE_DMALLOC_H 1/\/\* \#undef HAVE_DMALLOC_H \*\//' common/config.h
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/%{name}/sounds}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p cfsounds/*.wav cfsounds/sounds.conf $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/
%if %{with images}
cp -p images/bmaps.client images/crossfire.base images/crossfire.clsc \
	$RPM_BUILD_ROOT%{_datadir}/%{name}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/crossfire-client-gtk2
%{_mandir}/man6/crossfire-client-gtk2.6*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/themes
%{_datadir}/%{name}/ui

%files sounds
%defattr(644,root,root,755)
%doc cfsounds/AUTHORS
%attr(755,root,root) %{_bindir}/cfsndserv*
%{_datadir}/%{name}/sounds

%if %{with images}
%files images
%defattr(644,root,root,755)
%{_datadir}/%{name}/bmaps.client
%{_datadir}/%{name}/crossfire.base
%{_datadir}/%{name}/crossfire.clsc
%endif
