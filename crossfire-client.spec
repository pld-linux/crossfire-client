Summary:	Crossfire client.
Name:		crossfire-client
Version:	0.98.0
Release:	1
License:	GPL
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Source0:	ftp://ftp.scruz.net/users/mwedel/public/%{name}-%{version}.tar.gz
#Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/crossfire/%{name}-%{version}.tar.gz
Source1:	client-0.95.2-raw-sounds.tgz
URL:		http://crossfire.real-time.com
BuildRequires:	XFree86-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/usr/X11R6

%description 
X11 client to crossfire.

Crossfire is a multiplayer graphical arcade and adventure game made
for the X-Windows environment. There are also Windows and Java clients
available.

It has certain flavours from other games, especially Gauntlet (TM) and
Nethack/Moria.

Any number of players can move around in their own window, finding and
sing items and battle monsters. They can choose to cooperate or
compete in the same "world".

%package sounds
Summary:	Crossfire sounds.
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry

%description sounds
Some sound files and the sound server for crossfire.

%package gtk
Summary:	GTK Crossfire client.
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry

%description gtk
GTK client to crossfire.

Crossfire is a multiplayer graphical arcade and adventure game made
for the X-Windows environment. There are also Windows and Java clients
available.

It has certain flavours from other games, especially Gauntlet (TM) and
Nethack/Moria.

Any number of players can move around in their own window, finding and
sing items and battle monsters. They can choose to cooperate or
compete in the same "world".

%prep
%setup -q -a1

%build
for l in sounds.dist soundsdef.h ; do
	mv $l $l.bak
	sed -e"s@/usr/local/lib/@%{_datadir}/cfclient/@" -e's@\.au@.raw@' < $l.bak > $l
done
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
install sounds/*.raw $RPM_BUILD_ROOT%{_datadir}/cfclient/sounds/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README README.old def_keys
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
