Summary:	Crossfire client
Summary(pl):	Klient Crossfire
Name:		crossfire-client
Version:	1.0.0
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	ftp://ftp.scruz.net/users/mwedel/public/%{name}-%{version}.tar.gz
#Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/crossfire/%{name}-%{version}.tar.gz
Source1:	client-0.95.2-raw-sounds.tgz
URL:		http://crossfire.real-time.com/
BuildRequires:	XFree86-devel
BuildRequires:	gtk+-devel
BuildRequires:	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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

%description sounds
Some sound files and the sound server for crossfire.

%description sounds -l pl
Pliki d¼wiêkowe i serwer d¼wiêku dla Crossfire.

%package gtk
Summary:	GTK Crossfire client
Summary(pl):	Klient Crossfire pod GTK
Group:		Applications/Games

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

%prep
%setup -q -a1
mv -f sounds cfsounds

%build
%configure \
	--disable-alsa \
	--with-sound-dir=%{_datadir}/cfclient/sounds
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/cfclient/sounds}
install cfclient gcfclient cfsndserv $RPM_BUILD_ROOT%{_bindir}
install client.man $RPM_BUILD_ROOT%{_mandir}/man1/cfclient.1
install client.man $RPM_BUILD_ROOT%{_mandir}/man1/gcfclient.1
install cfsounds/*.raw $RPM_BUILD_ROOT%{_datadir}/cfclient/sounds/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README def_keys
%attr(755,root,root) %{_bindir}/cfclient
%{_mandir}/man?/cf*

%files sounds
%defattr(644,root,root,755)
%doc sounds/README* sounds.dist
%attr(755,root,root) %{_bindir}/cfsndserv
%{_datadir}/cfclient

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/g*
%{_mandir}/man?/g*
