Summary:	Glob2 is a state of the art Real Time Strategy (RTS) game.
Summary(pl):	Glob2 jest sztuk± przez du¿e "S" w postaci Strategii Czasu Rzeczywistego
Name:		globulation2
Version:	2.0.1
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Games
Vendor:		Stephane Magnenat, Julien Pilet, Luc-Olivier de Charri?re
Source0:	http://moneo.phear.org/~nct/glob2-latest.tar.gz
# Source0-md5:	9ca15309f68c450488393c73b244982e
URL:		http://ysagoon.com/glob2/
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_image-devel
#BuildRequires:	OpenGL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Glob2 jest sztuk± przez du¿e "S" w postaci Strategii Czasu Rzeczywistego 
(RTS). Jest to wolne oprogramowanie dystrybuowane zgodnie z zasadami 
okre¶lonymi w licencji GNU/GPL.

W ogólno¶ci Globulation jest projektem maj±cym na celu stworzenie wysokiej 
jako¶ci innowacyjnego ¶rodowiska gry poprzez minimalizacjê mikro-zarz±dzania
i automatycznego przypisywania zadañ jednostkom. Gracz musi tylko zamówiæ 
po¿±dan± ilo¶æ jednostek do realizacji danego zadania, a jednostki zrobi± 
wszystko co tylko mog±, ¿eby zaspokoiæ oczekiwania Gracza.

Glob2 mo¿e byæ grana pojedyñczo, poprzez sieæ LAN albo przez internet dziêki 
metaserwerowi Ysagoon Online Game (YOG). Istnieje tak¿e jêzyk skryptowy dla
zró¿nicowania gry oraz zintegrowany edytor map.


#%package subpackage
#Summary:	-
#Summary(pl):	-
#Group:		-
#
#%description subpackage
#
#%description subpackage -l pl

%prep
%setup -q -n %{name}-%{version}.orig

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}

#%files subpackage
#%defattr(644,root,root,755)
#%doc extras/*.gz
#%{_datadir}/%{name}-ext
