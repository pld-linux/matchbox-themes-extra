Summary:	Extra themes for Matchbox
Summary(pl):	Dodatkowe motywy dla ¶rodowiska Matchbox
Name:		matchbox-themes-extra
Version:	0.3
Release:	1
License:	GPL v2+
Group:		Themes
Source0:	http://projects.o-hand.com/matchbox/sources/matchbox-themes-extra/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	04312628f4a21f4105bce1251ea08035
URL:		http://projects.o-hand.com/matchbox/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extra themes for Matchbox: Industrial, expose, mbcrystal.

%description -l pl
Dodatkowe motywy dla ¶rodowiska Matchbox: Industrial, expose,
mbcrystal.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO
%{_iconsdir}/Industrial
%{_iconsdir}/expose
%{_iconsdir}/mbcrystal
%dir %{_datadir}/themes/Industrial
%{_datadir}/themes/Industrial/matchbox
%dir %{_datadir}/themes/expose
%{_datadir}/themes/expose/background
%{_datadir}/themes/expose/gtk-2.0
%{_datadir}/themes/expose/matchbox
%dir %{_datadir}/themes/mbcrystal
%{_datadir}/themes/mbcrystal/background
%{_datadir}/themes/mbcrystal/gtkrc-2.0
%{_datadir}/themes/mbcrystal/matchbox
