Summary:	Glob2 - a state of the art Real Time Strategy (RTS) game
Summary(pl.UTF-8):	Glob2 - gra Strategii Czasu Rzeczywistego będąca sztuką przez duże "S"
Name:		globulation2
Version:	0.9.1
Release:	1
Epoch:		2
License:	GPL v3+
Group:		Applications/Games
Vendor:		Stephane Magnenat, Julien Pilet, Luc-Olivier de Charriere
Source0:	http://dl.sv.nongnu.org/releases/glob2/%{version}/glob2-%{version}.tar.gz
# Source0-md5:	507da29c310f199f9b1a9a5f335b7a7a
Source1:	%{name}.desktop
Patch0:		%{name}-default_lang.patch
URL:		http://globulation2.org/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	SDL_image-devel >= 1.2
BuildRequires:	SDL_net-devel >= 1.2
BuildRequires:	SDL_ttf-devel >= 2.0
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	freetype-devel
BuildRequires:	libogg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel
BuildRequires:	scons
BuildRequires:	speex-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Glob2 is a state of the art Real Time Strategy (RTS) game. It is free
software released under the terms of the GNU General Public License.

Globulation in a whole is an on-going project to create an innovative
high quality gameplay by minimizing micro-managment and assigning
automatically the tasks to the units. The player just has to order the
number of units he wants for a selected task and the units will do
their best to satisfy your requirements.

Glob2 can be played by a single player, through your Local Area
Network (LAN), or through Internet thanks to Ysagoon Online Game
(YOG), a meta-server. It also features a scripting language for
versatile gameplay and an integrated map editor.

%description -l pl.UTF-8
Glob2 jest grą Strategii Czasu Rzeczywistego (RTS) będącą sztuką przez
duże "S". Jest to wolne oprogramowanie dystrybuowane zgodnie z
zasadami określonymi w licencji GNU/GPL.

W ogólności Globulation jest projektem mającym na celu stworzenie
wysokiej jakości innowacyjnego środowiska gry poprzez minimalizację
mikro-zarządzania i automatycznego przypisywania zadań jednostkom.
Gracz musi tylko zamówić pożądaną ilość jednostek do realizacji danego
zadania, a jednostki zrobią wszystko co tylko mogą, żeby zaspokoić
oczekiwania Gracza.

Glob2 może być grana pojedynczo, poprzez sieć LAN albo przez Internet
dzięki metaserwerowi Ysagoon Online Game (YOG). Istnieje także język
skryptowy dla zróżnicowania gry oraz zintegrowany edytor map.

%prep
%setup -q -n glob2-%{version}
%patch0 -p1

%build
scons \
	CXXFLAGS="%{rpmcxxflags}" \
	INSTALLDIR="%{_datadir}" \
	BINDIR="%{_bindir}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/glob2,%{_desktopdir},%{_pixmapsdir}}

install src/glob2 $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install data/icons/glob2-icon-48x48.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
cp -r {data,campaigns,maps,scripts} $RPM_BUILD_ROOT%{_datadir}/glob2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/glob2
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
