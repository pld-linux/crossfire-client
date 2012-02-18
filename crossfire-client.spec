#
# Conditional build:
%bcond_without	images	# don't build images package
#
%define		sndver	1.60.0
%define		imgver	1.60.0
Summary:	Crossfire client
Summary(pl.UTF-8):	Klient Crossfire
Name:		crossfire-client
Version:	1.60.0
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://downloads.sourceforge.net/crossfire/%{name}-%{version}.tar.gz
# Source0-md5:	7b22bf93ebb581a5bfd5682df107af76
Source1:	http://downloads.sourceforge.net/crossfire/%{name}-sounds-%{sndver}.tar.gz
# Source1-md5:	1985fc187a7624f48a4c4e9d609208ba
Source2:	http://downloads.sourceforge.net/crossfire/%{name}-images-%{imgver}.tar.gz
# Source2-md5:	e68b6f32c4d15e65af8535a346efe51a
Patch0:		%{name}-libpng15.patch
URL:		http://crossfire.real-time.com/
BuildRequires:	OpenGL-glut-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libtool
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
Suggests:	crossfire-client-images
Suggests:	crossfire-client-sounds
Obsoletes:	crossfire-client-common
Obsoletes:	crossfire-client-gtk
Obsoletes:	crossfire-client-gtk2
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
%setup  -q -a1
%patch0 -p1
mv -f sounds cfsounds
%if %{with images}
install -d images
cd images
tar xzf %{SOURCE2}
cd ..
%endif

%build
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure \
	%{?debug:--enable-debug} \
	--disable-alsa \
	--with-sound-dir=%{_datadir}/%{name}/sounds
%{__perl} -i -p -e 's/\#define HAVE_DMALLOC_H 1/\/\* \#undef HAVE_DMALLOC_H \*\//' common/config.h
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/%{name}/sounds}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install cfsounds/*.raw $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/
%if %{with images}
install images/bmaps.client images/crossfire.base images/crossfire.clsc \
	$RPM_BUILD_ROOT%{_datadir}/%{name}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/crossfire-client-gtk2
%{_mandir}/man?/crossfire-client-gtk2.*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/glade-gtk2
%{_datadir}/%{name}/themes

%files sounds
%defattr(644,root,root,755)
%doc cfsounds/README
%attr(755,root,root) %{_bindir}/cfsndserv*
%{_datadir}/%{name}/sounds

%if %{with images}
%files images
%defattr(644,root,root,755)
%{_datadir}/%{name}/bmaps.client
%{_datadir}/%{name}/crossfire.base
%{_datadir}/%{name}/crossfire.clsc
%endif
