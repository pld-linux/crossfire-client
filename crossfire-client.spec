Summary:	Crossfire client.
Name:		crossfire-client
Version:	0.95.8
Release:	1
License:	GPL
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Source0:	ftp://ftp.scruz.net/users/mwedel/public/%{name}-%{version}.tar.gz
Patch0:		%{name}-noalsa.patch
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

%package gtk
Summary:	GTK Crossfire client.
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Requires:	%{name}

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
%setup -q
%patch0 -p1

%build
autoconf
%configure \
	--with-sound-dir=%{_datadir}/crossfire-client/sounds
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install cfclient gcfclient cfsndserv $RPM_BUILD_ROOT%{_bindir}
install client.man $RPM_BUILD_ROOT%{_mandir}/man1/cfclient.1
install client.man $RPM_BUILD_ROOT%{_mandir}/man1/gcfclient.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README README.old 
%attr(755,root,root) %{_bindir}/cf*
%{_mandir}/man?/cf*

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/g*
%{_mandir}/man?/g*
