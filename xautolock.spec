%define	version 2.2
%define rel	2
%define	release	%mkrel %rel

Name:		xautolock
Summary:	Automatically starts programs when there is inactivity under X
Version:	%{version} 
Release:	%{release} 
Source0:	%{name}-%{version}.tar.bz2
URL:		https://www.ibiblio.org/pub/Linux/X11/screensavers/
Group:		Graphical desktop/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPLv2
Requires:	xlockmore
BuildRequires:	X11-devel imake
#(nl) Needed for rman
BuildRequires:  xorg-x11

%description
Xautolock monitors the user activity on an X Window display.
If none is detected within a certain amount of time a program specified
by the user will be run. Typically xautolock will be used to lock the screen
using for instance xlock.

%prep
%setup -q

%build
xmkmf
%make

%install
rm -rf $RPM_BUILD_ROOT
bzip2 ./xautolock.man
install -m644 xautolock.man.bz2 -D $RPM_BUILD_ROOT%{_mandir}/man1/xautolock.man.bz2
install -m755 xautolock -D $RPM_BUILD_ROOT%{_prefix}/X11R6/bin/xautolock
# Make sure all docs are readable
chmod a+r Changelog Readme Todo License

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc License Todo Readme Changelog
%{_prefix}/X11R6/bin/xautolock
%{_mandir}/*/*



%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2-2mdv2011.0
+ Revision: 615491
- the mass rebuild of 2010.1 packages

* Fri Jan 01 2010 Jérôme Brenier <incubusss@mandriva.org> 2.2-1mdv2010.1
+ Revision: 484760
- new version 2.2
- fix license tag
- fix install

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
    - fix no-buildroot-tag

* Thu Dec 20 2007 Thierry Vignaud <tv@mandriva.org> 2.1-2mdv2008.1
+ Revision: 135587
- BR imake
- kill re-definition of %%buildroot on Pixel's request


* Sat Oct 01 2005 Nicolas L�cureuil <neoclust@mandriva.org> 2.1-2mdk
- BuildRequires fix

* Sun May 29 2005 Eskild Hustvedt <eskild@mandriva.org> 2.1-1mdk
- Initial Mandriva Linux package

