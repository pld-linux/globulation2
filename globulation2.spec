Summary:	Glob2 - a state of the art Real Time Strategy (RTS) game
Summary(pl):	Glob2 - gra Strategii Czasu Rzeczywistego bêd±ca sztuk± przez du¿e "S"
Name:		globulation2
Version:	0.8.15
Release:	1
Epoch:		2
License:	GPL
Group:		Applications/Games
Vendor:		Stephane Magnenat, Julien Pilet, Luc-Olivier de Charriere
Source0:	http://epfl.ysagoon.com/~glob2/data/glob2-%{version}.tar.gz
# Source0-md5:	9adabb11048cd55c52822456b889b514
Source1:	http://moneo.phear.org/~nct/glob2gfx.tar
# Source1-md5:	368125e0e2c250e903eca18287a551b5
Source2:	http://goldeneye.sked.ch/~smagnena/sans.ttf
# Source2-md5:	48d9e359be3689eac14ef788a3bb1aa0
Source3:	%{name}.desktop
Source4:	%{name}.png
Patch0:		%{name}-default_lang.patch
URL:		http://epfl.ysagoon.com/wiki//
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_net-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel
BuildRequires:	speex-devel
BuildRequires:	unzip
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Glob2 is a state of the art Real Time Strategy (RTS) game. It is free
software released under the terms of the GNU General Public License.

Globulation in a whole is an on-going project to create an innovative
high quality gameplay by minimizing micro-managment and assigning
automatically the tasks to the units. The player just has to order
the number of units he wants for a selected task and the units will
do their best to satisfy your requirements.

Glob2 can be played by a single player, through your Local Area
Network (LAN), or through Internet thanks to Ysagoon Online Game (YOG),
a meta-server. It also features a scripting language for versatile
gameplay and an integrated map editor.

%description -l pl
Glob2 jest gr± Strategii Czasu Rzeczywistego (RTS) bêd±c± sztuk± przez
du¿e "S". Jest to wolne oprogramowanie dystrybuowane zgodnie z
zasadami okre¶lonymi w licencji GNU/GPL.

W ogólno¶ci Globulation jest projektem maj±cym na celu stworzenie
wysokiej jako¶ci innowacyjnego ¶rodowiska gry poprzez minimalizacjê
mikro-zarz±dzania i automatycznego przypisywania zadañ jednostkom.
Gracz musi tylko zamówiæ po¿±dan± ilo¶æ jednostek do realizacji danego
zadania, a jednostki zrobi± wszystko co tylko mog±, ¿eby zaspokoiæ
oczekiwania Gracza.

Glob2 mo¿e byæ grana pojedynczo, poprzez sieæ LAN albo przez Internet
dziêki metaserwerowi Ysagoon Online Game (YOG). Istnieje tak¿e jêzyk
skryptowy dla zró¿nicowania gry oraz zintegrowany edytor map.

%prep
%setup -q -n glob2-%{version}
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
CPPFLAGS="%{rpmcflags} -I%{_includedir}/speex"
LDFLAGS="%{rpmldflags} -L/usr/X11R6/lib"
%configure \
	--enable-opengl 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

tar -C $RPM_BUILD_ROOT%{_datadir}/glob2/data -xf %{SOURCE1}
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/glob2/data/fonts
install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/glob2
%{_desktopdir}/*
%{_pixmapsdir}/*
