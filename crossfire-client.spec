%define		sndver	1.4.0
%define		imgver	1.5.0
Summary:	Crossfire client
Summary(pl):	Klient Crossfire
Name:		crossfire-client
Version:	1.5.0
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/crossfire/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.sourceforge.net/pub/sourceforge/crossfire/%{name}-sounds-%{sndver}.tar.gz
Source2:	ftp://ftp.sourceforge.net/pub/sourceforge/crossfire/%{name}-images-%{imgver}.tar.gz
Patch0:		%{name}-sdl.patch
Patch1:		%{name}-dmalloc.patch
Patch2:		%{name}-errno.patch
URL:		http://crossfire.real-time.com/
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	gtk+-devel
BuildRequires:	perl
Requires:	%{name}-common = %{version}
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
Requires:	%{name}-common = %{version}

%description sounds
Some sound files and the sound server for crossfire.

%description sounds -l pl
Pliki d¼wiêkowe i serwer d¼wiêku dla Crossfire.

%package gtk
Summary:	GTK Crossfire client
Summary(pl):	Klient Crossfire pod GTK
Group:		Applications/Games
Requires:	%{name}-common = %{version}

%description gtk
GTK client to crossfire.

Crossfire is a multiplayer graphical arcade and adventure game made
for the X-Window environment. There are also Windows and Java clients
available.

It has certain flavours from other games, especially Gauntlet (TM) and
Nethack/Moria.

Any number of players can move around in their own window, finding and
sing items and battle monsters. They can choose to cooperate or
compete in the same "world".

%description gtk -l pl
Klient Crossfire pod GTK.

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
Requires:	%{name}-common = %{version}

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
%patch0 -p1
%patch1 -p1
%patch2 -p1
mv -f sounds cfsounds
%if %{?_without_images:0}%{?!_without_images:1}
install -d images
cd images
tar xzf %{SOURCE2}
cd ..
%endif

%build
%{__autoconf}
%configure \
	--disable-alsa \
	--disable-dmalloc \
	--with-sound-dir=%{_datadir}/%{name}/sounds
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/%{name}/sounds}

install x11/cfclient gtk/gcfclient sound-src/cfsndserv $RPM_BUILD_ROOT%{_bindir}
install x11/cfclient.man $RPM_BUILD_ROOT%{_mandir}/man1/cfclient.1
install gtk/gcfclient.man $RPM_BUILD_ROOT%{_mandir}/man1/gcfclient.1
install cfsounds/*.raw $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds/
%if %{?_without_images:0}%{?!_without_images:1}
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
%doc CHANGES README
%dir %{_datadir}/%{name}

%files sounds
%defattr(644,root,root,755)
%doc cfsounds/README
%attr(755,root,root) %{_bindir}/cfsndserv
%{_datadir}/%{name}/sounds

%if %{?_without_images:0}%{?!_without_images:1}
%files images
%defattr(644,root,root,755)
%{_datadir}/%{name}/bmaps.client
%{_datadir}/%{name}/crossfire.base
%{_datadir}/%{name}/crossfire.clsc
%endif

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/g*
%{_mandir}/man?/g*
