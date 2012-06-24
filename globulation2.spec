Summary:	Glob2 - a state of the art Real Time Strategy (RTS) game
Summary(pl):	Glob2 - gra Strategii Czasu Rzeczywistego b�d�ca sztuk� przez du�e "S"
Name:		globulation2
Version:	0.8.21
Release:	3
Epoch:		2
License:	GPL
Group:		Applications/Games
Vendor:		Stephane Magnenat, Julien Pilet, Luc-Olivier de Charriere
Source0:	http://globulation2.org/releases/%{version}/glob2-%{version}.tar.gz
# Source0-md5:	3173f82572f1dd5fba79019ebc43d427
Source1:	http://cursor.uam.mx/mirrors/gnu/savannah/files/glob2/glob2gfx.tar
# Source1-md5:	8e4516243ecaa76fa12d700f4a93e708
Source2:	http://goldeneye.sked.ch/~smagnena/sans.ttf
# Source2-md5:	48d9e359be3689eac14ef788a3bb1aa0
Patch0:		%{name}-default_lang.patch
Patch1:		%{name}-desktop.patch
URL:		http://globulation2.org/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-ref-devel
BuildRequires:	freetype-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel
BuildRequires:	speex-devel
BuildRequires:	unzip
Requires(post,postun):	desktop-file-utils
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

%description -l pl
Glob2 jest gr� Strategii Czasu Rzeczywistego (RTS) b�d�c� sztuk� przez
du�e "S". Jest to wolne oprogramowanie dystrybuowane zgodnie z
zasadami okre�lonymi w licencji GNU/GPL.

W og�lno�ci Globulation jest projektem maj�cym na celu stworzenie
wysokiej jako�ci innowacyjnego �rodowiska gry poprzez minimalizacj�
mikro-zarz�dzania i automatycznego przypisywania zada� jednostkom.
Gracz musi tylko zam�wi� po��dan� ilo�� jednostek do realizacji danego
zadania, a jednostki zrobi� wszystko co tylko mog�, �eby zaspokoi�
oczekiwania Gracza.

Glob2 mo�e by� grana pojedynczo, poprzez sie� LAN albo przez Internet
dzi�ki metaserwerowi Ysagoon Online Game (YOG). Istnieje tak�e j�zyk
skryptowy dla zr�nicowania gry oraz zintegrowany edytor map.

%prep
%setup -q -n glob2-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
CPPFLAGS="%{rpmcflags} -I%{_includedir}/speex"
%configure \
	--enable-opengl

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

tar -C $RPM_BUILD_ROOT%{_datadir}/glob2/data -xf %{SOURCE1}
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/glob2/data/fonts

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/glob2
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
