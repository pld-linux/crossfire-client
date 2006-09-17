#
# Conditional build:
%bcond_without	images	# don't build images package
#
%define		sndver	1.9.1
%define		imgver	1.9.1
Summary:	Crossfire client
Summary(pl):	Klient Crossfire
Name:		crossfire-client
Version:	1.9.1
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/crossfire/%{name}-%{version}.tar.gz
# Source0-md5:	e7084c22c1f2074c95fe34331ac2ceae
Source1:	http://dl.sourceforge.net/crossfire/%{name}-sounds-%{sndver}.tar.gz
# Source1-md5:	f996c3220d505098a4a226f92902b002
Source2:	http://dl.sourceforge.net/crossfire/%{name}-images-%{imgver}.tar.gz
# Source2-md5:	b2766880d5dffbf24ae98b8ca07cb89f
URL:		http://crossfire.real-time.com/
Patch0:		%{name}-gl.patch
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
# next 2 probably unneeded
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	autoconf
BuildRequires:	gtk+-devel
BuildRequires:	gtk+2-devel
BuildRequires:	perl-base
Requires:	%{name}-common = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X11 client to crossfire.

Crossfire is a multiplayer graphical arcade and adventure game made
for the X-Window environment. There are also Windows and Java clients
available.

It has certain flavours from other games, especially Gauntlet (TM) and
Nethack/Moria.

Any number of players can move around in their own window, finding and
sing items and battle monsters. They can choose to cooperate or
compete in the same "world".

%description -l pl
Klient Crossfire pod X11.

Crossfire to graficzna gra przygodowa dla ¶rodowiska X-Window. S±
tak¿e dostêpni klienci pod Windows i w Javie. £±czy cechy z kilku
gier, g³ównie Gauntleta i Nethacka/Morii.

Dowolna liczba graczy mo¿e siê poruszaæ w swoich oknach, szukaj±c
przedmiotów i walcz±c z potworami. Mog± graæ w kooperacji lub
przeciwko sobie w tym samym "¶wiecie".

%package sounds
Summary:	Crossfire sounds
Summary(pl):	D¼wiêki do Crossfire
Group:		Applications/Games
Requires:	%{name}-common = %{version}-%{release}

%description sounds
Some sound files and the sound server for crossfire.

%description sounds -l pl
Pliki d¼wiêkowe i serwer d¼wiêku dla Crossfire.

%package gtk
Summary:	GTK+ Crossfire client
Summary(pl):	Klient Crossfire pod GTK+
Group:		Applications/Games
Requires:	%{name}-common = %{version}-%{release}

%description gtk
GTK+ client to crossfire.

Crossfire is a multiplayer graphical arcade and adventure game made
for the X-Window environment. There are also Windows and Java clients
available.

It has certain flavours from other games, especially Gauntlet (TM) and
Nethack/Moria.

Any number of players can move around in their own window, finding and
sing items and battle monsters. They can choose to cooperate or
compete in the same "world".

%description gtk -l pl
Klient Crossfire pod GTK+.

Crossfire to graficzna gra przygodowa dla ¶rodowiska X-Window. S±
tak¿e dostêpni klienci pod Windows i w Javie. £±czy cechy z kilku
gier, g³ównie Gauntleta i Nethacka/Morii.

Dowolna liczba graczy mo¿e siê poruszaæ w swoich oknach, szukaj±c
przedmiotów i walcz±c z potworami. Mog± graæ w kooperacji lub
przeciwko sobie w tym samym "¶wiecie".

%package gtk2
Summary:	GTK+2 Crossfire client
Summary(pl):	Klient Crossfire pod GTK+2
Group:		Applications/Games
Requires:	%{name}-common = %{version}-%{release}

%description gtk2
GTK+2 client to crossfire.

Crossfire is a multiplayer graphical arcade and adventure game made
for the X-Window environment. There are also Windows and Java clients
available.

It has certain flavours from other games, especially Gauntlet (TM) and
Nethack/Moria.

Any number of players can move around in their own window, finding and
sing items and battle monsters. They can choose to cooperate or
compete in the same "world".

%description gtk2 -l pl
Klient Crossfire pod GTK+2.

Crossfire to graficzna gra przygodowa dla ¶rodowiska X-Window. S±
tak¿e dostêpni klienci pod Windows i w Javie. £±czy cechy z kilku
gier, g³ównie Gauntleta i Nethacka/Morii.

Dowolna liczba graczy mo¿e siê poruszaæ w swoich oknach, szukaj±c
przedmiotów i walcz±c z potworami. Mog± graæ w kooperacji lub
przeciwko sobie w tym samym "¶wiecie".

%package images
Summary:	Crossfire images
Summary(pl):	Obrazki do Crossfire
Group:		Applications/Games
Requires:	%{name}-common = %{version}-%{release}

%description images
Some images extracted from server for Crossfire.

%description images -l pl
Trochê obrazków wyci±gniêtych z serwera do Crossfire.

%package common
Summary:	Common Crossfire clients files
Summary(pl):	Pliki wspólne wszystkich klientów Crossfire
Group:		Applications/Games

%description common
This package includes files common to all Crossfire clients.

%description common -l pl
Ten pakiet zawiera pliki wspólne dla wszystkich klientów Crossfire.

%prep
%setup  -q -a1
mv -f sounds cfsounds
%if %{with images}
install -d images
cd images
tar xzf %{SOURCE2}
cd ..
%endif
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
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
%attr(755,root,root) %{_bindir}/cfclient
%{_mandir}/man?/cf*

%files common
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{_datadir}/%{name}

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

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gcfclient
%{_mandir}/man?/gcfclient.*

%files gtk2
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gcfclient2
