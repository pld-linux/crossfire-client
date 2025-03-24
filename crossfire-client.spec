#
# Conditional build:
%bcond_without	images	# images package
#
%define		sndver	1.72.0
%define		imgver	1.71.0
Summary:	Crossfire client
Summary(pl.UTF-8):	Klient Crossfire
Name:		crossfire-client
Version:	1.75.3
Release:	1
License:	GPL v2+
Group:		Applications/Games
Source0:	https://downloads.sourceforge.net/crossfire/%{name}-%{version}.tar.gz
# Source0-md5:	39f8efc273aaee00533b4cb7c5b00df6
Source2:	https://downloads.sourceforge.net/crossfire/%{name}-images-%{imgver}.tar.bz2
# Source2-md5:	91e9ad93276be1565d190fccdcfb810d
URL:		http://crossfire.real-time.com/
BuildRequires:	SDL2-devel >= 2
BuildRequires:	SDL2_mixer-devel >= 2
BuildRequires:	cmake >= 3.1
BuildRequires:	curl-devel
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libpng-devel
BuildRequires:	lua-devel >= 5.1.0
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	vala
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
Suggests:	crossfire-client-images = %{version}-%{release}
Suggests:	crossfire-client-sounds = %{version}-%{release}
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
Requires:	%{name} = %{version}-%{release}

%description sounds
Some sound files and the sound server for crossfire.

%description sounds -l pl.UTF-8
Pliki dźwiękowe i serwer dźwięku dla Crossfire.

%package images
Summary:	Crossfire images
Summary(pl.UTF-8):	Obrazki do Crossfire
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}

%description images
Some images extracted from server for Crossfire.

%description images -l pl.UTF-8
Trochę obrazków wyciągniętych z serwera do Crossfire.

%prep
%setup -q

%if %{with images}
install -d images
cd images
tar xf %{SOURCE2}
cd ..
%endif

%build
install -d build
cd build
%cmake .. \
	-DLUA=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with images}
cp -p images/bmaps.client images/crossfire.base images/crossfire.clsc \
	$RPM_BUILD_ROOT%{_datadir}/%{name}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst TODO
%attr(755,root,root) %{_bindir}/crossfire-client-gtk2
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/themes
%{_datadir}/%{name}/ui
%{_desktopdir}/crossfire-client.desktop
%{_iconsdir}/hicolor/*x*/apps/crossfire-client.png

%files sounds
%defattr(644,root,root,755)
%doc sounds/COPYING
%{_datadir}/%{name}/sounds

%if %{with images}
%files images
%defattr(644,root,root,755)
%{_datadir}/%{name}/bmaps.client
%{_datadir}/%{name}/crossfire.base
%{_datadir}/%{name}/crossfire.clsc
%endif
