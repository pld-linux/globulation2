Summary:	Glob2 is a state of the art Real Time Strategy (RTS) game.
Summary(pl):	Glob2 jest sztuk± przez du¿e "S" w postaci Strategii Czasu Rzeczywistego
Name:		glob2
Version:	0.1
Release:	0.1
License:	GPL
Group:		Applications/Games
Vendor:		Stephane Magnenat, Julien Pilet, Luc-Olivier de Charri?re
Source0:	http://moneo.phear.org/~nct/%{name}-latest.tar.gz
# Source0-md5:	6ee54e75dcee3edef86bfcdf1dd6ea79
Source1:	http://www.ysagoon.com/%{name}/data/map-max.zip
# Source1-md5:	ae15af82644d1382d428c0e2e5de3d54
Source2:	http://www.ysagoon.com/%{name}/data/map-amazon.zip
# Source2-md5:	8680f45bc1115f0ffda2f768d0e88324
Source3:	http://www.ysagoon.com/%{name}/data/map-amazon2.zip
# Source3-md5:	793f71bb87bdb619db3a40c0b10d9305
Source4:	http://www.ysagoon.com/%{name}/data/map-atoll.zip
# Source4-md5:	11366ef0f8ff216c347cc7a39237bdc7
Source5:	http://www.ysagoon.com/%{name}/data/map-atoll2.zip
# Source5-md5:	597a70a4bc49694c8d266a057480fd25
Source6:	http://www.ysagoon.com/%{name}/data/map-claustrophobic.zip
# Source6-md5:	29bf0d4939bdab46f24056f28eabd4c9
Source7:	http://moneo.phear.org/~nct/%{name}gfx.tar
# Source7-md5:	368125e0e2c250e903eca18287a551b5
Source8:	http://goldeneye.sked.ch/~smagnena/sans.ttf
# Source8-md5:	48d9e359be3689eac14ef788a3bb1aa0
Patch0:		%{name}-default_lang.patch
URL:		http://ysagoon.com/glob2/
BuildRequires:	SDL_net-devel
BuildRequires:	SDL_image-devel
BuildRequires:	libstdc++-devel
BuildRequires:	unzip
#BuildRequires:	OpenGL-devel
Obsoletes:	globulation2
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

%prep
%setup -q -n %{name}
%patch0 -p1

%build
rm -f missing
#%%{__gettextize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	LDFLAGS="%{rpmldflags} -L/usr/X11R6/lib"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
unzip %{SOURCE1} -d $RPM_BUILD_ROOT/%{_datadir}/%{name}/maps
unzip %{SOURCE2} -d $RPM_BUILD_ROOT/%{_datadir}/%{name}/maps
unzip %{SOURCE3} -d $RPM_BUILD_ROOT/%{_datadir}/%{name}/maps
unzip %{SOURCE4} -d $RPM_BUILD_ROOT/%{_datadir}/%{name}/maps
unzip %{SOURCE5} -d $RPM_BUILD_ROOT/%{_datadir}/%{name}/maps
unzip %{SOURCE6} -d $RPM_BUILD_ROOT/%{_datadir}/%{name}/maps
tar -C $RPM_BUILD_ROOT/%{_datadir}/%{name}/data -xf %{SOURCE7}
cp %{SOURCE8} $RPM_BUILD_ROOT/%{_datadir}/%{name}/data/fonts

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO doc/unit.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
