%define	version 2.1
%define rel	2
%define	release	%mkrel %rel

Name:		xautolock
Summary:	A program for automatically starting programs when there is inactivity under X
Version:	%{version} 
Release:	%{release} 
Source0:	%{name}-%{version}.tar.bz2
URL:		http://www.ibiblio.org/pub/Linux/X11/screensavers/
Group:		Graphical desktop/Other
License:	GPL
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
chmod a+r *

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc License Todo Readme Changelog
%{_prefix}/X11R6/bin/xautolock
%{_mandir}/*/*

